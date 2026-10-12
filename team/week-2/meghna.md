# Meghna: Week 2 (Web), 3 h a day

**Theme: the screens move onto the real API.** By Saturday the judgment page, the Act page
and the conversation list read from Akash's routes, not sample files. The sign-in screens
exist on a mock. Real sign-in comes in Week 4.

Keep using **`impeccable`** for design work, and the three rules from Week 1: wording only
from the strings file, citations only after the citations event, and never judge or party
names.

> **Tue 20 Oct is Dussehra.** If you take it off, **task 5.2 (role chooser) moves to
> Saturday** and the **phone pass (6.2) moves to Week 3**. Say so in the standup.

---

## Before Day 1

- [ ] Anything unfinished from Week 1 goes **first**
- [ ] Run the API locally (`infra/README.md`) so you can see real responses. Ask Akash if it
      won't start; don't lose more than 30 minutes on it

---

## Day 1, Mon 19 Oct: the API client

### 1.1 Generate the client (2 h)
CLAUDE.md rule 3: the website talks to the backend **only through the API**, and its client
is **generated** from the OpenAPI file, never written by hand.

- Use **openapi-typescript** (for the types) and **openapi-fetch** (for the calls)
- `npm run gen:api` reads `web/openapi.json` (Akash commits a copy on Friday; until then
  fetch it from your local API and commit it yourself)
- One file `web/src/lib/api.ts` creates the client. The base URL comes from
  `NEXT_PUBLIC_API_URL`
- **No hand-written types for anything the API returns.** If a type is wrong, the fix goes
  in the API, not the website

### 1.2 One error handler (1 h)
Every API error has the same shape: `{"error": {"code", "message", "request_id"}}`.
Write one function that maps `code` to the right failure screen from Week 1, and shows the
`request_id` in small text so a user can quote it in a complaint.

**Branch:** `meghna/api-client`

---

## Day 2, Tue 20 Oct: judgment and Act pages on the real API

### 2.1 Switch over (2 h)
Your Week 1 pages read the practice files. Point them at `GET /cases/{id}` and
`GET /acts/{act}/sections/{n}` through the generated client.
- A **loading state** (text-shaped grey blocks, no spinner) and an **error state** for each
- 404 shows a plain "not found in our dataset" page, wording from the strings file
- Paragraph anchors (`#p12`) still scroll and highlight

### 2.2 Remove the sample reader (30 min)
Delete the mock that read `tests/fixtures/` directly, so nothing quietly bypasses the API.

**Branch:** `meghna/real-pages`

---

## Day 3, Wed 21 Oct: the conversation list

### 3.1 Conversation list (2.5 h)
`GET /conversations`, built on Akash's Tuesday route.
- Newest first: title, date, number of messages
- "Load more" at the bottom using `next_cursor` (no page numbers)
- Empty state: a short line and the "Ask" button
- On a phone it's its own screen; on a laptop it's a left-hand panel

Akash's route not merged yet? Build against the types in `web/openapi.json` with a small
mock, and switch when it lands.

**Branch:** `meghna/conversation-list`

---

## Day 4, Thu 22 Oct: conversation history

### 4.1 One citation component (1 h)
Move the citation display from the chat screen into one shared component: tick or warning
mark **per citation**, the citation string labelled *"as recorded in the dataset"*, and the
link. History and the live chat both use it, so they can never drift apart.

### 4.2 History page (2 h)
`/c/[id]` from `GET /conversations/{id}`: every question and answer, with each answer's
citations through the shared component, and the data-as-of date, credit and notice under
each answer.

**Branch:** `meghna/conversation-history`

---

## Day 5, Fri 23 Oct: sign-in screens on a mock

### 5.1 Sign-in and sign-up (2 h)
The screens only. Firebase gets wired in during Week 4.
- "Continue with Google" and email sign-in
- A **mock** sign-in that just sets a fake user, behind `NEXT_PUBLIC_MOCK_AUTH`. It must be
  impossible to switch on in a production build
- Signed-out users who open a protected page are sent to sign-in, then **back to where
  they were**

### 5.2 Role chooser + consent placeholder (1 h)
- After the first sign-in: advocate / student / in-house / other
- A consent screen **placeholder**, clearly marked **"Draft"**. The real notice comes from
  counsel, so don't write legal wording yourself

**Branch:** `meghna/sign-in-mock`

---

## Day 6, Sat 24 Oct: Act lookup + phone pass

### 6.1 Act lookup (2 h)
`/acts`: one box where a user types an Act and a section ("NI Act 138", "BNS 103") and lands
on the section page. Suggest Act names as they type. If nothing matches, say so plainly and
offer the search instead. This is the free, public **Act and section lookup** from the MVP.

### 6.2 Phone pass (45 min)
Every screen built so far, at 375 px: nothing cut off, tap targets big enough, text readable
without zooming. Fix what you find.

### 6.3 Standup (15 min)

**Branch:** `meghna/act-lookup`

---

## Done by Saturday

- [ ] API client generated from OpenAPI; no hand-written API types
- [ ] One error handler; request ID visible on errors
- [ ] Judgment and Act pages on the real API, with loading and error states
- [ ] Conversation list with "load more"; history page using the shared citation component
- [ ] Sign-in, role chooser and consent placeholder on a mock that can't reach production
- [ ] Act lookup page
- [ ] Every screen checked at 375 px and 1280 px
