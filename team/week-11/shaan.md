# Shaan: Week 11 (Buffer, Christmas), about 2 h a day

**Theme: buffer.** The only slack in the whole plan. **No new features.** Catch up what
slipped, agree holiday cover, and plan the first week of real users.

> **Fri 25 Dec is Christmas: off.** The week runs at about half capacity.

---

## Day 1, Mon 21 Dec: holiday cover

### 1.1 Agree the rota (1 h)
From your Saturday proposal, agreed in the standup. For **21 Dec to 3 Jan**:
- Who gets the downtime and error alerts **each day**. Nobody covers alone for two weeks
- **Act now** only for: the site down, a **suspected data leak** (straight to
  `docs/BREACH-PLAYBOOK.md`, 72 hours), or a reported **made-up citation**
- **No deploys** unless it's one of those three

Write it into `team/beta/holiday-cover.md` (names and days only; **no phone numbers in the
repo**).

---

## Days 1 to 4: catch up

### 2.1 What slipped (about 6 h)
Only items already in the MVP that didn't finish, in this order:
1. Anything from the "Ready for the beta" list ([`../MONTH-3.md`](../MONTH-3.md)) still open
2. Serious bugs from bug bash 2
3. Anything else, **only if it's small and safe**. Otherwise it waits for January

Every fix still goes through a pull request, the tests and the deploy workflow.

**Branch:** `shaan/buffer`

---

## Day 4, Thu 24 Dec: plan the first beta week

### 3.1 `team/beta/week-1-plan.md` (2 h)
What happens from **Mon 4 Jan**:

| Every day | Who |
|---|---|
| Read the admin page: removed-citation rate, feedback, failed uploads | Shaan |
| Answer beta users the same working day | Ranveer |
| **Any report of a made-up citation**: pull the Langfuse trace, find which check missed it, write a test, fix. Same day | Shaan |
| **Any report of seeing someone else's data**: the breach playbook, immediately | Shaan + Akash |
| Screen bugs: triage daily, fix weekly | Meghna |

Plus: the kickoff-call schedule, and the date of the first beta review (end of week 1).

---

## Day 6, Sat 26 Dec: wrap Month 3

- [ ] "Done means" in [README.md](README.md) ticked honestly
- [ ] `team/V1-PLAN.md`: what shipped, what moved to January, what was dropped
- [ ] Check the "Ready for the beta" list again. **Anything still open gets a named owner
      and a date before 4 Jan, or the beta changes**

---

## Done by Saturday

- [ ] Holiday cover agreed and written down
- [ ] Slipped work caught up, or moved to January out loud
- [ ] Beta week 1 plan written
- [ ] Month 3 wrapped; readiness re-checked
