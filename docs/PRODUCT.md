# Product

From the PRD (9 Oct 2026). The Tech Stack wins on engineering; this file is the product
side: who it is for, what ships, and what it costs.

## Problem

Indian lawyers and students need fast, trustworthy legal research. Existing AI tools are
either expensive or unreliable on citations. KanoonBuddy gives fast answers with checked
citations at a low price.

## Goals

1. Deliver the core tools people use most: research chat, Act and section lookup, and
   upload and chat. Drafting follows as a P1 tool.
2. **Every case or Act cited is a real record in the dataset, and anything that cannot be
   verified is flagged.**
3. Keep the price low enough for students and small chambers, with **visible** usage limits.
4. Offer outcome statistics from real decisions.

## Non-goals for v1

- Court tracking, e-filing, or a full practice-management suite.
- **Giving legal advice.** KanoonBuddy is an information tool.

## Target users

| User | Need | Why they would switch |
|---|---|---|
| Law students | Case digests, moot prep, exam prep | Low price, student plan |
| Junior advocates, small chambers | Fast research and first drafts | Low price, clear limits |
| Solo practitioners in district courts | Drafting, quick precedent lookup | Simple interface, Hindi support |

Note on the third group: v1 has **no High Court or district-court judgments**, so their
value at launch is statute lookup, Supreme Court precedent and (later) drafting. Whether
that is enough is an explicit interview question.

## What competes on what

KanoonBuddy competes on three things, **not on price**:

1. **Supreme Court depth and verifiability** — 78.0% of SC cases predate 2015, citation
   strings are 100% complete, dispositions concentrate in ~10 readable outcomes (all
   Measured).
2. **Statute lookup with in-force status** — free, section-level, zero marginal cost on our
   own data, against Manupatra's paid editorial version.
3. **Visible usage limits in plain numbers** instead of hidden credits, and a free tier that
   costs almost nothing to run.

At Pro the price is at parity with Prism Premium, so it must win on the above.

## MVP scope

Priority key: **P0** = needed to launch · **P1** = within 3 months · **P2** = later.

| Feature | Priority | Cost to run |
|---|---|---|
| Research chat with citations | P0 | ~₹0.05 Voyage + ~₹0.03 Jev + 2–3 LLM calls per answer |
| Courts searchable at launch (SC + `acts_india`) | P0 | Free — already embedded |
| Citation verifier | P0 | Free for checks 1–3; check 4 inside the Jev figure |
| Act and section lookup | P0 | Free — payload filter, no embedding |
| Decision layer (Jev) | P0 | ~₹0.03 per answer |
| Knowledge notes (OKF) | P0 | Free to serve; reviewer time |
| Answer cache | P0 | Free — Redis |
| Invented-citation log | P0 | Free — database table |
| Source credit and data-as-of date | P0 | Free |
| Usage meter | P0 | Free — database counter |
| Upload and chat | P0 — **ships in v1 behind three conditions** | Gemini paid tier, OCR, Voyage embed |
| Outcome statistics | P1 | Free per query; one-time Jev cleaning pass |
| Drafting from templates (20 to start) | P1 | Paid LLM call |
| Review and compare drafts | P1 | Paid LLM call |
| Talk with a single judgment | P1 | Free fetch + paid LLM call |
| Hindi and regional languages | P1 → P0 if interviews demand | Same calls as research chat |
| Counter arguments | P2 | Embedding + LLM |
| Case outcome prediction | P2 | **Ship only with clear warnings, or skip** |
| Moot court and study buddy | P2 | Paid LLM call |
| Tribunal and regulator search | Later | OCR and extraction effort, not licensing |

**Upload and chat ships only after three things:** the advocate's written opinion on
privilege and DPDP roles, Voyage's written no-training and retention terms, and the upload
limits being set.

## Plans and pricing

**Proposed starting prices to test, not final numbers.** No lawyer has been asked, so
₹199 and ₹499 are hypotheses.

