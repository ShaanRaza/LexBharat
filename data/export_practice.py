"""Export the practice dataset the team builds against (issue #7).

A small, fixed sample of the real data in the local Qdrant, written to
tests/fixtures/practice/:

    judgments.jsonl.gz     20 complete Supreme Court judgments, full text rebuilt
    chunks.jsonl.gz        every chunk of those 20, plus extra chunks across the decades
    act_sections.jsonl.gz  sections of IPC, BNS, BNSS, the NI Act and the Evidence Act,
                           plus a few state-Act sections (their status is a default)
    vectors.npy            the stored voyage-4 vectors, float16, one row per chunk
                           and section, in the order of vector_ids.txt
    vector_ids.txt         the chunk_id of each row in vectors.npy

Read only: it never writes to Qdrant. Fields are copied from an allowlist, so
`judges`, `petitioner`, `respondent` and anything else unlisted never leave the
drive (CLAUDE.md §6).

Run from the repo root (LAWSSD plugged in, Qdrant running):
    .venv/bin/python data/export_practice.py
"""

import gzip
import io
import json
import os
from pathlib import Path

import numpy as np
from qdrant_client import QdrantClient, models

QDRANT_URL = os.environ.get("QDRANT_URL", "http://localhost:6333")
JUDGMENTS = "legal_corpus_v2"
ACTS = "acts_india"
OUT = Path("tests/fixtures/practice")

DECADES = [
    (1950, 1959),
    (1960, 1969),
    (1970, 1979),
    (1980, 1989),
    (1990, 1999),
    (2000, 2009),
    (2010, 2019),
    (2020, 2026),
]
COMPLETE_PER_DECADE = [2, 2, 3, 3, 3, 3, 2, 2]  # 20 judgments
COMPLETE_CHUNKS = (5, 15)  # keep complete judgments small, so the fixtures stay small
EXTRA_CHUNKS_PER_DECADE = int(
    os.environ.get("EXTRA_PER_DECADE", "110")
)  # 880: keeps it under 5 MB

# The Code of Criminal Procedure, 1973 isn't in the Central Acts file (only state-file
# copies), so the Indian Evidence Act, 1872 takes its place. BSA is in the law maps.
CENTRAL_ACTS = {
    "IND_REP_659_1860": 60,  # The Indian Penal Code (repealed)
    "IND_central_20062": 60,  # The Bharatiya Nyaya Sanhita, 2023
    "IND_central_20099": 60,  # The Bharatiya Nagarik Suraksha Sanhita, 2023
    "IND_central_2189": 60,  # The Negotiable Instruments Act, 1881
    "IND_REP_971_1872": 30,  # The Indian Evidence Act, 1872 (repealed)
    "IND_central_20063": 30,  # The Bharatiya Sakshya Adhiniyam, 2023
}
MUST_HAVE_SECTIONS = {
    "IND_REP_659_1860": ["302", "420", "377", "498A", "304B"],
    "IND_central_20062": ["103", "318", "80"],
    "IND_central_2189": ["138", "139", "141", "142"],
}
STATE_ACT_SECTIONS = 20

JUDGMENT_FIELDS = [
    "case_id",
    "title",
    "citation",
    "case_number",
    "decision_date",
    "year",
    "disposition",
    "court",
    "pdf_url",
]
CHUNK_FIELDS = [
    "chunk_id",
    "case_id",
    "chunk_index",
    "total_chunks",
    "text",
    "char_start",
    "char_end",
    "page_start",
    "page_end",
    "section_type",
    "title",
    "citation",
    "case_number",
    "decision_date",
    "year",
    "court",
    "pdf_url",
]
ACT_FIELDS = [
    "chunk_id",
    "act_id",
    "title",
    "year",
    "jurisdiction",
    "state",
    "chapter",
    "chapter_title",
    "section_number",
    "section_title",
    "sub_section",
    "chunk_index",
    "total_chunks",
    "text",
    "act_status",
    "section_status",
    "is_repealed",
    "source_url",
    "pdf_url",
]
NEVER = {"judges", "petitioner", "respondent", "bench"}
assert not NEVER & set(JUDGMENT_FIELDS + CHUNK_FIELDS + ACT_FIELDS)


