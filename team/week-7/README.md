# Week 7 in detail: Mon 23 Nov to Sat 28 Nov 2026

**Theme: uploads are safe.** Month overview: [`../MONTH-2.md`](../MONTH-2.md).

| Person | File | Hours |
|---|---|---|
| Shaan | [shaan.md](shaan.md) | 4 h a day |
| Akash | [akash.md](akash.md) | 4 h a day |
| Meghna | [meghna.md](meghna.md) | 3 h a day |
| Ranveer | [ranveer.md](ranveer.md) | When available, with deadlines |

**Week goal:** tests prove one user can never reach another's documents, and that a delete
removes everything. Users can delete their account and export their data. Knowledge notes
reach answers without ever being citations themselves, and the law maps are drafted. **All
200 test questions run for the first time.** The legal opinion arrives.

**Pipeline steps touched:** 3 (decide picks knowledge notes), 8 (answer reads them as
background). Step 9 (verify) is **not** changed.

**Tracking:** every task is a GitHub issue in the
[Week 7 milestone](https://github.com/ShaanRaza/LexBharat/milestone/7). **Status lives in the issues.**

| Person | Issues |
|---|---|
| Shaan | #134 notes design · #135 note checker · #136 notes in pipeline · #137 first full run · #140 careful reviews · #142 big upload + wrap |
| Akash | #138 isolation tests · #139 hard delete · #143 leftover check · #144 delete account · #145 export · #141 AWS basics |
| Meghna | #146 delete document · #147 law maps · #148 delete account + export screens |
| Ranveer | #149 legal opinion · #150 law maps + counsel + beta · #151 security quotes |

> **Written ahead of time.** Adjusted on Sat 21 Nov to match what really got done.

> **Tue 24 Nov is Guru Nanak Jayanti.** Each person's file says what moves if they take it
> off.

---

## Who waits on whom

| Who is waiting | For | From | Needed by |
|---|---|---|---|
| Meghna, Day 4 | `knowledge/check.py` | Shaan | **End of Day 2** |
| Meghna, Day 1 | The backup sentence for the delete screen | Shaan | Day 1 morning |
| Meghna, Day 5 | Delete-account and export routes | Akash | Days 4 and 5 |
| Shaan, Day 5 | Isolation tests and hard delete, for review | Akash | Days 1 and 2 |
| Shaan, Day 4 | The advocate's 200-question sign-off | Ranveer | Week 6 (otherwise "provisional") |
| **Shaan, Day 6** | **The backups bucket, with upload access** | **Akash** | **Sat 28 Nov, morning** |
| Ranveer, Day 6 | The readable law maps | Meghna | Sat 28 Nov |
| Shaan, Day 6 | The legal opinion | Ranveer | Sat 28 Nov |

## Never dropped, and finished this week

[`../V1-PLAN.md`](../V1-PLAN.md) §2 lists what can **never** be dropped to save time. This
week completes two of them: **the isolation tests** and **the hard delete**. They're
must-pass before any deploy from now on.

## Saturday: the long upload starts

The search collection (about 6 to 20 GB, Estimate) goes to S3 from Shaan's laptop. On a
home connection this may take **a day or more**, and Week 8 needs it on the server by
Friday. Starting it on Saturday is the plan's safety margin.

## Done means, by Saturday 28 Nov

- [ ] Isolation tests on every upload path; the shared function fails closed
- [ ] Hard delete from all three places; nightly leftover check; auto-delete on a setting (off)
- [ ] Delete account and export, with their screens
- [ ] Knowledge notes: only reviewed ones used; checker in CI; never a citation (tested)
- [ ] Three law maps drafted, checker green, **sent to the advocate**
- [ ] **First full 200-question run**; fix list ranked
- [ ] AWS account secured; **search collection upload to S3 running**
- [ ] Legal opinion received (or a firm new date); 25 beta yeses; security-test quotes asked
- [ ] Week 8 issues adjusted; **Standup: Week 8** opened
