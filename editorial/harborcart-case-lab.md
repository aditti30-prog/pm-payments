# HarborCart case lab — one transaction, five ledgers

**Synthetic teaching lab.** All customer, merchant and provider names, dates, numbers, contractual terms, and fees are invented. This is not a production transaction model. Work through the case before looking at the answer.

## Scenario

HarborCart sells groceries. For one order, a customer is quoted **S$100** and the card issuer approves a S$100 authorization. After picking, a S$20 item is unavailable. The provider supports partial capture and HarborCart captures **S$80**. The order is delivered, but one additional S$10 item is later refunded. The PSP's *fictional* fees are **2.0% of captured sales plus S$0.20 per captured transaction**; for simplicity, the PSP charges **no refund fee**, holds **no reserve** and makes **one payout containing only this order**. All amounts are SGD and belong to the same settlement/payout cycle.

Separately, a late duplicate `capture_succeeded` webhook arrives. The merchant's first callback had timed out after the capture request was processed.

### Source events

| Event | Provider/system evidence | Amount | What is **not** yet proven |
|---|---|---:|---|
| `auth_approved` | auth `A1`, order `O1`, attempt `P1` | S$100 | Capture, settlement and payout |
| `item_unavailable` | order revision `O1-v2` | −S$20 | Merchant receives any less money until capture is confirmed |
| `capture_accepted` | capture `C1` | S$80 | Bank credit or even same-day settlement |
| `capture_succeeded` webhook | `C1`, event `EV1` delivered twice | S$80 | That two distinct captures occurred |
| `refund_succeeded` | refund `R1` linked to `C1` | S$10 | Payout total unless fee/refund adjustment is known |
| `settlement_line` | provider settlement `S1` | +S$80 sale, −S$10 refund, −fee | Actual bank credit |
| `bank_credit` | bank payout `B1` | S$68.20 | That all order/refund event IDs matched unless transaction recon completed |

### Questions

1. Which event should mark the **order** confirmed, the **payment** captured, and the **merchant** paid? Can all three use a single Boolean?
2. What is the correct gross-to-net PSP payout bridge? Show each fee component and the final amount.
3. Why does the second `capture_succeeded` webhook not imply a second S$80 capture? What unique keys and atomic side effects prevent duplicate order fulfillment and ledger entries?
4. The capture API timed out. Before EV1 arrives, should the client try a new capture `C2`? What is the safe intermediate UI and operational state?
5. The bank credit is correct but the merchant order ledger has no `R1` refund reference. Does the three-party reconciliation pass?
6. Your dashboard shows one approved auth, two webhook deliveries and one settled capture. Which event counts belong in the authorization and payment-success metrics?

## Worked solution

1. Order fulfillment/commercial confirmation is distinct from financial events. `A1` authorizes a maximum amount but does not settle it. `C1` establishes a captured payment outcome when authoritatively confirmed. Only `B1` proves this bank payout. **Do not use a universal `is_paid` Boolean** for all three. Recommended events: `order_confirmed`, `payment_authorized`, `payment_captured`, `settlement_recorded`, `payout_confirmed` with references and timestamps.
2. **Fee** = 2% × S$80 + S$0.20 = S$1.60 + S$0.20 = **S$1.80**. **Payout** = S$80 capture − S$10 refund − S$1.80 fee = **S$68.20**. An S$100 authorization is *not* gross settled volume. Treat fee-refund behavior as specified solely for this fictional case.
3. Webhooks provide notifications about underlying provider events and may be delivered more than once. `EV1` and `C1` remain the **same source events**. Verify provider signature, dedupe on event ID, enforce allowed state transitions and write the order/ledger/fulfillment side effect only once via transactional inbox/outbox or equivalent. Do not dedupe by S$80 amount.
4. A network timeout creates `capture_outcome_unknown`, not `capture_failed`. Query status by `P1`/`C1` with documented API semantics; hold any new money-moving capture and preserve a customer-facing pending state. If C1 later succeeds, finalize once; if definitively failed, follow permitted capture recovery policy. Escalate aged unknown states to the operations queue.
5. **No.** Bank-level net tie-out is necessary but does not prove transaction-level correctness. Reconcile order ledger → PSP capture/refund detail → payout file/bank, and repair the missing `R1` source reference through a controlled, auditable adjustment, not a plug entry.
6. Authorization attempt denominator includes **one eligible auth attempt** and one approval. Captured payment count is **one** if confirmed. Webhook delivery count can be **two** in infrastructure observability but must **never** become two captures, two paid orders or two refunds. Preserve raw deliveries for incident diagnosis, distinct financial event IDs for business metrics.

## Product requirements that follow from the exercise

- `order_id`, `payment_intent_id`, `attempt_id`, `authorization_id`, `capture_id`, `refund_id`, `settlement_line_id` and `payout_id` are linked with explicit parent relationships; external IDs are namespaced by provider and merchant account.
- Unknown money-moving operations have **pending** state, bounded retries for status *reads*, alerts and manual recovery; cross-PSP operations are not assumed idempotent.
- Callback processing validates authenticity and idempotency, preserves event chronology and is safe under out-of-order delivery.
- Finance receives immutable source events and a gross-to-net bridge with fees, refunds, reserves and chargebacks as separate lines.
- PM scorecard includes unique orders completed, distinct captures, unresolved operations aging, duplicate settled charges, recon exception aging and verified payouts—not simply HTTP 2xx and webhook counts.

**Further study:** [Card payment lifecycle](../book/part-1/03-card-payment-lifecycle.md), [Checkout and payment state](../book/part-3/10-checkout-and-payment-state.md), [Three-party reconciliation](../book/part-4/16-three-way-reconciliation.md), and [Payment metrics](../book/part-4/16a-payment-metrics-and-observability.md).
