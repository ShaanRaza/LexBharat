---
description: Pre-deploy gate — run the must-pass checks and report whether this is safe to deploy. Never deploys.
---

# /ship

Decide whether the current state is safe to deploy. **Do not deploy.** Deploys go through
GitHub Actions; nothing here touches the server.

Work through `docs/RUNBOOK.md` → *Release checklist* and `docs/TESTING.md` →
*Must-pass before any deploy*:

1. Run the test suite. Report real output — if it fails, show the failure.
2. Confirm the verifier tests cover all four failure reasons, and the Jev-off and
   Jev-timeout paths.
3. Confirm the usage-meter tests pass: one count per non-cached answer, zero for cache hits,
   checked **before** any AI call.
4. Confirm every `user_documents` query goes through the shared filtered function.
5. Check migrations are numbered and reversible.
6. Check no secret appears in the diff, logs, traces or error payloads.
7. Report the **verified-citation rate** and the **removed-citation rate** from the last
   200-question run. If it has not been run against this commit, say so — do not infer it.

## Output

**Ship / do not ship**, then the evidence. One failing trust check means do not ship, even
if everything else is green. If something could not be checked, say "not verified" rather
than assuming it passes.
