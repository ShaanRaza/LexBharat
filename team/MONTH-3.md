# Month 3: Weeks 9 to 11, Mon 7 Dec to Sat 26 Dec 2026, then the beta

**Month 2 put the product on the real server. Month 3 makes it trustworthy, finishes the
MVP, and hands it to the first 30 users.**

Every task is a GitHub issue, **#170 to #206**, in the Week 9 to Week 11 milestones
([9](https://github.com/ShaanRaza/LexBharat/milestone/9) ·
[10](https://github.com/ShaanRaza/LexBharat/milestone/10) ·
[11](https://github.com/ShaanRaza/LexBharat/milestone/11)).

| Week | Dates | Theme | By Saturday | Summary |
|---|---|---|---|---|
| **9** | 7 to 12 Dec | **Hardening** | Second full 200-question run; hostile review of the verifier and isolation; server rebuild rehearsed and timed; the admin page; legal documents in; bug bash 1 | [WEEK-9.md](WEEK-9.md) |
| **10** | 14 to 19 Dec | **MVP done** | Final 200-question run; **beta go/no-go**; invite-only sign-up; onboarding; bug bash 2; release tagged | [WEEK-10.md](WEEK-10.md) |
| **11** | 21 to 26 Dec | **Buffer** *(Christmas)* | Slipped work caught up; **beta invites sent**; holiday cover agreed | [WEEK-11.md](WEEK-11.md) |
| | 28 Dec to 2 Jan | **No planned work** | Holiday cover only (below) | |
| | **Mon 4 Jan 2027** | **Private beta starts** | 20 students + 10 advocates | Checklist below |

---

## Written before Months 1 and 2 have happened

Planned from what Month 2 is **supposed** to deliver. On **Sat 5 Dec** Shaan checks this
list, and adjusts Week 9 first.

### What Month 3 assumes is done by Sat 5 Dec

| From Month 2 | If it isn't done |
|---|---|
| Live on the AWS server, deployed only by GitHub Actions, backups with one tested restore | **Week 9 finishes it first.** Nothing ships to users without it |
| Isolation tests, hard delete, the verifier's must-pass tests all green | **Stop and fix.** These are never dropped |
| First full 200-question run and its fix list | Week 9's run becomes the first; the final run moves to Week 11 |
| Uploads go/no-go decided | Decide on Mon 7 Dec; Week 10 sets the switch |
| Legal drafts with counsel; the legal opinion in | **Ranveer chases daily.** No reviewed consent notice = **no beta** |
| Law maps with the advocate | Unreviewed maps stay out of answers; the beta runs without them |

## What Month 3 adds that wasn't in the V1 plan

Gaps found while planning this month in detail. Each is small, and each would hurt the beta
if it were missing:

| Added | Why |
|---|---|
| **An admin page** (owner only) | `docs/CITATION-VERIFIER.md` says the invented-citation rate is "shown on the admin page", and nothing in the plan built one. During the beta it's how Shaan sees problems first |
| **Invite-only sign-up** | A *private* beta needs it. Without an allowlist, anyone who finds the address can sign up before the legal documents cover them |
| **A simple landing page** | The V1 plan moved the marketing site to January but said "a simple landing page is enough". Someone has to build it |
| **General feedback** (not tied to one answer) | Beta users need one place to say "this was confusing" |
| **Holiday cover and a beta-week-1 plan** | Alerts don't stop for Christmas, and the first week of real users needs a triage rule |

## Decisions this month (Shaan decides; recorded with `/decision`)

| Week | Decision | Decided from |
|---|---|---|
| 9 | Which law-map rows become `reviewed` | The advocate's marked-up maps |
| 9 | Retention periods, and the auto-delete period for uploads | Counsel's review |
| 9 | Is rebuilding the server under 1 hour? If not, what changes | The timed rehearsal |
| 10 | **Beta go/no-go** ([V1-PLAN.md](V1-PLAN.md) §5) | The final run, the checklist, the legal documents |
| 10 | Answers per month for beta users | Measured cost per answer (Week 5 onwards) |
| 10 | The security-test firm for February | Ranveer's quotes |
| 11 | Who covers alerts over the holidays | Agreement in the standup |

## People outside the team (Ranveer owns these)

| What | Due | If it's late |
|---|---|---|
| **Counsel's reviewed legal documents** | **Week 9** | **The beta can't open.** Escalate daily from Mon 7 Dec |
| Advocate's review of the law maps | Week 9 | Those notes stay out of answers |
| Beta participants' emails, for the allowlist | Week 10 | They can't sign in on 4 Jan |
| Kickoff calls for 4 to 8 Jan | Booked in Week 10 | The beta starts without a walkthrough |
| Beta invites | **Sent in Week 11** | The beta start moves |
| Security-test firm | Chosen in Week 10, for February | Public launch waits; the beta doesn't |

## Holidays

| Date | What the plan does |
|---|---|
| Fri 25 Dec, Christmas | Off. Week 11 is half capacity anyway |
| 28 Dec to 2 Jan | No planned work. Holiday cover only |

## Holiday cover (21 Dec to 3 Jan)

The server is live, and from late December real people can sign in. Agreed in Week 11:
- [ ] **Who gets the downtime and error alerts each day** (a rota; nobody covers alone for
      two weeks)
- [ ] What counts as "act now": the site is down, a **suspected data leak** (straight to
      [`../docs/BREACH-PLAYBOOK.md`](../docs/BREACH-PLAYBOOK.md); the clock is 72 hours), or
      a reported **made-up citation**
- [ ] **No deploys** over the holidays unless it's one of those

## Ready for the beta on Mon 4 Jan

[`V1-PLAN.md`](V1-PLAN.md) §5, checked at the Week 10 go/no-go and again on 2 Jan:

- [ ] Live on the AWS server, with sign-in and the **counsel-reviewed** consent notice
- [ ] Research chat with a tick **per citation**; Act lookup; judgment view
- [ ] Upload-and-chat as decided at the Week 8 go/no-go, hard delete proven
- [ ] Isolation tests pass
- [ ] Data-as-of date, CC BY credit and not-legal-advice notice everywhere
- [ ] The final 200-question run reviewed, with **no confirmed fabricated citation**
- [ ] Sign-up limited to invited people; onboarding and feedback working
- [ ] The admin page shows the invented-citation rate; alerts reach a person
- [ ] Invites sent; kickoff calls booked; holiday cover agreed

## Capacity

Weeks 9 and 10 at about 66 hours each, Week 11 at about half (~33): roughly **165 hours**.
That's the V1 plan's arithmetic, with the four additions above (~20 hours) taken from Week 11's
buffer. **Week 11 is the only slack in the whole plan.** If Weeks 9 and 10 overrun, the
choice is the drop list or moving the beta start, said out loud.
