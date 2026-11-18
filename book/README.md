# Read the Payments PM Handbook

This is the **reader-friendly table of contents** for a practical, 32-chapter guide to the systems, economics and product decisions behind modern payments. Choose a topic below—no need to decode the repository's file or folder names.

**New here?** Start with [How money moves](#payment-fundamentals-how-money-moves). **Already working in payments?** Jump to the problem you're solving.

## Start here: The job of a Payments PM

Learn the responsibilities, decisions, partners and first steps of a Payments Product Manager.

- **[What a Payments PM owns (and what they do not)](part-0/00-payments-pm-ownership.md)** — Product ownership, responsibilities and decision rights.
- **[Your first 90 days in payments](part-0/00a-first-90-days.md)** — Map payment flows, risk, metrics and key partners.
- **[How to prioritize payments work](part-0/00b-prioritization-and-tradeoffs.md)** — Balance customer growth, financial correctness, reliability and obligations.
- **[How to select a payment service provider](part-0/00c-psp-selection-and-slas.md)** — Compare providers, integrations, reliability and contractual commitments.

## Payment fundamentals: How money moves

Build the mental model: payment participants, messages, money movements and business economics.

- **[What is a payment, really?](part-1/01-what-is-a-payment.md)** — Separate an instruction, a payment message and a final movement of money.
- **[Who does what in a payment?](part-1/02-ecosystem.md)** — Understand banks, card networks, processors, providers, merchants and customers.
- **[How a card payment works, end to end](part-1/03-card-payment-lifecycle.md)** — Follow authorization, capture, settlement and payout.
- **[Who earns what? Payment pricing and economics](part-1/04-payment-economics.md)** — Understand interchange, merchant discount rates, fees and exposure.

## Core payment products: Acceptance, issuing and money movement

Learn the main products a payments team builds or integrates, and how those products fit together.

- **[Merchant acquiring and onboarding](part-2/05-merchant-acquiring.md)** — How merchants are verified, underwritten and enabled to accept payments.
- **[Marketplaces, PayFacs and splitting funds](part-2/05a-marketplaces-payfac-funds-flow.md)** — Who holds and owes seller funds, and how payout liabilities work.
- **[Payment gateways and orchestration](part-2/06-gateways-orchestration.md)** — Routing, retries, integrations and provider choice.
- **[Card issuing and tokenization](part-2/07-issuing-tokenization.md)** — How cards are issued, secured and used.
- **[Network tokens explained: FPAN, DPAN and stored credentials](part-2/07a-network-tokenization-fpan-dpan.md)** — Differentiate funding cards, device tokens and network tokens.
- **[Digital wallets, QR payments and alternative payment methods](part-2/08-wallets-qr-apms.md)** — Acceptance and customer experience beyond card entry.
- **[In-store payments: POS terminals and offline acceptance](part-2/08a-card-present-pos-and-offline.md)** — What changes at the physical checkout.
- **[Bank transfers, instant payments and buy now, pay later](part-2/09-transfers-real-time-bnpl.md)** — Compare payment rails and their business trade-offs.
- **[Cross-border payments, FX and treasury](part-2/09a-cross-border-fx-and-treasury.md)** — Understand currencies, liquidity and international payouts.

## Build better payment journeys: Checkout, conversion and risk

Turn payment-system knowledge into safer checkout flows, better conversion and measurable product decisions.

- **[Designing checkout and payment states](part-3/10-checkout-and-payment-state.md)** — Handle pending, failed, successful and unknown outcomes correctly.
- **[Subscriptions, saved cards and failed-payment recovery](part-3/10a-subscriptions-stored-credentials-and-dunning.md)** — Retries, recurring consent, dunning and entitlements.
- **[3-D Secure: When and why customers are challenged](part-3/11-3d-secure.md)** — Authentication, friction and liability trade-offs.
- **[Improving payment authorization rates](part-3/12-authorization-optimization.md)** — Diagnose declines and design safe optimization experiments.
- **[Payment fraud and risk controls](part-3/13-fraud-risk-and-payment-controls.md)** — Balance loss prevention, customer experience and approval.
- **[Compliance ownership: PCI, KYC, KYB and AML](part-3/13a-compliance-and-control-ownership.md)** — Assign responsibilities without confusing standards, laws and provider controls.
- **[Protecting customers from scams](part-3/13b-scams-and-regulatory-map.md)** — Distinguish unauthorized fraud from authorized scams, with Singapore examples.
- **[The craft of Payments PM: Discovery to delivery](part-3/14-payments-pm-craft.md)** — Metrics, requirements, trade-offs and cross-functional execution.

## Run payments at scale: Disputes, reconciliation and reliability

Understand what happens after checkout—and how to prove that money and records agree.

- **[Chargebacks and customer disputes](part-4/15-chargebacks-and-disputes.md)** — Dispute lifecycles, evidence, liability and customer outcomes.
- **[Reconciling merchant, provider and bank records](part-4/16-three-way-reconciliation.md)** — Match captured sales, fees, refunds and payouts.
- **[Payment metrics and observability](part-4/16a-payment-metrics-and-observability.md)** — Define denominators, dashboards, alerts and guardrails.
- **[Keeping payment systems reliable](part-4/17-reliability-and-payment-operations.md)** — Incidents, failure recovery, operations and accountability.

## What's next: Instant payments, stablecoins and AI agents

Explore evolving payment methods and new product/accountability questions. These chapters are working drafts.

- **[Real-time payments, open banking and account-to-account initiation](part-5/18-real-time-open-banking-payment-initiation.md)** — Bank-led payment initiation and instant-payment flows.
- **[Stablecoins, settlement and programmable money](part-5/19-stablecoins-programmable-money.md)** — Token-based value transfer, redemption and operational dependencies.
- **[Agentic commerce: Who can authorize an AI purchase?](part-5/20-agentic-commerce-delegated-payments.md)** — Delegated consent, credentials, checkout constraints and accountability.


---

**Learn by doing:** [Authorization decline lab](../cases/01-authorization-rate-drop.md) · [PSP timeout and retry lab](../cases/02-ambiguous-authorization-routing.md) · [Marketplace funds flow lab](../cases/03-marketplace-reserve-refund-dispute.md) · [HarborCart case study](../editorial/harborcart-case-lab.md).

**Apply the learning:** [Templates and sample PRDs](../README.md#templates-and-worked-artifacts) · [Worked exercise answers](../answers/chapter-exercises.md) · [Payment terminology glossary](../references/glossary.md).

*Editorial status: v0.6.1 working manuscript; independent specialist review is pending. Country, scheme and provider rules are not universal.*
