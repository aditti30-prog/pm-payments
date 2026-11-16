# Specialist review packet — highest-risk claims by chapter

**Base commit:** record the Git SHA you review against. **Status:** a reviewer aid, not a review. Nothing here is signed off. See the [specialist review program](specialist-review-program.md) for the process, record template and severity rubric, and the [primary-source audit](primary-source-audit-2026-11-16.md) for sources already consulted.

## How to use this packet

1. Pick a lane that matches your experience. Rows follow chapter order; use the **If wrong** column to prioritise.
2. For each row, try to **break** the claim: find the rule, scheme program, contract term or implementation that makes it false or incomplete in your market.
3. Reply per row with `confirmed`, `confirmed with caveat: ...`, or `wrong: ... proposed wording ... source`. Use the line format in the program file. Do not send PANs, customer data, partner credentials or confidential scheme material.
4. **If wrong** is the severity from the program rubric if the claim turned out to be wrong; it is a prior, not a finding.

Line numbers are located by text at generation time and drift as the book changes; search for the quoted opening words if a line has moved.

## What is already checked by machine

- Worked numbers in chapters and the answer key: `scripts/verify_chapter_arithmetic.py` (recomputes and binds each figure to the text).
- HarborCart funnel, fees, payout and reconciliation: `scripts/verify_metrics.py`, `scripts/verify_harborcart_reconciliation.py`, `scripts/verify_case.py`.
- Links, reading order, answer-key coverage and Markdown rendering: `scripts/check_internal_links.py`, `scripts/check_answer_coverage.py`, `scripts/check_markdown_structure.py`.
- None of these checks whether a rule, threshold, fee or process is **true**. That is what this packet is for.

## Lane 1 — Card issuance and EMV tokenization (7, 7A, 8A, 11)

| # | Where | Claim to attack | If wrong | Check against |
|---|---|---|---|---|
| 1 | [7A](../book/part-2/07a-network-tokenization-fpan-dpan.md) · L83 | DPAN is a wallet/device-domain token; a merchant card-on-file network token is a different domain and a merchant cannot reuse a device DPAN for background charges. | Major | EMVCo Payment Tokenisation Technical Framework; Visa Token Service and Mastercard MDES merchant docs; one issuer/TSP. |
| 2 | [7A](../book/part-2/07a-network-tokenization-fpan-dpan.md) · L91 | Whether freezing the physical card affects wallet tokens is issuer- and programme-specific, not uniform. | Major | Issuer card-control docs; TSP token lifecycle events (suspend, resume, delete). |
| 3 | [11](../book/part-3/11-3d-secure.md) · L89 | Liability shift covers certain fraud chargebacks only and depends on brand, region, authentication result and transaction type; not "3DS attempted". | Blocker | Visa and Mastercard chargeback rules for the target region; acquirer or PSP liability-shift documentation. |
| 4 | [11](../book/part-3/11-3d-secure.md) · L91 | After an eligible transaction-risk-analysis exemption, the merchant should not assume the issuer bears fraud chargeback liability. | Blocker | EBA RTS on SCA; scheme and PSP exemption guidance; which party requested the exemption. |
| 5 | [11](../book/part-3/11-3d-secure.md) · L104 | Funnel stages and "authenticated outcomes" map onto real 3DS result statuses and what a PSP reports. Arithmetic is machine-checked; the mapping is not. | Minor | EMVCo 3DS message statuses; PSP 3DS reporting fields. |
| 6 | [8A](../book/part-2/08a-card-present-pos-and-offline.md) · L42 | Offline EMV and store-and-forward are different modes; local acceptance does not guarantee issuer approval or funds. | Major | Adyen offline docs (provider-specific); acquirer and terminal rules; generalisation to other acquirers. |

## Lane 2 — Acquiring, gateway and merchant risk (5A, 6, 13A)

