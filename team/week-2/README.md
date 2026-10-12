# Week 2 in detail: Mon 19 Oct to Sat 24 Oct 2026

**Theme: search works.**

| Person | File | Hours |
|---|---|---|
| Shaan | [shaan.md](shaan.md) | 4 h a day |
| Akash | [akash.md](akash.md) | 4 h a day |
| Meghna | [meghna.md](meghna.md) | 3 h a day |
| Ranveer | [ranveer.md](ranveer.md) | When available, with deadlines |

**Week goal:** a question goes through search → re-rank → relevance gate and comes out as at
most 8 checked-for-relevance passages. The API has conversations and direct search. The
screens read from the real API. Interviews reach 10.

**Pipeline steps touched:** 5 (search), 6 (re-rank), 7 (gate), plus the decisions adapter
used by steps 3 and 7.

**Tracking:** every task is a GitHub issue in the
[Week 2 milestone](https://github.com/ShaanRaza/LexBharat/milestone/2). **Status lives in the issues.** These files hold the
detail and the reasoning.

| Person | Issues |
|---|---|
| Shaan | #31 pipeline contract · #32 load PostgreSQL · #33 search · #34 re-rank · #35 decisions adapter · #36 gate · #37 wrap week |
| Akash | #38 dev user · #39 conversations · #40 paging + audit · #41 search route · #42 OpenAPI + Firebase · #43 CI database |
| Meghna | #44 API client · #45 real pages · #46 conversation list · #47 history · #48 sign-in mock · #49 Act lookup |
| Ranveer | #50 interviews 4–10 · #51 legal opinion date · #52 Voyage · #53 trademark |

Every task with a pull request runs as **one Claude session**: `/start-task <number>`, then
`/finish-task <number>`.

> **This plan was written before Week 1 finished.** On Sat 17 Oct Shaan adjusts it to what
> really got done. Unfinished Week 1 work goes **first**, ahead of anything here.

> **Tue 20 Oct is Dussehra.** Each person's file says which task moves if they take the day
> off. Say so in the standup on Monday, so the plan changes out loud.

---

## Who waits on whom

| Who is waiting | For | From | Needed by |
|---|---|---|---|
| Akash (all week) and Meghna (Week 3) | **The pipeline contract** (`core/types.py`, `core/pipeline.py`, the fake) | Shaan | **End of Day 1** |
| Akash, Day 1 | The three contract decisions (`core/store/`, fake adapters, what the route calls) | Shaan + Akash call | Day 1 |
| Akash, Day 4 (search route) | `core/search.py` | Shaan | End of Day 3 (Akash uses the fake if it's late) |
| Shaan, Day 6 (gate) | The decisions adapter | Shaan | Day 5 |
| Meghna, Day 3 (conversation list) | `GET /conversations` | Akash | End of Day 2 (she uses a mock if it's late) |
| Meghna, Day 1 | The OpenAPI file | Akash | She fetches it from her local API until Akash commits the copy on Day 5 |
| Akash, Day 2 onwards | Shaan's review of `core/store/` | Shaan | Same day |

## Shared agreements this week

1. **The pipeline contract** (Day 1, Shaan, with Akash on a 30-minute call). Every step's
   input and output, and a fake pipeline that streams in the agreed format. Week 3 builds
   the real thing behind it without changing the route or the screen.
2. **Database code lives in `core/store/`.** Akash writes it, Shaan reviews it.
3. **`USE_FAKE_ADAPTERS`**: dev laptops run with fakes and no paid keys. The app refuses to
   start with it on outside dev.

All three are recorded with `/decision` in `docs/DECISIONS.md`.

## Done means, by Saturday 24 Oct

- [ ] Pipeline contract merged; the three decisions recorded
- [ ] All Supreme Court cases and Act sections in PostgreSQL; counts recorded as Measured
- [ ] Search (meaning + keyword + exact lookup, top 50) → re-rank (top 10) → gate (at most
      8, S1 to S8) working on the SSD collection
- [ ] Search stage timed against the 800 ms target
- [ ] Decisions adapter with the Gemini fallback; upload text can never reach Jev (tested)
- [ ] Conversation routes and `GET /search`, with the cross-user test running in CI
- [ ] Judgment page, Act page and conversation list on the real API; Act lookup page
- [ ] Sign-in screens on a mock
- [ ] Interviews 4 to 10 done; legal opinion date agreed in writing; trademark search started
- [ ] Week 3 issues adjusted; **Standup: Week 3** issue opened
