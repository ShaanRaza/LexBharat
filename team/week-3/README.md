# Week 3 in detail: Mon 26 Oct to Sat 31 Oct 2026

**Theme: answers are verified.**

| Person | File | Hours |
|---|---|---|
| Shaan | [shaan.md](shaan.md) | 4 h a day |
| Akash | [akash.md](akash.md) | 4 h a day |
| Meghna | [meghna.md](meghna.md) | 3 h a day |
| Ranveer | [ranveer.md](ranveer.md) | When available, with deadlines |

**Week goal:** a signed-in user asks a real question and gets a streamed answer where
**every citation has passed all four checks**, or was removed and logged. The answer is
saved in a conversation. The 50 trap questions exist.

**Pipeline steps touched:** 8 (answer), 9 (verify), 10 (show), 11 (save), and steps 5 to 10
wired together for the first time.

**Tracking:** every task is a GitHub issue in the
[Week 3 milestone](https://github.com/ShaanRaza/LexBharat/milestone/3). **Status lives in the issues.**

| Person | Issues |
|---|---|
| Shaan | #54 answer step · #55 check 4 · #57 on failure · #58 wire steps 5–10 · #59 first answers · #60 re-plan |
| Akash | #56 Firebase auth · #61 /me · #62 streaming route · #63 order test · #64 auth everywhere |
| Meghna | #65 stream reader · #66 real events · #67 saved chats · #68 jump to passage · #69 source panel · #70 polish |
| Ranveer | #71 interviews 11–16 · #72 trap questions · #73 status + numbers |

> **Written ahead of time.** Shaan adjusts this on Sat 24 Oct to match what really got done
> in Week 2. Unfinished Week 2 work goes **first**.

---

## Who waits on whom

| Who is waiting | For | From | Needed by |
|---|---|---|---|
| Shaan, Day 3 | `log_invented_citation(...)` in `core/store/` | Akash | **End of Day 1** |
| Akash, Day 4 | The real `core.pipeline.run(...)` | Shaan | End of Day 4 (Akash builds on the fake until then) |
| Meghna, Day 1 | The streaming route | Akash | Day 3 (she uses the fake pipeline locally until then) |
| Meghna, Day 4 | Agreement on how a citation finds its paragraph | Shaan + Meghna | **Day 1** |
| Meghna, Week 4 (the 200-question set) | 50 trap questions | Ranveer + advocate | Fri 30 Oct |
| Shaan, Day 6 | Everyone's planned vs done numbers | All | Sat 31 Oct morning |

## Two checks this week that guard the trust promise

1. **The four failure tests** (Shaan): one per reason, each proving the citation is removed
   and logged.
2. **The order test** (Akash): one citations event, after the text, never after an error,
   with no source label in any token.

Both are **must-pass before any deploy** (CLAUDE.md rule 6). Shaan reviews both with care.

## Friday: the first joint check

All three builders, one call, Day 5. A real question on Meghna's screen, through Akash's
route, on Shaan's pipeline. **Watch for any citation showing before the text finishes.**

## Saturday: the re-plan

[`../V1-PLAN.md`](../V1-PLAN.md) §8: the end of Week 3 is a **real re-plan**. Everyone sends
Shaan their tasks planned vs done and hours by Saturday morning. If it's slipping, the date
moves or the drop list is used, **out loud** in the standup issue. Quietly squeezing later
weeks isn't allowed.

## Done means, by Saturday 31 Oct

- [ ] The answer step streams clean text; source labels never reach the screen
- [ ] All four verifier checks; Jev-off, Jev-timeout and both-fail paths tested
- [ ] One must-pass test per failure reason, proving removal and logging
- [ ] Real sign-in through Firebase; every non-public route refuses without a token
- [ ] Streaming route on the real pipeline; the order test passes
- [ ] Chat screen on the real stream, saving conversations; citations jump to the passage
- [ ] 10 real questions answered and written up in `evals/runs/`
- [ ] Interviews reach 16; the 50 trap questions written
- [ ] **Re-plan posted**; `V1-PLAN.md` version 3; Week 4 issues adjusted
