# Security and compliance

Three sets of rules shape what the product shows and stores: the **DPDP Act and Rules**,
**BCI Rule 36**, and the line between **information and legal advice**.

This document is not legal advice. The PRD requires an **advocate's written legal opinion
before launch** (launch gate condition d).

---

## DPDP Act 2023 and Rules 2025

The PRD reads the data fiduciary duties as applying from about **mid-May 2027** (Needs
verification). **Build to them now.**

| Requirement | What we build |
|---|---|
| Consent notice | Shown at sign-up: purpose, data collected, retention period, how to withdraw. Each acceptance saved in `consents` |
| Retention per data type | Account data, chats, uploads, audit log, backups and Langfuse logs each get a stated period. All **Needs verification** until counsel decides |
| User deletion | Delete a chat or upload any time. `DELETE /me` removes the account and its data, deletes the Firebase user, cancels the Razorpay subscription (payment and invoice records kept as the law requires; Needs counsel). `GET /me/export` gives a copy. Backups age out on their normal cycle |
| Breach playbook | Written plan: notify affected users and the Data Protection Board, with a detailed report to the Board **within 72 hours** (Needs verification against the Rules) |
| Roles | For account data, KanoonBuddy is the **data fiduciary**. For an advocate's uploaded client documents, the advocate is probably the fiduciary and KanoonBuddy a **processor** (Needs counsel). The terms of service must say so |
| Data sent abroad | Voyage, Gemini and Jev process data outside India. Each vendor's terms and location checked and listed on the privacy page (Needs verification) |

## Where data goes

Every outside service gets **only what it needs**. This table is also the basis for the
privacy page.

| Service | What it receives | Where | Rule |
|---|---|---|---|
| AWS (EC2, S3) | Everything we store: accounts, chats, uploads, backups | Mumbai | Encrypted disks and buckets |
| Firebase | Email, name, sign-in | Google (outside India) | Login only; no chats or uploads |
| Razorpay | Payment details | India | Card and UPI details stay with Razorpay; we never see them |
| Voyage | Question text; upload chunks, if uploads use voyage-4 | Outside India | No-training terms; **upload terms Needs verification** |
| Jev | Questions and retrieved judgment passages | US West Coast | **Never upload text** |
| Gemini | Question, passages, knowledge notes; in upload chats, the needed upload passages | Outside India | **Paid tier only** (no training) |
| Langfuse | AI-call logs | Cloud or self-hosted | **Masked**: upload text, emails and phone numbers replaced with placeholders before sending; keep IDs, token counts, cost and speed |
| Sentry | Error reports | Cloud | **Scrubbed**: request bodies, tokens, emails and document text removed before sending |

## BCI Rule 36

- No listing, ranking, matching or recommending advocates. **No "find a lawyer" feature.**
- No named advocate testimonials or success stories. No payments to advocates per client
  referral.
- Share cards and stats pages are educational and **never name an advocate**.
- Whether naming an advocate advisor on the website counts as publicity: **Needs counsel.**

## Not legal advice

- **Every answer, stats page and Act page** carries a short notice: KanoonBuddy gives
  information, not legal advice.
- **Stronger notice when Jev's safety check flags a personal-advice question:** the answer
  opens by saying it cannot advise on the user's own situation and suggests consulting an
  advocate.
- Outcome statistics stay **descriptive**; no predictions or win chances.

## Security

- **Encrypted at rest:** EBS disks, S3 buckets and backups, with keys in AWS KMS.
- **Encrypted in transit:** HTTPS for every outside connection.
- **Secrets:** API keys and passwords in AWS Secrets Manager — never in the code or in a
  file on the server.
- **Private Docker network:** only the website and the API are reachable from the internet.
  **Qdrant, PostgreSQL and Redis are never exposed.** The Qdrant dashboard is opened only
  through a private tunnel.
- **Dependency updates:** GitHub Dependabot flags and patches outdated libraries.
- **Independent security test before public launch** (launch gate condition e). Cost:
  Needs verification — get quotes.

## Upload security (launch requirements)

- S3 bucket private, encrypted with an AWS KMS key, no public links. Downloads use links
  that expire in minutes.
- **Real hard delete.** One job removes the file from S3, the extracted text from
  PostgreSQL and all vectors from Qdrant by `document_id`. The job logs success; a nightly
  check finds leftovers.
- Auto-delete lifecycle rule after a fixed period (Needs verification: agreed with
  counsel), plus an optional "delete when I close this chat" mode. The default is shown in
  the app, not only in the terms.
- **Every query on uploads goes through one shared data-access function** that always adds
  the `user_id` filter.
- **No staff access by default.** The audit log records who opened or deleted what — never
  the document text.
- A warning before upload about privileged material.

## Privilege

- **Section 132 of the Bharatiya Sakshya Adhiniyam 2023** covers professional
  communications between an advocate and client. Reports on a Supreme Court ruling
  (November 2025) say digital data revealing legal advice on an advocate's device is
  protected. The PRD's author could not open the judgment or the statute text.
- Privilege belongs to the **client and advocate**, not to KanoonBuddy. But uploading
  privileged material to a third-party tool **might be argued to weaken it**, and no clear
  authority was found either way. **Needs verification: ask counsel before accepting
  uploads.**
- **Third parties in uploads.** Uploaded documents name opposing parties and witnesses who
  never agreed to anything. **Needs counsel.**
- Design for it regardless: no staff access by default, no training on uploads, an optional
  mode that deletes the upload when the session ends, a warning before upload, and a
  written policy for **how we answer legal orders**.

## The PN Vignesh point

BCI Rule 36 binds advocates, not software vendors. But in the **PN Vignesh** case the
Madras High Court held that platforms which filter or rank lawyers helped unlawful
solicitation, and asked the BCI to act against **both the platforms and the advocates**.

That is why "no listing, ranking, matching or recommending advocates" is a hard product
rule here and not just marketing guidance.

Whether AI answers to **non-lawyers** raise a practice-of-law issue also **needs counsel** —
the free tier will be read by non-lawyers.

## Takedown and redaction

The dataset card says victim names and contact details are already removed from the source
data. We still need **our own takedown request process**, and the card names
`contact@vaquill.ai` for redaction requests against the source. Draft the process in
[`../legal/`](../legal/).

## Related

- [RETENTION.md](RETENTION.md) — the per-type retention schedule, still undecided
- [BREACH-PLAYBOOK.md](BREACH-PLAYBOOK.md) — the 72-hour plan
- [`../legal/`](../legal/) — the documents users actually see
