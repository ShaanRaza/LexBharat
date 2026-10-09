# tests

Unit and integration tests. **Rule 6: tests guard the trust promise** — the citation
verifier and the usage meter must pass before any deploy.

The full must-pass list is in [../docs/TESTING.md](../docs/TESTING.md). Start with these,
because they are the ones that protect the product's whole reason to exist:

```
tests/
  verifier/      the four checks, each failure reason, Jev-off and Jev-timeout paths
  usage/         meter counts, cache hits free, limit check runs BEFORE any AI call
  isolation/     every user_documents query carries a user_id filter
  pipeline/      end to end against a small fixture collection; SSE ordering
  adapters/      each adapter, mocked
```

`tests/isolation/` is not optional. A missing `user_id` filter leaks one lawyer's client
files to another, and that is the kind of bug that ends the product rather than
embarrassing it.

Run with pytest. Keep fixtures small and committed; **never commit real corpus data or a
real upload.**
