# Runbook

Operations for one EC2 server in Mumbai running everything in Docker Compose.

**There is no failover.** That is accepted at launch to keep cost low. The whole plan for
staying at 99.5% (about 3.6 hours of downtime a month) is: recover fast.

## Watch these first

The two things expected to break first, per the architecture doc:

1. **Qdrant search memory** — vectors need ~4–5 GB with quantization on a 16 GB box shared
   with PostgreSQL, Redis, the website, the API, the worker and the backup reranker.
2. **OCR time** — the worker is capped at 1 CPU and takes one job at a time so chat stays
   fast. Watch queue depth.

Measure both in Langfuse and Sentry from week 1.

## Rebuild from snapshot — target under 1 hour

**This plan must be written out and timed before launch.** A target nobody has rehearsed
is not a target.

Outline:

1. Launch a fresh EC2 r7g instance in ap-south-1 from the base image. **ARM.**
2. Pull secrets from AWS Secrets Manager.
3. `docker compose up` on the private Docker network.
4. Restore PostgreSQL from the latest daily S3 backup.
5. Restore the Qdrant snapshot from S3, **then delete the snapshot file** — the 200 GB disk
   is sized assuming you do.
6. Point DNS / the Elastic IP at the new box.
7. Verify: a research answer end to end, an Act lookup, a stats page, and a login.

- [ ] Write this out step by step with real commands
- [ ] Rehearse it once and record the actual time
- [ ] Record the time here and in the launch checklist

## Backups

| What | Where | Cadence |
|---|---|---|
| PostgreSQL | S3, encrypted | Daily |
| Qdrant | S3 snapshot | Daily |
| Uploads | S3, encrypted with a KMS key, lifecycle auto-delete | Continuous |

Deleted data ages out of backups **on the normal cycle** — say so in the privacy notice
rather than claiming instant removal everywhere.

## Monitoring

| Tool | Watches | Rule |
|---|---|---|
| **Langfuse** | Every AI call: prompt, answer, cost, speed, token counts | **Masked** — upload text, emails and phone numbers replaced before sending |
| **Sentry** | Crashes and errors | **Scrubbed** — request bodies, tokens, emails and document text removed |
| Admin page | The 200-question test set, raw scores from all three searches, any record's payload, bad-record marking | Behind the owner's login |
| Qdrant dashboard | Collections, points, test searches | **Private tunnel only — never on the public internet** |

Every API response carries a **request ID**, written into every log line and Langfuse
trace, so one ID finds everything about a complaint.

## Release checklist

Before any deploy:

- [ ] Unit and integration tests pass (see [TESTING.md](TESTING.md))
- [ ] The verifier's four failure reasons each still remove and log the citation
- [ ] The usage meter tests pass
- [ ] The 200-question test set has run, and the **verified-citation rate is ≥ 98%**
- [ ] The **invented-citation rate is under 0.5%**, reviewed on the admin page
- [ ] No secret appears in any log, trace or error payload
- [ ] Migrations are numbered and reversible

Deploys go through **GitHub Actions**. **Never touch the production server directly.**

## Incidents

1. Capture the request ID and the Sentry event.
2. If data may have been exposed, go straight to
   [BREACH-PLAYBOOK.md](BREACH-PLAYBOOK.md) — **the clock is 72 hours**.
3. If an answer contained a bad citation that reached a user, log it, pull the Langfuse
   trace, and check whether the verifier was bypassed or wrong. A **confirmed fabricated
   citation reaching a user breaks launch gate condition (c)** — record it.
4. If the server is gone, run the rebuild plan above.

## Routine jobs

| Job | When |
|---|---|
| Nightly leftover check for hard-deleted uploads | Nightly |
| Knowledge-note source check after any data refresh | Per refresh |
| Clear the answer cache | After any data refresh |
| Dependabot review | Weekly |