def match(key, value):
    return models.FieldCondition(key=key, match=models.MatchValue(value=value))


def year_range(lo, hi):
    return models.FieldCondition(key="year", range=models.Range(gte=lo, lte=hi))


SUPREME_COURT = match("court_type", "supreme_court")


def pick(payload, fields):
    return {f: payload.get(f) for f in fields}


def dense(point):
    vec = point.vector["dense"] if isinstance(point.vector, dict) else point.vector
    return np.asarray(vec, dtype=np.float32)


def body_of(payload):
    """Chunk text without its "Case: ..." header, so it lines up with char_start."""
    span = payload["char_end"] - payload["char_start"]
    return payload["text"][len(payload["text"]) - span :]


def rebuild_full_text(chunks):
    """Stitch overlapping chunks by character position. Gaps are padded with spaces
    so every chunk still sits at exactly [char_start:char_end]; gaps are returned."""
    full, gaps = "", []
    for c in sorted(chunks, key=lambda c: c["chunk_index"]):
        start, body = c["char_start"], body_of(c)
        if start > len(full):
            gaps.append([len(full), start])
            full += " " * (start - len(full))
        overlap = len(full) - start
        if full[start:] != body[:overlap]:
            raise ValueError(f"overlap mismatch in {c['chunk_id']}")
        full += body[overlap:]
    for c in chunks:
        assert full[c["char_start"] : c["char_end"]] == body_of(c), c["chunk_id"]
    return full, gaps


DUPLICATES: dict[str, int] = {}


def dedupe(points):
    """Some chunks are stored twice under different point IDs (Measured, 13 Oct 2026).
    Keep one per chunk_id: the lowest point ID, so reruns pick the same one."""
    by_chunk = {}
    for p in sorted(points, key=lambda p: str(p.id)):
        by_chunk.setdefault(p.payload["chunk_id"], p)
    return list(by_chunk.values())


def scroll_all(client, collection, flt, limit, vectors=True):
    points, offset = [], None
    while len(points) < limit:
        batch, offset = client.scroll(
            collection,
            scroll_filter=flt,
            limit=min(256, limit - len(points)),
            offset=offset,
            with_payload=True,
            with_vectors=vectors,
        )
        points += batch
        if offset is None:
            break
    return points


def complete_judgments(client):
    lo_c, hi_c = COMPLETE_CHUNKS
    picked = []
    for (lo, hi), n in zip(DECADES, COMPLETE_PER_DECADE):
        flt = models.Filter(
            must=[
                SUPREME_COURT,
                year_range(lo, hi),
                models.FieldCondition(
                    key="total_chunks", range=models.Range(gte=lo_c, lte=hi_c)
                ),
            ]
        )
        cases = []
        for p in scroll_all(client, JUDGMENTS, flt, 300, vectors=False):
            cid = p.payload["case_id"]
            if p.payload.get("citation") and cid not in cases:
                cases.append(cid)
            if len(cases) == n:
                break
        picked += cases
    judgments, points = [], []
    for cid in picked:
        found = scroll_all(
            client, JUDGMENTS, models.Filter(must=[match("case_id", cid)]), 500
        )
        pts = dedupe(found)
        DUPLICATES[cid] = len(found) - len(pts)
        payloads = [p.payload for p in pts]
        if len(pts) != payloads[0]["total_chunks"]:
            raise ValueError(
                f"{cid}: {len(pts)} of {payloads[0]['total_chunks']} chunks"
            )
        full, gaps = rebuild_full_text(payloads)
        judgments.append(
            {
                **pick(payloads[0], JUDGMENT_FIELDS),
                "full_text": full,
                "gaps": gaps,
                "chunk_count": len(pts),
            }
        )
        points += sorted(pts, key=lambda p: p.payload["chunk_index"])
    return judgments, points


