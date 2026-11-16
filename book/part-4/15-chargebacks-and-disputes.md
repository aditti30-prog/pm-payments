# 15. Chargebacks and card disputes: lifecycle, evidence and product controls

**Part IV — Operating and Scaling Payments** · Prerequisites: Chapters 3, 5, 11 and 12

> **Central idea:** A completed sale can be financially reversed much later. A Payments PM must build products that preserve evidence, explain outcomes, handle deadlines and correctly account for dispute debits and credits.

## Learning outcomes

Explain the difference between refunds and chargebacks, trace a dispute across issuer, scheme, acquirer and merchant, define a minimum evidence data model, assess when to defend, and connect the dispute process to financial reconciliation.

## 15.1 What is a chargeback?

A **refund** is a merchant-initiated return of funds, typically through the payment provider, following the applicable payment-method rules. A **chargeback** is a card-network dispute process generally initiated through a cardholder's issuer; its result can cause funds to be debited back from the merchant/acquirer side. These are not interchangeable operations and should not share a generic status or ledger entry. Some payment methods have other dispute and recovery processes; **not every instant transfer has a card-style chargeback**.

A dispute may concern an allegedly unauthorized transaction, duplicate processing, incorrect amount, goods or services not received, cancellation, credit not processed, or goods not as described. The exact *reason codes* and their definitions depend on the card brand and current rules; there is no universal cross-scheme list you can hard-code forever.

Three questions often get muddled:

1. **Did a valid authorization occur?** Technical payment acceptance.
2. **Did the merchant deliver what was promised?** Commercial/order fulfillment.
3. **Who bears financial responsibility if the customer contests the transaction?** Scheme rules, evidence, applicable liability shift, contractual arrangements and outcome.

A captured and paid-out card transaction can later be disputed. A 3DS-authenticated payment is still disputable; any liability protection is category- and rule-specific.

## 15.2 The actors and dispute path

```mermaid
sequenceDiagram
    participant C as Cardholder
    participant I as Issuer
    participant N as Card network / scheme
    participant A as Acquirer / PSP
    participant M as Merchant + ops
    C->>I: Raise a concern / dispute
    I->>N: Submit eligible dispute under scheme process
    N->>A: Route dispute and reason
    A->>M: Notify; request response/evidence
    alt Merchant accepts / does not respond
      M-->>A: Accept or no defense
    else Merchant contests
      M->>A: Evidence / representment within deadline
      A->>N: Forward supported defense
      N->>I: Dispute resolution steps
    end
    I-->>N: Outcome / further step
    N-->>A: Financial and status events
    A-->>M: Debit/credit and final status
```

*Not every dispute uses every stage; some programmes include inquiries, automated defense, pre-arbitration and arbitration, with scheme-specific deadlines and fees.*

**Common workflow:** early inquiry or request for information (where supported) → chargeback notification and debit → merchant choice to accept or defend → evidence submission/representment → possible reversal, second chargeback or pre-arbitration/arbitration → final accounting. The order and names differ across providers.

## 15.3 Reason codes drive evidence, not a generic appeal letter

Examples of evidence categories (subject to local law and scheme rules):

| Dispute family | Useful records | Caution |
|---|---|---|
| Fraud / unauthorized | Authorization and applicable authentication result; issuer/PSP fields; customer account/activity context | 3DS liability shift depends on transaction and rules; do not send raw card credentials |
| Goods not received | Order confirmation, delivery and recipient confirmation, shipment tracking, customer contact | A tracking number alone may not prove delivery or service fulfillment |
| Duplicate processing | Separate order IDs, attempts, captures, voids and refunds; reconciliation detail | Repeated authorization is not automatically repeated settled charge |
| Cancellation / credit not processed | Terms accepted, cancellation timestamp, merchant refund record, provider refund status | A merchant UI showing “refund initiated” is not proof the refund completed |
| Not as described | Product description at time of sale, disclosures, support exchanges, fulfillment evidence | Preserve versioned descriptions, not just the current webpage |

Evidence collection is a **product architecture problem**: if event identities, terms-version, shipping state and refund references are never captured, the dispute team cannot recreate the truth months later. Preserve only necessary data with appropriate access controls, retention rules and privacy protections. Provider instructions may explicitly prohibit including sensitive IDs or PANs in defense uploads.

## 15.4 Representment, decisions and deadlines

**Representment** is the merchant/acquirer's formal response contesting a chargeback under applicable scheme processes. It is not a guarantee of reversal. Some cases may warrant immediate acceptance because the refund was owed, the evidence is weak, the response deadline is near, or the likely defense costs exceed the recoverable amount. Others warrant defense when there is strong evidence and a reasonable chance of success.

**Do not build a fixed “30-day dispute deadline” into a universal product.** Time limits depend on stage, reason code, scheme, provider, geography and transaction circumstances. Ingest the actual provider-provided response due date and apply internal buffers for weekends, file preparation and partner submission.

An operational work queue should show the dispute reason, source payment and order, amount and currency, current stage, financial effect, response deadline, available evidence, assigned owner and next action. Record every submission and acknowledgement idempotently. Updates can be delayed or out of order; a case should not be marked won solely because evidence was uploaded.

