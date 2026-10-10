---
name: pipeline-step
description: Use when adding, changing, reordering or removing any step of the research pipeline - remember, rewrite, decide, cache, search, re-rank, gate, answer, verify, show, save. Also use when changing passage counts, the Jev gate threshold, conversation memory, the query rewrite, the answer cache, streaming behaviour, or when tempted to introduce an agent, router or framework that decides its own next step at runtime.
---

# Pipeline step

The research pipeline is **fixed, not agentic**. Every answer goes through the same 11
steps in the same order, every time. That is what guarantees every answer hits the
verifier. Full detail: `docs/ARCHITECTURE.md`.

## The order — do not change it without a decision entry

`remember → rewrite → decide (Jev) → cache → search → re-rank → gate (Jev) → answer →
verify → show → save`

## Rule 7

**Each step is a separate function with a fixed input and output.** It must be swappable
on its own. If your change couples two steps, split it.

## Fixed numbers

| Thing | Value |
|---|---|
| Search merges | top **50** |
| Re-rank keeps | top **10** |
| Gate keeps | **at most 8**, labelled S1–S8 |
| Jev gate threshold | **0.6** to start (Estimate, set from the test set) |
| Jev timeout | 800 ms, then the Gemini fallback |
| Conversation memory | last **6 turns** in full + a rolling summary |
| Answer cache | 7 days, exact match on rewritten query + filters + model name |

Changing any of these means updating `docs/DECISIONS.md` in the same change.

## Hard rules

- **No CrewAI, no full LangChain, no runtime agent.** Agents build this product; they do
  not run it. LangGraph is month 6 at the earliest, and only with the verifier still forced.
- **Out of scope stops at step 3** — the coverage message, no search, no writing cost.
- **If no passage clears the gate, the user gets "not found" and nothing is written.** Never
  let the model answer from general knowledge to fill a gap.
- Only **verified** answers are cached. **Upload chats are never cached.**
- Cache hits are free and do not count against the user's limit.
- Scope, filters, routing and safety run **in parallel with the Voyage embedding**. Gate and
  claim checks run on all passages at once.
- Model routing (easy/hard) is **off at launch**.

## When you touch a step

1. Say which of the 11 steps you changed.
2. Keep its input and output contract stable, or change both ends deliberately.
3. If it affects what the model sees, re-run the 200-question test set.
4. Prompts live in `core/prompts/` as files, not inline strings.