| # | Where | Claim to attack | If wrong | Check against |
|---|---|---|---|---|
| 1 | [5A](../book/part-2/05a-marketplaces-payfac-funds-flow.md) · L46 | Seller entitlement of S$88 holds only if the contract allocates all processing cost to the seller; if the platform absorbs it, seller gets S$90 and platform net fee is S$8. | Major | Finance reviewer: gross-to-net treatment; marketplace contract terms; MoR versus PayFac accounting. |
| 2 | [5A](../book/part-2/05a-marketplaces-payfac-funds-flow.md) · L68 | Platform or acquirer may have to fund a later refund or chargeback before recovering from the seller. | Major | PayFac sponsorship agreement; acquirer sub-merchant liability; negative-balance recovery terms. |
| 3 | [13A](../book/part-3/13a-compliance-and-control-ownership.md) · L67 | PCI SSC FAQ 1588 clarifies one SAQ A script criterion and does not grant universal SAQ A eligibility. | Blocker | PCI SSC FAQ 1588 and 1604; QSA or acquirer confirmation of actual eligibility. |
| 4 | [13A](../book/part-3/13a-compliance-and-control-ownership.md) · L100 | FATF Recommendations updated June 2026; MAS PSN01 AML/CFT duties apply to specified payment services, not to every merchant or provider. | Major | MAS PSN01 current revision and scope; Singapore compliance counsel. |
| 5 | [6](../book/part-2/06-gateways-orchestration.md) · L68 | Unsent attempts can often be rerouted to a healthy PSP if eligible; already-submitted ambiguous attempts need status resolution, not blind replay. | Major | PSP idempotency and status-query semantics; acquirer duplicate-detection behaviour. |

## Lane 3 — Disputes and fraud policy (12, 13, 13B, 15)

| # | Where | Claim to attack | If wrong | Check against |
|---|---|---|---|---|
| 1 | [15](../book/part-4/15-chargebacks-and-disputes.md) · L86 | VAMP is count-based (TC40 + TC15 over TC05) and the merchant excessive threshold fell from 220 to 150 bps in Asia Pacific, Canada, the EU and the US on 1 April 2026. | Major | Visa VAMP documentation and acquirer notices; exclusions, minimum counts and other regions. |
| 2 | [12](../book/part-3/12-authorization-optimization.md) · L106 | Certain declines are final or must not be retried under network rules. No program or date is cited. | Major | Visa and Mastercard reattempt and decline-code rules; PSP retry guidance. |
| 3 | [13B](../book/part-3/13b-scams-and-regulatory-map.md) · L41 | SRF took effect 16 December 2024 and covers a defined phishing-credential sequence; it is not general reimbursement for deceived-but-intended payments. | Blocker | MAS/IMDA SRF Guidelines (definitions, duties); Singapore counsel. |
| 4 | [13B](../book/part-3/13b-scams-and-regulatory-map.md) · L43 | SRF loss-sharing excludes transactions on Singapore-issued credit, charge and debit cards (footnote 1 of the Guidelines). | Blocker | Exact footnote wording in the Guidelines PDF; whether the exclusion is for loss-sharing only. |
| 5 | [13B](../book/part-3/13b-scams-and-regulatory-map.md) · L45 | Protection from Scams Act 2025 commenced 1 July 2025 and lets Police issue restriction orders to banks. | Major | MHA commencement notice and the Act text; which banks are in scope. |
| 6 | [13](../book/part-3/13-fraud-risk-and-payment-controls.md) · L54 | Chapter 13 and 13B must describe SRF scope identically. | Major | Diff the two passages against the Guidelines. |

## Lane 4 — Payments finance, treasury and reconciliation (3, 9A, 16, 16A, 17)

| # | Where | Claim to attack | If wrong | Check against |
|---|---|---|---|---|
| 1 | [3](../book/part-1/03-card-payment-lifecycle.md) · L22 | PSP "settled" is a provider status and may precede bank receipt by the merchant. | Major | Two PSPs' payout and settlement status definitions. |
| 2 | [9A](../book/part-2/09a-cross-border-fx-and-treasury.md) · L28 | PvP reduces principal FX settlement risk; BIS contrasts PvP with methods that only mitigate it. Chapter correctly calls this wholesale context. | Minor | BIS Quarterly Review, June 2026 (36% PvP; 90% eliminate or minimise). |
| 3 | [9A](../book/part-2/09a-cross-border-fx-and-treasury.md) · L65 | Originator and beneficiary data duties vary by jurisdiction; virtual-asset Travel Rule is separate. | Major | FATF R16 update (June 2025); local transposition; corridor partner contract. |
| 4 | [16](../book/part-4/16-three-way-reconciliation.md) · L66 | S$10,000 vs S$8,750 is explained by S$500 refunds, S$200 dispute debit, S$250 fees and S$300 reserve; each deduction still needs checking for authorization and attribution. | Major | Finance reviewer: whether a reserve belongs on the same bridge as fees, sign conventions and fee timing. |
| 5 | [16](../book/part-4/16-three-way-reconciliation.md) · L86 | Join keys must be namespaced by account/entity; amount + date is not a safe key. | Major | Two PSPs' reference-ID uniqueness guarantees. |
| 6 | [16A](../book/part-4/16a-payment-metrics-and-observability.md) · L96 | Fraud loss bps is value-based on matched captured sales, unlike the count-based VAMP ratio in chapter 15. | Major | Confirm no passage conflates the internal rate with a scheme monitoring ratio. |

