# Risks

Combined register from the PRD and the Tech Stack. The biggest are **data quality**, the
**Voyage dependency** and **distribution**.

| Risk | Why it matters | What we do |
|---|---|---|
| **Hallucinated citations** | One fake case in a court filing can badly hurt a lawyer | The verifier is P0. Show the badge only when the check passes, and use the defined wording. Never skip steps 7 and 9 of the pipeline to save cost |
| **No distribution** | Prism sits on Indian Kanoon's existing traffic; KanoonBuddy has none | Free indexed pages, shareable statistics, law school pilots |
| **Outcome field may mislead** | For High Courts, `disposition` may describe an interlocutory order rather than the final result | Hand-check 100 judgments (50 SC, 50 HC) with the pass rule agreed first. The SC half can unblock SC statistics alone. **Do not launch High Court statistics until their half passes** |
| **Data quality** | Citations 100% for SC but 0.0% for High Courts. Judges 32.7% filled and sampled values were garbage. Party names often counsel names | Fill rates are measured. Run the garbage check on judges and party names. **Do not display any field that fails the audit** |
| **Voyage lock-in** | Meaning search only works with voyage-4 query embeddings. A price rise or outage hits every semantic search; changing model means re-embedding | Keep it behind one adapter. Cache repeated questions. Keyword search and Act lookup still work without it |
| **Text without vectors** | Either ~1,153,189 chunks (3.5%) or ~55,000 (0.2%) have no vector | Reconcile the counts in the audit, then embed the gap or leave those courts out |
| **Dependence on Vaquill** | One organisation publishes the whole dataset | Keep the licence, dataset card and checksums as downloaded; keep an offline copy and the scraper code. See [DATASET.md](DATASET.md) |
| **Regulatory exposure** | BCI advertising rules, the DPDP Act and privilege all touch the product | See [SECURITY-AND-COMPLIANCE.md](SECURITY-AND-COMPLIANCE.md). **Get the advocate's written opinion before launch** |
| **Jev dependency** | Early access, US West Coast servers, no-training terms unconfirmed, small startup. It makes the scope, gate and claim-support decisions, so an outage or a bad decision touches every answer | Own adapter, per-use switches, Gemini fallback under 800 ms, and **upload text never sent to Jev** |
| **One server, no failover** | One EC2 runs the website, API, database, Qdrant and Redis | EC2 auto recovery, daily S3 snapshots, a written rebuild plan (target under 1 hour). Second server when paying users justify it |
| **Memory pressure on 16 GB** | Qdrant search memory and OCR time are the two things that break first | Scalar quantization. One OCR job at a time, capped at 1 CPU. Count the SC points in build step 1 and move to 32 GB if needed |
| **Partial, frozen data** | Fewer documents than the largest databases, no district courts, nothing after v2026.08 | Data-as-of date on every result; refresh plan in the roadmap |
| **Messy outcome labels** | 577 disposition values — a High Court problem; the SC does not have it | Clean the High Court values once, then spot-check by hand before showing any High Court statistic |
| **LLM vendor data terms** | The free Gemini API tier may train on data | **Paid tier only.** Get written no-training and retention terms from every vendor before launch |
| **Model cost eats margin** | Usage-based cost rises with heavy users | Model router, monthly limits, caching repeat questions |
| **Legal advice liability** | Outcome prediction can be read as advice | Clear disclaimers. Prefer descriptive statistics over prediction |
| **Client confidentiality** | Lawyers will not upload case files to an unknown tool | Indian hosting, no training on user data, a clear privacy page |
| **Name and branding** | "KanoonBuddy" is close to Indian Kanoon and to the existing KanoonGPT | Trademark search before any branding spend. Five alternatives in [PRODUCT.md](PRODUCT.md) |
| **Team too small for the schedule** | ~18.5 person-weeks in weeks 3 to 10; a solo build is longer | Riskiest parts first (build steps 1 and 2), then re-plan from measured time |
| **No tribunal data** | The copy has no tribunal files. 813,168 tribunal matters are free PDFs with no text layer | The blocker is OCR effort, not money — a credible post-launch expansion. **Do not advertise tribunals at launch** |
| **Infrastructure size** | ~440 GB of vectors is too big to run well on a laptop in production | Launch with SC + `acts_india` on one 16 GB server. Phase 2 gated on paying users |
| **Competitors** | Prism has Indian Kanoon's traffic; SCC Online and Manupatra have editorial content and long-standing customers | Compete on SC depth with per-citation verification, free section-level Act lookup, Hindi, team workspace and visible limits. **Treat Prism's answer quality as the accuracy bar and test the verifier against it** |
