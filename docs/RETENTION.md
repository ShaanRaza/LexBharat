# Retention schedule

**Status: not decided. Every period below needs counsel.** The DPDP Act requires a stated
retention period per data type, shown in the consent notice — so this document must be
filled in and published before sign-up works.

Do not invent a period to unblock a build. Leave it blank and raise it.

| Data type | Where it lives | Retention period | Status |
|---|---|---|---|
| Account data (`users`, `subscriptions`, `memberships`) | PostgreSQL | — | **Needs counsel** |
| Chats (`conversations`, `messages`, `message_sources`) | PostgreSQL | — | **Needs counsel** |
| Uploaded files | S3, encrypted | — | **Needs counsel.** Options discussed: 7, 30 or 90 days. Also an optional "delete when I close this chat" mode |
| Extracted upload text and chunks | PostgreSQL + Qdrant `user_documents` | Same as the file | Follows the file |
| `audit_log` | PostgreSQL | — | **Needs counsel** |
| Backups | S3 | Deleted data ages out on the normal cycle | State the cycle length |
| Langfuse AI-call logs (masked) | Langfuse cloud or self-hosted | — | **Needs verification** — vendor retention terms |
| Sentry error reports (scrubbed) | Sentry cloud | — | **Needs verification** — vendor retention terms |
| Payment and invoice records | PostgreSQL + Razorpay | Kept as the law requires, even after `DELETE /me` | **Needs counsel** on the period |
| Consent records (`consents`) | PostgreSQL | — | **Needs counsel** |

## Rules that are already settled

- Users can **delete a chat or an upload at any time**.
- `DELETE /me` removes the account and its data, deletes the Firebase user and cancels the
  Razorpay subscription. **Payment and invoice records are the only exception.**
- `GET /me/export` gives the user a copy of their account data, chats and upload list.
- Delete means **hard delete**: the S3 object, the PostgreSQL text and the Qdrant vectors,
  in one job, logged, with a nightly leftover check.
- An **auto-delete lifecycle rule** removes uploads after a fixed period. The default is
  shown **in the app**, not only in the terms.
- `audit_log` records who opened or deleted what. **It never stores document text.**

## Vendor retention — to confirm before launch

Each vendor's retention terms and processing location must be confirmed in writing and
listed on the privacy page:

- [ ] Voyage AI — including terms for **upload text** specifically
- [ ] Google / Gemini — paid tier, no training
- [ ] TypeSafe AI (Jev) — written no-training and retention terms
- [ ] Firebase
- [ ] Razorpay
- [ ] Langfuse
- [ ] Sentry
- [ ] AWS
