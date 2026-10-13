"""Read-only inspection of the local judgment collections (issue #6).

For each collection: the payload field names of a few sample points, the values of the
court field with their counts, an exact count of Supreme Court points, and whether the
chunk text is stored in the payload.

Read only: it never writes to Qdrant. It never prints the values of `judges`,
`petitioner` or `respondent` (CLAUDE.md §6: those fields are unreliable and never shown).

Run from the repo root:
    .venv/bin/python data/inspect_collections.py
"""

import os
import time

from qdrant_client import QdrantClient, models

QDRANT_URL = os.environ.get("QDRANT_URL", "http://localhost:6333")
COLLECTIONS = ["legal_corpus_v1", "legal_corpus_v2"]
COURT_FIELD = "court"
SAMPLE_SIZE = 5
NEVER_PRINT = {"judges", "petitioner", "respondent"}
# Both identify the Supreme Court and agree exactly (Measured, 13 Oct 2026).
SUPREME_COURT_FILTERS = [
    ("court_type", "supreme_court"),
    ("court", "Supreme Court of India"),
]


def describe_collection(client: QdrantClient, name: str) -> None:
    print(f"\n=== {name} ===")
    info = client.get_collection(name)
    print(f"total points: {info.points_count:,}")

    points, _ = client.scroll(
        name, limit=SAMPLE_SIZE, with_payload=True, with_vectors=False
    )
    keys = sorted({key for point in points for key in (point.payload or {})})
    print(
        f"payload fields in {len(points)} sample points ({len(keys)}): {', '.join(keys)}"
    )

    for point in points:
        payload = point.payload or {}
        text = payload.get("text")
        shown = {
            k: payload.get(k)
            for k in ("court", "court_type", "case_id", "chunk_id", "chunk_index", "id")
            if k in payload and k not in NEVER_PRINT
        }
        text_note = (
            f"text: {len(text)} chars" if isinstance(text, str) else "text: absent"
        )
        print(f"  point {point.id}: {shown} | {text_note}")

    facet = client.facet(name, key=COURT_FIELD, limit=100)
    print(f"values of '{COURT_FIELD}' (approximate counts, from the index):")
    for hit in facet.hits:
        print(f"  {hit.value!r}: {hit.count:,}")


def count_supreme_court(client: QdrantClient, name: str, key: str, value: str) -> int:
    start = time.monotonic()
    result = client.count(
        name,
        count_filter=models.Filter(
            must=[models.FieldCondition(key=key, match=models.MatchValue(value=value))]
        ),
        exact=True,
    )
    print(
        f"exact count of {key} == {value!r} in {name}: {result.count:,} "
        f"({time.monotonic() - start:.1f} s)"
    )
    return result.count


def main() -> None:
    client = QdrantClient(
        url=QDRANT_URL, api_key=os.environ.get("QDRANT_API_KEY"), timeout=300
    )
    for name in COLLECTIONS:
        describe_collection(client, name)
    print()
    for name in COLLECTIONS:
        for key, value in SUPREME_COURT_FILTERS:
            count_supreme_court(client, name, key, value)


if __name__ == "__main__":
    main()
