# Shaan: Week 4 (Data + Core + Lead), 4 h a day

**Theme: the whole engine.** By Friday all 11 pipeline steps are real: the answer
**remembers** the conversation, **rewrites** follow-ups into a standalone question,
**decides** what's in scope, and **caches** verified answers.

Pipeline steps touched: **1 (remember), 2 (rewrite), 3 (decide), 4 (cache)**.

**Friday is the decision point.** The 20 interviews are done, and what lawyers said may
change Weeks 5 to 10.

> **Fri 6 Nov is Dhanteras and Sat 7 Nov is Choti Diwali** (Diwali is Sun 8 Nov). The
> decision point is on **Friday**, and **Saturday is deliberately light**: buffer only.

---

## Before Day 1

- [ ] The re-plan from Sat 31 Oct is posted. **This file follows the re-plan, not the
      other way round.** If the re-plan moved anything, this week changes first
- [ ] Week 3 leftovers first, especially the verifier tests

---

## Day 1, Mon 2 Nov: remember (step 1)

### 1.1 `core/memory.py` (3 h)
- The **last 6 turns in full**, plus a **rolling summary** of everything older
- When a conversation passes 6 turns, the oldest turn is folded into
  `conversations.rolling_summary` by the cheap model (`MODEL_REWRITE`), after the answer
  is sent, so the user never waits for it
- The summary keeps **which Acts, sections and cases** were discussed. Those matter most
  for follow-ups
- The summary is **background only**: it never counts as a source and is never cited

Tests: 3 turns (no summary), 8 turns (summary + last 6), and the summary model failing
(the answer still works, using the last 6 turns only).

**Branch:** `shaan/memory`

---

## Day 2, Tue 3 Nov: rewrite (step 2)

### 2.1 `core/rewrite.py` (3 h)
Turns "and what about the next section?" into one standalone question, and pulls out the
**Act, section, case number and year** as structured fields.
- Uses `MODEL_REWRITE` with a fixed output shape. Anything that doesn't fit the shape → use
  the user's message as written
- A section or case number found here sends search down the **exact lookup** path (Week 2)
- Prompt in `core/prompts/rewrite.md`

Tests, with the fake LLM: a follow-up resolved from memory; "Section 138 NI Act" extracted;
a first question passed through unchanged; bad output falls back safely.

**Branch:** `shaan/rewrite`

---

## Day 3, Wed 4 Nov: decide (step 3)

### 3.1 `core/decide.py` (3 h)
Three decisions through the decisions adapter, **at the same time as** the Voyage embedding,
so they add little waiting:

| Decision | Choices | Effect |
|---|---|---|
| **Scope** | in scope / needs a High Court / needs a tribunal / after the snapshot / not a legal question | Anything except "in scope" **stops here** with the coverage message. No search, no writing cost |
| **Filters** | Court and years from fixed lists; Act from up to 20 keyword-matched candidates | Narrows the search |
| **Safety** | normal / personal legal advice / trying to trick the AI | Personal advice → the answer **opens** with the advice notice. Tricks → blocked |

Each has its own `JEV_ENABLED_*` switch. Off or failing → the Gemini fallback. **Both
failing → treat as in scope, no filters, normal**, and let the gate and verifier protect
the answer. Never block a real question because a decision service is down.

### 3.2 Two missing sentences (30 min)
`docs/UX-COPY.md` has no wording yet for **a blocked trick question** or **the monthly limit
reached**. Write both (plain words, no blame) and tell Meghna. They're yours to decide.

**Branch:** `shaan/decide`

---

## Day 4, Thu 5 Nov: cache (step 4) + the full pipeline

### 4.1 `core/cache.py` (2 h)
- Key: the **rewritten question + filters + model name**, hashed
- **Only answers that passed verification** are stored. Upload chats are **never** cached
- Kept for `ANSWER_CACHE_TTL_DAYS` (7)
- A hit replays the same events (text, then citations, then done), is marked `from_cache`,
  and **doesn't count** against the user's limit (Akash's meter reads this flag)

### 4.2 Run the whole pipeline (1.5 h)
All 11 steps on **20 real questions** from the interviews, including at least 3 follow-ups
and 3 that should be out of scope. Record in `evals/runs/week4-full-pipeline.md`: the time
per step, total time to first word (target under 3 s), and anything wrong.

**Branch:** `shaan/cache`

---

## Day 5, Fri 6 Nov (Dhanteras): the decision point

### 5.1 The decision memo, with Ranveer (2.5 h)
`docs/research/decision-memo-week4.md`. For each assumption in
[`../../docs/METRICS.md`](../../docs/METRICS.md) ("Assumptions being tested"): what the 20
interviews said, how many said it, and **what changes**.

| Question | Could change |
|---|---|
| Do advocates trust the "record found" tick? | Invest in one-tap source viewing instead of the badge |
| Phone or laptop? | How much phone work stays in Week 8 |
| Hindi? | Whether Hindi moves into the MVP (it would cost something else) |
| Would they upload client documents? | Upload limits, the warning wording, or uploads' place in the MVP |
| ₹199 and ₹499? | Prices for after the beta |
| Is Indian Kanoon already enough? | Whether to focus on students first |

### 5.2 Change Weeks 5 to 10 now (1 h)
V1-PLAN.md: **change it now, not later.** Update the plan, record decisions with `/decision`,
and adjust the Week 5 issues. Post a short summary in the standup issue.

---

## Day 6, Sat 7 Nov (Choti Diwali): light day

- [ ] Merge anything ready; tick "Done means" in [README.md](README.md)
- [ ] Open **Standup: Week 5**
- [ ] `docker stop qdrant && colima stop`

---

## Pull requests to expect

| Day | From Akash | From Meghna | Yours |
|---|---|---|---|
| 1 | `akash/usage-meter` | `meghna/firebase-sign-in` | `shaan/memory` |
| 2 | `akash/meter-limits` | `meghna/consent-role` | `shaan/rewrite` |
| 3 | `akash/consent` | `meghna/answers-left` | `shaan/decide` |
| 4 | `akash/langfuse-masking` | `meghna/eval-set` | `shaan/cache` |
| 5 | `akash/sentry-scrubbing` | `meghna/eval-lookups` | `shaan/decision-memo` |

**Review the usage meter (`core/meter.py`) and both privacy PRs (masking, scrubbing) with
care.** The meter has must-pass tests (CLAUDE.md rule 6), and the other two decide what
leaves the server.

## Done by Saturday

- [ ] Remember, rewrite, decide and cache all real, each with tests
- [ ] All 11 steps run on 20 real questions; times recorded
- [ ] Wording for blocked questions and the monthly limit added to `UX-COPY.md`
- [ ] **Decision memo written; Weeks 5 to 10 changed and posted**
