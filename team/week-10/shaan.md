# Shaan: Week 10 (Data + Core + Lead), 4 h a day

**Theme: MVP done.** This week the product stops changing. You run the **final 200-question
run** on a frozen setup, finish the breach playbook, hold the **beta go/no-go** with everyone
on Friday, and tag the release on Saturday.

Pipeline steps touched: **none, by design.** Only fixes for what the final run or bug bash 2
finds, and only if they're serious.

---

## Day 1, Mon 14 Dec: last fixes

### 1.1 What's left (3.5 h)
From Week 9's run and hostile review. The setup freezes tomorrow, and **from Thursday only
serious fixes merge**: a wrong citation, a trap answered confidently, a privacy hole, a crash.

**Branch:** `shaan/final-fixes`

---

## Day 2, Tue 15 Dec: the final run

### 2.1 Freeze, then run (3.5 h)
- **Freeze the setup**: models, gate threshold, Jev switches, prompts, notes. Record the
  exact versions in the run's notes
- Run all 200 on the production server
- This is the run the beta go/no-go uses, and the baseline every later release is compared
  against

---

## Day 3, Wed 16 Dec: read it like an advocate would

### 3.1 The numbers (1.5 h)
| Measure | Target | Gate |
|---|---|---|
| Verified-citation rate | **98%+** | Launch gate (a), measured now so the beta shows the trend |
| Answers with a removed citation | **under 0.5%** | Launch gate (c) |
| **Confirmed fabricated citations** | **zero** | **Beta readiness**: a single one is a no-go until fixed |
| Traps answered correctly | all 50 | Each failure explained |

### 3.2 Read 30 answers yourself (2 h)
Ten real questions, ten lookups, ten traps. Would you be comfortable with an advocate reading
each one? Write a one-line verdict per answer in the run's notes.

---

## Day 4, Thu 17 Dec: the breach playbook

### 4.1 Finish `docs/BREACH-PLAYBOOK.md` (3 h)
It's a skeleton. Before real users arrive it must say, step by step, what happens in the
first hour, the first day and the **72 hours** (DPDP):
- Who's told first, and how (phone numbers stay **outside** the repo; say where they are)
- How to stop the leak: switch uploads off, revoke keys, take the server offline
- Who decides whether to notify the Data Protection Board and the users
- Notification templates (drafts for counsel)

### 4.2 Two short legal drafts (1 h)
`legal/takedown-process-v1-draft.md` and `legal/legal-orders-policy-v1-draft.md`, from
`legal/README.md`. Marked **draft, for counsel**. Not needed to open the beta, but needed
before the public launch.

**Branch:** `shaan/breach-playbook`

---

## Day 5, Fri 18 Dec: the beta go/no-go (all four, 1 h)

### 5.1 Walk the checklist (1 h call + 1 h prep)
[`../V1-PLAN.md`](../V1-PLAN.md) §5 and the "Ready for the beta" list in
[`../MONTH-3.md`](../MONTH-3.md). Every box: ticked with evidence, or not.

| Outcome | Then |
|---|---|
| **Go** | Ranveer sends invites in Week 11; beta opens Mon 4 Jan |
| **Go, smaller** | Fewer invites, or uploads off, for the things that aren't ready |
| **No-go** | A new date, said plainly to everyone already recruited |

Record with `/decision`. **You decide.** Push-back from the others is welcome; the call is
yours.

### 5.2 Beta settings (1 h)
- Answers per month for beta users: from the measured cost per answer. Record it
- Tell Akash: the uploads switch, the limit, the invite list confirmed

---

## Day 6, Sat 19 Dec: tag the release

### 6.1 Release (2 h)
- Akash deploys the final version through the workflow
- Tag it `v0.1.0-beta` in git, with a short `CHANGELOG.md` entry: what's in, what's
  switched off, the final run's numbers
- Confirm the morning backup ran **after** the release

### 6.2 Wrap (1.5 h)
"Done means" in [README.md](README.md); adjust Week 11; open **Standup: Week 11**. Propose
the **holiday cover rota** for agreement on Monday.

---

## Pull requests to expect

| Day | From Akash | From Meghna | Yours |
|---|---|---|---|
| 1 | `akash/prod-fixes` | `meghna/bug-bash-2` | `shaan/final-fixes` |
| 2 | `akash/prod-fixes` | `meghna/bug-bash-2` | |
| 3 | `akash/uploads-switch` | `meghna/welcome` | |
| 4 | `akash/alerts-final` | `meghna/general-feedback` | `shaan/breach-playbook` |
| 5 | `akash/release-check` | `meghna/landing-page` | |
| 6 | | `meghna/release-check` | `shaan/release-v0.1` |

**After Wednesday, merge only serious fixes.** Everything else waits for January.

## Done by Saturday

- [ ] Setup frozen; final 200-question run done and read; zero confirmed fabricated citations
- [ ] Breach playbook complete; takedown and legal-orders drafts for counsel
- [ ] **Beta go/no-go recorded**; beta limits set
- [ ] `v0.1.0-beta` tagged and deployed, with a changelog
