# Week 5 in detail: Mon 9 Nov to Sat 14 Nov 2026

**Theme: measured.** Month overview: [`../MONTH-2.md`](../MONTH-2.md).

| Person | File | Hours |
|---|---|---|
| Shaan | [shaan.md](shaan.md) | 4 h a day (light Monday) |
| Akash | [akash.md](akash.md) | 4 h a day (light Monday) |
| Meghna | [meghna.md](meghna.md) | 3 h a day (light Monday) |
| Ranveer | [ranveer.md](ranveer.md) | When available, with deadlines |

**Week goal:** the guesses become measurements. 50 real questions decide the models, the
gate threshold and the Jev switches. Uploaded files have a safe place to land, a worker to
process them, and **one shared function** guarding every query on them. The legal drafts go
to counsel.

**Pipeline steps touched:** measured, not changed: 3 (decide), 7 (gate), 8 (answer),
9 (verify). Upload groundwork (no answers from uploads yet).

**Tracking:** every task is a GitHub issue in the
[Week 5 milestone](https://github.com/ShaanRaza/LexBharat/milestone/5). **Status lives in the issues.**

| Person | Issues |
|---|---|
| Shaan | #94 pick 50 · #95 test runner · #96 baseline · #97 model choice · #98 Jev + threshold · #99 upload design + drop-list check |
| Akash | #100 MinIO · #101 upload link · #102 status + list · #103 worker · #104 file checks + feedback · #105 shared uploads function |
| Meghna | #106 upload screen · #107 progress · #108 status · #109 documents list |
| Ranveer | #110 legal drafts to counsel · #111 outside answers · #112 beta plan |

> **Written before Month 1 happened.** On Sat 7 Nov Shaan checks
> [`../MONTH-2.md`](../MONTH-2.md) ("What Month 2 assumes is done") and adjusts this week.
> **The Week 4 decision memo wins over this file.**

> **Mon 9 Nov (Govardhan Puja) is a light day. Wed 11 Nov is Bhai Dooj.** Each person's
> file says what moves if they take Wednesday off.

---

## Who waits on whom

| Who is waiting | For | From | Needed by |
|---|---|---|---|
| Shaan, Day 2 | All 11 pipeline steps working (Month 1) | Shaan | Day 2 |
| Shaan, Day 1 | Real questions in `evals/questions.jsonl` | Meghna (Week 4) | Day 1 |
| Meghna, Day 2 | Upload link route | Akash | Day 2 (she builds against a mock until then) |
| Meghna, Day 4 | Status route | Akash | Day 3 |
| Akash, Day 6 | Shaan's review of the shared uploads function | Shaan | **Same day** |
| Shaan, Day 6 | Voyage status | Ranveer | Fri 13 Nov |
| Shaan, Day 6 | Planned vs done from everyone (the drop-list check) | All | Sat 14 Nov morning |

## Two decisions made from evidence this week

1. **Models, threshold, Jev switches** (Shaan, Days 4 and 5): recorded with `/decision`,
   with the numbers, labelled **Measured**.
2. **The Week 5 drop-list check** (Shaan, Day 6): [`../V1-PLAN.md`](../V1-PLAN.md) §2. If
   Weeks 1 to 5 ran long, use the drop list, **out loud**.

## Done means, by Saturday 14 Nov

- [ ] The test runner scores citations, behaviour, speed and cost
- [ ] 50 real questions run; models, gate threshold and Jev switches chosen and recorded
- [ ] Upload links, completion check, status and list, behind `FEATURE_UPLOADS`
- [ ] Worker: 1 CPU, one job at a time
- [ ] **Shared uploads function that fails closed, with a build-failing guard test**
- [ ] Upload screens: limits and warning first, resumable upload, status, list
- [ ] Five legal drafts **sent to counsel** with the retention questions
- [ ] Drop-list check posted; Week 6 issues adjusted; **Standup: Week 6** opened
