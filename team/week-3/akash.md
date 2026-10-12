# Akash: Week 3 (Platform), 4 h a day

**Theme: real sign-in and real streaming.** By Saturday a signed-in user asks a question
and the answer streams back word by word, then **one** citations event, then done. Every
route except the public ones refuses a request without a valid sign-in.

Two pieces need Shaan's careful review: the **streaming route** and the **test that no
citation leaves early**. A citation shown before verification breaks the product's core
promise.

---

## Before Day 1

- [ ] Week 2 leftovers first
- [ ] Firebase dev project ready (Week 2, task 5.2); the service-account file outside the repo

---

## Day 1, Mon 26 Oct: the Firebase token check

### 1.1 The adapter (1.5 h)
CLAUDE.md rule 1: one file per outside service. `adapters/auth_firebase.py` does one thing:
takes a token and returns the Firebase user ID and email, or says it's invalid. It has a
**fake** for tests.

### 1.2 `current_user` switches over (2 h)
The dependency from Week 2 now:
- Reads `Authorization: Bearer <token>` and checks it through the adapter
- **Creates the `users` row on first sign-in** (by `firebase_uid`), then returns it
- Writes a `login` row to the audit log on first sign-in of a session
- Missing or bad token → **401** in the standard error format
- The Week 2 dev user still works **in dev only**, so local testing doesn't need Firebase

### 1.3 A function Shaan needs by Wednesday (30 min)
Shaan's verifier needs `core/store/citations.py: log_invented_citation(...)` by Wednesday.
Write it today: question, model, cited text, reason (one of the four only).

**Branch:** `akash/firebase-auth`

---

## Day 2, Tue 27 Oct: `GET /me`

### 2.1 Profile route (2 h)
`GET /api/v1/me`: profile, plan, and **answers left this month**. The real meter arrives in
Week 4; for now, answers left = the plan's limit (from settings) minus answers counted in
`usage_daily` this month.

`PATCH /api/v1/me` sets the **role** (advocate / student / in-house / other) and name, for
Meghna's role chooser. It isn't in `docs/API.md` yet, **so add it there in the same PR**.

### 2.2 Tests (1.5 h)
- [ ] New token → user created once, never twice (even with two requests at once)
- [ ] Role must be one of the four
- [ ] A user can only ever read and change **their own** profile

**Branch:** `akash/me-route`

---

## Day 3, Wed 28 Oct: the streaming route

### 3.1 `POST /api/v1/conversations/{id}/messages` (3 h)
- Checks the conversation belongs to the user (404 if not)
- Saves the user's question
- Calls `core.pipeline.run(...)` (still the **fake** today) and turns each event into a
  server-sent event: `token`, `citations`, `done`, `error`
- When the stream finishes, saves the answer, model, token counts, timing and **each
  source** (`message_sources`) through `core/store/`. That's pipeline step 11 (save)
- If the user closes the tab, **stop the model call**, so nobody pays for an answer no one
  reads

### 3.2 Errors mid-stream (1 h)
If something fails after tokens have started, send one `error` event and stop. **Never** send
a citations event after an error.

**Branch:** `akash/stream-route`

**Ask Claude Code:**
> Build POST /api/v1/conversations/{id}/messages per team/week-3/akash.md Day 3 and the "Streaming events" section of docs/API.md. It calls core.pipeline.run and only converts events to SSE. Save the message and its sources through core/store at the end. Stop the model call if the client disconnects. Explain the event flow with a diagram.

---

## Day 4, Thu 29 Oct: prove no citation leaves early

### 4.1 The order test (2.5 h)
This test guards the trust promise, so it must pass before any deploy. On a full streamed
response, assert:
- [ ] Zero or more `token` events, then **exactly one** `citations` event, then `done`
- [ ] **No token text contains a source label** (`[S1]`), a `record_id` or a citation string
- [ ] After an `error` event, **no** citations event
- [ ] The "not found" path sends no tokens and no citations: just the not-found event and done

### 4.2 Switch to the real pipeline (1.5 h)
When Shaan's `shaan/pipeline-wired` merges (Thursday), your route uses the real `run(...)`.
**Nothing in the route should change.** If something has to, tell Shaan: the contract
missed something.

**Branch:** `akash/stream-order-test`

---

## Day 5, Fri 30 Oct: sign-in on every route

### 5.1 Lock everything down (2 h)
API.md: every route needs a Firebase token **except** the public ones (Act sections, and
later the stats pages and sitemap).
- One test that walks **every route in the OpenAPI file** and checks it returns 401 without a
  token, except a short, written list of public routes. A new route added without auth then
  fails CI automatically
- `GET /cases/{id}` now needs sign-in. Tell Meghna in the standup

### 5.2 Joint check (1 h)
With Shaan and Meghna: a real question, on the real screen, through your route. Watch the
order of events.

### 5.3 Standup + refresh `web/openapi.json` (30 min)

**Branch:** `akash/auth-everywhere`

---

## Day 6, Sat 31 Oct: buffer and the re-plan

- [ ] Finish anything that slipped this week (2 h)
- [ ] Send Shaan your **honest numbers for Weeks 1 to 3**: tasks planned vs done, hours
      planned vs spent. He re-plans today (1 h)
- [ ] Standup

---

## Done by Saturday

- [ ] Firebase token check through one adapter; users created on first sign-in
- [ ] `GET /me` and `PATCH /me`, documented in `docs/API.md`
- [ ] Streaming route on the real pipeline, saving messages and sources
- [ ] The order test passes: one citations event, after the text, never after an error
- [ ] Every non-public route refuses requests without a token, checked automatically
