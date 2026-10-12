# Akash: Week 2 (Platform), 4 h a day

**Theme: the API grows real routes.** By Saturday: a user (a fake dev user for now) can
start a conversation, list conversations, read one back with its sources, and run a direct
search. Every list pages properly, and CI tests against a real PostgreSQL.

Two things need Shaan: the **contract call** on Monday, and his review of **`core/store/`**
(database code in his folder).

> **Tue 20 Oct is Dussehra.** If you take it off, **task 3.2 (audit log) moves to
> Saturday**, and **6.2 (smoke script) moves to Week 3**. Say so in the standup.

---

## Before Day 1

- [ ] Anything unfinished from Week 1 goes **first**
- [ ] `docker compose -f infra/docker-compose.yml up` healthy; `alembic upgrade head` clean

---

## Day 1, Mon 19 Oct: contract call + a dev user

### 1.1 Contract call with Shaan (30 min)
Shaan proposes; you push back if anything won't work for you. Three decisions:
1. **`core/store/`** is where database code lives. You write it; Shaan reviews.
2. **`USE_FAKE_ADAPTERS`**: dev laptops run with test fakes, no paid keys. The app refuses
   to start with it on outside dev.
3. **The streaming route calls `core.pipeline.run(...)`** and only turns its events into
   server-sent events.

### 1.2 Database sessions (1 h)
`core/store/db.py`: one SQLAlchemy session per request, opened and closed by a FastAPI
dependency. Settings give the URL. Nothing else in the app opens its own connection.

### 1.3 A dev-only user (2 h)
Sign-in arrives in Week 3. Until then routes still need **a user**, so every query can be
filtered by `user_id` from the start.

- `api/deps.py`: `current_user`. **In dev only**, it reads an `X-Dev-User` header and
  returns (or creates) that user
- **Outside dev it refuses**: the app won't start if dev users are switched on with
  `ENV` not equal to `dev`. A test proves it
- In Week 3 the same dependency switches to the Firebase token check, so **no route
  changes**

**Branch:** `akash/dev-auth`

---

## Day 2, Tue 20 Oct: conversation routes

### 2.1 Routes (3 h)
From [`../../docs/API.md`](../../docs/API.md):

| Route | Does |
|---|---|
| `POST /api/v1/conversations` | Start a conversation (`module`: `research`; `document` comes with uploads) |
| `GET /api/v1/conversations` | The user's conversations, newest first |
| `GET /api/v1/conversations/{id}` | Full history: messages plus each message's sources |

- **Every query filters by the current user.** Asking for someone else's conversation
  returns **404, not 403**, so it doesn't even confirm it exists
- Database code goes in `core/store/conversations.py`; the routes only call it
- Sources come back with the citation string **as stored**, and never `judges`,
  `petitioner` or `respondent`

### 2.2 Tests (1 h)
- [ ] User A can't read, list or see user B's conversation (the most important test this week)
- [ ] History returns messages in order, with their sources

**Branch:** `akash/conversations`

**Ask Claude Code:**
> Build the three conversation routes per team/week-2/akash.md Day 2 and docs/API.md. Database code in core/store/conversations.py, routes in api/. Every query filters by current_user. Another user's conversation returns 404. Write the isolation test first.

---

## Day 3, Wed 21 Oct: paging + the audit log

### 3.1 Cursor paging (1.5 h)
API.md: **every list uses cursor pagination**. One shared helper, not one per route.
- Request: `?limit=` (default 20, max 100) and `?cursor=`
- Response: `items` and `next_cursor` (empty on the last page)
- The cursor is opaque to the client: encode it, don't expose raw IDs or offsets
- Apply it to `GET /conversations`

### 3.2 The audit-log writer (1.5 h)
`core/store/audit.py`: `record(user_id, action, target_id, ip, request_id)`.
- `action` is one of: login, upload, delete, export, admin_view
- **It has no parameter that could carry text**, so document text can't end up there
- Nothing calls it yet. Login (Week 3), uploads and delete (Weeks 5 to 7) wire it in

Tests: a row is written with the request ID; an unknown action is refused.

**Branch:** `akash/pagination-audit`

---

## Day 4, Thu 22 Oct: the direct search route

### 4.1 `GET /api/v1/search` (3 h)
**Direct search with filters, no AI answer**, so it's cheap. It calls Shaan's
`core/search.py` (merged Wednesday). If it isn't merged yet, build against the function
signature in `core/pipeline.py` with the fake, and switch over on Friday.

| Parameter | Example |
|---|---|
| `q` | `cheque bounce limitation` |
| `court` | `supreme_court` (the only value in v1) |
| `year_from`, `year_to` | `1990`, `2010` |
| `act`, `section` | `Negotiable Instruments Act`, `138` |
| `case_number` | as stored |

- Returns the title, a short snippet, `record_id`, the citation string **as stored**, the
  link, and `keyword_only` when the meaning search was unavailable
- Paged with the Day 3 helper
- Bad filters (a year range backwards, an unknown court) give a 422 in the standard format

**Branch:** `akash/search-route`

---

## Day 5, Fri 23 Oct: OpenAPI tidy + Firebase prep

### 5.1 Make the OpenAPI file good for Meghna (1.5 h)
She generates her client from it, so its quality is her productivity.
- Every route has a **response model**, not a bare dict
- Stable **operation IDs** (`list_conversations`, not `list_conversations_api_v1_get`)
- The error format declared as a shared schema on every route
- **Commit a copy** to `web/openapi.json` with a script that refreshes it, so the web build
  never needs the API running. CI fails if the copy is out of date

### 5.2 Firebase project for sign-in (1.5 h)
Week 3 starts with the token check, so set it up now:
- One Firebase project for development; Google and email sign-in switched on
- The service-account file stays **outside the repo**; its path goes in your `.env`
- Write down (in `infra/README.md`) what Meghna needs on the web side. The web config
  values are public by design, but still go through `NEXT_PUBLIC_*` settings
- **Never paste the service-account file anywhere.** If it leaks, delete the key in the
  Firebase console

**Branch:** `akash/openapi-firebase-prep`

---

## Day 6, Sat 24 Oct: CI against a real database

### 6.1 CI integration job (2.5 h)
Today the Python CI job runs without a database, so the isolation tests can't run there.
- Add PostgreSQL 16 as a **service container** in `.github/workflows/ci.yml`
- Run `alembic upgrade head`, then the tests marked `integration`
- The conversation isolation test **must** run in CI from now on

### 6.2 A smoke script (1 h)
`infra/dev/smoke.sh`: start Compose, migrate, load the practice data, call every route
once, and print OK or the failing route. Anyone can run it after `git pull` to check their
laptop.

**Branch:** `akash/ci-integration`

---

## Done by Saturday

- [ ] `core/store/` set up; dev user that refuses to run outside dev
- [ ] Conversation routes, with the cross-user test passing **in CI**
- [ ] Cursor paging shared by every list
- [ ] Audit-log writer that can't hold text
- [ ] `GET /search` on Shaan's search, with filters and paging
- [ ] OpenAPI tidy and copied to `web/openapi.json`; Firebase project ready
- [ ] CI runs against a real PostgreSQL
