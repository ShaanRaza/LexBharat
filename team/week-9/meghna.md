# Meghna: Week 9 (Web), 3 h a day

**Theme: bug bash 1, and the screens the beta needs.** By Saturday every problem found on
the live server is fixed or filed, the **admin page** exists for Shaan, the final legal
texts are in the app, and the **beta onboarding guide** is written with Ranveer.

---

## Days 1 and 2, Mon 7 and Tue 8 Dec: bug bash 1

### 1.1 Everything, on the real server (6 h over two days)
Start from the issues you filed on Sat 5 Dec. Then go through **every screen**, on a phone
and a laptop, signed in and signed out:

| Area | Try |
|---|---|
| Research chat | Normal questions, follow-ups, a trap, a personal-advice question, an out-of-scope question |
| Citations | Every tick and warning; jump to the passage; the "what this means" page |
| Acts and judgments | Lookup, anchors, the in-force rule, PDFs on tap |
| Uploads (test account) | All three file kinds, a failing scan, delete |
| Account | Consent, answers left, delete account, export |
| Failures | Turn off your connection mid-answer; reload mid-upload |

Fix what's yours. File what isn't, with a screenshot, labelled for the right lane.

**Branch:** `meghna/bug-bash-1`

---

## Day 3, Wed 9 Dec: the admin page

### 3.1 Screens for Shaan (3 h)
On Akash's admin routes, at `/admin` (not in the navigation):
- **Trust**: the share of answers with a removed citation, by day, against the **0.5%** line,
  and the four reasons
- **Runs**: each 200-question run's summary
- **Feedback**: newest first, with the reason and comment
- **Health**: upload queue, failed uploads, errors
Plain tables and one simple chart. Anyone who isn't an admin sees the normal "not found" page.

**Branch:** `meghna/admin-page`

---

## Day 4, Thu 10 Dec: the final legal texts

### 4.1 Legal pages (3 h)
When Shaan commits counsel's v1 documents:
- Pages at `/legal/privacy`, `/legal/terms`, `/legal/consent`, linked from the footer
- The consent screen, upload warning and not-legal-advice notice use the **v1** text
- **Remove the "Draft" mark only from documents that are now final**
- The text comes **from the files in `legal/`**, never retyped

**Branch:** `meghna/legal-pages`

---

## Day 5, Fri 11 Dec: onboarding guide + "private beta"

### 5.1 The beta guide, with Ranveer (2 h)
`team/beta/onboarding-guide.md`, then a short in-app version. Plain words, one page:
- What it covers (Supreme Court + Central Acts, snapshot date) and what it doesn't
- **What the tick means, and what it doesn't** (from `docs/CITATION-VERIFIER.md`)
- What to upload, and what not to (per the Week 8 go/no-go)
- How to report a wrong answer, and why it matters
- It's information, not legal advice

Take screenshots on the live server.

### 5.2 The "private beta" screen (1 h)
What someone not on the invite list sees after signing in: a polite "this is a private beta,
by invitation" with no further detail. Wording through the strings file (ask Shaan).

**Branch:** `meghna/onboarding-guide`

---

## Day 6, Sat 12 Dec: fixes

- [ ] Whatever bug bash 1 left (2.5 h)
- [ ] Standup (15 min)

---

## Done by Saturday

- [ ] Bug bash 1: everything fixed or filed
- [ ] Admin page for Shaan, invisible to everyone else
- [ ] Final legal texts in the app, from `legal/`; "Draft" marks only where still draft
- [ ] Beta onboarding guide written with Ranveer; "private beta" screen
