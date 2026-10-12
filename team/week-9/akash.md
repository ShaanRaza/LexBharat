# Akash: Week 9 (Platform), 4 h a day

**Theme: hardening the server.** By Saturday you've **rebuilt the server from scratch
against the clock**, measured every speed target on it, built the **admin page's API**,
limited sign-up to **invited people only**, and switched everyone to the counsel-reviewed
consent notice.

---

## Before Day 1

- [ ] Month 2 leftovers first: the server, deploys, backups and monitoring must all work
- [ ] The rebuild steps in `docs/RUNBOOK.md` (Week 8)

---

## Day 1, Mon 7 Dec: rebuild the server, timed

### 1.1 The rehearsal (3.5 h)
`docs/RUNBOOK.md`: **a rebuild target nobody has rehearsed is not a target.** Start a
timer, then follow your written steps **exactly** on a **second, temporary** server:
1. New EC2 r7g in Mumbai from the base image
2. Secrets from Secrets Manager
3. Compose up
4. Restore PostgreSQL from last night's backup
5. Restore the search collection, then delete the snapshot file
6. Point a **test** subdomain at it (never the real one during a rehearsal)
7. Check: an answer end to end, an Act lookup, a sign-in

Every step that wasn't written down, or didn't work as written, is **a fix to the runbook**.

**Branch:** `akash/rebuild-rehearsal`

---

## Day 2, Tue 8 Dec: record it + speed checks

### 2.1 Finish the rehearsal (1 h)
- [ ] Record the real time in `docs/RUNBOOK.md`. **Target: under 1 hour**. If it's over,
      write what would bring it down
- [ ] **Delete the temporary server and its disk** (it costs money every hour)

### 2.2 Speed on the real server (2.5 h)
CLAUDE.md §10, measured on production with a test account:

| Measure | Target |
|---|---|
| First word of an answer | under 3 s |
| Full answer | under 20 s |
| Search + re-rank | under 800 ms |
| Act lookup | under 500 ms |
| Text PDF under 50 pages ready | under 60 s |
| Scanned PDF under 50 pages ready | under 5 min |

Ten tries each; record the typical and the worst in `docs/RUNBOOK.md`. Also record **Qdrant's
memory use** (the first thing expected to break on 16 GB).

**Branch:** `akash/speed-checks`

---

## Day 3, Wed 9 Dec: the admin API

### 3.1 Owner-only routes (3.5 h)
`docs/CITATION-VERIFIER.md`: the invented-citation rate is **shown on the admin page**. Build
its API under `/api/v1/admin/`:

| Route | Shows |
|---|---|
| `GET /admin/trust` | Answers with a removed citation, by day, with the four reasons. **Target under 0.5%** |
| `GET /admin/runs` | The 200-question runs and their summaries |
| `GET /admin/feedback` | Thumbs and wrong-answer reports, newest first |
| `GET /admin/health` | Upload queue depth, failed uploads, error counts |

Rules:
- Only users with an **admin flag** (set by a script, not by any route) get in; everyone
  else gets **404**
- **Never document text or anyone's chat text** in these routes. Counts, reasons, IDs,
  feedback comments only. (Feedback comments are user-written; Meghna's box already warns
  against client details)
- Every admin request writes an **`admin_view`** row to the audit log

**Branch:** `akash/admin-api`. **Shaan must review before merge.**

---

## Day 4, Thu 10 Dec: invite-only sign-up

### 4.1 The allowlist (3 h)
The beta is **private**. Without this, anyone who finds the address can sign up.
- An `invites` table (a migration): email, invited_at, used_at. Emails are personal data:
  never logged, masked in Langfuse, scrubbed from Sentry
- On first sign-in, an email **not on the list** gets a clear "private beta, by invitation"
  error code, and **no account is created**
- A small script adds emails from a file **on your laptop**. Ranveer sends the list through a
  private channel. **Never in GitHub, the standup or a group chat**
- Behind a setting (`SIGNUP_INVITE_ONLY`, on), so public launch is a config change

**Branch:** `akash/invite-only`

---

## Day 5, Fri 11 Dec: the real consent notice

### 5.1 Consent v1 (2 h)
Once Shaan commits counsel's documents:
- The notice version setting moves from `v0` to `v1`
- **Everyone, test accounts included, is asked to agree again**
- The `v0` draft stays in the repo (people agreed to it), marked superseded

### 5.2 Retention settings (1 h)
`UPLOAD_RETENTION_DAYS` from counsel's period (via Shaan). Check the nightly job deletes an
upload older than the period on a test account.

### 5.3 Dependabot (30 min)
`docs/TESTING.md`: switch on the pip, npm and docker sections in `.github/dependabot.yml` now
that their files exist.

**Branch:** `akash/consent-v1`

---

## Day 6, Sat 12 Dec: alerts and cost

### 6.1 Alerts that reach a person (1.5 h)
Check each one **actually arrives**: site down, error spike, disk over 80%, Qdrant memory high,
upload queue stuck, backup failed.

### 6.2 What it costs (1.5 h)
- The AWS bill so far, and the month's projection, against the estimate of **₹7,200 to ₹7,500
  a month** (`docs/ARCHITECTURE.md`)
- Cost per answer from Langfuse, against the Week 5 measurement
- Write both into `docs/RUNBOOK.md`; anything well over the estimate goes to Shaan

**Branch:** `akash/alerts-and-cost`

---

## Done by Saturday

- [ ] Rebuild rehearsed and timed; runbook fixed; temporary server deleted
- [ ] Every speed target measured on production; Qdrant memory recorded
- [ ] Admin API: owner only, no document or chat text, every view audited
- [ ] Invite-only sign-up; the list never in GitHub or chats
- [ ] Everyone moved to consent v1; retention period set; Dependabot fully on
- [ ] Every alert tested; cost checked against the estimate
