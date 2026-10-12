# Akash: Week 4 (Platform), 4 h a day

**Theme: limits, consent and privacy.** By Friday every answer is **counted before any AI
call**, users see how many answers they have left, nobody can use the AI before agreeing to
the consent notice, and the monitoring tools **can't see** private text.

Three of these are guarded by tests that must pass before any deploy: the **usage meter**,
**masking** (Langfuse) and **scrubbing** (Sentry). Shaan reviews all three carefully.

> **Fri 6 Nov is Dhanteras and Sat 7 Nov is Choti Diwali.** Friday has a smaller task, and
> Saturday is light on purpose.

---

## Before Day 1

- [ ] The re-plan is posted; this week follows it
- [ ] Week 3 leftovers first

---

## Day 1, Mon 2 Nov: the usage meter

### 1.1 The counting rule (30 min, with Shaan)
Two questions the docs don't answer yet. Agree them and record with `/decision`:

| Question | My recommendation |
|---|---|
| Does a **"not found"** answer count? | **No.** Nothing was written, so it costs almost nothing. Counting it feels unfair to the user |
| Does a **model failure** (sources shown, no answer) count? | **No.** Refund it |

Already settled: **cache hits are free**, and unreadable uploads aren't charged.

### 1.2 `core/meter.py` (3 h)
API.md: **the usage check runs before any AI call** and stops with a clear message at the
limit.
- **Reserve** one answer before the pipeline starts; **confirm** it when the answer is
  saved; **release** it on not-found, model failure or a cache hit
- Monthly limit per plan from settings (`PLAN_LIMIT_*`)
- Counts go into `usage_daily`
- **Two requests at the same moment can't both use the last answer.** Use a database lock
  or an atomic counter

**Branch:** `akash/usage-meter`

**Ask Claude Code:**
> Build core/meter.py per team/week-4/akash.md Day 1: reserve before any AI call, confirm on save, release on not-found, model failure or cache hit. Limits from settings. Safe under concurrent requests. Explain how the lock works in plain words, with a diagram of reserve, confirm and release.

---

## Day 2, Tue 3 Nov: limits the user can see

### 2.1 Limits in headers and errors (1.5 h)
- Every AI response carries `X-Answers-Limit` and `X-Answers-Remaining`
- At the limit: error code **`quota_exceeded`**, in the standard format, **before** any AI
  call
- `GET /me` reads answers left from the meter

### 2.2 The must-pass meter tests (2.5 h)
- [ ] The answer at the limit is refused, and **no AI call happens** (the fake LLM records
      zero calls)
- [ ] 10 requests at once with 1 answer left → exactly 1 succeeds
- [ ] A cache hit doesn't change the count
- [ ] Not-found and model failure release the reservation
- [ ] The count resets at the start of the month (fixed clock in the test)

**Branch:** `akash/meter-limits`

---

## Day 3, Wed 4 Nov: consent

### 3.1 Consent routes (2.5 h)
`GET` and `POST /api/v1/me/consents` (DPDP):
- A consent row records the **notice version**, the purpose and the time
- **Every AI route refuses** with code `consent_required` until the user has agreed to the
  **current** version. A new notice version means asking again
- Withdrawing consent sets `withdrawn_at` and blocks AI routes again
- Consents are never deleted when withdrawn; they're the record

### 3.2 A placeholder notice (30 min)
`legal/consent-notice-v0.md`, headed **"DRAFT: not reviewed by counsel. Not for real
users."** The real notice comes from counsel (Weeks 5 to 7). The version string comes from
settings, so swapping it in is a config change.

**Branch:** `akash/consent`

---

## Day 4, Thu 5 Nov: Langfuse, masked

### 4.1 `adapters/tracing.py` (3 h)
One trace per question, tagged with the **request ID**, with one span per pipeline step
(agree the span names with Shaan) and the model name, tokens and time on each.

**Masking, before anything leaves the server:**
- Upload text → `[UPLOAD_TEXT]`
- Email addresses → `[EMAIL]`; phone numbers → `[PHONE]`
- Secrets and tokens are never logged at all

Tests: a trace with an email, a phone number (Indian formats: +91, 10 digits, with and
without spaces) and upload text comes out masked. If `LANGFUSE_*` is empty, tracing is
simply off and nothing fails.

**Branch:** `akash/langfuse-masking`

---

## Day 5, Fri 6 Nov (Dhanteras): Sentry, scrubbed

### 5.1 Sentry with a scrubber (2.5 h)
A `before_send` function that removes **request bodies, tokens, cookies, emails and any
document text** from every error report.

Test: raise an error inside a request that carries a token, an email and a question, and
check the payload Sentry would receive contains **none** of them. If `SENTRY_DSN` is empty,
Sentry is off.

**Branch:** `akash/sentry-scrubbing`

---

## Day 6, Sat 7 Nov (Choti Diwali): light day

- [ ] Finish anything that slipped; refresh `web/openapi.json`
- [ ] Standup

---

## Done by Saturday

- [ ] Counting rule decided and recorded
- [ ] Usage meter: reserve, confirm, release; safe at the same moment; all must-pass tests green
- [ ] Limits in headers; `quota_exceeded` before any AI call
- [ ] Consent routes; AI routes blocked until the current notice is agreed; draft notice clearly marked
- [ ] Langfuse traces masked; Sentry reports scrubbed; both tested
