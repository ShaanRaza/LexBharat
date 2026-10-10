---
name: outside-service
description: Use when integrating, calling, swapping or configuring any outside service - Voyage, Gemini, Jev, LiteLLM, Firebase, Razorpay, S3, OCR, Qdrant, Redis, Langfuse, Sentry - or any new vendor or API. Also use when adding an API key, choosing a model, adding a fallback, or when a vendor library is about to be imported anywhere outside the adapters folder.
---

# Outside service

**Rule 1: one adapter per outside service.** Every vendor is called from exactly one file
in `adapters/`. The rest of the code calls `embed(text)`, never the Voyage library directly.

This is what lets a later engineer swap any part without rewriting the rest. It is the
single most load-bearing rule in the repo.

## Checklist for any vendor

- [ ] Exactly **one** file in `adapters/` imports the vendor library
- [ ] Nothing outside that file imports it — grep to confirm
- [ ] The function signature is about **our** domain, not the vendor's
- [ ] Keys, model names, limits and prices come from **config**, never literals
- [ ] A **fallback** path exists and is tested, if the service can be down
- [ ] A **timeout** is set
- [ ] Failure degrades to something honest, not a guess

## Vendor-specific rules

| Service | Rule |
|---|---|
| **Any AI model** | **Only providers on no-training terms.** The config model list accepts nothing else. Gemini **paid tier only** — the free tier may train on user data |
| **Jev** | One on/off switch **per use** (`JEV_ENABLED_*`). 800 ms timeout, then Gemini with the same fixed choices. **Upload text never goes to Jev** |
| **Voyage** | Query embeddings must use **voyage-4** — it must match the stored vectors. Changing the model means re-embedding everything |
| **Qdrant / PostgreSQL / Redis** | Never exposed to the internet. Private Docker network only |
| **Razorpay** | **Always verify the webhook signature** |
| **Firebase** | Login only. All app data lives in our PostgreSQL, keyed by `firebase_uid`. No chats or uploads go to Firebase |
| **Langfuse** | **Masked** — upload text, emails, phone numbers replaced before sending |
| **Sentry** | **Scrubbed** — request bodies, tokens, emails, document text removed |
| **S3** | Private, encrypted with a KMS key, no public links, expiring download links |

## Before adding a *new* vendor

1. Can an existing adapter cover it?
2. What are its **written** data terms — training, retention, processing location?
3. Does data leave India? If so it goes in the "Where data goes" table in
   `docs/SECURITY-AND-COMPLIANCE.md` **and** on the privacy page.
4. Record the choice in `docs/DECISIONS.md`.

A new vendor that receives user data and has no written no-training terms is **not
approved**. Say so rather than wiring it up behind a flag.
