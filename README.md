# The Merchant Payments PM Handbook

**A practical handbook for product managers who accept, optimize and operate payments on the merchant side.**

A free, open-source handbook for **merchant-side Payments PMs** at ecommerce companies, retailers, marketplaces, subscription businesses and omnichannel merchants. It connects payment mechanics to merchant product decisions: checkout conversion, payment methods, authorization rates, fraud, refunds, acceptance cost, settlement, reconciliation and incident response.

**Scope and expectations:** This is written for a **merchant integrating with and depending on payment infrastructure**, rather than for teams building the infrastructure itself. Gateways, acquirers, issuers, networks, wallets and emerging rails are explained so merchant PMs can select partners, understand behavior, specify integrations and manage outcomes. **It is not a complete operating manual for a payment gateway, fintech issuer, acquiring institution, bank, or payment network.** Those specialist areas appear as supporting context, not a promise of full infrastructure product training.

**[Browse all 32 chapters](book/README.md)** · **[Try a real payments case](cases/01-authorization-rate-drop.md)** · **[Explore templates and PRDs](#templates-and-worked-artifacts)** · **[Worked chapter exercises](answers/chapter-exercises.md)**

## What is inside?

| Explore | What you will learn |
| --- | --- |
| [What a Payments PM actually does](book/00-start-here-payments-pm-role/README.md) | Learn the responsibilities, decisions, partners and first steps of a Payments Product Manager. |
| [Payment fundamentals and economics](book/01-how-payments-work/README.md) | Build the mental model: payment participants, messages, money movements and business economics. |
| [Payment providers, infrastructure dependencies and methods](book/02-payment-products-and-infrastructure/README.md) | Understand providers and rails from the merchant's selection, integration, risk, economics and operating perspective. |
| [Checkout, fraud, authentication and PM craft](book/03-checkout-authorization-and-fraud/README.md) | Turn payment-system knowledge into safer checkout flows, better conversion and measurable product decisions. |
| [Disputes, reconciliation and operations](book/04-disputes-reconciliation-and-operations/README.md) | Understand what happens after checkout—and how to prove that money and records agree. |
| [New payment rails and agentic commerce](book/05-new-and-emerging-payments/README.md) | Optional merchant horizon-scanning for future acceptance, checkout and settlement choices; these chapters are working drafts. |

Every section has its own readable chapter guide. You can **[see the complete table of contents](book/README.md)** without browsing technical filenames.

## Where should you start?

- **New to payments?** Start with [How money moves](book/01-how-payments-work/README.md) to understand the lifecycle, actors and economics. Then explore [core products](book/02-payment-products-and-infrastructure/README.md).
- **Already a product manager?** Read [what a Payments PM owns](book/00-start-here-payments-pm-role/00-what-a-payments-pm-owns.md), then work through [checkout, authorization and fraud](book/03-checkout-authorization-and-fraud/README.md).
- **Responsible for merchant payment operations?** Go to [disputes, reconciliation and reliability](book/04-disputes-reconciliation-and-operations/README.md) and use the linked PRDs and checklists.
- **Working on AI-led checkout or new payment rails?** Explore [emerging payments](book/05-new-and-emerging-payments/README.md) and the [agentic checkout intent test](artifacts/agentic-checkout-intent-test.md).

## Learn by solving a payment problem

**An authorization rate falls from 94% to 89%.** Where do you look first, which cohorts do you investigate, and how do you raise approvals without creating fraud or duplicate charges? Work through the [authorization decline case](cases/01-authorization-rate-drop.md).

**A PSP times out but may have approved a charge.** Work through [ambiguous authorization and safe routing](cases/02-ambiguous-authorization-routing.md).

**A marketplace must refund one seller while holding reserves for another.** Explore the [seller funds-flow and dispute case](cases/03-marketplace-reserve-refund-dispute.md).

**Merchant operating playbooks:** [PSP orchestration strategy and migration](artifacts/merchant-psp-routing-and-migration-playbook.md) · [Reconciliation investigation and exception closure](artifacts/merchant-reconciliation-operations-checklist.md) · [Fraud framework: customer, transaction and context](artifacts/merchant-fraud-control-framework.md).

More practice: [HarborCart end-to-end case lab](editorial/harborcart-case-lab.md) · [Solutions to all chapter exercises](answers/chapter-exercises.md).

## About this project

This is a **working manuscript (v0.6.1, 16 November 2026)**. Draft chapters, examples and executable case checks are available, but independent specialist review remains pending. It is educational material, not regulatory, legal, financial or scheme-operational advice. Provider, network and regulatory rules may change; verify current primary sources and contracts before implementation.

Maintained by [@aditti30-prog](https://github.com/aditti30-prog). We welcome source-backed technical corrections: [how to contribute](CONTRIBUTING.md) · [primary-source audit](editorial/primary-source-audit-2026-11-16.md) · [specialist review](editorial/specialist-review-program.md) · [editorial roadmap](ROADMAP.md).

## Templates and worked artifacts

Each artifact is linked from the chapter it supports. They are teaching templates, not authority on any provider, scheme or regulator.

| Artifact | Use it to | Chapter |
|---|---|---|
| [Decision record template](artifacts/payment-decision-record-template.md) | Record a payments trade-off, owner and rollback | Part 0: [First 90 days](book/00-start-here-payments-pm-role/00a-your-first-90-days.md), [Prioritization](book/00-start-here-payments-pm-role/00b-prioritization-and-product-tradeoffs.md) |
| [PSP evaluation template](artifacts/psp-evaluation-template.md) | Score acquiring and PSP partners | Part 0: [PSP selection](book/00-start-here-payments-pm-role/00c-selecting-payment-service-providers.md) |
| [Payment recovery PRD](artifacts/sample-prd-payment-recovery.md) | Specify safe recovery from unknown outcomes | Part 0: [Ownership](book/00-start-here-payments-pm-role/00-what-a-payments-pm-owns.md), [3](book/01-how-payments-work/03-how-card-payments-work.md), [14](book/03-checkout-authorization-and-fraud/14-how-to-manage-payment-products.md) |
| [Platform funds-flow specification](artifacts/platform-funds-flow-spec.md) | Map who holds, owes and pays out money | [5A](book/02-payment-products-and-infrastructure/05a-marketplaces-payfacs-and-funds-flow.md) |
| [Cross-border payout checklist](artifacts/cross-border-payout-checklist.md) | Review a corridor before launch | [9A](book/02-payment-products-and-infrastructure/09a-cross-border-payments-fx-and-treasury.md) |
| [Payment API and state-machine checklist](artifacts/payment-api-requirements-checklist.md) | Turn state rules into testable requirements | [10](book/03-checkout-authorization-and-fraud/10-checkout-and-payment-status-design.md) |
| [Subscription recovery PRD](artifacts/subscription-recovery-prd.md) | Specify retries, notices and truthful entitlements | [10A](book/03-checkout-authorization-and-fraud/10a-subscriptions-recurring-payments-and-dunning.md) |
| [Compliance control-ownership matrix](artifacts/compliance-control-ownership-matrix.md) | Assign control owners across product, risk and legal | [13A](book/03-checkout-authorization-and-fraud/13a-compliance-pci-kyc-aml-and-ownership.md) |
| [Merchant-onboarding PRD](artifacts/sample-prd-merchant-onboarding-controls.md) | Specify onboarding states and gates | [13A](book/03-checkout-authorization-and-fraud/13a-compliance-pci-kyc-aml-and-ownership.md) |
| [Merchant PSP routing and migration](artifacts/merchant-psp-routing-and-migration-playbook.md) | Decide how and when to shift volume using resilience, success and cost | [6](book/02-payment-products-and-infrastructure/06-payment-gateways-routing-and-orchestration.md) |
| [Merchant reconciliation investigation checklist](artifacts/merchant-reconciliation-operations-checklist.md) | Diagnose order-to-PSP-to-bank mismatches and prove exception closure | [16](book/04-disputes-reconciliation-and-operations/16-payment-reconciliation-and-payouts.md) |
| [Merchant-side fraud framework worksheet](artifacts/merchant-fraud-control-framework.md) | Design customer/transaction/context signals and safe risk policy changes | [13](book/03-checkout-authorization-and-fraud/13-payment-fraud-and-risk-controls.md) |
| [Metrics dashboard specification](artifacts/payments-metrics-dashboard-spec.md) | Define metrics, denominators and guardrails | [16A](book/04-disputes-reconciliation-and-operations/16a-payment-performance-metrics-and-dashboards.md) |
| [Incident review template](artifacts/payment-incident-review-template.md) | Run a payment incident review | [17](book/04-disputes-reconciliation-and-operations/17-payment-outages-incidents-and-operations.md) |
| [Agentic checkout intent test](artifacts/agentic-checkout-intent-test.md) | Test delegated-purchase constraints | [20](book/05-new-and-emerging-payments/20-agentic-commerce-and-ai-payments.md) |

## Read from an actual product decision

**An AI agent changes a shopping cart after consent.** Read [Chapter 20](book/05-new-and-emerging-payments/20-agentic-commerce-and-ai-payments.md) and the [intent-preservation test](artifacts/agentic-checkout-intent-test.md) to distinguish permission, checkout, credential and payment execution.

**A platform owes several sellers while payouts fail.** Read [Chapter 5A](book/02-payment-products-and-infrastructure/05a-marketplaces-payfacs-and-funds-flow.md) and the [funds-flow spec](artifacts/platform-funds-flow-spec.md) before introducing split payments.

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
