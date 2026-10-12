# Shaan: Week 5 (Data + Core + Lead), 4 h a day

**Theme: measured.** Until now every model, threshold and switch was a guess. This week you
build the tool that runs questions and scores them, run **50 real questions** through
several setups, and **choose from evidence**: which model each plan uses, the gate
threshold, and which Jev uses stay on.

Pipeline steps touched: none change shape. You're **measuring** steps 3, 7, 8 and 9 and
setting their config.

> **Mon 9 Nov is Govardhan Puja: light day.** **Wed 11 Nov is Bhai Dooj.** If you take
> Wednesday off, the **model comparison (4.1) moves to Thursday afternoon** and the **Jev
> comparison (5.1) to Saturday**. Say so in the standup.

---

## Before Day 1

- [ ] The Week 4 decision memo is done. **If it changed uploads, Hindi or devices, re-plan
      this week first.** The memo wins over this file
- [ ] Check [`../MONTH-2.md`](../MONTH-2.md), "What Month 2 assumes is done". Anything
      missing from Month 1 goes **first**

---

## Day 1, Mon 9 Nov (Govardhan Puja): light, about 1.5 h

### 1.1 Pick the 50 questions (1 h)
From `evals/questions.jsonl`, the **real** part only. Choose 50 that cover the mix
lawyers actually asked about: criminal, civil, constitutional, procedure, and some
follow-up style questions. Save the list of IDs as `evals/sets/measure-50.txt`.

### 1.2 Reviews (30 min)

---

## Day 2, Tue 10 Nov: the test runner

### 2.1 `evals/run.py` (3 h)
Runs a set of questions through the **real pipeline** with a named setup, and records
everything per question.

| Records per question | Why |
|---|---|
| Every citation: tick, warning or removed, with the reason | The verified-citation rate (target 98%+) |
| Whether the behaviour matched `expect` (answer / not found / coverage / advice notice / blocked) | The traps prove the verifier works |
| Time to first word, total time, time per step | Speed targets (CLAUDE.md §10) |
| Tokens in and out per model call; **cost** | Cost per answer |
| Gate scores for all 10 passages | So threshold changes can be tested **without re-running** |

Output: `evals/runs/<date>-<setup>.jsonl` plus a one-page `summary.md`. **No question text
from real interviews goes to Langfuse unmasked** (Akash's masking is already on).

**Ask Claude Code:**
> Write evals/run.py and a scorer per team/week-5/shaan.md task 2.1. It runs question IDs from a file through core.pipeline.run with a named config, records per-question results as JSONL, and writes a summary with the verified-citation rate, removed-citation rate, behaviour match for traps, timing percentiles and cost per answer. Explain the scoring in plain words.

**Branch:** `shaan/eval-runner`

---

## Day 3, Wed 11 Nov (Bhai Dooj): the baseline

### 3.1 First run (2 h)
The 50 questions on the current setup. Read the summary, then **read 10 answers yourself**
and grade them right / partly / wrong. The scorer measures citations; only a person can
judge whether the answer is correct.

### 3.2 What the baseline says (1 h)
Write the three biggest problems you see into `evals/runs/<date>-baseline/notes.md`. These
are the first entries on the Week 8 fix list.

---

## Day 4, Thu 12 Nov: which model

### 4.1 Model comparison (3 h)
The same 50 questions on each answer model. **Only providers marked no-training** (the
config refuses anything else):

| Setup | Model |
|---|---|
| A | Gemini 2.5 Flash-Lite |
| B | Gemini 3.1 Flash-Lite |
| C | One stronger model (pick one, no-training terms) |

Compare: verified-citation rate, removed-citation rate, your grade on the same 10 answers,
time to first word, **cost per answer**.

### 4.2 Choose (1 h)
Set `MODEL_FREE`, `MODEL_STUDENT` and `MODEL_PRO`, and decide whether
`FEATURE_MODEL_ROUTING` has a reason to exist yet. Record with `/decision`, with the
numbers. **Label them Measured.**

**Branch:** `shaan/model-choice`

---

## Day 5, Fri 13 Nov: the gate threshold and Jev

### 5.1 Jev on vs off (2 h)
For each use (scope, filters, gate, claim, safety): the chosen model with that Jev use on,
then off (Gemini fallback). docs/TESTING.md: **a `JEV_ENABLED_*` switch turns on only once
it beats the version without it.** No Jev access yet? Record that, and every switch stays
off.

### 5.2 Gate threshold (1.5 h)
Using the gate scores saved on Day 2, replay 0.5, 0.6 and 0.7 **without re-running the
model**. Watch two things: answers that wrongly say "not found", and answers built on weak
passages. Pick one; record it with `/decision`.

**Branch:** `shaan/jev-and-threshold`

---

## Day 6, Sat 14 Nov: design for uploads, and the drop-list check

### 6.1 Upload answers on paper first (1.5 h)
Next week you build answering from uploads. Write the design into `docs/ARCHITECTURE.md`
(Uploads) **before** coding:
- How document passages are labelled (proposal: **D1 to D8**, separate from S1 to S8)
- How the answer keeps **"Your document says"** apart from **"Supreme Court judgments say"**
- Which verifier checks apply to document citations (1 to 3 the same; 4 through Gemini,
  **never Jev**)
- What happens when Voyage's terms haven't arrived (**bge-m3**, from `docs/DECISIONS.md`)

### 6.2 The Week 5 drop-list check (1 h)
[`../V1-PLAN.md`](../V1-PLAN.md) §2: **check at the end of Week 5.** Planned vs done for
Weeks 1 to 5. If it's slipping, use the drop list (PWA polish → law maps beyond IPC → BNS
→ Word uploads → OCR → the export screen), **out loud**, in the standup issue.

### 6.3 Wrap (30 min)
"Done means" in [README.md](README.md); adjust the Week 6 issues; open **Standup: Week 6**.

**Branch:** `shaan/upload-answer-design`

---

## Pull requests to expect

| Day | From Akash | From Meghna | Yours |
|---|---|---|---|
| 1 | `akash/minio-dev` | | |
| 2 | `akash/upload-links` | `meghna/upload-screen` | `shaan/eval-runner` |
| 3 | `akash/document-status` | `meghna/upload-progress` | |
| 4 | `akash/worker-skeleton` | `meghna/upload-status` | `shaan/model-choice` |
| 5 | `akash/upload-safety-feedback` | `meghna/documents-list` | `shaan/jev-and-threshold` |
| 6 | `akash/uploads-access` (**careful review**) | | `shaan/upload-answer-design` |

**`akash/uploads-access` is the most important review this month.** It's the one function
that stops one lawyer seeing another's client files.

## Done by Saturday

- [ ] `evals/run.py` scores a run: citations, behaviour, speed, cost
- [ ] 50 real questions run on the baseline; 10 graded by hand
- [ ] Models chosen per plan, with the numbers, labelled Measured
- [ ] Each Jev use on or off by evidence; gate threshold chosen
- [ ] Upload-answer design written before any code
- [ ] **Drop-list check posted**
