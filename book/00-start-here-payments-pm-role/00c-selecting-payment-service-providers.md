# Part 0 · Selecting PSPs, managing partners and writing useful SLAs

**Estimated study time:** ~17 minutes · **Prerequisites:** [Prioritization](00b-prioritization-and-product-tradeoffs.md) · **Status:** Editorial draft, 16 November 2026

> A PSP is not merely a pricing line. It is an external dependency in the customer's experience, your transaction state machine and your finance controls.

## Learning outcomes

After this chapter, you should be able to: (1) distinguish gateway, acquiring, orchestration and PayFac contracting responsibilities; (2) translate provider selection into end-to-end failure-state tests; (3) build a weighted scorecard with non-negotiable compliance and financial-integrity gates; and (4) define SLA measurements, escalation and an exit/credential-portability plan.

## 0C.1 First decide what you are buying

A **gateway API**, **acquiring service**, **full-stack PSP**, **payment orchestrator** and **payment facilitator** have overlapping but different accountabilities. For each candidate, clarify: legal contracting entity; merchant of record; acquirer of record; scheme registration where applicable; funds custody; geographic coverage; sponsor-bank dependencies; underwriting ownership; liability allocation; and who produces the settlement/payout report.

A processor promising “all payment methods” does not mean it supports the payment methods, countries, currencies, funding models and refund behaviors you need in production. Build your requirements around real transaction journeys.

## 0C.2 Write the RFP as testable journeys

For a merchant checkout product, include at least these end-to-end tests:

1. **Normal purchase:** guest and stored credential, 3DS challenge when triggered, authorization, capture, partial capture where supported.
2. **Uncertain outcome:** timeout after submitted request, duplicate retry, status query, late webhook and reconcilable resolution.
3. **Refund:** full and partial refund, asynchronous success/failure, source transaction linkage, fee and payout treatment.
4. **Dispute:** notification, evidence deadline and upload, representment status, separate financial adjustments.
5. **Credentials:** vault token vs network token, lifecycle after card reissue, customer-consent/data controls and portability limitations.
6. **Operations:** settlement batch, fees, reserves, payout IDs, bank statement matching, API versioning and incident escalation.

For issuing, also test authorization controls, reversals, settlement files, card lifecycle and token provisioning. For acquiring/PayFac, include KYB, underwriting, reserves, delayed payouts, negative balances, funding failure and merchant termination.

## 0C.3 Score providers transparently, then stress-test winners

**Illustrative weighted scorecard — not a universal ranking.** Score 1 (poor) to 5 (strong) against evidence, then multiply by the weight. Scores are hypotheses until tested by proofs of concept and contract reviews.

| Category | Weight | Provider A (fictional) | Provider B (fictional) |
|---|---:|---:|---:|
| Market and payment-method coverage | 20% | 5 | 4 |
| Reliability and failure-state semantics | 25% | 3 | 5 |
| Financial reporting and reconciliation | 20% | 3 | 5 |
| Security, compliance and contractual controls | 15% | 4 | 4 |
| Developer and operational experience | 10% | 5 | 3 |
| Total cost of acceptance | 10% | 5 | 3 |
| **Weighted score (out of 5)** | **100%** | **3.95** | **4.25** |

Provider A: `0.20×5 + 0.25×3 + 0.20×3 + 0.15×4 + 0.10×5 + 0.10×5 = 3.95`. Provider B: `0.20×4 + 0.25×5 + 0.20×5 + 0.15×4 + 0.10×3 + 0.10×3 = 4.25`. Document the calculations and validate the scorecard before it influences procurement.

**Important:** A higher score does not override missing legal coverage, unacceptable settlement terms or a failing financial-integrity test. Define hard gates separately. Weights should reflect your actual business model, not copied templates.

Downloadable [evaluation template](../../artifacts/psp-evaluation-template.md).

## 0C.4 SLAs need a measurement contract, not just “99.9% uptime”

A useful SLA distinguishes:

- **Availability:** Which endpoint or transaction operation, from which locations, measured over what window? Are scheduled maintenance and third-party disruptions excluded?
- **Latency:** p50/p95/p99 for the named operation; end-to-end time may include issuer/ACS dependencies outside a PSP's API latency measure.
- **Payment outcomes:** A timeout is not necessarily an unsuccessful authorization; distinguish technical acceptance, approved auth, captured payment and confirmed order.
- **Webhook delivery:** Expected timing, retries, signature verification, duplicate delivery, retention and recovery after prolonged outage.
- **Support response:** Severity definitions, acknowledgement vs mitigation vs resolution, on-call escalation and incident communication.
- **Finance operations:** Settlement report availability, payout timing, cutoff calendars, exception investigation and corrections.
- **Data controls:** Access, key management, incident notification, audit evidence, retention, subcontractors and exit provisions.

**Sample (hypothetical) SLO, not a provider promise:** For payment status queries, 99.95% successful technical responses over 30 days, measured from two production regions, excluding invalid merchant requests. Even then, define how a query returns `pending`, and never interpret transport availability as payment approval rate.

## 0C.5 Contract, commercial and exit risks

The lowest MDR can conceal cross-border markups, refunds/chargeback fees, FX spreads, dispute administration charges, token-vault dependency, reserves, minimum commitments or settlement financing costs. Compare **cost per confirmed paid order**, adjusted for acceptance, risk and operations, instead of simply comparing transaction fee percentages.

Ask about token portability before storing millions of credentials with one PSP. A PSP vault token generally does not automatically work at another provider; EMV network token domains, supported integrations, PCI responsibilities and scheme rules require separate diligence.

Plan for exit: how will you migrate credentials where legally/permissibly supported, retrieve transaction/dispute history, retain settlement files, and continue refunds on old transactions? A provider outage is a test of your state machine; a provider termination is a test of your architecture and operational ownership.

## 0C.6 Partner operating cadence

Set up weekly operational review for approval/failure segmentation, incidents and dispute aging; monthly product review for roadmap, feature flags, integrations, cost, treasury and reliability; quarterly commercial review for volumes, terms, reserves and switching risk. Record the precise owner and due date for every unresolved status mismatch or settlement exception.

The PM should be able to answer **“What could this partner stop us from doing?”** and **“What evidence will tell us a contract is no longer fit?”**. This is partner *product management*, not merely procurement.

## 0C.7 Exercise and answer check

**Scenario:** Provider A offers 15 bps lower processing fees, but has no reliable status-query API and settlement reports arrive two days late. Your checkout experiences ambiguous outcomes and finance has a daily close requirement. What should determine the decision?  
**Answer check:** Treat status certainty and finance reporting as hard requirements; quantify duplicate-charge exposure, reconciliation cost, and recovery limitations. Only compare headline price among eligible providers; insist on an integration pilot and finance sign-off.

**Exercises:** [Worked solutions](../../answers/chapter-exercises.md#00c-selecting-payment-service-providers) (companion answer key; review your reasoning before opening).

**Next:** [1. What is a payment?](../01-how-payments-work/01-understanding-a-payment.md).
