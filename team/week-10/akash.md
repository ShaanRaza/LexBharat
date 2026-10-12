# Akash: Week 10 (Platform), 4 h a day

**Theme: MVP done.** Fix what's broken on production, set the switches the go/no-go
decides, make sure every alert reaches a person, and deploy the release that 30 people will
use from 4 January.

**After Wednesday, only serious fixes.** Everything else waits for January.

---

## Days 1 and 2, Mon 14 and Tue 15 Dec: production fixes

### 1.1 The fix list (7 h over two days)
From bug bash 1, the hostile review, speed checks and anything Meghna filed. Worst first:
privacy and data problems, then anything that loses a user's work, then speed.

### 1.2 General feedback (1 h, part of the fixes)
`POST /feedback` also accepts feedback **not tied to an answer** (a "send feedback" form),
with no message ID. Meghna builds the form on Thursday.

**Branch:** `akash/prod-fixes`

---

## Day 3, Wed 16 Dec: the uploads switch

### 3.1 Set it as decided (3 h)
The Week 8 go/no-go chose one of three outcomes. Build what that outcome needs:

| Outcome | What changes |
|---|---|
| On for client documents | `FEATURE_UPLOADS` on |
| **On, with a warning** | On, **plus** a setting that shows the "don't upload client documents yet" warning on every upload |
| Off for the beta | Stays off; the "My documents" item is hidden |

Test each state on the server with a test account. **Don't switch it on for real users
until the beta go/no-go on Friday.**

**Branch:** `akash/uploads-switch`

---

## Day 4, Thu 17 Dec: alerts, final

### 4.1 Every alert, to a person (2.5 h)
| Alert | Goes to |
|---|---|
| Site down (outside uptime check) | Shaan and Akash |
| Error spike (Sentry) | Shaan and Akash |
| Disk over 80%, Qdrant memory high | Akash |
| Upload queue stuck, or a failed hard delete | Akash |
| Backup failed | Akash |
| **The nightly leftover check found something** | **Shaan and Akash**: it means a delete didn't fully work |
| Removed-citation rate over 0.5% in a day | Shaan |

Trigger each one once on purpose and check it arrives. Write the list into `docs/RUNBOOK.md`.

**Branch:** `akash/alerts-final`

---

## Day 5, Fri 18 Dec: release checks + the go/no-go

### 5.1 Rollback, tested (1.5 h)
Deploy a harmless change, then roll it back through the workflow. Time it. If rollback has
never been tested, it isn't a safety net.

### 5.2 The release checklist (1 h)
`docs/RUNBOOK.md`, "Release checklist": every box, with evidence, ready for tomorrow.

### 5.3 Beta go/no-go call (1 h)

**Branch:** `akash/release-check`

---

## Day 6, Sat 19 Dec: release

- [ ] Deploy `v0.1.0-beta` through the workflow (1 h)
- [ ] Set the beta limit and the uploads switch as decided (30 min)
- [ ] Sign in as a test invitee: consent, ask, upload (if on), report a wrong answer, delete
      the account (1 h)
- [ ] The morning backup runs after the release; check it (30 min)
- [ ] Standup

---

## Done by Saturday

- [ ] Production fixes in; general feedback accepted
- [ ] Uploads switch built for the decided outcome and tested in each state
- [ ] Every alert triggered once and received
- [ ] Rollback tested and timed; release checklist complete
- [ ] `v0.1.0-beta` deployed; switches set; a test invitee's whole journey works
