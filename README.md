# Subscription & Warranty Leak Detector

Local-first agentic tool to find money leaking out through forgotten subscriptions, silent price increases, and unclaimed/expiring warranties. Runs entirely on-device via Ollama — no financial data leaves the machine except through explicit, redacted, opt-in outbound calls (e.g. warranty recall lookups).

See [`docs/ADR.md`](docs/ADR.md) for design decisions and [`docs/SLO.md`](docs/SLO.md) for target objectives.

## Status

Phase 1 (in progress): subscription-leak detection from manually-exported bank/card CSV statements.

Phase 2 (planned): warranty-leak detection from receipts/invoices.

## Folders

- `docs/` — ADR and SLO tracking
- `src/` — application code
- `data/raw/` — your exported CSV statements go here (gitignored — never commit real financial data)
- `data/processed/` — normalized/extracted data used by detectors
