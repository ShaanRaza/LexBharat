---
description: Where the build actually stands — what exists, what the next build step is, and which blockers are not engineering work.
---

# /where

Report the real state of the build. Inspect the tree; do not take the docs' word for it.

1. **What exists.** Which of `web/ api/ core/ adapters/ workers/ data/ knowledge/ evals/
   tests/ migrations/ infra/ legal/` contain real code or content versus only a README or
   `.gitkeep`.
2. **Current build step.** Read `docs/BUILD-ORDER.md` and say which step is in progress and
   which items in it are done, based on what is actually in the repo.
3. **Feature switches.** Read `.env.example` and report which are off and what each one is
   waiting on.
4. **Blockers that are not code.** From `docs/DECISIONS.md`, list the top 5 open questions
   and flag the ones that need a person rather than a commit — the 20 interviews, the
   100-judgment hand check, counsel, and Vaquill.
5. **Launch gate.** From `docs/METRICS.md`, list the seven conditions and mark each
   met / not met / cannot be assessed yet.

Be blunt about what has not started. A list of unstarted work is more useful than an
optimistic summary.
