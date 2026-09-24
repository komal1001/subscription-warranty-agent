# Service Level Objectives

Targets the system should meet. These are drafts based on the design discussion — review and adjust before treating them as locked.

| # | Objective | Target (draft) | Rationale |
|---|-----------|-----------------|-----------|
| 1 | Data privacy | 100% of raw transaction/receipt data stays on-device; zero unredacted PII in any outbound network call | Core reason for choosing local Ollama over a cloud LLM |
| 2 | Processing time | A full CSV statement (12 months, ~500 transactions) processes in under 5 minutes on local hardware | Keeps the tool usable for periodic manual runs, not a background daemon |
| 3 | Detection accuracy | Price-increase and forgotten-renewal detectors: 0 false negatives on charges with 2+ prior data points for the same merchant | These are pure arithmetic on known data — should be reliable, not probabilistic |
| 4 | Merchant name matching | Correctly group >90% of same-merchant transactions despite naming variants (e.g. "NETFLIX.COM" vs "NETFLIX CA") | Bad grouping silently breaks every detector downstream |
| 5 | Manual input burden | Zombie-subscription detection requires no more than one manual entry (cancel date) per canceled subscription | Keeps the "semi-automatic" detector lightweight, not a chore |

<!-- Update targets as we learn real numbers from testing; add rows for new objectives as needed -->
