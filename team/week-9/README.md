# Week 9 in detail: Mon 7 Dec to Sat 12 Dec 2026

**Theme: hardening.** Month overview: [`../MONTH-3.md`](../MONTH-3.md).

| Person | File | Hours |
|---|---|---|
| Shaan | [shaan.md](shaan.md) | 4 h a day |
| Akash | [akash.md](akash.md) | 4 h a day |
| Meghna | [meghna.md](meghna.md) | 3 h a day |
| Ranveer | [ranveer.md](ranveer.md) | When available, with deadlines |

**Week goal:** reviewed knowledge notes go live; the second full run happens on the real
server; a hostile reviewer attacks the verifier and isolation; the server is rebuilt from
scratch against the clock; the admin page and invite-only sign-up exist; counsel's legal
documents land; bug bash 1 is done.

**Pipeline steps touched:** 3 and 8 start using reviewed law maps; 9 is attacked and only
changes if the attack finds a hole.

**Tracking:** every task is a GitHub issue in the
[Week 9 milestone](https://github.com/ShaanRaza/LexBharat/milestone/9). **Status lives in the issues.**

| Person | Issues |
|---|---|
| Shaan | #170 law maps live · #171 second run + fixes · #173 legal v1 + retention · #174 hostile review |
| Akash | #175 rebuild rehearsal · #176 speed checks · #177 admin API · #178 invite-only · #179 consent v1 · #180 alerts + cost |
| Meghna | #181 bug bash 1 · #182 admin page · #183 legal pages · #184 onboarding guide |
| Ranveer | #172 counsel's documents · #185 law maps, invite list, guide, trademark, kickoff plan |

> **Written before Months 1 and 2 happened.** On Sat 5 Dec Shaan checks
> [`../MONTH-3.md`](../MONTH-3.md) ("What Month 3 assumes is done") and adjusts this week.

---

## Who waits on whom

| Who is waiting | For | From | Needed by |
|---|---|---|---|
| Shaan, Day 1 | The advocate's marked-up law maps | Ranveer | **Mon 7 Dec** |
| **Shaan, Day 4; Akash, Day 5; Meghna, Day 4** | **Counsel's reviewed documents** | **Ranveer** | **Wed 9 Dec** |
| Meghna, Day 3 | The admin routes | Akash | Day 3 (she mocks from the OpenAPI types until then) |
| Akash, Day 4 | The invite list, privately | Ranveer | Fri 11 Dec |
| Akash, Day 5 | The upload retention period | Shaan (from counsel) | Day 4 |
| Meghna, Day 5 | Onboarding guide content | Ranveer | Day 5 |

## The biggest risk this week

**Counsel's review.** Without a reviewed consent notice, nobody can sign up, so the beta
can't open. If there's no firm date by **Wed 9 Dec**, Shaan plans the Week 10 go/no-go for a
later start, and the invites (Week 11) wait.

## Done means, by Saturday 12 Dec

- [ ] Advocate-approved law-map rows `reviewed` and live; the rest stay `draft`
- [ ] Second full 200-question run on the server; fix round 2 done
- [ ] Hostile review of the verifier and isolation; every finding a test; fixes in
- [ ] Server rebuilt from scratch and **timed**; runbook fixed; temporary server deleted
- [ ] Every speed target measured on production
- [ ] Admin page (owner only, no document text, every view audited)
- [ ] Invite-only sign-up; invite list loaded privately
- [ ] Counsel's v1 documents in `legal/` and in the app; everyone on consent v1; retention set
- [ ] Bug bash 1 done; onboarding guide written
- [ ] Alerts tested; cost checked; Week 10 adjusted; **Standup: Week 10** opened