def extra_chunks(client, skip_cases):
    points, seen = [], set(skip_cases)
    for lo, hi in DECADES:
        flt = models.Filter(must=[SUPREME_COURT, year_range(lo, hi)])
        taken = 0
        for p in scroll_all(client, JUDGMENTS, flt, EXTRA_CHUNKS_PER_DECADE * 4):
            if taken == EXTRA_CHUNKS_PER_DECADE:
                break
            if p.payload["case_id"] not in seen:  # one chunk per case, for spread
                seen.add(p.payload["case_id"])
                points.append(p)
                taken += 1
    return points


def act_sections(client):
    points = []
    for act_id, n in CENTRAL_ACTS.items():
        chosen = {}
        for sec in MUST_HAVE_SECTIONS.get(act_id, []):
            flt = models.Filter(
                must=[match("act_id", act_id), match("section_number", sec)]
            )
            for p in scroll_all(client, ACTS, flt, 5):
                chosen[p.payload["chunk_id"]] = p
        flt = models.Filter(must=[match("act_id", act_id)])
        for p in scroll_all(client, ACTS, flt, n * 3):
            if len(chosen) >= n:
                break
            chosen.setdefault(p.payload["chunk_id"], p)
        points += list(chosen.values())
    flt = models.Filter(
        must=[match("jurisdiction", "state"), match("state", "maharashtra")]
    )
    first = scroll_all(client, ACTS, flt, 1, vectors=False)[0].payload["act_id"]
    points += scroll_all(
        client, ACTS, models.Filter(must=[match("act_id", first)]), STATE_ACT_SECTIONS
    )
    return dedupe(points)


def write_jsonl_gz(path, rows):
    # mtime=0 keeps the bytes identical between runs, so git sees no false change
    with (
        gzip.GzipFile(path, "wb", mtime=0) as raw,
        io.TextIOWrapper(raw, encoding="utf-8") as f,
    ):
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main():
    client = QdrantClient(
        url=QDRANT_URL, api_key=os.environ.get("QDRANT_API_KEY"), timeout=300
    )
    OUT.mkdir(parents=True, exist_ok=True)

    judgments, judgment_points = complete_judgments(client)
    extra = extra_chunks(client, {j["case_id"] for j in judgments})
    acts = act_sections(client)

    chunk_points = judgment_points + extra
    chunks = [{**pick(p.payload, CHUNK_FIELDS), "point_id": p.id} for p in chunk_points]
    sections = [{**pick(p.payload, ACT_FIELDS), "point_id": p.id} for p in acts]

    write_jsonl_gz(OUT / "judgments.jsonl.gz", judgments)
    write_jsonl_gz(OUT / "chunks.jsonl.gz", chunks)
    write_jsonl_gz(OUT / "act_sections.jsonl.gz", sections)
    vectors = np.stack([dense(p) for p in chunk_points + acts]).astype(np.float16)
    np.save(OUT / "vectors.npy", vectors)
    (OUT / "vector_ids.txt").write_text(
        "\n".join(r["chunk_id"] for r in chunks + sections) + "\n", encoding="utf-8"
    )

    gaps = sum(1 for j in judgments if j["gaps"])
    dup = sum(1 for n in DUPLICATES.values() if n)
    print(
        f"judgments: {len(judgments)} complete ({gaps} with gaps between chunks; "
        f"{dup} had duplicate points, {sum(DUPLICATES.values())} removed)"
    )
    print(
        f"chunks: {len(chunks)} ({len(judgment_points)} from complete judgments, "
        f"{len(extra)} extra across {len(DECADES)} decades)"
    )
    print(
        f"act sections: {len(sections)}; "
        f"statuses: {sorted({str(s['act_status']) for s in sections})}"
    )
    print(f"vectors: {vectors.shape} {vectors.dtype}")
    total = sum(f.stat().st_size for f in OUT.iterdir() if f.is_file())
    print(f"total size of {OUT}: {total / 1_000_000:.2f} MB")


if __name__ == "__main__":
    main()
