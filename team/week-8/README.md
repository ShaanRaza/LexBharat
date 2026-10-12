# Week 8 in detail: Mon 30 Nov to Sat 5 Dec 2026

**Theme: on the real server.** Month overview: [`../MONTH-2.md`](../MONTH-2.md).

| Person | File | Hours |
|---|---|---|
| Shaan | [shaan.md](shaan.md) | 4 h a day |
| Akash | [akash.md](akash.md) | 4 h a day |
| Meghna | [meghna.md](meghna.md) | 3 h a day |
| Ranveer | [ranveer.md](ranveer.md) | When available, with deadlines |

**Week goal:** the whole product runs on one AWS server in Mumbai, deployed only by GitHub
Actions, backed up daily, and watched with private text masked. The worst failures from the
first full run are fixed. The product has been attacked with hostile questions and hostile
documents, and what got through is fixed. **Uploads go/no-go decided.**

**Pipeline steps touched:** whatever the fix list names (most likely 5, 7 and 8), the safety
part of 3, and the upload path of 8.

**Tracking:** every task is a GitHub issue in the
[Week 8 milestone](https://github.com/ShaanRaza/LexBharat/milestone/8). **Status lives in the issues.**

| Person | Issues |
|---|---|
| Shaan | #152 fix list · #153 injection review · #154 injection fixes · #157 collection on server · #159 go/no-go + month review |
| Akash | #155 EC2 · #156 prod Compose · #160 deploy workflow · #161 data + backups · #162 monitoring · #163 smoke test |
| Meghna | #164 PWA · #165 phone pass · #166 accessibility · #167 prod build · #168 live check |
| Ranveer | #158 legal follow-up + go/no-go · #169 beta list + chases |

> **Written ahead of time.** Adjusted on Sat 28 Nov to match what really got done.

---

## Who waits on whom

| Who is waiting | For | From | Needed by |
|---|---|---|---|
| Shaan + Akash, Day 5 | **The search collection in S3** (upload started Sat 28 Nov) | Shaan | **Day 5**; check it on Day 1 |
| Akash, Day 1 | The domain | Shaan + Ranveer (Week 6) | Day 1 |
| Akash, Day 4 | A dump of the local `cases` and `act_sections` | Shaan | Day 3 |
| Meghna, Day 5 | Production Compose and the domain | Akash | Day 2 |
| Everyone, from Day 3 | The deploy workflow, reviewed | Akash → Shaan | Day 3 |
| Shaan + Ranveer, Day 6 | The legal opinion's open questions answered | Ranveer | Wed 2 Dec |
| Meghna, Day 6 | The live server | Akash | Day 5 |

## From this week, the rules change

- **Code reaches the server only through the deploy workflow.** Nobody logs in to change
  things by hand (CLAUDE.md §6)
- **The must-pass tests gate every deploy** (`docs/TESTING.md`)
- **Real users don't arrive until the beta.** The server is live but private: the domain
  isn't shared, and uploads stay switched off for users until the go/no-go says otherwise

## The uploads go/no-go (Saturday)

Shaan and Ranveer decide, from the legal opinion, the upload embedding choice, the
interviews and the safety work. Three outcomes: **on for client documents / on with a
"don't upload client documents yet" warning / off for the beta.** Recorded with
`/decision`; the switch is set in Week 10.

## Done means, by Saturday 5 Dec

- [ ] Top of the fix list fixed, with before and after numbers
- [ ] Prompt-injection review done; every attack is a test; what got through is fixed
- [ ] Server live in Mumbai over HTTPS; only the website and API reachable
- [ ] Deploy workflow: tests first, ARM images, health check, rollback
- [ ] Search collection and corpus tables on the server; counts match
- [ ] Daily backups, with **one restore tested**; masking and scrubbing checked live; alerts on
- [ ] Installable; phone, slow-network and accessibility passes done; every screen checked live
- [ ] **Uploads go/no-go recorded**; 30 beta participants confirmed
- [ ] Month 2 reviewed; `V1-PLAN.md` updated; **Standup: Week 9** opened
