# Template — PSP / acquiring partner evaluation

Use this for merchant acceptance; adapt for issuing, wallets, bank transfers, PayFac or payment orchestration. **All weights and scores below are illustrative and must be locally validated.**

## Hard gates — evaluate before numerical ranking

| Gate | Needed evidence | Pass / conditional / fail | Owner |
|---|---|---|---|
| Legal contracting and required market coverage | Licences, contractual structure and liability map | | Legal/compliance |
| Applicable security and card-data handling | Scope evidence, PCI responsibilities, key management | | Security |
| Status certainty and idempotent recovery | Timeout/query/webhook integration tests | | Engineering |
| Settlement, payout and ledger data | Sample batch files, fees, refunds, reserves, bank IDs | | Finance |
| Approved risk and fraud model | KYB, underwriting, 3DS and dispute ownership | | Risk |
| Operational escalation and exit | Sev definitions, migration plan, data access, support | | Product/operations |

## Weighted assessment (only for eligible candidates)

| Criterion | Weight (example) | Candidate A score (1–5) | Candidate B score (1–5) | Evidence link |
|---|---:|---:|---:|---|
| Country/rail coverage | 20% | | | |
| Reliability and state API | 25% | | | |
| Reconciliation and payout reporting | 20% | | | |
| Security, risk and contract fit | 15% | | | |
| Developer and operations UX | 10% | | | |
| Total cost of accepted order | 10% | | | |
| **Total** | **100%** | | | |

Weighted score = sum of `criterion weight × score`; never rank a failed hard gate as the winner. Compare real approval and fee data on eligible merchant cohorts, not public headline rates. Include FX, refunds, reversals, disputes and reserve cost when applicable.

## Required test-case record

For each provider, attach: environment, timestamp, request/response IDs (synthetic/redacted), authorization and capture result, status-query result, webhook behavior, refund status, settlement record, payout/bank record, latency distribution, error category, issue owner and date.

## Decision memo

Recommended partner and alternatives; commercial assumptions; open contractual exceptions; token exit/migration; trial milestones; finance/risk sign-offs; fallback if the partner degrades or changes pricing.

*Do not store live PANs, secrets, customer financial details or confidential partner contracts in this public repository.*
