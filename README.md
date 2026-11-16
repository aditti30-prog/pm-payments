# The Payments PM Handbook

**An open-source textbook on how modern payments work — and how product managers design, operate, and improve them.**

> **Editorial status: v0.3 working manuscript (16 November 2026).** Parts I–IV contain draft chapters and teaching examples. Part V is planned, not written. This is an educational resource, not regulatory, legal, scheme-operational or financial advice. Country, brand and provider rules change; follow linked primary sources and current contracts before implementing.

The objective is not to memorize payment jargon. Readers should understand **who does what**, **where money and obligations move**, **what can fail**, **who bears risk**, and **which decisions a PM can influence**.

**Maintained by [@aditti30-prog](https://github.com/aditti30-prog).** Specialist peer review is welcome; chapters are editorial drafts, not certified standards guidance.

## Who should read this?

- Product managers transitioning from ecommerce, fintech or banking into payments.
- Payments PMs who want to understand adjacent products (issuing, acquiring, tokenization, risk, reconciliation).
- Engineers, designers, risk professionals and founders who need the product and business context around payment infrastructure.

## How to use the book

**New Payments PM:** Start with Part 0 to understand role boundaries and work practices, then follow Parts I–IV in order. **Experienced PM or engineer:** Jump to the relevant payment-system chapter and use Part 0 as a working reference. Each chapter aims to explain the underlying mechanism and connect it to a product decision. Some chapters still require deeper examples, answer keys and specialist review.

### Part 0 — The Payments PM's job

- [What a Payments PM owns — archetypes, decision rights and example RACI](book/part-0/00-payments-pm-ownership.md)
- [First 90 days: mapping systems, metrics, risk and partners](book/part-0/00a-first-90-days.md)
- [Prioritization: obligations, financial integrity, reliability and growth](book/part-0/00b-prioritization-and-tradeoffs.md)
- [PSP selection: partner scorecards, integrations and SLAs](book/part-0/00c-psp-selection-and-slas.md)

Supporting tools: [decision record template](artifacts/payment-decision-record-template.md) and [PSP evaluation template](artifacts/psp-evaluation-template.md).

### Part I — Understanding Payments

1. [What is a payment?](book/part-1/01-what-is-a-payment.md)
2. [Who participates in a payment? The ecosystem](book/part-1/02-ecosystem.md)
3. [How a card payment works: authorization to payout](book/part-1/03-card-payment-lifecycle.md)
4. [Payment economics: interchange, MDR and exposure](book/part-1/04-payment-economics.md)

### Part II — Payment Products and Infrastructure

5. [Merchant acquiring and onboarding](book/part-2/05-merchant-acquiring.md)
6. [Gateways and payment orchestration](book/part-2/06-gateways-orchestration.md)
7. [Card issuing and tokenization](book/part-2/07-issuing-tokenization.md)
   - **Deep dive:** [Network tokens, FPAN, DPAN and token lifecycles](book/part-2/07a-network-tokenization-fpan-dpan.md)
8. [Wallets, QR and alternative payment methods](book/part-2/08-wallets-qr-apms.md)
9. [Bank transfers, instant payments and BNPL](book/part-2/09-transfers-real-time-bnpl.md)

### Part III — Building Payment Products

10. [Checkout, payment state and customer experience](book/part-3/10-checkout-and-payment-state.md)
11. **Deep dive:** [EMV 3-D Secure: frictionless, challenge and liability](book/part-3/11-3d-secure.md)
12. [Authorization optimization](book/part-3/12-authorization-optimization.md)
13. [Payment fraud, risk decisions and controls](book/part-3/13-fraud-risk-and-payment-controls.md)
14. [The Payments PM's craft: discovery, metrics and delivery](book/part-3/14-payments-pm-craft.md)

### Part IV — Operating and Scaling Payments

15. **Deep dive:** [Chargebacks and disputes](book/part-4/15-chargebacks-and-disputes.md)
16. **Deep dive:** [Three-party reconciliation: merchant, PSP and bank](book/part-4/16-three-way-reconciliation.md)
17. [Payment reliability, incidents and operations](book/part-4/17-reliability-and-payment-operations.md)

### Part V — Modern and Emerging Payments · planned

18. Real-time payments, open banking and payment initiation *(not written)*
19. Stablecoins and programmable money *(not written)*
20. Agentic commerce, delegated payment credentials and customer consent *(not written)*

See [ROADMAP.md](ROADMAP.md) for the editorial plan, known limitations and unfilled coverage areas.

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
