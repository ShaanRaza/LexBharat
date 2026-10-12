# Month 2: Weeks 5 to 8, Mon 9 Nov to Sat 5 Dec 2026

**Month 1 built the engine. Month 2 measures it, adds uploads, makes uploads safe, and puts
everything on the real server.**

Every task is a GitHub issue: **#94 to #169**, in the Week 5 to Week 8 milestones
([5](https://github.com/ShaanRaza/LexBharat/milestone/5) ·
[6](https://github.com/ShaanRaza/LexBharat/milestone/6) ·
[7](https://github.com/ShaanRaza/LexBharat/milestone/7) ·
[8](https://github.com/ShaanRaza/LexBharat/milestone/8)).

| Week | Dates | Theme | By Saturday | Summary |
|---|---|---|---|---|
| **5** | 9 to 14 Nov | **Measured** | 50 real questions measured; models, gate threshold and Jev switches chosen from evidence. Upload storage and the worker skeleton | [WEEK-5.md](WEEK-5.md) |
| **6** | 16 to 21 Nov | **Uploads work** | Text PDFs, Word files and scans become searchable; questions answered from your own document, kept apart from the judgments | [WEEK-6.md](WEEK-6.md) |
| **7** | 23 to 28 Nov | **Uploads are safe** | Isolation tests that fail closed; hard delete; account deletion and export. Knowledge notes; law maps drafted. **First full 200-question run** | [WEEK-7.md](WEEK-7.md) |
| **8** | 30 Nov to 5 Dec | **On the real server** | Live on AWS in Mumbai; prompt-injection review done; **uploads go/no-go** | [WEEK-8.md](WEEK-8.md) |

---

## Written before Month 1 has happened

Today is 12 Oct. Week 1 hasn't started, so this month is planned from what Month 1 is
**supposed** to deliver. On **Sat 7 Nov** Shaan checks the list below against what really
happened, and adjusts Week 5 first.

### What Month 2 assumes is done by Sat 7 Nov

| From Month 1 | Needed by | If it isn't done |
|---|---|---|
| All 11 pipeline steps real, with tests (Weeks 2 to 4) | Week 5, Day 2 (the measuring runs) | Week 5 finishes the pipeline instead; measuring moves to Week 6 and **uploads slip a week** |
| The four verifier failure tests and the order test pass | Always | **Stop and fix first.** Nothing else matters if these fail |
| Usage meter, consent, masking and scrubbing | Week 8 (going live) | Akash finishes them in Week 5 before upload storage |
| `evals/questions.jsonl`: traps, lookups, real questions | Week 5 (50 real), Week 7 (all 200) | Run what exists, and say the run is partial |
| Decision memo (Week 4) | Week 5, Day 1 | **The memo wins over this file.** If it changes uploads, Hindi or devices, re-plan Weeks 5 to 8 first |
| Firebase sign-in on the website | Week 8 | Meghna finishes it in Week 5 |

## The rules this month adds

1. **Upload text never reaches Jev, Langfuse (unmasked) or Sentry.** Every upload path is
   tested for this.
2. **Every query on uploads goes through one shared function** that always adds `user_id`.
   It's built in **Week 5**, before anything writes to the uploads collection. (The V1 plan
   had it in Week 7. Building it first means nothing is ever written around it.)
3. **No real client documents in development, ever.** Test with public documents only:
   judgment PDFs from the dataset's own `pdf_url` links, and agreements written for testing.
4. **Uploads stay switched off for users** (`FEATURE_UPLOADS`) until the Week 8 go/no-go.
5. **Never touch the server directly.** From Week 8, GitHub Actions deploys.

## Decisions this month (Shaan decides; recorded with `/decision`)

| Week | Decision | Decided from |
|---|---|---|
| 5 | Model per plan (`MODEL_FREE`, `_STUDENT`, `_PRO`), the gate threshold, each `JEV_ENABLED_*` switch | The 50-question runs |
| 5 | Is there time for everything? (the **Week 5 drop-list check** in [V1-PLAN.md](V1-PLAN.md) §2) | Planned vs done, Weeks 1 to 5 |
| 6 | Upload embeddings: **voyage-4 or bge-m3** (the free local model in `docs/DECISIONS.md`) | Voyage's written terms, if they've arrived |
| 6 | Upload limits (`UPLOAD_MAX_MB`, `UPLOAD_MAX_PAGES`) and the OCR quality threshold | OCR timing on 20 real public scans |
| 6 | Where a "page" is in a Word file (Word has no fixed pages) | Akash's proposal |
| 7 | How knowledge notes reach an answer without breaking check 1 | Shaan's design, before building |
| 6 | The domain the server uses (the product name isn't cleared) | Trademark result |
| 8 | **Uploads go/no-go** for real client documents | Legal opinion + Voyage terms + the interviews |

## People outside the team (Ranveer owns these)

| What | Due | If it's late |
|---|---|---|
| Consent notice, privacy policy, terms, upload warning: **drafts sent to counsel** | **Fri 13 Nov** | Counsel's review must be back by **Week 9**, or **the beta can't open** |
| Retention periods from counsel (`docs/RETENTION.md`) | With the drafts | The consent notice can't be finished without them |
| Advocate signs off the 200 questions | **Week 6** | Week 7's run is marked provisional |
| **Advocate's written legal opinion** | **Sat 28 Nov** | Uploads ship with the "don't upload client documents yet" warning |
| Voyage's written upload terms | Week 6 | Uploads use bge-m3 on our own server |
| Advocate reviews the law maps | Sent Week 7, back Week 9 | Those notes stay out of live answers |
| Beta recruits: 20 students + 10 advocates | List final in Week 8 | The beta starts smaller |

## Holidays

| Date | Day | What the plan does |
|---|---|---|
| Mon 9 Nov | Govardhan Puja (the day after Diwali) | **Light day** for everyone |
| Wed 11 Nov | Bhai Dooj | Each file says which task moves if you take it off |
| Tue 24 Nov | Guru Nanak Jayanti | Each file says which task moves |

Dates checked on 12 Oct against published 2026 calendars; regional practice varies.

## Capacity

About **66 hours a week** (Shaan 24, Akash 24, Meghna 18), minus about 8 hours in Week 5
for the light Monday: roughly **255 hours** this month. Weeks 5 to 8 in the V1 plan need
about the same. **There's no slack in Month 2.** Anything that slips goes to Week 11 (the
only buffer) or down the drop list, said out loud.

## The two most likely problems

1. **The search collection is large to move.** About 42 to 55 GB (Estimate). Uploading it to
   S3 from a home connection may take **a day or more**. That's why Shaan starts the upload
   on **Sat 28 Nov**, not on the day it's needed.
2. **OCR is slow on one CPU.** Scans may miss the 5-minute target. Week 6 measures it, and
   the upload limits are set from that measurement, not guessed.
