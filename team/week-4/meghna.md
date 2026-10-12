# Meghna: Week 4 (Web), 3 h a day

**Theme: real sign-in, and the 200-question test set.** By Friday users really sign in,
agree to the consent notice and see how many answers they have left. You also turn the
interview questions and traps into the **200-question test set**, the yardstick every
release is measured against.

> **Fri 6 Nov is Dhanteras and Sat 7 Nov is Choti Diwali.** Saturday is light on purpose.

---

## Before Day 1

- [ ] Week 3 leftovers first
- [ ] The Firebase web settings from Akash (`infra/README.md`), in your `.env.local`

---

## Day 1, Mon 2 Nov: real sign-in

### 1.1 Firebase in the website (3 h)
Replace the Week 2 mock with real Firebase sign-in: Google and email.
- `web/src/lib/auth.ts` is the **only** file that talks to Firebase
- Every API call sends the sign-in token automatically, and refreshes it when it expires
- Sign out clears everything
- The mock stays **for local development only**, and a production build can't switch it on

**Branch:** `meghna/firebase-sign-in`

---

## Day 2, Tue 3 Nov: consent and role, for real

### 2.1 Consent screen (2 h)
On Akash's consent routes (merged Wednesday; build against the OpenAPI types until then):
- After first sign-in, the notice is shown **in full** before anything else, with its
  version. The user can't ask a question until they agree
- The `consent_required` error from any route brings this screen back
- Account page: **withdraw consent**, with a plain explanation of what that stops
- The notice text is the **draft** from `legal/`, and the screen shows the "Draft" mark
  while it is one

### 2.2 Role chooser on the real API (1 h)
`PATCH /me`, from your Week 2 screen.

**Branch:** `meghna/consent-role`

---

## Day 3, Wed 4 Nov: answers left

### 3.1 The numbers (2 h)
- "**N research answers left this month**". Plain numbers, never credits (UX-COPY rule)
- Read from the `X-Answers-Remaining` header after each answer, and from `GET /me` on load
- The monthly-limit screen for `quota_exceeded`. Shaan writes its wording on Wednesday;
  use it from the strings file
- A cached answer doesn't change the number. Don't fake a change

### 3.2 Account page (1 h)
Name, role, plan, answers left, sign out, withdraw consent. **Delete account** and **export**
come in Week 7; leave a clear placeholder.

**Branch:** `meghna/answers-left`

---

## Day 4, Thu 5 Nov: the 200-question set

### 4.1 The format (1 h)
`evals/questions.jsonl`, one question per line:

```
{"id": "R001", "part": "real", "question": "...", "expect": "answer",
 "expected_records": [], "source": "interview-07", "notes": ""}
```

| Field | Values |
|---|---|
| `part` | `real` (100) · `lookup` (50) · `trap` (50) |
| `expect` | `answer` · `not_found` · `coverage_message` · `advice_notice_first` · `blocked` |
| `expected_records` | Record IDs a correct answer should cite (lookups always; real ones when known) |
| `source` | `interview-NN` for real questions; `advocate` for traps |

### 4.2 Fill it in (2 h)
- **The 50 traps** from Ranveer, with their `expect` from his "what a correct answer does"
- **The real questions** from `docs/research/interview-*.md`, **word for word**. Strip
  anything that names a person, firm or case they're handling

**Branch:** `meghna/eval-set`

---

## Day 5, Fri 6 Nov (Dhanteras): lookups + a check

### 5.1 The 50 lookups (1.5 h)
Act and section questions with a known right answer: "What does Section 138 of the
Negotiable Instruments Act say?", "Which BNS section replaced IPC 302?". Use the Act
lookup page to find each `record_id` for `expected_records`. Mix old and new Acts.

### 5.2 A check script (1 h)
`evals/check_questions.py`: exactly 100 / 50 / 50 (once complete), unique IDs, every
required field, every lookup has a record. **It's in Shaan's folder**, so say so in the
standup; Shaan reviews it.

### 5.3 A readable copy for the advocate (30 min)
`evals/questions-for-review.md`, generated from the file: one numbered list per part. Send it
to Ranveer, who sends it to the advocate for sign-off.

**Branch:** `meghna/eval-lookups`

---

## Day 6, Sat 7 Nov (Choti Diwali): light day

- [ ] Phone check of sign-in and consent at 375 px
- [ ] Standup

---

## Done by Saturday

- [ ] Real Firebase sign-in; token on every call; mock can't reach production
- [ ] Consent shown in full before first use; withdraw works
- [ ] Answers left shown as plain numbers; monthly-limit screen
- [ ] `evals/questions.jsonl` with the traps, the real questions so far and 50 lookups
- [ ] Check script; readable copy sent for the advocate's sign-off
