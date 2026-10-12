# Meghna: Week 3 (Web), 3 h a day

**Theme: the chat screen goes live.** By Saturday you ask a real question and watch a real
answer stream in, with real ticks and warnings, saved into a conversation you can come back
to. The citations jump to the exact passage in the judgment.

This is the screen lawyers will judge the product by. Use **`impeccable`**, and check every
state at 375 px and 1280 px.

---

## Before Day 1

- [ ] Week 2 leftovers first
- [ ] Your local setup runs with `USE_FAKE_ADAPTERS` on, so the fake pipeline answers
      without paid keys

---

## Day 1, Mon 26 Oct: a stream reader for the real API

### 1.1 The stream client (2.5 h)
The browser's built-in `EventSource` can't send a POST with a sign-in header, so read the
stream with `fetch` instead.
- `web/src/lib/stream.ts`: sends the question, reads the response piece by piece, and turns
  it into the four event types from `docs/API.md`
- Copes with an event **split across two network chunks**
- A setting picks the source: your Week 1 `mockStream.ts`, or the real API

Tests: a recorded stream played back in odd-sized pieces gives the same events.

### 1.2 Switch the chat screen over (30 min)
Same screen, new source. Nothing else changes yet.

**Branch:** `meghna/stream-client`

---

## Day 2, Tue 27 Oct: every real event on the screen

### 2.1 Handle each event (3 h)

| Event | What the screen does |
|---|---|
| `token` | Appends the text. **Never** shows a citation |
| `citations` | Shows the sources, each with a **tick** (supports) or **warning mark** (partly). If `removed_count` is above zero, the note that an authority couldn't be verified |
| `done` | Stops the "writing" indicator; updates answers left |
| `error` | The right failure screen for its `code`, with the request ID |
| not found | The "No relevant results" screen. No answer box at all |
| keyword only | The **"keyword results only"** label and a retry |
| model failed | The sources with links but **no written answer**, and a retry |

**Branch:** `meghna/chat-real-events`

---

## Day 3, Wed 28 Oct: chats that save

### 3.1 Conversations from the chat screen (3 h)
- The first question **starts a conversation** (`POST /conversations`), and the address
  becomes `/c/[id]`
- Follow-up questions go into the same conversation
- Reloading the page shows the history (your Week 2 page) and lets you carry on
- "New chat" button; the conversation list updates

**Branch:** `meghna/chat-conversations`

---

## Day 4, Thu 29 Oct: jump to the passage

### 4.1 Citation → judgment page (3 h)
Tapping a citation opens the judgment **at the passage that was cited**, highlighted.

The citation carries the `record_id` and the passage text. The judgment page is split into
numbered paragraphs. **Proposal** (agree it with Shaan on Monday): the link passes the
chunk ID, the page finds the paragraph where that passage starts, scrolls to it and
highlights the passage.

If the passage can't be found on the page, open the judgment at the top and say so. **Never
highlight the wrong paragraph.**

**Branch:** `meghna/jump-to-passage`

---

## Day 5, Fri 30 Oct: the source panel

### 5.1 Sources you can read in place (2 h)
- Tap a source → its exact passage text expands, **one at a time**
- The badge reads **"Record found in dataset"**, with the data-as-of date and a small
  "what this means" link

### 5.2 "What the tick means" page (1 h)
`/about/verification`: the "means / does not mean" table from
[`../../docs/CITATION-VERIFIER.md`](../../docs/CITATION-VERIFIER.md), **word for word**
through the strings file. Plain layout. This page is where the trust claim is explained
honestly, so don't soften it.

`GET /cases/{id}` needs sign-in from today (Akash's Day 5). Make sure the judgment page sends
the token.

**Branch:** `meghna/source-panel`

---

## Day 6, Sat 31 Oct: polish and numbers

### 6.1 Polish pass (2 h)
- Keyboard: you can ask, read and open sources without a mouse; focus is visible
- Screen readers: the tick and warning have text labels, not just colour
- Slow connection (browser dev tools, "Slow 3G"): the text still appears word by word

### 6.2 Your numbers for the re-plan (30 min)
Send Shaan your tasks planned vs done and hours for Weeks 1 to 3. **Be honest.** The re-plan
is only as good as these numbers.

### 6.3 Standup (30 min)

**Branch:** `meghna/week3-polish`

---

## Done by Saturday

- [ ] Stream client copes with split events; chat screen on the real API
- [ ] Every event and failure state shown correctly
- [ ] Chats save into conversations and reload
- [ ] Citations jump to and highlight the passage (or say they couldn't)
- [ ] Source panel and the "what the tick means" page
- [ ] Keyboard, screen-reader labels and slow-network checked
