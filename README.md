# The Payments PM Handbook

**An open-source textbook on how modern payments work — and how product managers design, operate, and improve them.**

> **Editorial status: v0.6.1 working manuscript (16 November 2026).** All five parts plus Part 0 now have chapter drafts and examples; technical and specialist review remain outstanding. This is an educational resource, not regulatory, legal, scheme-operational or financial advice. Country, brand and provider rules change; follow linked primary sources and current contracts before implementing.

The objective is not to memorize payment jargon. Readers should understand **who does what**, **where money and obligations move**, **what can fail**, **who bears risk**, and **which decisions a PM can influence**.

**Maintained by [@aditti30-prog](https://github.com/aditti30-prog).** Specialist peer review is welcome; chapters are editorial drafts, not certified standards guidance.

## Who should read this?

- Product managers transitioning from ecommerce, fintech or banking into payments.
- Payments PMs who want to understand adjacent products (issuing, acquiring, tokenization, risk, reconciliation).
- Engineers, designers, risk professionals and founders who need the product and business context around payment infrastructure.

## How to use the book

**New Payments PM:** Start with Part 0 to understand role boundaries and work practices, then follow Parts I–IV in order. **Experienced PM or engineer:** Jump to the relevant payment-system chapter and use Part 0 as a working reference. Each chapter aims to explain the underlying mechanism and connect it to a product decision. Some chapters still require deeper examples and independent specialist review; a worked-solutions companion now covers all chapter exercises. v0.4 adds metrics, operational failure response and compliance control ownership. v0.5 adds marketplace funds flow, card-present/offline POS, cross-border FX/treasury, subscriptions/dunning, scam protection and draft chapters on real-time payments, stablecoins and agentic commerce.

**Editorial companions:** [Worked solutions for all 32 chapters](answers/chapter-exercises.md) · [HarborCart end-to-end case lab](editorial/harborcart-case-lab.md) · [Primary-source audit (16 November 2026)](editorial/primary-source-audit-2026-11-16.md) · [Specialist review program](editorial/specialist-review-program.md) · [Specialist review packet: highest-risk claims](editorial/specialist-review-packet.md). **Independent specialist reviews are still pending.**

### Part 0 — The Payments PM's job

- [What a Payments PM owns — archetypes, decision rights and example RACI](book/part-0/00-payments-pm-ownership.md)
- [First 90 days: mapping systems, metrics, risk and partners](book/part-0/00a-first-90-days.md)
- [Prioritization: obligations, financial integrity, reliability and growth](book/part-0/00b-prioritization-and-tradeoffs.md)
- [PSP selection: partner scorecards, integrations and SLAs](book/part-0/00c-psp-selection-and-slas.md)

### Part I — Understanding Payments

1. [What is a payment?](book/part-1/01-what-is-a-payment.md)
2. [Who participates in a payment? The ecosystem](book/part-1/02-ecosystem.md)
3. [How a card payment works: authorization to payout](book/part-1/03-card-payment-lifecycle.md)
4. [Payment economics: interchange, MDR and exposure](book/part-1/04-payment-economics.md)

### Part II — Payment Products and Infrastructure

5. [Merchant acquiring and onboarding](book/part-2/05-merchant-acquiring.md)
   - **Deep dive:** [5A. Marketplaces, PayFacs and platform funds flow](book/part-2/05a-marketplaces-payfac-funds-flow.md)
6. [Gateways and payment orchestration](book/part-2/06-gateways-orchestration.md)
7. [Card issuing and tokenization](book/part-2/07-issuing-tokenization.md)
   - **Deep dive:** [Network tokens, FPAN, DPAN and token lifecycles](book/part-2/07a-network-tokenization-fpan-dpan.md)
8. [Wallets, QR and alternative payment methods](book/part-2/08-wallets-qr-apms.md)
   - **Deep dive:** [8A. Card-present POS and offline acceptance](book/part-2/08a-card-present-pos-and-offline.md)
9. [Bank transfers, instant payments and BNPL](book/part-2/09-transfers-real-time-bnpl.md)
   - **Deep dive:** [9A. Cross-border FX, treasury and payouts](book/part-2/09a-cross-border-fx-and-treasury.md)

### Part III — Building Payment Products

10. [Checkout, payment state and customer experience](book/part-3/10-checkout-and-payment-state.md)
    - **Deep dive:** [10A. Subscriptions, stored credentials and dunning](book/part-3/10a-subscriptions-stored-credentials-and-dunning.md)
11. **Deep dive:** [EMV 3-D Secure: frictionless, challenge and liability](book/part-3/11-3d-secure.md)
12. [Authorization optimization](book/part-3/12-authorization-optimization.md)
13. [Payment fraud, risk decisions and controls](book/part-3/13-fraud-risk-and-payment-controls.md)
    - **Deep dive:** [13A. Compliance, PCI scope, KYC/KYB/AML and control ownership](book/part-3/13a-compliance-and-control-ownership.md)
    - **Deep dive:** [13B. Scam protection and a jurisdictional regulation map](book/part-3/13b-scams-and-regulatory-map.md)
14. [The Payments PM's craft: discovery, metrics and delivery](book/part-3/14-payments-pm-craft.md)

### Part IV — Operating and Scaling Payments

15. **Deep dive:** [Chargebacks and disputes](book/part-4/15-chargebacks-and-disputes.md)
16. **Deep dive:** [Three-party reconciliation: merchant, PSP and bank](book/part-4/16-three-way-reconciliation.md)
    - **Deep dive:** [16A. Payments metrics and observability](book/part-4/16a-payment-metrics-and-observability.md)
17. [Payment reliability, incidents and operations](book/part-4/17-reliability-and-payment-operations.md)

### Part V — Modern and Emerging Payments · working drafts

18. [Real-time payments, open banking and payment initiation](book/part-5/18-real-time-open-banking-payment-initiation.md)
19. [Stablecoins, settlement and programmable money](book/part-5/19-stablecoins-programmable-money.md)
20. **Deep dive:** [Agentic commerce, delegated credentials and customer consent](book/part-5/20-agentic-commerce-delegated-payments.md)

**Practice:** [Agentic Checkout Intent & Permission Test](artifacts/agentic-checkout-intent-test.md) contains a deterministic, simulated-policy case and eight executable test fixtures. These check customer constraints but are not a production implementation of any payment protocol.

See [ROADMAP.md](ROADMAP.md) for the editorial plan, known limitations and unfilled coverage areas.

**Post-review quality patch (v0.5.1):** Singapore SRF and Protection from Scams Act scope, MAS stablecoin consultation dates and EU/US comparators, AP2 v0.2/FIDO governance, FATF Recommendation 16, treasury liquidity example and CSV-driven HarborCart metric checks. A [weekly external reference-link audit](.github/workflows/external-link-audit.yml) reports confirmed 404/410 failures separately from links that cannot be verified. Specialist review and exercise-answer coverage remain incomplete.

## Templates and worked artifacts

Each artifact is linked from the chapter it supports. They are teaching templates, not authority on any provider, scheme or regulator.

| Artifact | Use it to | Chapter |
|---|---|---|
| [Decision record template](artifacts/payment-decision-record-template.md) | Record a payments trade-off, owner and rollback | Part 0: [First 90 days](book/part-0/00a-first-90-days.md), [Prioritization](book/part-0/00b-prioritization-and-tradeoffs.md) |
| [PSP evaluation template](artifacts/psp-evaluation-template.md) | Score acquiring and PSP partners | Part 0: [PSP selection](book/part-0/00c-psp-selection-and-slas.md) |
| [Payment recovery PRD](artifacts/sample-prd-payment-recovery.md) | Specify safe recovery from unknown outcomes | Part 0: [Ownership](book/part-0/00-payments-pm-ownership.md), [3](book/part-1/03-card-payment-lifecycle.md), [14](book/part-3/14-payments-pm-craft.md) |
| [Platform funds-flow specification](artifacts/platform-funds-flow-spec.md) | Map who holds, owes and pays out money | [5A](book/part-2/05a-marketplaces-payfac-funds-flow.md) |
| [Cross-border payout checklist](artifacts/cross-border-payout-checklist.md) | Review a corridor before launch | [9A](book/part-2/09a-cross-border-fx-and-treasury.md) |
| [Payment API and state-machine checklist](artifacts/payment-api-requirements-checklist.md) | Turn state rules into testable requirements | [10](book/part-3/10-checkout-and-payment-state.md) |
| [Subscription recovery PRD](artifacts/subscription-recovery-prd.md) | Specify retries, notices and truthful entitlements | [10A](book/part-3/10a-subscriptions-stored-credentials-and-dunning.md) |
| [Compliance control-ownership matrix](artifacts/compliance-control-ownership-matrix.md) | Assign control owners across product, risk and legal | [13A](book/part-3/13a-compliance-and-control-ownership.md) |
| [Merchant-onboarding PRD](artifacts/sample-prd-merchant-onboarding-controls.md) | Specify onboarding states and gates | [13A](book/part-3/13a-compliance-and-control-ownership.md) |
| [Metrics dashboard specification](artifacts/payments-metrics-dashboard-spec.md) | Define metrics, denominators and guardrails | [16A](book/part-4/16a-payment-metrics-and-observability.md) |
| [Incident review template](artifacts/payment-incident-review-template.md) | Run a payment incident review | [17](book/part-4/17-reliability-and-payment-operations.md) |
| [Agentic checkout intent test](artifacts/agentic-checkout-intent-test.md) | Test delegated-purchase constraints | [20](book/part-5/20-agentic-commerce-delegated-payments.md) |

## Read from an actual product decision

**An AI agent changes a shopping cart after consent.** Read [Chapter 20](book/part-5/20-agentic-commerce-delegated-payments.md) and the [intent-preservation test](artifacts/agentic-checkout-intent-test.md) to distinguish permission, checkout, credential and payment execution.

**A platform owes several sellers while payouts fail.** Read [Chapter 5A](book/part-2/05a-marketplaces-payfac-funds-flow.md) and the [funds-flow spec](artifacts/platform-funds-flow-spec.md) before introducing split payments.

## Operational failure labs — follow the IDs and the money

These two synthetic labs connect provider events, merchant state, customer outcomes and finance reconciliation. They are **teaching examples**, not production procedures or independent specialist sign-off.

| Lab | Start here | Why a PM needs it |
|---|---|---|
| [02 — Timeout and unsafe PSP failover](cases/02-ambiguous-authorization-routing.md) | One original request may be approved even if the merchant saw a timeout | Protect against duplicate authorizations/captures; distinguish 3DS, approval and paid orders |
| [03 — Seller reserve, refund and dispute waterfall](cases/03-marketplace-reserve-refund-dispute.md) | A platform owes two sellers after a S$250 capture | Prove gross-to-net allocations, reserve liability, a seller receivable and post-payout dispute exposure |

The inputs are kept in [operational-case-inputs.json](cases/data/operational-case-inputs.json), and [CI recomputes the outcomes](scripts/verify_operational_cases.py). Arithmetic checks cannot substitute for legal, scheme-rule or provider-contract validation.

## Start with a real problem

**A payment authorization rate drops from 94% to 89%.** Read [the worked case](cases/01-authorization-rate-drop.md), identify the affected cohorts, and define an experiment that doesn't create duplicate charges or a later fraud spike.

**An approved payment is timed out in the merchant system.** Review the [sample payment recovery PRD](artifacts/sample-prd-payment-recovery.md) and specify what the UI, merchant backend, PSP and finance teams must each do.

## Editorial principles

1. **Payment lifecycle before PM opinion.** Teach the underlying system before recommending a product intervention.
2. **Authorization ≠ capture ≠ settlement ≠ payout.** Keep precise financial states.
3. **Authentication ≠ authorization.** 3DS and network tokens have different jobs.
4. **A provider practice is not a universal standard.** State scope, jurisdiction and scheme dependencies.
5. **No unexplained money.** Every refund, dispute, fee, reserve and payout should have reconcilable identifiers.
6. **Clearly hypothetical examples.** Numbers and scenarios in worked cases are teaching data, not actual merchant performance.
7. **No sensitive or proprietary material.** Do not commit customer PANs, credentials or confidential contracts.

## References and contributions

Chapters link to relevant EMVCo, network, payment provider and regulatory resources for further learning. Technical corrections with primary sources are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

Original content is offered under [CC BY 4.0](LICENSE.md) unless otherwise noted. Linked external materials are under their own terms.
