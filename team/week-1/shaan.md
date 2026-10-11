# Shaan: Week 1 (Data + Core + Lead), 4 h a day

Your week has two jobs. **First, unblock the others**: the practice dataset and the
streaming format, both by the end of Day 2. **Then build the search collection** on your SSD.

**Every day, about 30 minutes:** review and merge pull requests. Expected ones are listed
at the bottom.

---

## Before Day 1 (one-time, ~30 min)

- [ ] Plug in **LAWSSD**. Qdrant runs inside a virtual machine whose disk lives on that
      drive. Without it, nothing starts. (If `colima` says *"cannot make required
      directory ~/.colima: file exists"*, the drive isn't plugged in.)
- [ ] Install `uv` (a fast Python installer), in Terminal:
      ```bash
      brew install uv
      ```
- [ ] Python **3.12** for this project, the same as CI. Your Mac's default is 3.14, which
      some of the data libraries may not support yet.

---

## Day 1, Tue 13 Oct: kickoff, count, start the practice dataset

### 1.1 Kickoff call (30 min)
Agenda in [README.md](README.md). Confirm Akash has accepted the GitHub invite.

### 1.2 Start the data machine (15 min)
Terminal:
```bash
colima start && docker start qdrant
```
```bash
curl -s localhost:6333/collections
```
**Done when:** you see `legal_corpus_v1`, `legal_corpus_v2` and `acts_india`.

> **Always** run `docker stop qdrant && colima stop` before unplugging LAWSSD.

### 1.3 Data environment (20 min)
In the repo folder:
```bash
uv venv --python 3.12 .venv && source .venv/bin/activate && uv pip install duckdb qdrant-client fastembed pyarrow numpy
```
`.venv/` is already ignored by git. Once Akash's `pyproject.toml` is merged, switch to
`uv pip install -e ".[dev,data]"`.

### 1.4 Count and inspect the Supreme Court points (60 min)
What we already know (my notes, 23 Sep): **`legal_corpus_v2` holds 371,159 Supreme Court
points.** `legal_corpus_v1` hasn't been counted.

Find out, for **both** collections:
- the **exact name and value of the court field** in the payload (so far it looks like
  `supreme_court`; confirm the field name)
- how many Supreme Court points there are
- whether the payload contains the chunk **text**, or only an ID to join with the parquet
  files
- the payload key that links a point to its parquet row

**Ask Claude Code:**
> Read docs/DATASET.md. Qdrant is at localhost:6333. For legal_corpus_v1 and legal_corpus_v2, show me the payload keys of 5 points, find the court field, and count Supreme Court points in each with a filtered count. Read only: change nothing. Report in plain words.

**Done when:** both open rows ("Court field name" and "Supreme Court point count") are
moved to Settled in `docs/DECISIONS.md` (use `/decision`) with the numbers, labelled
**Measured**.

### 1.5 Find the parquet files (15 min)
```bash
find /Volumes/LAWSSD -name "*.parquet" | head -20
```
Note which file(s) hold Supreme Court judgments and which hold the Acts. Write the
**paths only** (no data) into `data/README.md`.

### 1.6 Start the practice dataset (remaining ~70 min)
This is what Akash and Meghna build against until the real search collection is on the
server. Script: `data/export_practice.py`. Output: `tests/fixtures/practice/`.

**Contents:**

| Part | How many | Why |
|---|---|---|
| **Complete** Supreme Court judgments: all their chunks + the full text rebuilt in order | 20 | Judgment page and paragraph anchors need whole judgments |
| More Supreme Court chunks, spread across the decades | ~1,000 | Realistic search and citation testing |
| Act sections from **IPC, BNS, CrPC, BNSS and the NI Act** | ~300 | Act pages and the coming law maps. Include some sections **with** `act_status` and some **without**, to exercise the in-force rule |
| Their meaning vectors, as `float16` in one `.npy` file in the same order | one per chunk | Lets Akash test real similarity search without a Voyage key |

**Leave out** `judges`, `petitioner` and `respondent`. They're never shown anyway.

**Ask Claude Code:**
> Write data/export_practice.py per team/week-1/shaan.md task 1.6. Use DuckDB for the parquet files on /Volumes/LAWSSD and the Qdrant client for vectors. Output JSONL + one float16 .npy to tests/fixtures/practice/. Exclude judges, petitioner and respondent. Print the total size at the end.

**Branch:** `shaan/practice-dataset`

---

## Day 2, Wed 14 Oct: hand over the dataset and the format

### 2.1 Finish and share the practice dataset (75 min)
- [ ] `du -sh tests/fixtures` is **under 5 MB**. If not, cut the extra chunks first, then
      the Act sections.
- [ ] `tests/fixtures/practice/README.md`: what's in it, how it was made, the line
      `Data: Open India Law by Vaquill AI, CC BY 4.0`, and *"never display judges or party
      names"*.
- [ ] Open the PR and **merge it today**. Akash loads it tomorrow.

### 2.2 Agree the streaming format with Akash (20 min call + 20 min writing)
Meghna builds the chat screen against this **tomorrow**. Add a "Streaming events"
section to `docs/API.md`. **Starting draft; change anything you disagree with:**

```
event: token        data: {"text": "Under Section 138 of the "}
event: citations    data: {"citations": [
                       {"source_id": "S1", "record_id": "...", "kind": "judgment",
                        "title": "...", "citation_string": "[1979] 3 S.C.R. 453",
                        "support": "supports",            // or "partly"
                        "url": "<pdf_url or source_url>",
                        "data_as_of": "2026-08-.."}],
                     "removed_count": 0,
                     "notice": "<not-legal-advice text>",
                     "credit": "Data: Open India Law by Vaquill AI, CC BY 4.0"}
event: done         data: {"message_id": "...", "answers_left": 42}
event: error        data: {"error": {"code": "...", "message": "...", "request_id": "..."}}
```

Rules to keep in the doc: **exactly one** `citations` event, always **after** the last
`token`; nothing citation-shaped inside the tokens; citations with "does not support" are
never sent (they're removed and logged).

**Branch:** `shaan/stream-format`. **Merge today.**

### 2.3 Accounts and keys (30 min)
- [ ] **Apply for Jev early access** (TypeSafe AI). Ask in writing about no-training terms
      and where data is processed.
- [ ] **Voyage account + API key.** You need it Day 4 to embed real questions.
- [ ] **Gemini API key with billing switched on.** Paid tier only; the free tier may train
      on user data. Needed from Week 3.
- [ ] Keys go **only** in your local `.env`. Never in a commit, a chat or a screenshot.

### 2.4 Reviews (30 min)
`akash/python-setup` (**merge today**: your Day 5 tests need it), `meghna/web-setup`.

---

## Day 3, Thu 15 Oct: build the search collection

### 3.1 The build script (90 min)
`data/build_collection.py`. The collection name comes from config (`CORPUS_COLLECTION`),
never typed into the code.

| Setting | Value |
|---|---|
| Meaning vector | named `dense`, 1024 dimensions, cosine, kept on disk, **scalar quantization (int8) in memory** |
| Keyword vector | named `sparse`, BM25 with IDF, computed with fastembed (`Qdrant/bm25`) |
| Payload indexes | `record_id`, `source_type`, `court`, `year`, `citation`, `case_number`, `act_name`, `section_number`, `in_force`, `act_status` |

Steps the script takes:
1. Read Supreme Court points **with their vectors** from both collections (court filter).
   **No re-embedding**: reuse the stored voyage-4 vectors.
2. Join each point to its text in the parquet files (DuckDB).
3. Compute the BM25 vector from the text.
4. Upsert in batches, saving progress to a checkpoint file so a stopped run **resumes**.
5. Do the same for every `acts_india` point.

**Dry run first** on 1,000 points: time it and work out how long the full run will take.

**Ask Claude Code:**
> Write data/build_collection.py per team/week-1/shaan.md task 3.1 and docs/DATA-MODEL.md "Building kanoon_v1". Read-only on the source collections. Resumable via a checkpoint file. Add a --limit flag for a dry run. Read the collection name from settings.

### 3.2 Start the full run (15 min)
Run it in the background with `caffeinate -i` so the Mac doesn't sleep, logging to a file.
**Keep LAWSSD plugged in and Colima running** until it finishes.

### 3.3 Reviews (30 min)
`akash/compose-alembic`, `meghna/app-shell`, `meghna/web-setup` if not already merged.

**Branch:** `shaan/build-collection`

---

## Day 4, Fri 16 Oct: check the collection

### 4.1 Did it build correctly? (30 min)
- [ ] Point count = Supreme Court points (v1 + v2) + 1,098,577 Act points
- [ ] 5 random points each have a dense vector, a sparse vector, text and payload
- [ ] Reclaim disk space afterwards (the VM disk never shrinks by itself):
      `colima ssh -- sudo fstrim /var/lib/docker`

### 4.2 Twenty searches by hand (60 min)
- **10 keyword searches** (no Voyage key needed): section numbers, case numbers, exact
  phrases. For example "Section 138 Negotiable Instruments Act".
- **10 meaning searches**: embed the question with voyage-4 (as a *query*), then search.
  For example "is anticipatory bail available for cheque bounce cases".

Write each one into `data/notes/hand-searches-week1.md`: the query, the top 5 titles, and
good / partly / bad. **Done when:** 20 rows, plus one line on what looks weakest.

### 4.3 The chunk gap (45 min)
Count rows per judgment parquet file against points per collection. Is the gap about
55,000 (0.2%) or about 1,153,189 (3.5%)? Record it in `docs/DECISIONS.md` as **Measured**.

### 4.4 Review Akash's database tables carefully (45 min)
The data model is yours to defend, so **don't rubber-stamp it**. Check:
- [ ] IDs are UUIDs; every table has `created_at` and `updated_at`
- [ ] **No password column anywhere**
- [ ] `document_chunks` keeps `page_no`, `char_start` and `char_end`
- [ ] `invented_citation_log.reason` allows exactly the four reasons
- [ ] `audit_log` has **no column that could hold document text**
- [ ] Every migration can be undone (`alembic downgrade` works)

---

## Day 5, Sat 17 Oct: first core code, then wrap the week

### 5.1 Adapters, with test fakes (75 min)
One file per outside service (CLAUDE.md rule 1):
- `adapters/embeddings.py`: `embed(texts, kind="query" | "document")` → voyage-4
- `adapters/rerank.py`: `rerank(query, passages, top_k)` → rerank-2.5-lite
- `adapters/llm.py`: through LiteLLM; model names from config; **refuses any model not
  marked no-training**

Each has a **fake** for tests, so no test ever calls a real, paid API.
**Done when:** `grep -rn "import voyageai\|import litellm" --include=*.py .` finds those
imports **only** in `adapters/`.

### 5.2 The verifier's three free checks (75 min)
`core/verify.py`. Read [`../../docs/CITATION-VERIFIER.md`](../../docs/CITATION-VERIFIER.md)
first.
1. **Retrieved for this question**: the source ID was one of the S1–S8 given this turn
2. **Record exists**: the `record_id` is in the collection (passed in as a lookup, so
   tests don't need Qdrant)
3. **Quotes match**: quoted words appear in the record's text after tidying spaces and
   punctuation

Each failure returns its reason: `not_retrieved`, `record_missing` or `quote_not_found`.
Check 4 (`claim_not_supported`, via Jev) waits until Week 3.

**Done when:** at least one test per failure reason plus one that passes, and CI is green.

**Branch:** `shaan/verifier-free-checks`

### 5.3 Wrap the week (60 min)
- [ ] Merge everything that's ready
- [ ] Tick the "Done means" list in [README.md](README.md); be honest about what isn't
- [ ] Write `team/WEEK-2.md` from what **actually** got done, using the Week 2 row of
      [`../V1-PLAN.md`](../V1-PLAN.md)
- [ ] Before unplugging: `docker stop qdrant && colima stop`

---

## Pull requests to expect, by day

| Day | From Akash | From Meghna | Yours |
|---|---|---|---|
| 1 | `akash/python-setup` | `meghna/web-setup` | |
| 2 | `akash/compose-alembic` | `meghna/app-shell` | `shaan/practice-dataset`, `shaan/stream-format` |
| 3 | `akash/api-skeleton` | `meghna/chat-screen` | `shaan/build-collection` |
| 4 | `akash/core-tables` (**careful review**) | `meghna/failure-screens` | |
| 5 | `akash/act-and-judgment-routes` | `meghna/judgment-act-pages` | `shaan/verifier-free-checks` |

Merging rule: CI green, the PR checklist ticked, and it stays inside the author's lane.
