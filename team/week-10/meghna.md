# Meghna: Week 10 (Web), 3 h a day

**Theme: MVP done.** Bug bash 2 with the whole team, the **first-time welcome**, a general
feedback form, and a **simple landing page** for the private beta. By Saturday a beta user's
first five minutes are smooth.

**After Wednesday, only serious fixes.**

---

## Days 1 and 2, Mon 14 and Tue 15 Dec: bug bash 2

### 1.1 The whole team, 30 minutes each (Monday)
Ask Shaan, Akash and Ranveer to each spend **30 minutes** on the live server with a test
account, on their own phone, trying to break it. Ranveer especially: he knows what a lawyer
would try. Everything goes into GitHub issues with screenshots.

### 1.2 Fix (6 h over two days)
Yours first, worst first. Anything that could confuse a lawyer about **what's verified** is
the most serious kind of bug.

**Branch:** `meghna/bug-bash-2`

---

## Day 3, Wed 16 Dec: the welcome

### 3.1 First sign-in (3 h)
After consent, three short screens (skippable, never shown again):
1. **What it covers**: Supreme Court judgments and Central Acts, up to the snapshot date.
   Not High Courts or tribunals yet
2. **What the tick means**: "Record found in dataset", and what it doesn't promise. Link to
   the full page
3. **Tell us when it's wrong**: where the report button is, and why it matters
Wording from the onboarding guide, through the strings file.

**Branch:** `meghna/welcome`

---

## Day 4, Thu 17 Dec: general feedback

### 4.1 "Send feedback" (2.5 h)
In the menu on every screen: a short form (what were you trying to do, what happened) through
Akash's general feedback route. The same **"don't paste client details"** warning.

**Branch:** `meghna/general-feedback`

---

## Day 5, Fri 18 Dec: the landing page

### 5.1 A simple page for the private beta (2 h)
The V1 plan moved the marketing site to January; a private beta needs only this:
- What it is, in two sentences. **No claims** we can't prove: no user counts, no logos, no
  testimonials, no uptime or security claims (`docs/UX-COPY.md`, copy rules)
- "Private beta, by invitation" and a sign-in button
- Not legal advice; the data credit; the data-as-of date
- The product name **from config**, and **hidden from search engines** for now
  (`noindex`)

### 5.2 Beta go/no-go call (1 h)

**Branch:** `meghna/landing-page`

---

## Day 6, Sat 19 Dec: check the release

- [ ] After Akash deploys `v0.1.0-beta`: every screen once on the live server, phone and
      laptop (2 h)
- [ ] Fresh screenshots for the onboarding guide (30 min)
- [ ] Standup

**Branch (only if a fix is needed):** `meghna/release-check`

---

## Done by Saturday

- [ ] Bug bash 2 done with the whole team; serious bugs fixed
- [ ] First-time welcome (three screens)
- [ ] "Send feedback" on every screen
- [ ] Simple landing page: no unprovable claims, not indexed
- [ ] Release checked on the live server; guide screenshots updated
