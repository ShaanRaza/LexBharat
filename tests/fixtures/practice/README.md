# Practice dataset

A small, fixed sample of the real data, for building and testing **without the LAWSSD
drive or a Voyage key**. Everyone builds against this until the real search collection is
on the server.

Data: Open India Law by Vaquill AI, CC BY 4.0. Snapshot v2026.08.

> **Never display judge or party names.** The `judges`, `petitioner` and `respondent`
> fields were left out on purpose (CLAUDE.md §6). Don't add them back.

## What's in it

| File | Contents |
|---|---|
| `judgments.jsonl.gz` | **20 complete Supreme Court judgments**, 2 or 3 per decade from the 1950s to the 2020s: title, citation (exactly as stored), case number, date, year, disposition, `pdf_url`, the **rebuilt `full_text`**, and `gaps` |
| `chunks.jsonl.gz` | **1,078 Supreme Court chunks**: all 198 chunks of the 20 judgments, plus **880 more** (110 per decade, one per judgment, for spread) |
| `act_sections.jsonl.gz` | **320 Act sections**: IPC (60, repealed), BNS (60), BNSS (60), NI Act (60), Indian Evidence Act 1872 (30, repealed), Bharatiya Sakshya Adhiniyam (30), and 20 sections of one Maharashtra state Act |
| `vectors.npy` | The stored **voyage-4** vectors, `float16`, shape `(1398, 1024)`: one row per chunk, then one per Act section |
| `vector_ids.txt` | The `chunk_id` of each row in `vectors.npy`, in the same order: chunks first, then Act sections |

Each record carries `point_id` (its ID in the local Qdrant) so it can be traced back.
Total size: about 4.4 MB (`du -sh tests/fixtures`).

### Reading it

```python
import gzip, json
import numpy as np

chunks = [
    json.loads(line)
    for line in gzip.open("tests/fixtures/practice/chunks.jsonl.gz", "rt")
]
vectors = np.load("tests/fixtures/practice/vectors.npy").astype(
    np.float32
)  # float32 for Qdrant
```

The `.jsonl` files are gzip-compressed because uncompressed they'd be about 9 MB, over the
5 MB limit for fixtures.

## Things to know before building on it

| Fact | What it means for you |
|---|---|
| **A chunk's `text` starts with a short header** (`Case: <title> … Section: BODY`) before the judgment text | `char_start`/`char_end` point at the text **after** the header. The body is the last `char_end - char_start` characters of `text`. The verifier and the highlighting must use the body |
| **Neighbouring chunks overlap** (by a varying amount, from about 80 to 450 characters in the samples checked) | Don't concatenate chunks to show a judgment. Use `full_text` from `judgments.jsonl.gz` |
| **`full_text` has small gaps**, padded with spaces, listed in `gaps` as `[start, end]` | 17 of the 20 judgments have one or more; 80 characters in total. Padding keeps every chunk at exactly `full_text[char_start:char_end]`. A screen can mark a gap as "text missing in the source" |
| **No paragraph numbers yet** | Paragraph anchors (`p1`, `p2`, …) are split from `full_text` by the API (Akash, Day 5) |
| **`act_status` is never empty** | Central Acts here are `in_force` or `repealed`. The 20 state-Act sections say `in_force`, but every state Act in the dataset says that (Measured), so it looks like a default, not a check. How the in-force rule should treat them is an open decision in `docs/DECISIONS.md` |
| **No CrPC, 1973** | The Code of Criminal Procedure, 1973 isn't in the Central Acts file, only in state files (Measured). The Indian Evidence Act, 1872 was included instead |
| Act sections can be split into parts | A long section has several chunks (`IND_central_..._s002_d1`, `_d2`). `section_number` is the same for all parts |

## How it was made

`data/export_practice.py`, run on 13 Oct 2026 against the local Qdrant (snapshot v2026.08):

- Supreme Court points from `legal_corpus_v2` (`court_type = "supreme_court"`); Act sections from `acts_india`
- Complete judgments chosen per decade from cases with 5 to 15 chunks and a citation
- **Duplicates removed**: some chunks are stored twice in Qdrant under different point IDs. One of the 20 judgments had 5 duplicate points; the lowest point ID is kept
- Only fields on an allowlist are copied, so anything not listed never leaves the drive
- Vectors copied as stored (checked: cosine 1.00000 against Qdrant), then converted to `float16`

To rebuild it (LAWSSD plugged in, Qdrant running):
```bash
.venv/bin/python data/export_practice.py
```
The selection is deterministic: the same snapshot gives the same files.