| Plan | Proposed price | Includes |
|---|---|---|
| **Free** | ₹0 | Monthly limits on research chat, upload and chat, and Act lookup. Outcome statistics added when they pass the 50-judgment check |
| **Student** | ₹199 a month | Research, study tools, moot court |
| **Pro** | ₹499 a month (₹4,990 a year, 2 months free) | Higher limits, drafting, document review |
| **Chambers** | ₹299 per user a month, **minimum 3 users** | One bill for the team; each member's chats and uploads stay private in v1. Shared workspace from month 6 |

Blended figure used in cost planning: **₹349** (assuming half Student, half Pro).

### Pricing-page rules

- **Show limits in plain numbers** ("100 research answers a month"), never hidden credits.
- Usage limits are **monthly on every plan, including Free**.
- **Answers served from the cache do not count** against a limit.
- Put features that need no embedding — Act lookup, outcome statistics — in the free tier.
  They cost almost nothing per query.
- Annual plans give 2 months free.
- **A plan must earn a margin after model cost.** Check before launch:
  `margin = price − (answers/month × cost per answer) − hosting share − payment fees`.
- Whether prices include GST is **undecided** (accountant).

### What would change the pricing

| Evidence | What it would change |
|---|---|
| Most interviewed advocates name a price well above ₹499 | Raise Pro and add a higher tier |
| Students will not pay ₹199 | Make Student free with a low limit, charge from Pro |
| Measured cost per answer exceeds what ₹499 covers at the planned limit | Lower the limit or raise the price |
| Free-to-paid conversion in the beta is below break-even | Fix the product or the free tier before spending on acquisition |

## Go-to-market

Distribution is the biggest unsolved problem. Prism is an upsell on Indian Kanoon's
existing traffic; KanoonBuddy starts with none. The plan is to earn attention with free
features that cost almost nothing to serve.

1. **Free, no-login, searchable tier** — public Act and outcome-statistics pages, each on
   its own indexable address.
2. **Shareable outcome statistics** — permanent links and share cards with source,
   data-as-of date and CC BY credit. **Educational only; never name or promote an advocate.**
3. **Law school partnerships** — moot court societies, legal aid clinics and libraries.
   Free student access for a semester in return for feedback and a named contact.
   **Cap free usage per student** — each free seat has an LLM cost.
4. **First 100 users (targets, not forecasts):** 40 students, 30 advocates, 30 free-tier
   sign-ups. If a group is under half its target after 6 weeks, change the channel before
   adding spend.

## Support model (proposed)

| Channel | Staffed by | First response |
|---|---|---|
| Support email and in-app help form | Part-time support and operations | 1 business day free, same business day paid (during beta) |
| **"Report a wrong answer" button on every answer** | Advocate advisor triages legal-accuracy reports | 2 business days |
| Optional WhatsApp number for paid users | Same support person | Decide after the interviews |

## Naming

"KanoonBuddy" uses Indian Kanoon's brand word and KanoonGPT already exists — a confusion
and trademark risk. Five alternatives, none derived from a competitor's name:

| Name | Meaning | Why it fits | Watch-out |
|---|---|---|---|
| **Praman** (प्रमाण) | Proof, evidence | Matches the promise of checked citations | A common Hindi word, so crowded |
| Nirnay (निर्णय) | Judgment, decision | Fits judgments and outcome statistics | May already be used |
| Dhara (धारा) | A section of a law | Fits Act and section lookup | Also means "stream"; very common |
| Sandarbh (संदर्भ) | Reference, citation | Fits citations | Harder for English speakers |
| Nazeer (नज़ीर) | Precedent | Fits case law | Also a common personal name |

**PRD recommendation: Praman.** Every name needs a trademark search with IP India, plus
domain, app stores and social handles — none checked.

**Internal naming rule:** internal names such as the collection `kanoon_v1` are placeholders
too. The product name and the collection name each live in **one config value**, so
renaming is a config change. **Prefer neutral internal names (for example `research_v1`)
in anything new.**
