# Testing

Rule 6 of the seven: **tests guard the trust promise.** The citation verifier and the usage
meter have tests that must pass before any deploy. The 200-question test set runs on every
release.

## Three layers

| Layer | What it covers | When it runs |
|---|---|---|
| Unit tests | Verifier checks 1–3, usage meter, chunk offsets, the shared upload data-access function, adapters (mocked) | Every push |
| Integration tests | Pipeline end to end against a small fixture collection; SSE ordering; Razorpay webhook signature | Every push |
| The 200-question test set | Real questions, scored for verified citations, correctness, cost and speed | **Every release**, from the admin page |

## Must-pass before any deploy

- [ ] Each of the four verifier failure reasons removes the citation **and** logs it:
      `not_retrieved`, `record_missing`, `quote_not_found`, `claim_not_supported`
- [ ] A case the model names but that was **not** in S1–S8 is removed (check 1)
- [ ] Checks 1–3 still run with **Jev switched off** and with Jev timing out
- [ ] No citation-shaped content is emitted before the single post-verification `citations`
      event
- [ ] The usage meter counts one answer per non-cached answer, and **zero** for cache hits
- [ ] The usage check runs **before** any AI call and stops at the limit with a clear error
- [ ] Every `user_documents` query carries a `user_id` filter — assert at the data-access
      function, and fail the build if any other module queries that collection
- [ ] Hard delete removes the S3 object, the PostgreSQL text **and** the Qdrant vectors
- [ ] The not-legal-advice notice and the data-as-of date are present on every answer,
      stats page and Act page
- [ ] No secret appears in any log line, Langfuse trace or Sentry payload

## The 200-question test set

Lives in [`../evals/`](../evals/) with its scorer.

| Metric | Target |
|---|---|
| **Verified-citation rate** | **≥ 98%** — launch gate condition (a) |
| Answers with a removed citation (any of the four reasons) | **< 0.5%** |
| Confirmed fabricated citations reaching a user | **zero** — launch gate condition (c) |
| First word | under 3 s |
| Full answer | under 20 s |
| Search stage | under 800 ms |
| Cost per answer | tracked in Langfuse, compared against the Estimate |

The set is also how every threshold gets set rather than guessed: the **Jev gate threshold
(0.6 to start)**, and each `JEV_ENABLED_*` switch, which turns on for users **only once it
beats the version without it**.

## Separate hand checks (not automated)

| Check | Gate |
|---|---|
| **50-judgment Supreme Court hand check** of outcome labels | Supreme Court stats go live only if it passes, against a pass rule **agreed with the advocate before checking** |
| Advocate review of knowledge notes | Only `status: reviewed` notes are used in live answers |
| Independent security test | Launch gate condition (e) |
| Advocate's written legal opinion | Launch gate condition (d) |
| 20 real court scans | Sets the OCR quality threshold and the upload size/page limits |
| Week-1 test on 50 real questions | Picks the model per plan; decides whether model routing turns on |
