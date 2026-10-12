# Shaan: Week 2 (Data + Core + Lead), 4 h a day

**Theme: search works.** By Saturday a question goes through **search → re-rank → relevance
gate** and comes out as at most 8 passages labelled S1 to S8. The answer step comes in Week 3.

This week you touch pipeline steps **5 (search), 6 (re-rank) and 7 (gate)**, plus the
decisions adapter that steps 3 and 7 both use.

**Your first job on Monday is the pipeline contract.** Akash and Meghna both build against
it, the same way they built against the streaming format in Week 1.

**Every day, about 30 minutes:** review and merge pull requests (expected ones at the bottom).

> **Tue 20 Oct is Dussehra.** If you take it off, task **2.2 moves to Wednesday morning**
> and **6.2 (the gate) moves to Week 3 Day 1**. Say so in the standup.

---

## Before Day 1

- [ ] Week 1 wrapped (issue #19): everything that's ready is merged, and the "Done means"
      list in [`../week-1/README.md`](../week-1/README.md) is ticked honestly
- [ ] Anything unfinished from Week 1 is **carried over first**. It goes ahead of this file.
- [ ] LAWSSD plugged in: `colima start && docker start qdrant`

---

## Day 1, Mon 19 Oct: the pipeline contract

### 1.1 The contract (2 h)
CLAUDE.md rule 7: each pipeline step is a separate function with a **fixed input and
output**. Write those shapes down **before** anyone builds the steps.

| File | Holds |
|---|---|
| `core/types.py` | The shared shapes: `Question`, `Filters` (court, years, Act, section, case number), `Passage` (record_id, chunk_id, text, source_type, title, citation, url, scores), `GatedPassage` (adds the S-label and relevance), `Citation` (the checked result), and the four streaming `Event`s from `docs/API.md` |
| `core/pipeline.py` | One function per step (remember, rewrite, decide, cache, search, rerank, gate, answer, verify, show, save), each with its input and output types. Bodies raise `NotImplementedError` for now. Plus `run(...)`, which yields `Event`s |
| `core/fake_pipeline.py` | A fake `run(...)` that yields a realistic answer **in the streaming format**, citing passages from the practice dataset. Akash's streaming route and Meghna's chat screen use it in Week 3 |

**Ask Claude Code:**
> Read CLAUDE.md §2 rule 7 and §4, docs/ARCHITECTURE.md and the "Streaming events" section of docs/API.md. Write core/types.py, core/pipeline.py (stubs only, one function per step with typed input and output) and core/fake_pipeline.py per team/week-2/shaan.md task 1.1. Explain each type in plain words. Don't implement the steps.

**Done when:** the types import cleanly, the fake yields token… citations… done in the right
order, and a test proves it.

### 1.2 Contract call with Akash (30 min)
Agree three things and record each with `/decision`:

| Question | My recommendation |
|---|---|
| **Where does database code live?** Routes can't hold it (`api/` is routes only), and `core/` is your lane | `core/store/`: Akash writes it, you review it. One module per table group. Pipeline steps call `core/store`, never SQLAlchemy directly |
| **How do dev laptops run without paid keys?** | A setting `USE_FAKE_ADAPTERS` (dev only, default off). When on, every adapter returns its test fake. The app **refuses to start** with it on outside dev. Add it to `.env.example` and `docs/ENVIRONMENT.md` |
| **What does the streaming route call?** | `core.pipeline.run(question, conversation, user)`, which yields `Event`s. The route only turns events into server-sent events. Week 3 swaps the fake for the real one with no route change |

**Branch:** `shaan/pipeline-contract`. **Merge today.** Akash and Meghna both need it.

### 1.3 Start the PostgreSQL load (1 h)
See Day 2.

---

## Day 2, Tue 20 Oct: load cases and Act sections into PostgreSQL

### 2.1 The load script (2.5 h)
`data/load_postgres.py` fills the `cases` and `act_sections` tables from the parquet files
(DuckDB). It covers **all** Supreme Court judgments and **all** `acts_india` sections, not
the practice sample.

- `full_text` rebuilt **in order** from the chunks
- `citation` stored **exactly as in the dataset**: no tidying, no reformatting
- `in_force` filled **only** where `act_status` is filled; otherwise left empty
- `judges`, `petitioner` and `respondent` **not loaded at all**
- One `court_coverage` row: `supreme_court`, `v2026.08`, the data-as-of date, the point
  count, `live = yes`, `stats_live = no`
- **Safe to re-run** (upsert by `record_id`), and refuses any database that isn't local

### 2.2 Check it (1 h)
- [ ] Row count in `cases` = distinct Supreme Court judgments in the parquet files
- [ ] Row count in `act_sections` matches `acts_india`
- [ ] 5 random judgments: `full_text` reads in the right order, and the citation string is
      byte-for-byte the stored one
- [ ] Record both counts in `docs/DECISIONS.md` as **Measured**

**Branch:** `shaan/load-postgres`

---

## Day 3, Wed 21 Oct: search (step 5)

### 3.1 `core/search.py` (3 h)
Read [`../../docs/ARCHITECTURE.md`](../../docs/ARCHITECTURE.md), "Search: three ways at once".

| Path | When | How |
|---|---|---|
| **Meaning + keyword** | Normal questions | One Qdrant call: dense (voyage-4, embedded as a *query*) and sparse (BM25) prefetches, merged by Reciprocal Rank Fusion. **Top 50** |
| **Exact lookup** | A named section, case number or citation | Straight to a payload filter. No merge |
| **Keyword only** | Voyage is down or times out | Sparse only, results marked `keyword_only = true` so the screen can say **"keyword results only"** |

- Filters (court, year range, Act) applied **inside** the Qdrant call, never afterwards
- Collection name from settings
- Returns `list[Passage]`, the type from 1.1

Tests with the fake embedding adapter: the filter is built correctly, the exact-lookup path
skips the merge, and Voyage failing falls back to keyword-only.

**Branch:** `shaan/search`

**Ask Claude Code:**
> Implement core/search.py per team/week-2/shaan.md task 3.1, using the types in core/types.py and the embeddings adapter. One Qdrant query with dense + sparse prefetch and RRF fusion; exact lookups go straight to a payload filter; Voyage failure falls back to sparse only. Tests with the fake adapter. Explain the Qdrant query in plain words.

---

## Day 4, Thu 22 Oct: re-rank (step 6) and timing

### 4.1 `core/rerank.py` (1.5 h)
Top 50 in, **top 10** out, through `adapters/rerank.py` (rerank-2.5-lite). If the re-ranker
fails, keep the search order and cut to 10. **Never fail the whole answer** because
re-ranking failed. Tests for both paths.

### 4.2 Run your 20 hand searches again (1.5 h)
The same 20 questions from Week 1 (`data/notes/hand-searches-week1.md`), now through
search + re-rank on the real SSD collection.
- Rate the top 5 again: good / partly / bad
- **Time the search stage.** Target **under 800 ms** for search + re-rank (CLAUDE.md §10)
- Write it into `data/notes/hand-searches-week2.md`, with one line: better or worse than
  Week 1, and why

**Branch:** `shaan/rerank`

---

## Day 5, Fri 23 Oct: the decisions adapter

### 5.1 `adapters/decisions.py` (3 h)
Every fixed-choice decision goes through this one file: scope, filters, safety, the
relevance gate and the claim check.

- **Jev** when its switch is on and it answers within `JEV_TIMEOUT_MS` (800)
- **Gemini Flash-Lite fallback** with **the same fixed choices** when Jev is off, down or slow
- One switch per use: `JEV_ENABLED_SCOPE`, `_FILTERS`, `_GATE`, `_CLAIM`, `_SAFETY`
- **A guard:** any call marked as containing upload text **never goes to Jev**, whatever
  the switches say. A test proves it.
- The answer always comes back as one of the allowed choices, plus a confidence. Anything
  else counts as a failure and uses the fallback.

No Jev access yet? Build the Jev side against its documented API behind the switch, and run
everything on the fallback.

**Branch:** `shaan/decisions-adapter`

---

## Day 6, Sat 24 Oct: the gate (step 7), then wrap

### 6.1 `core/gate.py` (2 h)
10 passages in, **at most 8** out, labelled **S1 to S8**.
- One decision per passage: answers it / partly / not relevant, **all in parallel**
- "Not relevant" is dropped
- If **no** passage clears `JEV_GATE_THRESHOLD` (0.6), return "not found". **No answer is
  written**, and the screen shows the "No relevant results" state
- Labels are given **after** dropping, so they're always S1, S2, … with no gaps

Tests: all relevant (8 kept), none relevant (not found), a mix, and the decisions adapter
failing (keep the re-rank top 8, marked as ungated).

### 6.2 Wrap the week (1 h)
- [ ] Merge what's ready; tick "Done means" in [README.md](README.md) honestly
- [ ] Adjust the Week 3 issues to match what really got done
- [ ] Open the **Standup: Week 3** issue (label `standup`)
- [ ] `docker stop qdrant && colima stop` before unplugging

**Branch:** `shaan/gate`

---

## Pull requests to expect, by day

| Day | From Akash | From Meghna | Yours |
|---|---|---|---|
| 1 | `akash/dev-auth` | `meghna/api-client` | `shaan/pipeline-contract` |
| 2 | `akash/conversations` | `meghna/real-pages` | `shaan/load-postgres` |
| 3 | `akash/pagination-audit` | `meghna/conversation-list` | `shaan/search` |
| 4 | `akash/search-route` | `meghna/conversation-history` | `shaan/rerank` |
| 5 | `akash/openapi-firebase-prep` | `meghna/sign-in-mock` | `shaan/decisions-adapter` |
| 6 | `akash/ci-integration` | `meghna/act-lookup` | `shaan/gate` |

`core/store/` is in your folder, so **review Akash's database code as carefully as the
tables last week**.

## Done by Saturday

- [ ] Pipeline contract merged; `USE_FAKE_ADAPTERS` and `core/store/` decisions recorded
- [ ] All SC cases and Act sections in PostgreSQL; counts recorded as Measured
- [ ] Search: meaning + keyword + exact lookup, top 50, with the keyword-only fallback
- [ ] Re-rank to 10; search stage timed against the 800 ms target
- [ ] Decisions adapter with the Gemini fallback, and the upload-text guard tested
- [ ] Gate: at most 8, S1 to S8, "not found" below the threshold
