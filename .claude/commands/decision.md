---
description: Record a decision in docs/DECISIONS.md — move an open row to settled, or add a new one, with the evidence that settled it.
argument-hint: "<the decision, and what settled it>"
---

# /decision

Record this decision: **$ARGUMENTS**

1. Read `docs/DECISIONS.md`.
2. If it matches an **open** row, move that row to **Settled** with the date and the
   evidence. Do not leave it in both places.
3. If it is new, add it to Settled with a one-line *why*.
4. If it was one of the **top 5 questions before any code**, update that table too and say
   so — those gate real work.
5. If it contradicts the PRD or the Tech Stack, note which and that the Tech Stack wins on
   engineering.
6. Carry the evidence label: **Measured**, **Checked**, **Dataset card**,
   **Competitor claim**, **Estimate** or **Needs verification**. Do not promote an Estimate
   to a fact without a measurement.
7. If the decision changes a number used elsewhere — a passage count, a threshold, a price,
   a limit — update those files in the same change and list them.

If the decision is not actually settled, say so and leave it open rather than recording a
guess.
