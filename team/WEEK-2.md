# Week 2: Mon 19 Oct to Sat 24 Oct 2026

**Theme: search works.** The detailed plan, one file per person, is in
[`week-2/`](week-2/README.md). This page is the one-screen summary.

| | **Shaan (4 h)** | **Akash (4 h)** | **Meghna (3 h)** |
|---|---|---|---|
| **Day 1** Mon 19 | **Pipeline contract**: shared types, one stub per step, a fake pipeline. Contract call with Akash | Contract call. `core/store/` sessions. A dev-only user | API client generated from OpenAPI. One error handler |
| **Day 2** Tue 20 *(Dussehra)* | Load all SC cases and Act sections into PostgreSQL; check the counts | Conversation routes; the cross-user test | Judgment and Act pages on the real API |
| **Day 3** Wed 21 | **Search**: meaning + keyword + exact lookup, top 50; keyword-only fallback | Cursor paging; the audit-log writer | Conversation list with "load more" |
| **Day 4** Thu 22 | **Re-rank** to 10. Redo the 20 hand searches; time the search stage | `GET /search` (direct search, no AI) | Shared citation component; history page |
| **Day 5** Fri 23 | **Decisions adapter**: Jev + Gemini fallback; upload-text guard | OpenAPI tidy, copied to `web/`; Firebase project | Sign-in screens, role chooser, consent placeholder (mock) |
| **Day 6** Sat 24 | **Gate**: at most 8, S1 to S8, "not found". Wrap the week | CI against a real PostgreSQL; smoke script | Act lookup page; phone pass |

**Ranveer this week:** interviews 4 to 10, the legal opinion's scope and date **agreed by
Wed**, chase Voyage, start the trademark search, book interviews 11 to 16. Detail in
[`week-2/ranveer.md`](week-2/ranveer.md).

**By Saturday:** a question comes out of search, re-rank and the gate as at most 8 passages.
The answer step is Week 3.
