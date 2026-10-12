# Meghna: Week 8 (Web), 3 h a day

**Theme: ready for real phones and real people.** Lawyers research in court on weak phone
connections, so this week the website has to work **text-first on a slow network**, be
**installable** on a phone, and pass an **accessibility check**. On Friday it goes onto the
real server, and on Saturday you look at every screen there.

---

## Day 1, Mon 30 Nov: installable app (PWA)

### 1.1 The basics (3 h)
- A web app manifest: the name **from config** (never typed), icons, colours from the
  design tokens
- Installable on Android and iPhone ("Add to Home screen")
- A service worker that caches **only the app's own files** (layout, styles, scripts) so it
  opens fast. It must **never cache API responses, answers, conversations or documents**.
  Those are private and must stay fresh. A test checks what's cached

This is first on the V1 plan's drop list, so keep it simple.

**Branch:** `meghna/pwa`

---

## Days 2 and 3, Tue 1 and Wed 2 Dec: the phone and slow-network pass

### 2.1 Every screen, on a phone, on "Slow 3G" (6 h over two days)
In the browser's tools, at 375 px, with the network on "Slow 3G":

| Check | Every screen |
|---|---|
| **Text first** | Words appear before anything heavy; placeholders, not spinners |
| PDFs | Only on tap, with the size shown first |
| Tap targets | Big enough for a thumb; nothing too close together |
| Long content | Judgments, Act sections and documents scroll smoothly |
| Weight | Check the size of the first page load and note it in the PR; cut anything unused |
| Lost connection | A plain message and a retry, never a blank screen |

Fix as you go, and open one pull request at the end of Day 3.

**Branch:** `meghna/phone-pass`

---

## Day 4, Thu 3 Dec: accessibility check

### 4.1 `a11y-audit` (3 h)
Run the **`a11y-audit`** skill over every screen, then fix what it finds, most serious
first:
- Colour contrast (the amber "not found" and the warning marks especially)
- Every button and icon has a text label; the tick and warning are **words to a screen
  reader**, not just colour
- Headings in order; focus visible; everything reachable by keyboard
- Streaming answers announced politely, not word by word

**Branch:** `meghna/a11y`

---

## Day 5, Fri 4 Dec: the production build

### 5.1 With Akash (3 h)
- The website's container in production Compose (Akash's file; agree the change with him)
- `NEXT_PUBLIC_API_URL` set to the real domain. **Say in the PR exactly which address the
  website uses afterwards**, and don't change it back silently
- Firebase settings for the real domain
- **Mock sign-in impossible** in the production build. Test it
- `/dev/states` **not reachable** in production

**Branch:** `meghna/prod-build`

---

## Day 6, Sat 5 Dec: every screen on the real server

- [ ] Go through every screen on the real domain, on your phone and a laptop (2 h)
- [ ] Every problem becomes a **GitHub issue** with a screenshot, labelled `web`. These start
      Week 9's bug bash (45 min)
- [ ] Standup (15 min)

---

## Done by Saturday

- [ ] Installable; the service worker never caches private data
- [ ] Every screen passes the phone and slow-network checks
- [ ] Accessibility audit run; serious issues fixed
- [ ] Production build on the server; mock sign-in and `/dev/states` impossible there
- [ ] Every screen checked on the live server; problems filed as issues
