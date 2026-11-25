# Read the Merchant Payments PM Handbook

This is a practical, 32-chapter guide to **merchant-side payment acceptance, optimization and operations**. It covers gateways, issuers, acquirers and fintech infrastructure **as systems a merchant relies on**, not as training to operate those businesses. Choose a topic below—no need to decode the repository's file or folder names.

**New here?** Start with [How money moves](#payment-fundamentals-how-money-moves). **Already working in payments?** Jump to the problem you're solving.

## Start here: The job of a Payments PM

Learn the responsibilities, decisions, partners and first steps of a Payments Product Manager.

- **[What a Payments PM owns (and what they do not)](00-start-here-payments-pm-role/00-what-a-payments-pm-owns.md)** — Product ownership, responsibilities and decision rights.
- **[Your first 90 days in payments](00-start-here-payments-pm-role/00a-your-first-90-days.md)** — Map payment flows, risk, metrics and key partners.
- **[How to prioritize payments work](00-start-here-payments-pm-role/00b-prioritization-and-product-tradeoffs.md)** — Balance customer growth, financial correctness, reliability and obligations.
- **[How to select a payment service provider](00-start-here-payments-pm-role/00c-selecting-payment-service-providers.md)** — Compare providers, integrations, reliability and contractual commitments.

## Payment fundamentals: How money moves

Build the mental model: payment participants, messages, money movements and business economics.

- **[What is a payment, really?](01-how-payments-work/01-understanding-a-payment.md)** — Separate an instruction, a payment message and a final movement of money.
- **[Who does what in a payment?](01-how-payments-work/02-players-in-the-payments-ecosystem.md)** — Understand banks, card networks, processors, providers, merchants and customers.
- **[How a card payment works, end to end](01-how-payments-work/03-how-card-payments-work.md)** — Follow authorization, capture, settlement and payout.
- **[Who earns what? Payment pricing and economics](01-how-payments-work/04-payment-fees-interchange-and-mdr.md)** — Understand interchange, merchant discount rates, fees and exposure.

## Core payment products: Acceptance, issuing and money movement

Learn the main products a payments team builds or integrates, and how those products fit together.

- **[Merchant acquiring and onboarding](02-payment-products-and-infrastructure/05-merchant-acquiring-and-onboarding.md)** — How merchants are verified, underwritten and enabled to accept payments.
- **[Marketplaces, PayFacs and splitting funds](02-payment-products-and-infrastructure/05a-marketplaces-payfacs-and-funds-flow.md)** — Who holds and owes seller funds, and how payout liabilities work.
- **[Payment gateways and orchestration](02-payment-products-and-infrastructure/06-payment-gateways-routing-and-orchestration.md)** — Routing, retries, integrations and provider choice.
- **[Card issuing and tokenization](02-payment-products-and-infrastructure/07-card-issuing-and-tokenization.md)** — How cards are issued, secured and used.
- **[Network tokens explained: FPAN, DPAN and stored credentials](02-payment-products-and-infrastructure/07a-network-tokens-and-card-credentials.md)** — Differentiate funding cards, device tokens and network tokens.
- **[Digital wallets, QR payments and alternative payment methods](02-payment-products-and-infrastructure/08-wallets-qr-and-alternative-payment-methods.md)** — Acceptance and customer experience beyond card entry.
- **[In-store payments: POS terminals and offline acceptance](02-payment-products-and-infrastructure/08a-in-store-pos-contactless-and-offline.md)** — What changes at the physical checkout.
- **[Bank transfers, instant payments and buy now, pay later](02-payment-products-and-infrastructure/09-bank-transfers-real-time-payments-and-bnpl.md)** — Compare payment rails and their business trade-offs.
- **[Cross-border payments, FX and treasury](02-payment-products-and-infrastructure/09a-cross-border-payments-fx-and-treasury.md)** — Understand currencies, liquidity and international payouts.

## Build better payment journeys: Checkout, conversion and risk

Turn payment-system knowledge into safer checkout flows, better conversion and measurable product decisions.

- **[Designing checkout and payment states](03-checkout-authorization-and-fraud/10-checkout-and-payment-status-design.md)** — Handle pending, failed, successful and unknown outcomes correctly.
- **[Subscriptions, saved cards and failed-payment recovery](03-checkout-authorization-and-fraud/10a-subscriptions-recurring-payments-and-dunning.md)** — Retries, recurring consent, dunning and entitlements.
- **[3-D Secure: When and why customers are challenged](03-checkout-authorization-and-fraud/11-3d-secure-and-customer-authentication.md)** — Authentication, friction and liability trade-offs.
- **[Improving payment authorization rates](03-checkout-authorization-and-fraud/12-improving-payment-authorization-rates.md)** — Diagnose declines and design safe optimization experiments.
- **[Payment fraud and risk controls](03-checkout-authorization-and-fraud/13-payment-fraud-and-risk-controls.md)** — Build a merchant risk framework using customer, transaction and contextual behavior.
- **[Compliance ownership: PCI, KYC, KYB and AML](03-checkout-authorization-and-fraud/13a-compliance-pci-kyc-aml-and-ownership.md)** — Assign responsibilities without confusing standards, laws and provider controls.
- **[Protecting customers from scams](03-checkout-authorization-and-fraud/13b-scams-and-customer-protection.md)** — Distinguish unauthorized fraud from authorized scams, with Singapore examples.
- **[The craft of Payments PM: Discovery to delivery](03-checkout-authorization-and-fraud/14-how-to-manage-payment-products.md)** — Metrics, requirements, trade-offs and cross-functional execution.

## Run payments at scale: Disputes, reconciliation and reliability

Understand what happens after checkout—and how to prove that money and records agree.

- **[Chargebacks and customer disputes](04-disputes-reconciliation-and-operations/15-chargebacks-and-dispute-management.md)** — Dispute lifecycles, evidence, liability and customer outcomes.
- **[Reconciling merchant, provider and bank records](04-disputes-reconciliation-and-operations/16-payment-reconciliation-and-payouts.md)** — Match merchant orders and tenders to PSP settlement and bank payouts; investigate and close discrepancies.
- **[Payment metrics and observability](04-disputes-reconciliation-and-operations/16a-payment-performance-metrics-and-dashboards.md)** — Define denominators, dashboards, alerts and guardrails.
- **[Keeping payment systems reliable](04-disputes-reconciliation-and-operations/17-payment-outages-incidents-and-operations.md)** — Incidents, failure recovery, operations and accountability.

## What's next: Instant payments, stablecoins and AI agents

Explore evolving payment methods and new product/accountability questions. These chapters are working drafts.

- **[Real-time payments, open banking and account-to-account initiation](05-new-and-emerging-payments/18-instant-payments-open-banking-and-account-to-account.md)** — Bank-led payment initiation and instant-payment flows.
- **[Stablecoins, settlement and programmable money](05-new-and-emerging-payments/19-stablecoins-and-programmable-payments.md)** — Token-based value transfer, redemption and operational dependencies.
- **[Agentic commerce: Who can authorize an AI purchase?](05-new-and-emerging-payments/20-agentic-commerce-and-ai-payments.md)** — Delegated consent, credentials, checkout constraints and accountability.


---

**Learn by doing:** [Authorization decline lab](../cases/01-authorization-rate-drop.md) · [PSP timeout and retry lab](../cases/02-ambiguous-authorization-routing.md) · [Marketplace funds flow lab](../cases/03-marketplace-reserve-refund-dispute.md) · [HarborCart case study](../editorial/harborcart-case-lab.md).

**Merchant operating worksheets:** [Reconciliation investigation](../artifacts/merchant-reconciliation-operations-checklist.md) · [Fraud signals and decisions](../artifacts/merchant-fraud-control-framework.md).

**Apply the learning:** [Templates and sample PRDs](../README.md#templates-and-worked-artifacts) · [Worked exercise answers](../answers/chapter-exercises.md) · [Payment terminology glossary](../references/glossary.md).

*Editorial status: v0.6.1 working manuscript; independent specialist review is pending. Country, scheme and provider rules are not universal.*
