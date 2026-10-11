# Akash: Week 1 (Platform), 4 h a day

Your week turns empty folders into a skeleton that runs. By Saturday: CI checks Python,
`docker compose up` starts the databases, the API answers its first two routes, and the
database tables exist.

Most of this is **setup work**, so let Claude Code do the heavy lifting. Two things need
Shaan's eyes: the **database tables** (Day 4) and the **streaming format** (Day 2).

Commands below are for macOS. On Windows, use WSL2.

---

## Before Day 1 (~30 min)

- [ ] **Accept the GitHub invite** for `mrharit`. Nothing else works until you do.
- [ ] Clone the repo and open it in VS Code. Accept the recommended extensions.
- [ ] Install **Docker** (Docker Desktop, or Colima) and **uv**: `brew install uv`
- [ ] Read [`../../CLAUDE.md`](../../CLAUDE.md) §1, §2, §5, §6 and
      [`../README.md`](../README.md). About 15 minutes; it saves hours later.

---

## Day 1, Tue 13 Oct: Python project + CI

**Kickoff call:** 30 min with everyone.

### 1.1 The Python project (2 h)
`pyproject.toml` at the repo root:

| Part | Contents |
|---|---|
| Python | `>=3.12` (same as CI) |
| Main dependencies | fastapi, uvicorn[standard], pydantic-settings, sqlalchemy 2, alembic, psycopg[binary], redis, arq, qdrant-client, httpx |
| `dev` extra | ruff, pytest, pytest-asyncio |
| `data` extra | duckdb, pyarrow, fastembed, numpy (Shaan's data scripts) |
| Packages | `api`, `core`, `adapters`, `workers`, `data`. Add an empty `__init__.py` to each |
| ruff | line length 88 (matches the VS Code ruler), target Python 3.12 |
| pytest | tests live in `tests/` |

CI runs `pip install -e ".[dev]"`, then `ruff check .`, `ruff format --check .` and
`pytest -q`. **All four must pass.**

> **Trap:** `pytest` fails CI if there are **zero** tests. Task 1.2 adds the first one.
> **Trap:** run `ruff format .` before committing; it also checks the existing script in
> `.github/scripts/`.

### 1.2 One settings module (1 h)
`core/settings.py`, using pydantic-settings. It's a shared file (CLAUDE.md rule 2:
settings live in config, not code).
- One field for **every name in `.env.example`**, with the same defaults.
- Every `FEATURE_*` and `JEV_ENABLED_*` switch defaults to **off**.
- Secret fields must **never** print their value (use `SecretStr`).

First test, `tests/test_settings.py`: the defaults load, and every feature switch is off.

### 1.3 Open the PR (30 min)
Run locally: `ruff format . && ruff check . && pytest -q`.

**Branch:** `akash/python-setup`. Ask Shaan to merge **today**: his Day 5 tests depend on it.

**Done when:** CI's **Python** job runs on your PR and is green. Today it switches on for
the first time.

**Ask Claude Code:**
> Set up pyproject.toml and core/settings.py per team/week-1/akash.md tasks 1.1 and 1.2. Read .env.example for the setting names. Add tests/test_settings.py. Then run ruff format, ruff check and pytest -q, and show me the output.

---

## Day 2, Wed 14 Oct: Docker Compose + database migrations

### 2.1 Compose (2 h)
`infra/docker-compose.yml`, with PostgreSQL 16, Redis 7 and Qdrant, **versions pinned**.
- All on one **private network**
- **Named volumes** (not folders from your laptop)
- A health check on each service
- Ports open to your laptop **only** (`127.0.0.1`), and on **non-default numbers**, because
  Shaan already runs a Qdrant on 6333:

| Service | Laptop port |
|---|---|
| PostgreSQL | `127.0.0.1:15432` |
| Redis | `127.0.0.1:16379` |
| Qdrant | `127.0.0.1:16333` |

Write these ports into `infra/README.md`. Note that `.env.example` uses Docker's internal
names (`postgres`, `redis`, `qdrant`); in your own `.env`, use `127.0.0.1` plus the port
above when running the API from your laptop.

### 2.2 ARM check (30 min)
The server is ARM (AWS Graviton). For each image:
```bash
docker buildx imagetools inspect postgres:16 | grep arm64
```
Record the results in `infra/README.md`. **If any image lacks arm64, say so in the standup
today.**

### 2.3 Alembic (45 min)
Set Alembic up in `migrations/` (it already exists, with a `.gitkeep`), reading
`DATABASE_URL` from settings. Make one empty first revision.
**Done when:** `alembic upgrade head` works against the Compose PostgreSQL.

### 2.4 Streaming format with Shaan (20 min call)
Agree the answer-streaming events. Shaan writes them into `docs/API.md` today, and Meghna
builds against them tomorrow. Your real streaming route follows the same format in Week 3,
so **push back now** if anything won't work.