## 15.5 Chargeback economics: the sale is not guaranteed revenue

**Fictional example:** A merchant captures S$200. It later receives a S$200 chargeback debit and an illustrative S$15 dispute handling fee. The merchant might lose the S$200 cash inflow and incur the fee; whether the original processing fee is refunded and how chargeback costs are allocated depend on agreements. If the merchant wins, a subsequent S$200 reversal credit may arrive **in a later payout batch**. Do not book a dispute victory as bank cash until the provider/bank records confirm the credit.

A good product metric is not just the “win rate.” Analyze **fraud dispute rate**, total disputed amount, recoveries, cost to defend, customer experience, cases aging toward deadlines and loss by product/issuer/market. Denominators matter: disputes raised this month can concern transactions from prior months. Use mature transaction cohorts and distinguish **received / defended / won** case populations.

**3DS link:** qualifying authentication can shift liability for certain fraud disputes, but does not remove refund obligations or all other chargeback categories. Review [Chapter 11](../part-3/11-3d-secure.md) for the authentication and liability distinction.

### Dated network-program anchor — Visa VAMP (source checked 16 November 2026)

Visa's [VAMP fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) describes a **count-based** monitoring ratio using fraud reports (TC40) and disputes (TC15) relative to settled transactions (TC05), subject to exclusions, minimum counts and region-dependent rules. It states that the excessive merchant threshold in **Asia Pacific, Canada, the EU and the US** reduced from **220 basis points (2.2%) to 150 basis points (1.5%) on 1 April 2026**. LAC and CEMEA have separate conditions; applicability depends on the acquirer/program status and other eligibility thresholds. This is a **scheme-monitoring metric**, not a generic cardholder dispute win rate or a universal chargeback target. Confirm current requirements with your acquiring partner and scheme documentation before using it in a production decision.

**PM implications:** establish ownership of scheme alerts; forecast with the **scheme-defined denominator** rather than checkout attempts; segment by merchant descriptor, acquirer and region; and account for delayed fraud/dispute reports. A percentage without the minimum count, reporting clock and regional scope is incomplete.

## 15.6 A PM's product requirements

At minimum, define:

- **Data model:** `payment_id`, `order_id`, `capture_id`, `dispute_id`, provider/scheme references, reason code, financial transaction ID, deadline, evidence version, status history. All values shown here are illustrative normalized fields.
- **Event model:** `dispute_opened`, `chargeback_debited`, `evidence_submitted`, `representment_accepted_or_rejected`, `case_closed`, `chargeback_reversed`. These names are illustrative; preserve the provider's actual event codes too.
- **Controls:** due-date monitoring, case ownership, permissioned evidence access, PII handling, audit trail, double-submission prevention, and alerts for cases that change stage.
- **Financial mapping:** chargeback debit, defense fee, reversal credit, second chargeback and payout adjustment must appear as distinct journal entries in reconciliation.
- **Customer experience:** support can say whether the dispute is open, in review or final; avoid promising that a reversal is immediate.

### Worked product case: groceries allegedly not delivered

A customer disputes a S$120 grocery order as “goods not received.” The order shows `delivered` but the support chat says the customer reported a missing package an hour later. A responsible workflow links the order, proof-of-delivery event and customer-service case, verifies whether a goodwill refund was already issued, and chooses appropriate response under the applicable reason code. It should **not** auto-defend every “delivered” order, because the evidence and customer claim can conflict.

The PM's intervention is to improve event integrity: one shared order reference, durable timestamps, proof-of-delivery metadata, refund-state checks and a decision workflow. This reduces both lost disputes and wrongful customer outcomes.

## Exercises

1. A customer wins a dispute for a product the merchant already refunded. What duplicate credit/debit risk must finance check?
2. A PSP webhook says `information_supplied`. Does that mean the merchant won?
3. Which event should be attached to the original order when a chargeback debit hits a later settlement batch?
4. How do you compare dispute performance without the survivorship bias of only looking at closed cases?
5. What evidence would a merchant require for a “duplicate processing” reason code?

**Answer prompts:** (1) Refund/chargeback overlap, potential second credit and provider adjustment. (2) No, only evidence was sent. (3) Separate dispute financial event with references, not a rewrite of the original capture. (4) Cohort by transaction date and maturity; track open cases. (5) Attempt/capture identifiers and matched order history.

**Applied finance case:** [A seller dispute after payout](../../cases/03-marketplace-reserve-refund-dispute.md) distinguishes a dispute notification, a financial debit, a platform fee and an *uncollected* seller receivable.

**Exercises:** [Worked solutions](../../answers/chapter-exercises.md#15-chargebacks-and-disputes) (companion answer key; review your reasoning before opening).

**Next:** [16. Three-party reconciliation](16-three-way-reconciliation.md).

## Further reading

- [Adyen — Dispute lifecycle and stages](https://docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow)
- [Adyen — Dispute management and evidence requirements](https://docs.adyen.com/risk-management/manage-disputes/)
- [Stripe — Dispute evidence examples](https://docs.stripe.com/disputes/visual-evidence)
- [Adyen — Settlement details report](https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report)
