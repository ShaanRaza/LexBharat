# Build order

**Build the riskiest part first: search plus the citation verifier.** If that does not give
good answers, nothing else matters. Each step ends with something you can try.

Timing (Estimate): solo with AI agents, full time, roughly **10–16 weeks** for steps 2–9.
The PRD's plan of 3 engineers assumed 8 weeks. Time steps 1 and 2, then replace this range
with a measured one.

---

## 1. Data (your laptop)

- [ ] Count Supreme Court points in the local Qdrant
- [ ] Build `kanoon_v1` (dense voyage-4 + BM25 sparse) for the Supreme Court and `acts_india`
- [ ] Check 20 searches by hand in the Qdrant dashboard
- [ ] Apply for **Jev early access**; email TypeSafe about no-training terms
- [ ] Test re-embedding SC chunks with a short header (case name, court, year) in front — keep it only if search improves
- [ ] Run the Jev cleaning job on Supreme Court dispositions
- [ ] Agree the 50-judgment pass rule **with the advocate, before checking**
- [ ] Start the 50-judgment Supreme Court hand check
- [ ] Evaluate upgrading to snapshot **v2026.08.1** (fills `source_url` on 83.3% of rows) against its download time

## 2. Pipeline in a notebook or script

- [ ] Question in, answer with verified citations out
- [ ] Conversation memory, query rewrite, answer cache, invented-citation log
- [ ] Wire the Jev adapter **with its fallback**; compare each Jev use on and off
- [ ] Wire LiteLLM, Voyage rerank and Langfuse
- [ ] Run 50 real questions; record cost per answer

## 3. Backend API

- [ ] FastAPI routes: research chat (streaming), Act and section lookup, record view, stats, consents, account deletion
- [ ] **Tests for the verifier**

## 4. Website

- [ ] Chat screen, citation ticks, judgment view with paragraph anchors
- [ ] Act pages, data-as-of date, CC BY credit, not-legal-advice notice
- [ ] Consent notice at sign-up

## 5. Login, usage meter and workspaces

- [ ] Firebase sign-in, `users` table, monthly limits per plan
- [ ] Chambers organisations and memberships (shared billing; each member's chats and uploads stay private in v1)

## 6. AWS server

- [ ] EC2 in Mumbai. **r7g is ARM (Graviton) — check every Docker image has an ARM build**
- [ ] Docker Compose on a private Docker network
- [ ] Restore the snapshot from S3, then **delete the snapshot file** to free disk
- [ ] HTTPS, encrypted disks, secrets in AWS Secrets Manager, daily backups
- [ ] GitHub Actions deploy

## 7. Upload and chat

- [ ] S3 upload links, background OCR job, voyage-4 embeddings (free local model as fallback)
- [ ] Shared `user_documents` collection filtered by user, delete controls
- [ ] **Built now, switched on for users only if the interviews and the legal opinion support it**

## 8. Payments

- [ ] Razorpay subscriptions for Student, Pro and Chambers (minimum 3 seats)
- [ ] Webhook with signature verification

## 9. Admin page, test set and public pages

- [ ] The **200-question test set**, run from the admin page
- [ ] Free public Act pages and Supreme Court stats pages, with sitemap and share cards
- [ ] **Stats go live only after the 50-judgment hand check passes**
- [ ] Draft the first knowledge notes (law maps and coverage rules); send for advocate review
- [ ] Write the breach playbook and the retention list

## 10. Private beta

- [ ] 20 students and 10 advocates, as in the PRD

## 11. Launch gate

Public launch happens **only if all six are true** at the end of the private beta:

- [ ] a. Verified-citation rate **98% or higher** on the 200-question test set
- [ ] b. At least **6 of the 10** beta advocates say they would pay the Pro price
- [ ] c. **Zero** confirmed fabricated citations reaching a beta user
- [ ] d. The advocate's **written legal opinion** received
- [ ] e. The **independent security test** passed
- [ ] f. The **data-as-of date** shown prominently on every result, stats page and Act page

If any condition fails, the launch date moves. **Akshita Johari decides.**

---

## Not in the MVP

| Item | Priority | Note |
|---|---|---|
| Hindi | P1 (within 3 months) | P0 if the interviews show strong demand |
| Drafting, review and compare | P1 (within 3 months) | Editor (TipTap) and Word export |
| Data refresh pipeline | Post-MVP backlog (D2) | MVP ships on snapshot v2026.08 |
| High Courts | Phase 2 | Only when paying users cover the cost |
| Tribunals | Post-launch | Free PDFs with no text layer — all OCR cost |
| Counter-arguments, moot court, study buddy | P2 | LangGraph only if needed |