**Branch:** `akash/compose-alembic`

---

## Day 3, Thu 15 Oct: API skeleton + practice data in Qdrant

### 3.1 API skeleton (2.5 h)
`api/main.py`, with every route under `/api/v1`. **No business logic in `api/`**; that
lives in `core/`.

| Piece | What it does |
|---|---|
| `GET /api/v1/healthz` | Reports whether PostgreSQL, Redis and Qdrant are reachable |
| Request-ID middleware | Uses the incoming `X-Request-ID` or makes one; returns it on **every** response; puts it in every log line |
| One error format | Every error, including 404, 422 and 500, looks like `{"error": {"code": "...", "message": "...", "request_id": "..."}}` |
| OpenAPI | Published at `/api/v1/openapi.json`. Meghna generates her client from it |

It must start with `uvicorn api.main:app --reload`, which matches the VS Code debug
config already in `.vscode/launch.json`.

Tests: a health check, a request ID on a normal response, and the error format on a
missing route.

### 3.2 Load the practice data into Qdrant (1.5 h)
Shaan's practice dataset lands in `tests/fixtures/practice/` by the end of Day 2.

`infra/dev/load_fixtures.py`:
- Creates a dev collection named from settings (`QDRANT_COLLECTION`) and loads the chunks
  with their vectors (stored as float16; convert to float32) and payload
- **Safe to re-run**: drops and recreates the dev collection
- **Refuses to run against anything except localhost**

**Branch:** `akash/api-skeleton`

**Ask Claude Code:**
> Build the API skeleton per team/week-1/akash.md task 3.1 and docs/API.md "Rules every route follows". Then write infra/dev/load_fixtures.py per task 3.2. Add tests and run them.

---

## Day 4, Fri 16 Oct: the database tables

### 4.1 Migrations (3 h)
Tables from [`../../docs/DATA-MODEL.md`](../../docs/DATA-MODEL.md), the ones the MVP needs:

`users` · `consents` · `usage_daily` · `conversations` · `messages` · `message_sources` ·
`invented_citation_log` · `feedback` · `documents` · `document_chunks` · `audit_log` ·
`cases` · `act_sections` · `court_coverage`

**Not yet:** `organisations`, `memberships` and `subscriptions`. Team accounts and payments
moved to January.

Rules, which Shaan will check:
- IDs are UUIDs; **every** table has `created_at` and `updated_at`
- **No password column anywhere.** Firebase holds passwords.
- `document_chunks` keeps `page_no`, `char_start` and `char_end`
- `invented_citation_log.reason` allows exactly: `not_retrieved`, `record_missing`,
  `quote_not_found`, `claim_not_supported`
- `audit_log` has **no column that could hold document text**
- **Reversible:** `alembic downgrade base && alembic upgrade head` works cleanly

### 4.2 Load cases and Act sections into PostgreSQL (1 h)
Extend `infra/dev/load_fixtures.py` to fill `cases` and `act_sections` from the practice
dataset.

**Branch:** `akash/core-tables`. **Shaan must review before merge**, because the data
model is his to defend. Open it early in the day.

---

## Day 5, Sat 17 Oct: the first two real routes

### 5.1 Act section route (1.5 h)
`GET /api/v1/acts/{act}/sections/{n}`, **public** (no login).
- Returns the section text, title, Act name and year, and `source_url`
- **The in-force rule:** show `in_force` **only** when `act_status` is filled. Otherwise
  return the status "not checked" (Meghna shows "in-force status not checked")
- Missing section → 404 in the standard error format

Tests: one section with `act_status`, one without.

### 5.2 Judgment route (1.5 h)
`GET /api/v1/cases/{id}`
- The full text split into numbered paragraphs (`p1`, `p2`, …) for anchors
- Title, decision date, case number, `pdf_url`, and the citation string **exactly as
  stored**
- **Never** return `judges`, `petitioner` or `respondent`. A test must prove those fields
  are absent.
- Sign-in comes in Week 3. Leave a clear note where the check will go.

### 5.3 Hand over (1 h)
- [ ] Check the OpenAPI file shows both routes, so Meghna can generate her client
- [ ] Fill in the **Commands** section of `CLAUDE.md` with the real commands: start
      Compose, run migrations, start the API, run the tests
- [ ] Standup

**Branch:** `akash/act-and-judgment-routes`

---

## Done by Saturday

- [ ] CI Python job green on `main`
- [ ] `docker compose -f infra/docker-compose.yml up` starts all three, healthy
- [ ] ARM check recorded for every image
- [ ] Health check, error format and request IDs, with tests
- [ ] Tables migrated and reviewed by Shaan; undo works
- [ ] Act and judgment routes working on the practice data, with tests
