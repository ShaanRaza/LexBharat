# data

Scripts that read the open-india-law snapshot (v2026.08) on the **LAWSSD** drive and build
the search collection. **No data is committed here**: only scripts and file paths.
`*.parquet` is gitignored.

Data: Open India Law by Vaquill AI, CC BY 4.0.

## Before running anything

```bash
colima start && docker start qdrant
```
Always `docker stop qdrant && colima stop` before unplugging LAWSSD.

Python environment (Python 3.12, the same as CI):
```bash
uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python duckdb pyarrow numpy "qdrant-client~=1.16.0"
```
`qdrant-client` is pinned to **1.16.x** to match the local Qdrant server (1.16.3). A newer
client warns that it's incompatible.

## Scripts

| Script | What it does |
|---|---|
| `inspect_collections.py` | **Read-only.** Payload fields, court values and exact Supreme Court counts in `legal_corpus_v1` and `legal_corpus_v2`. Run: `.venv/bin/python data/inspect_collections.py` |

## Where the source data is

75 parquet files, all in one folder (Measured, 13 Oct 2026):

```
/Volumes/LAWSSD/open-india-law/
```

| What | File(s) | Rows | Loaded into Qdrant as |
|---|---|---|---|
| **Supreme Court judgments** | `in_supreme-court_judgments.parquet` | 1,113,313 chunks: **371,247 English** + translations in 15 languages | `legal_corpus_v2`, English only: **371,159 points** |
| Central Acts | `in_central_legislation.parquet` | 74,484 | `acts_india` (`jurisdiction = central`: 74,509 points) |
| State Acts | 36 more `in_<state>_legislation.parquet` files | 469,594 (all 37 legislation files: 544,078) | `acts_india` (`jurisdiction = state`) |
| Regulations | 12 `in_<regulator>_regulations.parquet` files | 554,191 | `acts_india` (`jurisdiction = regulatory`) |
| High Court judgments | 25 more `in_<court>_judgments.parquet` files | not counted | `legal_corpus_v1`, `legal_corpus_v2` (not used in v1) |

**`acts_india` holds all 49 legislation and regulation files**: 1,098,269 parquet rows
against 1,098,577 points (the 308 difference is still unexplained). See the open decision
"What `acts_india` covers in v1" in [`../docs/DECISIONS.md`](../docs/DECISIONS.md).

## How a Qdrant point links to its parquet row

| Key | Format | Notes |
|---|---|---|
| `chunk_id` | `<case_id>_<3-digit chunk index>`, e.g. `2020_INSC_548_012` | **The join key.** English rows have no suffix; translations add one (`2020_INSC_548_012_hin`) |
| `case_id` | e.g. `2020_INSC_548` | One judgment |
| `chunk_index`, `total_chunks` | integers | Order of the chunks within a judgment |
| `char_start`, `char_end`, `page_start`, `page_end` | integers | Where the chunk sits in the judgment |

**The chunk text is stored in the Qdrant payload** (`text`, about 4,000 characters per
chunk), so search results don't need a parquet lookup. Every one of the 371,159 Supreme
Court points has non-empty text (Measured).

Both judgment collections also carry `judges`, `petitioner` and `respondent`.
**Never display or copy them** (CLAUDE.md §6).
