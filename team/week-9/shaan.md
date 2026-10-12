# Shaan: Week 9 (Data + Core + Lead), 4 h a day

**Theme: hardening.** By Saturday the advocate-approved knowledge notes are live, the
**second full 200-question run** has run on the real server, someone hostile has tried to
break the verifier and the isolation (and failed, or you've fixed it), and the
counsel-reviewed legal documents are in the repo.

Pipeline steps touched: **3 (decide)** and **8 (answer)** start using reviewed law maps;
**9 (verify)** is attacked, and only changes if the attack finds a hole.

---

## Before Day 1

- [ ] Check [`../MONTH-3.md`](../MONTH-3.md), "What Month 3 assumes is done". Anything
      missing from Month 2 goes **first**
- [ ] The uploads go/no-go is recorded. If not, it's Monday's first job

---

## Day 1, Mon 7 Dec: reviewed notes go live

### 1.1 The advocate's law-map review (3 h)
Ranveer brings back the marked-up maps.
- Fix every row the advocate corrected; **remove** rows they marked wrong or misleading
- Set `status: reviewed`, `reviewed_by` (the advocate's role, **not their name**: BCI Rule
  36) and `last_checked` **only** on maps the advocate approved
- Run `knowledge/check.py`: green
- Rows not reviewed stay `draft`, so they're never used. Partial approval is fine

No review back yet? Leave everything `draft`; the beta runs without law maps. Say so in the
standup.

**Branch:** `shaan/law-maps-reviewed`

---

## Day 2, Tue 8 Dec: the second full run, on the server

### 2.1 Run all 200 on the real server (2.5 h)
The production setup, not your laptop: same models, threshold and switches users get.
Compare it with the first run (Week 7) question by question.

### 2.2 First read (1.5 h)
- Verified-citation rate (target **98%+**) and answers with a removed citation (target
  **under 0.5%**)
- **Every trap answered confidently**, and every answer that **got worse** since Week 7
- What the law maps changed on IPC/BNS questions

---

## Day 3, Wed 9 Dec: fix the worst

### 3.1 Fix list, round 2 (4 h)
Same rules as Week 8: worst first, rerun what each fix touches plus 20 that already passed,
**never weaken the verifier, never drop a trap**.

**Branch:** `shaan/fixes-round-2`

---

## Day 4, Thu 10 Dec: the legal documents land

### 4.1 Counsel's documents into the repo (2 h)
When counsel's reviewed versions arrive (Ranveer):
- Save as `legal/consent-notice-v1.md`, `privacy-policy-v1.md`, `terms-of-service-v1.md`,
  `upload-warning-v1.md`, `not-legal-advice-v1.md`. **Never edit them afterwards**; a
  change is a new version (`legal/README.md`)
- Update `legal/README.md` statuses
- Tell Akash the new notice version (everyone re-consents) and Meghna which texts are final

### 4.2 Retention (1.5 h)
Fill [`../../docs/RETENTION.md`](../../docs/RETENTION.md) with counsel's periods. Each one
becomes a decision (`/decision`). The upload auto-delete period goes to Akash for
`UPLOAD_RETENTION_DAYS`.

**Not back from counsel by Thursday?** This is the biggest risk to the beta. Escalate with
Ranveer the same day, and plan the go/no-go for a later start date.

**Branch:** `shaan/legal-v1`

---

## Day 5, Fri 11 Dec: a hostile review

### 5.1 Someone tries to break it (3.5 h)
Use the **`adversarial-reviewer`** skill **in a fresh Claude session** (one that didn't
write the code). Two targets, the ones that would hurt most:

| Target | It tries to |
|---|---|
| **The verifier** (`core/verify.py` and everything that feeds it) | Get a citation through that wasn't retrieved; a quote that isn't in the record; a removed citation that still shows; the order rule broken |
| **Isolation** (the shared uploads function and every caller) | Reach another user's document by any path: routes, the pipeline, the export, the admin page, error messages |

Every finding becomes a **test first**, then a fix. Record findings in `docs/RISKS.md`.

**Ask Claude Code (new session):**
> Use the adversarial-reviewer skill. Attack core/verify.py and the citation flow, then core/store/uploads_access.py and every caller, per team/week-9/shaan.md task 5.1. You didn't write this code. Find ways a fabricated citation reaches a user or one user reaches another's data. Write each finding as a failing test. Don't fix anything.

**Branch:** `shaan/adversarial-review`

---

## Day 6, Sat 12 Dec: fix findings + wrap

### 6.1 Fixes (2.5 h)
Fix what the hostile review found. All new tests pass. If something serious can't be fixed
by Saturday, **it's an item for the beta go/no-go**, not something to hide.

### 6.2 Wrap (1 h)
"Done means" in [README.md](README.md); adjust Week 10 issues; open **Standup: Week 10**.

---

## Pull requests to expect

| Day | From Akash | From Meghna | Yours |
|---|---|---|---|
| 1 | `akash/rebuild-rehearsal` | `meghna/bug-bash-1` | `shaan/law-maps-reviewed` |
| 2 | `akash/speed-checks` | `meghna/bug-bash-1` | |
| 3 | `akash/admin-api` (**careful**) | `meghna/admin-page` | `shaan/fixes-round-2` |
| 4 | `akash/invite-only` | `meghna/legal-pages` | `shaan/legal-v1` |
| 5 | `akash/consent-v1` | `meghna/onboarding-guide` | `shaan/adversarial-review` |
| 6 | `akash/alerts-and-cost` | | |

**Review the admin route carefully.** It's the one place built to see across users, so it
must never show document text or let anyone but you in.

## Done by Saturday

- [ ] Approved law-map rows `reviewed`; the rest stay `draft`
- [ ] Second full 200-question run on the server, compared with the first
- [ ] Fix list round 2 done, with before and after numbers
- [ ] Counsel's v1 documents in `legal/`; retention periods decided (or the delay escalated)
- [ ] Hostile review of the verifier and isolation; every finding a test; fixes in
