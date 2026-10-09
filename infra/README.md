# infra

Docker Compose and deploy scripts. Not built yet — **build step 6**.

Six services on a private Docker network: `web`, `api`, `worker`, `qdrant`, `postgres`,
`redis`.

Rules that must hold:

- **Only `web` and `api` are reachable from the internet.** Qdrant, PostgreSQL and Redis
  are never exposed. The Qdrant dashboard is reached through a private tunnel only.
- **The server is ARM (Graviton, r7g)** — every image needs an ARM build. Check this before
  step 6, not during it.
- Secrets come from AWS Secrets Manager, never from a file on the box.
- The worker is capped at **1 CPU** and a fixed memory limit, and takes **one job at a
  time**, so OCR never slows chat.
- Daily PostgreSQL backups and Qdrant snapshots to S3.
- After restoring the Qdrant snapshot, **delete the snapshot file** — the 200 GB disk is
  sized assuming you do.
- A written rebuild-from-snapshot plan, target **under 1 hour**. One server has no
  failover; that is accepted at launch.
