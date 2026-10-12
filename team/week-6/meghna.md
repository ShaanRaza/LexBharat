# Meghna: Week 6 (Web), 3 h a day

**Theme: chatting with your own document.** By Saturday a user opens a ready document, asks
about it, and gets an answer split into **"Your document says"** and **"Supreme Court
judgments say"**. Tapping a document citation **jumps to that page and highlights the
passage**. Every answer gets thumbs up/down and "Report a wrong answer".

**Test with public documents only.** Never a client document.

---

## Before Day 1

- [ ] Week 5 leftovers first
- [ ] Shaan's upload design in `docs/ARCHITECTURE.md` (Uploads): what D-labels are and how
      document citations look in the citations event

---

## Day 1, Mon 16 Nov: the document viewer

### 1.1 Viewer page (3 h)
`/documents/[id]`: the document's extracted text, **page by page**, with page numbers and
next/previous. Akash's page route lands on Tuesday; build against the OpenAPI types with a
small mock until then.
- Text first (fast on a weak connection). "Open the original file" is a separate tap, with
  the file size shown first
- Long pages scroll inside the viewer, not the whole screen

**Branch:** `meghna/document-viewer`

---

## Day 2, Tue 17 Nov: the document chat screen

### 2.1 Two kinds of source (3 h)
The chat screen, in document mode:
- A header showing **which document** this chat is about
- The answer in **two labelled parts**: **"Your document says"** (with page numbers) and
  **"Supreme Court judgments say"** (the usual citations)
- Document citations look **clearly different** from judgment citations (a page icon and
  "p. 4", not a case citation string)
- Everything else as before: citations only after the citations event; tick or warning per
  citation

**Branch:** `meghna/document-chat`

---

## Day 3, Wed 18 Nov: jump and highlight

### 3.1 Document citation → page (3 h)
A document citation carries `document_id`, `page_no`, `char_start` and `char_end`. Tapping
it opens the viewer **on that page** with exactly those characters highlighted, scrolled
into view.
- On a phone, the viewer opens over the chat with a clear "back to the answer"
- If the positions don't match the page (they always should), open the page **without** a
  highlight and say so. **Never highlight the wrong words**

**Branch:** `meghna/document-citations`

---

## Day 4, Thu 19 Nov: feedback

### 4.1 Thumbs and "Report a wrong answer" (3 h)
Under every answer, research and document alike, through `POST /feedback`:
- 👍 / 👎, one tap
- **"Report a wrong answer"**: choose a reason (wrong citation / wrong law / out of date /
  didn't answer my question / other) plus an optional comment
- Short "thank you" with no fuss. Wording through the strings file (ask Shaan for any
  sentence that isn't in `docs/UX-COPY.md` yet)
- **The comment box warns: don't paste client details**

**Branch:** `meghna/feedback`

---

## Day 5, Fri 20 Nov: uploads on the real worker

### 5.1 End to end (3 h)
With Akash's worker wired today: upload a public text PDF, a Word file and a scan, and
watch each go through every real status to `ready`. "Ask about this document" now starts a
document chat.
- Fix anything that looked fine on mocks but breaks on real data (long filenames, 0-page
  failures, slow scans)
- Time the whole flow for each file in the PR

**Branch:** `meghna/uploads-live`

---

## Day 6, Sat 21 Nov: phone and accessibility pass

- [ ] The full document flow at 375 px: upload, status, chat, jump, back (1.5 h)
- [ ] Keyboard and screen reader: the highlight is announced, not just coloured (1 h)
- [ ] Standup (15 min)

**Branch:** `meghna/document-polish`

---

## Done by Saturday

- [ ] Viewer: text page by page; original file only on tap
- [ ] Document chats split into "your document says" and "Supreme Court judgments say"
- [ ] Citations jump to the page and highlight the exact passage (or say they couldn't)
- [ ] Thumbs and "report a wrong answer" on every answer
- [ ] Real uploads of all three file kinds work end to end
- [ ] Checked at 375 px, by keyboard and with a screen reader
