## What changed

<!-- One or two lines. If you touched the pipeline, say which of the 11 steps. -->

## Trust-promise checks

- [ ] Verifier tests pass — all four failure reasons still remove **and** log the citation
- [ ] Checks 1–3 still run with Jev off and with Jev timing out
- [ ] No citation-shaped content is emitted before the single post-verification `citations` event
- [ ] Usage meter: counts one per non-cached answer, zero for cache hits, checked **before** any AI call
- [ ] Every `user_documents` query goes through the shared `user_id`-filtered data-access function
- [ ] Not-legal-advice notice and data-as-of date still present on answers, stats and Act pages

## The seven rules

- [ ] Outside services called only through their adapter
- [ ] Settings in config, not code (no hard-coded model name, price, limit or product name)
- [ ] Frontend talks to the backend only through the API
- [ ] Database changes are numbered, reversible migrations
- [ ] Still starts with one `docker compose up`
- [ ] Tests added or updated
- [ ] Pipeline steps remain separate functions with fixed inputs and outputs

## Docs

- [ ] Any decision I made that the docs left open is recorded in `docs/DECISIONS.md`
- [ ] Evidence labels kept (no Estimate promoted to fact without measuring)
- [ ] No secret in the diff
