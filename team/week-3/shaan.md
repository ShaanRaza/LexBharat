# Shaan: Week 3 (Data + Core + Lead), 4 h a day

**Theme: answers are verified.** This is the week the trust promise becomes code. By
Saturday the pipeline writes an answer from S1 to S8, **all four verifier checks** run on
every citation, failures are removed and logged, and the whole thing streams through
Akash's route to Meghna's screen.

Pipeline steps touched: **8 (answer), 9 (verify), 10 (show)**, and wiring steps 5 to 10
together.

**Read [`../../docs/CITATION-VERIFIER.md`](../../docs/CITATION-VERIFIER.md) again before
Monday.** Every rule in it is tested this week.

**Saturday is the re-plan.** Don't skip it.

---

## Before Day 1

- [ ] Week 2 leftovers first, especially the gate (step 7). This week needs it
- [ ] Gemini key with billing on, in `.env` (from Week 1). The answer step needs it

---

## Day 1, Mon 26 Oct: the answer step (8)

### 1.1 The prompt (1.5 h)
`core/prompts/answer.md`, a file rather than a string in code, so it can be read and
reviewed. It tells the model:
- Use **only** passages S1 to S8 (and background notes, once they exist in Week 7)
- Put the source label **after every point** taken from a passage: `[S3]`
- Quote **only** words that appear in the passage, inside quotation marks
- If the passages don't answer the question, say so. Don't fill gaps from memory
- Plain words; short; no advice on the user's own situation
- **Never** retype a citation string. The screen shows it from the record

### 1.2 `core/answer.py` (2 h)
Builds the prompt from the gated passages, calls `adapters/llm.py` with the model from
config, and **streams** the text back.

**The important rule:** the `[S3]` labels must **never reach the screen as text**
(CLAUDE.md §4 step 10: nothing citation-shaped before the citations event). As the text
streams, strip each label out and remember which sentence it belonged to. The verifier
gets the labels; the screen gets clean text.

Tests with the fake LLM: labels are stripped from every token; each label is matched to
the right sentence; a label split across two tokens (`[S` then `3]`) is still caught.

**Branch:** `shaan/answer-step`