## Lane 5 — Real-time rails, open banking and stablecoins (9, 18, 19)

| # | Where | Claim to attack | If wrong | Check against |
|---|---|---|---|---|
| 1 | [9](../book/part-2/09-transfers-real-time-bnpl.md) · L17 | FAST is the transfer infrastructure; PayNow is proxy addressing. Same wording must hold in chapters 2, 8, 9 and 18. | Minor | MAS payments pages; PayNow operator documentation. |
| 2 | [19](../book/part-5/19-stablecoins-programmable-money.md) · L66 | The MAS-regulated stablecoin designation is not mandatory for every token branded a stablecoin; DPT obligations remain. | Major | MAS 2023 framework announcement; current PSA status. |
| 3 | [19](../book/part-5/19-stablecoins-programmable-money.md) · L68 | Consultation published 1 September 2026, closed 16 October 2026; proposals are not enacted obligations. | Major | MAS consultation page, and any later response paper or legislation. |
| 4 | [19](../book/part-5/19-stablecoins-programmable-money.md) · L74 | GENIUS Act signed 18 July 2025; operational obligations depend on implementing rules. | Major | Federal and state rulemaking status on the review date. |
| 5 | [18](../book/part-5/18-real-time-open-banking-payment-initiation.md) · L21 | PayNow, FAST, SGQR and a merchant wallet QR are not interchangeable protocols; a merchant displaying SGQR must know which scheme settled the tender. UK Open Banking comparator is scoped to its own standard. | Minor | ABS PayNow page and MAS SGQR description (chapter 8 cites MAS, chapter 18 cites ABS); Open Banking UK standards. |

## Lane 6 — Agentic-commerce architecture and security (20)

| # | Where | Claim to attack | If wrong | Check against |
|---|---|---|---|---|
| 1 | [20](../book/part-5/20-agentic-commerce-delegated-payments.md) · L51 | AP2 v0.2.0 released 28 April 2026; core specification contributed to the FIDO Alliance; future work moves through FIDO. | Major | AP2 releases page; FIDO announcement; AP2 CONTRIBUTING.md. Re-pin the revision at each review. |
| 2 | [20](../book/part-5/20-agentic-commerce-delegated-payments.md) · L53 | v0.1 "CartMandate" was renamed "Checkout Mandate" in v0.2. | Major | AP2 v0.2 specification and release notes. |
| 3 | [20](../book/part-5/20-agentic-commerce-delegated-payments.md) · L59 | AP2 samples include an x402 example; this does not make x402 or stablecoins mandatory. | Major | AP2 docs index; chapter 19 cross-reference. |
| 4 | [20](../book/part-5/20-agentic-commerce-delegated-payments.md) · L49 | Vendor announcements are labelled as such and not presented as standards or production support. | Minor | Each vendor page and date. |

## Cross-chapter consistency checks

| Check | What to compare |
|---|---|
| Same fact, same words | SRF scope (13, 13B); PayNow/FAST layering (2, 8, 9, 18); DPAN as device token (7, 7A, 8, 11); PCI/SAQ A wording (3, 13A). |
| One rule for unknown outcomes | Resolve status before retry or resend: 3, 6, 9A, 10, 10A, 12, 17. Check no chapter lets a UI retry bypass it. |
| Count-based vs value-based ratios | VAMP (15) is count-based; fraud loss bps (16A) is value-based. Check 11, 13, 15 and 16A never use one for the other. |
| Authentication is not authorization | 3DS result vs issuer decision in 3, 11, 12; identical wording and the same liability caveat. |
| Time-sensitive anchors | 15 (VAMP), 13B (SRF, PSA), 19 (MAS consultation, GENIUS), 20 (AP2/FIDO), 11 (3DS version), 7A (EMVCo). Each is dated 16 November 2026 and goes stale first. |

## Suggested first 30 minutes

Read the **Blocker** rows in your lane first (3DS liability shift and exemptions; PCI SAQ A; SRF scope and card exclusion). Then the dated anchors in the last cross-chapter check, because they go stale first.
