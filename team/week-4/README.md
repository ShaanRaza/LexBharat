# Week 4 in detail: Mon 2 Nov to Sat 7 Nov 2026

**Theme: the whole engine.**

| Person | File | Hours |
|---|---|---|
| Shaan | [shaan.md](shaan.md) | 4 h a day |
| Akash | [akash.md](akash.md) | 4 h a day |
| Meghna | [meghna.md](meghna.md) | 3 h a day |
| Ranveer | [ranveer.md](ranveer.md) | When available, with deadlines |

**Week goal:** all 11 pipeline steps are real. Answers are counted before any AI call,
consent comes before first use, and monitoring can't see private text. The 20 interviews
are finished and turned into decisions.

**Pipeline steps touched:** 1 (remember), 2 (rewrite), 3 (decide), 4 (cache), and the usage
meter that guards step 8.

**Tracking:** every task is a GitHub issue in the
[Week 4 milestone](https://github.com/ShaanRaza/LexBharat/milestone/4). **Status lives in the issues.**

| Person | Issues |
|---|---|
| Shaan | #74 remember · #75 rewrite · #76 decide · #78 cache + full run · #80 decision memo · #81 wrap week |
| Akash | #77 usage meter · #82 limits + tests · #83 consent · #84 Langfuse · #85 Sentry |
| Meghna | #86 sign-in · #87 consent + role · #88 answers left · #89 200-question set · #90 lookups + check |
| Ranveer | #79 interviews 17–20 + summary · #91 decision memo · #92 questions to advocate · #93 counsel + status |

> **Written ahead of time, and the re-plan comes first.** The Week 3 re-plan (Sat 31 Oct)
> may change this week. Where they disagree, the re-plan wins.

> **Fri 6 Nov is Dhanteras and Sat 7 Nov is Choti Diwali** (Diwali is Sun 8 Nov). The
> decision point is on **Friday**, and **Saturday is light for everyone**: catch-up and the
> standup only. That's about 8 hours fewer than the V1 plan assumed. This week's tasks
> already fit into Monday to Friday.

---

## Who waits on whom

| Who is waiting | For | From | Needed by |
|---|---|---|---|
| Akash, Day 1 | The counting rule (does not-found count? does a model failure?) | Shaan + Akash | **Day 1** |
| Shaan, Day 4 (cache) | The meter reading the `from_cache` flag | Akash | Day 2 |
| Akash, Day 4 | Span names for each pipeline step | Shaan | Day 3 |
| Meghna, Day 2 | Consent routes | Akash | Day 3 (she builds against the OpenAPI types until then) |
| Meghna, Day 3 | Wording for the monthly limit and blocked questions | Shaan | **Day 3** |
| Meghna, Day 4 | The 50 trap questions | Ranveer | Already due Fri 30 Oct |
| Shaan + Ranveer, Day 5 | All 20 interviews and the one-page summary | Ranveer | **Thu 5 Nov** |
| Ranveer, Day 6 | `evals/questions-for-review.md` | Meghna | Fri 6 Nov |

## Friday: the decision point

[`../V1-PLAN.md`](../V1-PLAN.md): **the interviews may change what lawyers need**: prices,
Hindi, phone versus desktop, whether they'd upload at all. Shaan and Ranveer write
`docs/research/decision-memo-week4.md`, and Weeks 5 to 10 change **now, not later**.

Uploads start in Week 5. If the interviews say lawyers won't upload client documents, that's
the moment to decide what uploads look like in the MVP.

## Done means, by Saturday 7 Nov

- [ ] Remember, rewrite, decide and cache all real, with tests
- [ ] All 11 steps run on 20 real questions; time to first word recorded
- [ ] Usage meter: counted before any AI call, cache hits free, safe at the same moment;
      must-pass tests green
- [ ] Consent required before first use; withdraw works; draft notice clearly marked
- [ ] Langfuse masked and Sentry scrubbed, both tested
- [ ] Real sign-in, consent and answers-left screens
- [ ] `evals/questions.jsonl` started (traps, real questions so far, 50 lookups) and sent to
      the advocate
- [ ] 20 interviews done and summarised; **decision memo written; Weeks 5 to 10 updated**
