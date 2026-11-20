# Architecture Decision Records

Log of decisions made during design/build, in the order they were made. Each entry is short: what we decided, why, and what it rules out.

| # | Date | Decision | Why | Rules out / open question |
|---|------|----------|-----|---------------------------|
| 1 | 2026-09-16 | Run the LLM locally via Ollama, not a cloud API | Personal financial data (bank statements, receipts) must not leave the machine | Cloud LLM providers for the core pipeline; any future outbound calls (web lookups, sending emails) must go through a redaction step first |
| 2 | 2026-09-16 | Phase 1 data source is manually-exported bank/card CSV statements | CSV is structured, simple to parse, and needs no OAuth/email access to get started | Not automatic — user must export and upload statements periodically; email inbox parsing deferred to a later phase |
| 3 | 2026-09-16 | Phase 1 scope is subscription-leak detectors only; warranty detectors deferred | CSV only contains merchant/amount/date, not product-level info (model, warranty terms) needed for warranty detectors | Warranty detection needs a second data source (receipts/invoices) — separate phase, separate ingestion pipeline |
| 4 | 2026-09-16 | Detectors are built as independent, pluggable modules (input: extracted transactions, output: flags) | Lets us add new detector types later without touching ingestion/storage/reporting | N/A |
| 5 | 2026-09-16 | Phase 1 detector set: price increase, forgotten annual renewal, billing frequency change, duplicate subscriptions (fully automatic); zombie subscription (semi-automatic, needs a manually logged cancel date); unused subscription (not a true detector — surfaced as a review checklist, since usage data isn't available from CSV) | Matches what's actually knowable from bank statement data alone | FX creep, recall matching, and all warranty detectors excluded from phase 1 |
| 6 | 2026-11-20 | Architecture is an agent orchestrating deterministic tools: a local Ollama LLM with tool calling decides which tools to run (ingest, merchant grouping, detectors) and when to ask the user for missing data (e.g. a cancel date); the LLM itself only handles fuzzy tasks — grouping ambiguous merchant names the rules can't resolve, explaining and ranking flags | Detectors must be exact and testable (SLO #3: 0 false negatives), which an LLM can't guarantee; the agent layer adds flexible orchestration and human-in-the-loop prompts on top of reliable tools | The LLM doing arithmetic or deciding on its own whether a charge is a leak; any agent tool that makes outbound calls must go through the redaction step (ADR #1). Open question: how to evaluate the agent's tool choices |

<!-- Add new rows above this line as decisions are made -->
