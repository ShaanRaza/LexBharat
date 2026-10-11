# Meghna: Week 1 (Web), 3 h a day

Your week builds the screens people will actually use, on **sample data**, so you never
have to wait for the backend. By Saturday: the chat screen, every failure screen, the
judgment page and the Act page all work and look right on a phone and a laptop.

Use the **`impeccable`** skill in Claude Code for design work. The design source is
[`../../docs/KanoonBuddy-Website-Design-Doc-v2.md`](../../docs/KanoonBuddy-Website-Design-Doc-v2.md).

---

## Before Day 1 (~20 min)

- [ ] Node.js **22** (CI uses 22), Git, VS Code, Claude Code
- [ ] Clone the repo; accept VS Code's recommended extensions
- [ ] Read [`../../CLAUDE.md`](../../CLAUDE.md) §1 and §5 (what the tick means),
      [`../../docs/UX-COPY.md`](../../docs/UX-COPY.md), and [`../README.md`](../README.md)

### Three rules for every screen you build

1. **Never invent wording.** Every user-facing sentence comes from `docs/UX-COPY.md`,
   through one strings file.
2. **A citation is shown only after the `citations` event**, with a tick or warning **per
   citation**. Never one badge for the whole answer.
3. **Never show judge or party names**, even if the data contains them.

---

## Day 1, Tue 13 Oct: the web app + design tokens

**Kickoff call:** 30 min with everyone.

### 1.1 Create the app (75 min)
Delete `web/.gitkeep`, then in Terminal from the repo root:
```bash
npx create-next-app@latest web --typescript --tailwind --eslint --app --src-dir --use-npm
```
- Use **npm**. CI runs `npm ci` and needs `web/package-lock.json`.
- CI runs `npm run lint`, `npx tsc --noEmit` and `npm run build`. **Check `package.json`
  has a `lint` script**; newer Next.js versions don't add one the old way.
- Run all three locally before opening the PR.

### 1.2 Design tokens (60 min)
From §6 of the design doc:

| Token | Value |
|---|---|
| `text` | `#0F1B33` |
| `accent` / `accent-hover` | `#D9480F` / `#B43A0A` |
| `panel` / `tint` | `#FFF5EE` / `#FFE3D0` |
| `line` | `#F3E1D4` |
| `verified` (the tick) | `#1F7A4D` |
| `notfound` (the "not found" state) | `#B45309` |

Font: **Plus Jakarta Sans** through `next/font`: 800 for headlines, 400 for body, 600 to
700 for labels. Content width up to 1040 px. Rounded cards, thin borders, no heavy
shadows. **Light theme only.**

### 1.3 Pull request (15 min)
**Branch:** `meghna/web-setup`. **Done when:** CI's **web** job runs on your PR and is
green. Today it switches on for the first time.

---

## Day 2, Wed 14 Oct: app shell + the strings file

### 2.1 App shell (90 min)
- Header: the product name from `NEXT_PUBLIC_PRODUCT_NAME`. **Never type "KanoonBuddy"
  into the code**; the name may change.
- Navigation: **Ask · Acts · My documents · Account**. It collapses into a menu on phones.
- Footer on every page: the not-legal-advice line, `Data: Open India Law by Vaquill AI, CC
  BY 4.0`, and a "Data as of …" placeholder.
- Build for a **375 px phone first**, then widen to desktop.

### 2.2 The strings file (60 min)
`web/src/lib/strings.ts`. Copy the **exact** wording from `docs/UX-COPY.md`:
- all seven failure states
- the badge: **"Record found in dataset"**
- the standing notices and the coverage message
- the credit line

From now on, components read text **only** from this file.

### 2.3 Pull request (30 min)
**Branch:** `meghna/app-shell`. Add screenshots at 375 px and 1280 px.

---

## Day 3, Thu 15 Oct: the chat screen (on a fake stream)

Shaan and Akash write the **streaming format** into `docs/API.md` by the end of Day 2.
Read that section first.

### 3.1 A fake stream (45 min)
`web/src/lib/mockStream.ts` plays back an answer **exactly** in that format: words one by
one, then **one** citations event, then done. Add small delays so it feels real. Label the
content **"Sample"**.

### 3.2 The chat screen (2 h)
- A question box, plus 3 example questions as tappable chips (labelled "Sample")
- The answer **streams in word by word**
- **No citation appears until the citations event arrives.** Then show the sources, each
  with:
  - a **tick** (supports) or a **warning mark** (partly), **per citation**
  - the title, and the citation string labelled *"as recorded in the dataset"* when there
    is one
  - a link to the source
- If any citations were removed: the note that one authority could not be verified
- Under every answer: data-as-of date, CC BY credit, not-legal-advice notice
- Tapping a source expands its exact text, **one at a time**

**Done when:** it works at 375 px and 1280 px. Put both screenshots in the PR.

**Branch:** `meghna/chat-screen`

**Ask Claude Code:**
> Using the impeccable skill and docs/KanoonBuddy-Website-Design-Doc-v2.md, build the chat screen per team/week-1/meghna.md Day 3. Stream from web/src/lib/mockStream.ts, which follows the "Streaming events" section of docs/API.md. All wording from web/src/lib/strings.ts. Check it at 375 px and 1280 px.

---

## Day 4, Fri 16 Oct: every failure screen

### 4.1 Failure screens (2.5 h)
One component each. Wording **only** from the strings file:

| State | What the user sees |
|---|---|
| No relevant results | No answer at all, plus suggestions to rephrase or use Act lookup |
| Meaning search down | A notice, results labelled **"keyword results only"**, and a retry button |
| AI answer failed | The sources with links but **no written answer**, and a retry button |
| Outside coverage | The coverage message, with a link to the official court site |
| Personal-advice question | The stronger notice **at the top** of the answer |

Add a page at `/dev/states` that shows all of them side by side for checking. Don't link it
from the navigation. Use the amber `notfound` colour for "not found".

### 4.2 Pull request (30 min)
**Branch:** `meghna/failure-screens`, with a screenshot of `/dev/states`.

---

## Day 5, Sat 17 Oct: judgment page + Act page

Use Akash's routes if they're merged by the time you start. Otherwise read the files in
`tests/fixtures/practice/` through a small mock, and switch over next week.

### 5.1 Judgment page (90 min)
`/cases/[id]`
- **Text first.** Paragraphs carry anchors, so a link to `#p12` scrolls to and highlights
  paragraph 12
- The PDF opens **only on tap**, with its file size shown first (lawyers on weak phone
  connections)
- The citation string labelled *"as recorded in the dataset"*
- **No judge or party names**, ever

### 5.2 Act section page (60 min)
`/acts/[act]/[section]`
- The section text
- An in-force badge **only if** `act_status` is filled. Otherwise show **"in-force status
  not checked"**
- Data-as-of date and the credit line

### 5.3 Pull request + standup (30 min)
**Branch:** `meghna/judgment-act-pages`

---

## Done by Saturday

- [ ] CI web job green on `main`
- [ ] App shell with footer notices; no hard-coded product name
- [ ] Strings file holds every user-facing sentence
- [ ] Chat screen streams, with citations only after the citations event, per citation
- [ ] All five failure screens, viewable at `/dev/states`
- [ ] Judgment page with paragraph anchors; Act page with the in-force rule
- [ ] Every screen checked at 375 px and 1280 px