**Ask Claude Code:**
> Read CLAUDE.md §4 and docs/CITATION-VERIFIER.md. Write core/prompts/answer.md and core/answer.py per team/week-3/shaan.md Day 1. The [S#] labels must be stripped from the streamed text and kept per sentence for the verifier, including labels split across tokens. Tests with the fake LLM. Explain the stripping logic in plain words.

---

## Day 2, Tue 27 Oct: the fourth check (claim supported)

### 2.1 Check 4 in `core/verify.py` (2.5 h)
Your three free checks went in during Week 1. Now add the fourth:
- For each (sentence, passage) pair, ask the decisions adapter: **supports / partly /
  does not support**, all pairs **in parallel**
- **Supports** → tick. **Partly** → warning mark. **Does not support** → removed, reason
  `claim_not_supported`
- Checks 1 to 3 run **first** and **always**. Check 4 only runs on citations that passed them
- In upload chats (later) this check goes to Gemini, never Jev. The adapter's guard
  already enforces it; pass the flag

### 2.2 When Jev is off or slow (1 h)
Tests for both:
- **Jev switched off** → the Gemini fallback answers with the same three choices
- **Jev times out** (over 800 ms) → the fallback answers, and the answer is still on time
- **Both fail** → checks 1 to 3 still decide; the citation shows a warning mark, never a
  tick. **Never** pass a citation that check 4 couldn't look at as if it had

**Branch:** `shaan/verifier-claim-check`

---

## Day 3, Wed 28 Oct: what happens on failure

### 3.1 Remove, note, log (2 h)
When any check fails:
1. The citation is **removed** from the result (it never reaches the citations event)
2. `removed_count` goes up, and the screen shows the note that one authority couldn't be
   verified
3. A row goes to `invented_citation_log`: question, model, the failed citation, the reason.
   Written through `core/store/` (ask Akash for a `log_invented_citation(...)` function on
   Monday)

### 3.2 The must-pass tests (2 h)
CLAUDE.md rule 6: these must pass before **any** deploy. One test per reason, each proving
the citation is **removed and logged**:

| Reason | The test |
|---|---|
| `not_retrieved` | The model cites `[S9]`, or a real case it wasn't given |
| `record_missing` | The passage's `record_id` isn't in the collection |
| `quote_not_found` | A quoted phrase that isn't in the record's text |
| `claim_not_supported` | The adapter says "does not support" |

Plus: an answer where **every** citation fails still streams its text, shows the note, and
sends an empty citations list.

**Branch:** `shaan/verifier-failures`

---

## Day 4, Thu 29 Oct: wire steps 5 to 10 together

### 4.1 The real `core/pipeline.py` (3 h)
Replace the stubs with the real steps: **search → re-rank → gate → answer → verify → show**.
Steps 1 to 4 (remember, rewrite, decide, cache) stay as simple pass-throughs until Week 4.

The three short paths:

| Situation | What happens |
|---|---|
| Gate finds nothing relevant | "Not found" event. **No answer is written**, so no model cost |
| The model fails or times out | The passages are sent **with links but no written answer**, and a retry is offered |
| Meaning search is down | Keyword-only results, marked so the screen can label them |

The citations event carries the data-as-of date (from `court_coverage`), the CC BY credit
and the not-legal-advice notice. Never typed in code: from settings and the strings.

### 4.2 Hand over to Akash (30 min)
Tell Akash in the standup that the real `run(...)` is merged. His route switches from the
fake with **no code change**, which is the point of last week's contract.

**Branch:** `shaan/pipeline-wired`

---

## Day 5, Fri 30 Oct: the first real answers

### 5.1 Ten real questions (2.5 h)
Run 10 questions from the interview notes in `docs/research/` through the real pipeline on
the SSD collection. For each, record in `evals/runs/week3-first-answers.md`:
- The answer, and every citation with tick, warning or removed (and why)
- Time to first word, total time
- Your verdict: right / partly / wrong, and what an advocate would object to

### 5.2 Joint check with Akash and Meghna (1 h)
One call: ask a question on Meghna's screen, through Akash's route, on your pipeline.
Watch for **a citation appearing before the text finishes**. That must never happen.

---

## Day 6, Sat 31 Oct: the re-plan

### 6.1 The honest numbers (2 h)
V1-PLAN.md §8: **the end of Week 3 is a real re-plan.**
- [ ] For each person: tasks planned in Weeks 1 to 3 vs done. Hours planned vs spent
      (from the standups)
- [ ] If Weeks 1 to 3 took noticeably longer, **the rest will too**. Either move the MVP
      date or use the drop list in [`../V1-PLAN.md`](../V1-PLAN.md) §2, and **say which, out
      loud**, in the standup issue
- [ ] Update `V1-PLAN.md` (it's version 2; this makes version 3) and adjust the Week 4 issues
- [ ] Never cut the verifier, the isolation tests or the 200-question runs

### 6.2 Wrap the week (1 h)
- [ ] Tick "Done means" in [README.md](README.md) honestly
- [ ] Open **Standup: Week 4**
- [ ] `docker stop qdrant && colima stop`

---

## Pull requests to expect, by day

| Day | From Akash | From Meghna | Yours |
|---|---|---|---|
| 1 | `akash/firebase-auth` | `meghna/stream-client` | `shaan/answer-step` |
| 2 | `akash/me-route` | `meghna/chat-real-events` | `shaan/verifier-claim-check` |
| 3 | `akash/stream-route` | `meghna/chat-conversations` | `shaan/verifier-failures` |
| 4 | `akash/stream-order-test` | `meghna/jump-to-passage` | `shaan/pipeline-wired` |
| 5 | `akash/auth-everywhere` | `meghna/source-panel` | `shaan/first-answers` |
| 6 | | `meghna/week3-polish` | `shaan/replan` |

**Review the streaming route (`akash/stream-route`) and the order test with the same care
as the verifier.** A citation leaking early breaks the trust promise as surely as a fake one.

## Done by Saturday

- [ ] Answer step with labels stripped from the stream and kept per sentence
- [ ] All four checks; Jev-off, Jev-timeout and both-fail paths tested
- [ ] One must-pass test per failure reason, proving removal and logging
- [ ] Steps 5 to 10 wired; not-found and model-failure paths work
- [ ] 10 real questions answered and written up
- [ ] **Re-plan done and posted**; V1-PLAN.md version 3
