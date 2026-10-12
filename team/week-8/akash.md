# Akash: Week 8 (Platform), 4 h a day

**Theme: on the real server.** By Saturday the whole product runs on one AWS server in
Mumbai, reachable over HTTPS on the agreed domain, **deployed only by GitHub Actions**,
backed up daily, and watched by Langfuse and Sentry with masking and scrubbing working.

The rules from `docs/SECURITY-AND-COMPLIANCE.md` and `docs/RUNBOOK.md` are your checklist:
**only the website and the API reachable from the internet; Qdrant, PostgreSQL and Redis
never exposed; secrets only in Secrets Manager; every disk and bucket encrypted.**

**Write down every step in `infra/aws/README.md` as you go.** Week 9 rebuilds this server
from those notes and times it.

---

## Before Day 1

- [ ] The domain is bought (agreed in Week 6)
- [ ] Every image's ARM build checked (Week 1 list, plus MinIO and the worker since)

---

## Day 1, Mon 30 Nov: the server

### 1.1 EC2 in Mumbai (3.5 h)
- **r7g.large (ARM, Graviton)** in ap-south-1
- **Encrypted 200 GB disk** (EBS with KMS)
- **No open SSH.** Use AWS Systems Manager (Session Manager) to get in, so there's no SSH
  port to attack
- Security group: **only 443 (and 80 for the certificate)** open to the internet
- An Elastic IP; the domain's DNS points at it
- **EC2 automatic recovery** switched on (`docs/ARCHITECTURE.md`, One server)

**Branch:** `akash/aws-server` (scripts and notes in `infra/aws/`)

---

## Day 2, Tue 1 Dec: production Compose + HTTPS

### 2.1 `infra/docker-compose.prod.yml` (3.5 h)
- Every service on one **private Docker network**
- A reverse proxy (Caddy is simplest) in front of the website and the API, with **HTTPS
  certificates handled automatically**
- **Qdrant, PostgreSQL and Redis have no published ports at all**
- The worker: **1 CPU, one job at a time**, as on laptops
- Secrets come from **AWS Secrets Manager** when the containers start. **Never a `.env`
  file on the server**
- The uploads bucket: private, KMS-encrypted, public access blocked, links that expire in
  minutes. The auto-delete period stays **off** until counsel sets it
- Firebase: add the domain to its authorised domains

**Branch:** `akash/prod-compose`

---

## Day 3, Wed 2 Dec: the deploy workflow

### 3.1 `.github/workflows/deploy.yml` (3.5 h)
The skeleton from setup, made real:
- Builds **ARM images** in GitHub Actions and pushes them to a private registry
- **Runs the must-pass tests first** (`docs/TESTING.md`). Any failure: no deploy
- Deploys through Systems Manager, runs migrations, then **checks the health route**
- If the health check fails, **rolls back** to the previous images automatically
- Manual start only (`workflow_dispatch`) for now; Shaan decides when it becomes automatic

CLAUDE.md: **never touch the production server directly.** From today this is the only way
code gets there.

**Branch:** `akash/deploy-workflow`. **Shaan must review before merge.**

---

## Day 4, Thu 3 Dec: data and backups

### 4.1 PostgreSQL on the server (1.5 h)
Load `cases`, `act_sections` and `court_coverage` from a dump of Shaan's local database (no
user data exists yet). Check the row counts match.

### 4.2 Daily backups (2 h)
- PostgreSQL: a daily dump to the encrypted backups bucket
- Qdrant: a daily snapshot to the same bucket, then **delete the local snapshot file**
- **Test a restore once**: restore last night's PostgreSQL backup into a scratch database
  and count rows. A backup that's never been restored isn't a backup

**Branch:** `akash/backups`

---

## Day 5, Fri 4 Dec: Qdrant restore + monitoring

### 5.1 With Shaan: the search collection (1.5 h)
Restore his snapshot from S3, check counts with him, delete the snapshot file.

### 5.2 Monitoring live (2 h)
- Langfuse and Sentry switched on with the server's settings
- **Check masking and scrubbing on the live server**: send a test question containing a
  made-up email and phone number, and look at what Langfuse and Sentry actually received
- An outside **uptime check** on the health route, with an alert to Shaan and you
- Alerts for error spikes in Sentry

**Branch:** `akash/monitoring-live`

---

## Day 6, Sat 5 Dec: smoke test the server

### 6.1 Everything once (2.5 h)
On the real domain, with a test account:
- [ ] Sign in; consent; ask a question; the answer streams with ticks
- [ ] Act lookup works without signing in
- [ ] Upload a **public** document, chat about it, delete it, and check all three places
      are empty (uploads stay switched off for real users until the go/no-go)
- [ ] Delete the test account
- [ ] Time to first word, and how much memory Qdrant uses (**the first thing expected to
      break** on 16 GB, `docs/RUNBOOK.md`)

### 6.2 Rebuild notes (1 h)
Turn your week's notes into the numbered rebuild steps in `docs/RUNBOOK.md`, with real
commands. **Week 9 rehearses them against the clock.**

**Branch:** `akash/server-smoke`

---

## Done by Saturday

- [ ] EC2 in Mumbai, ARM, encrypted, no open SSH, auto-recovery on
- [ ] Production Compose: only the website and API reachable; HTTPS; secrets from Secrets Manager
- [ ] Deploy workflow: tests first, ARM images, migrations, health check, rollback
- [ ] Data on the server; daily backups, with **one restore tested**
- [ ] Masking and scrubbing checked on the live server; uptime and error alerts
- [ ] Smoke test passed; rebuild steps written for Week 9
