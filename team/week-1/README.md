# Week 1 in detail: Tue 13 Oct to Sat 17 Oct 2026

Everyone's detailed task list:

| Person | File | Hours |
|---|---|---|
| Shaan | [shaan.md](shaan.md) | 4 h a day |
| Akash | [akash.md](akash.md) | 4 h a day |
| Meghna | [meghna.md](meghna.md) | 3 h a day |
| Ranveer | [ranveer.md](ranveer.md) | When available, with deadlines |

**Week goal:** everyone is building in parallel from Day 1. By Saturday the search data is
built, the API answers its first routes, the first screens work on sample data, and the
legal requests for uploads are sent.

**Tracking:** every task below is a GitHub issue in the
[Week 1 milestone](https://github.com/ShaanRaza/LexBharat/milestone/1). **Status lives in the
issues** (open, in progress, in review, closed). These files hold the detail and the
reasoning, so don't tick progress in both places.

| Person | Issues |
|---|---|
| Shaan | #6 SC counts · #7 practice dataset · #8 streaming format · #9 keys · #15 build collection · #16 check collection · #17 adapters · #18 verifier · #19 wrap week |
| Akash | #10 Python + CI · #11 Compose + Alembic · #12 API skeleton · #13 tables · #14 routes |
| Meghna | #20 web app · #21 app shell · #22 chat screen · #23 failure screens · #24 judgment + Act pages |
| Ranveer | #25 legal opinion · #26 Voyage terms · #27 Vaquill · #28 script + list · #29 interviews · #30 GitHub account |

Every task with a pull request runs as **one Claude session**: `/start-task <number>`, then
`/finish-task <number>`.

---

## How every task in these files is written

- **Time box:** stop and say so in the standup if you go over by half.
- **Branch / PR:** the branch to make and the pull request to open.
- **Done when:** the check that proves it's finished. If you can't tick it, it isn't done.
- **Ask Claude Code:** a starting prompt you can paste. Claude reads `CLAUDE.md` itself;
  the prompt just points it at the task.

## Daily rhythm

| When | What |
|---|---|
| Start of every session | `git pull origin main`, then create or switch to your branch |
| During the day | Small commits; open the pull request as soon as one task is done |
| By 10 PM | Standup comment on [issue #5](https://github.com/ShaanRaza/LexBharat/issues/5) |
| Shaan, daily | 30 minutes reviewing and merging pull requests (expected ones listed in [shaan.md](shaan.md)) |
| 11:52 PM | The nightly log writes the team note in Obsidian |

## Day 1 kickoff call: 30 minutes, all four

1. Who does what: the four lanes, from [`../README.md`](../README.md) (5 min)
2. The one rule that matters: branches and pull requests only; Shaan merges (3 min)
3. The trust promise in one sentence: never show a citation that wasn't checked (2 min)
4. Walk through this week's dependencies, below (10 min)
5. Ranveer's two urgent requests: the legal opinion and Voyage's terms (5 min)
6. Questions (5 min)

## Who waits on whom

| Who is waiting | For | From | Needed by |
|---|---|---|---|
| Akash, Day 3 (load the practice data into Qdrant) | Practice dataset | Shaan | **End of Day 2** |
| Meghna, Day 3 (chat screen) | Streaming event shapes in `docs/API.md` | Shaan + Akash | **End of Day 2** |
| Meghna, Day 5 (judgment and Act pages) | The two routes, or the fixture files | Akash / Shaan | Day 5 (she uses fixtures if routes aren't merged) |
| Shaan, Day 5 (verifier tests) | Python and pytest setup merged | Akash | **End of Day 1** |
| Akash, Day 4 (migrations merged) | Shaan's review | Shaan | Day 4 evening |
| Everyone, all week | Akash accepting the GitHub invite | Akash | **Before Day 1** |
| Uploads for real lawyers (Week 8) | Legal opinion + Voyage terms | Ranveer | **Requested this week** |

## Two shared agreements made this week

1. **The streaming answer format** (Day 2, Shaan + Akash, 20 min). Meghna's chat screen is
   built against it on Day 3, and Akash's real route follows it in Week 3. Starting draft is
   in [shaan.md](shaan.md), Day 2.
2. **The practice dataset** (Day 2, Shaan). Everyone develops against it until the real
   search collection is on the server. Its contents are in [shaan.md](shaan.md), Day 1.

## Done means, by Saturday 17 Oct

- [ ] Practice dataset in `tests/fixtures/` (under 5 MB) and documented
- [ ] Search collection built on the SSD; counts checked; 20 searches checked by hand
- [ ] Python and web CI checks both green on `main`
- [ ] `docker compose up` starts PostgreSQL, Redis and Qdrant on every builder's laptop
- [ ] API: health check, an Act section and a judgment, each with a request ID
- [ ] Database tables created by migration and reviewed by Shaan
- [ ] Chat screen, every failure screen, judgment page and Act page working on sample data
- [ ] Streaming format written in `docs/API.md`
- [ ] Legal opinion, Voyage terms and Vaquill emails **sent**; 5 interviews booked
- [ ] `team/WEEK-2.md` and the Week 2 issues adjusted by Shaan on Saturday
