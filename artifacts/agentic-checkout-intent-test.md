# Agentic Checkout Intent & Permission Test — template and worked example

**Audience:** Payments PM, commerce PM, agent developer, risk and merchant operations. **Status:** Educational design artifact (16 November 2026), not an AP2, UCP, ACP, Visa or Mastercard certified implementation.

## 1. Test contract

The test system receives **an explicit customer instruction** plus a **merchant-produced checkout**. It evaluates a small set of hard constraints before allowing a payment attempt. Agent-generated natural language descriptions are not enough to establish authority; the final order must be checked against canonical merchant records, independently of what an LLM says it intended.

| Field | Example | Evidence/owner |
|---|---|---|
| `intent_id` | `INT-1001` | Trusted consent system |
| `user_id` / authenticated principal | `USR-100` | Identity provider; never PAN |
| Allowed seller | `merchant_id=HARBOR-1` | Merchant directory and user approval |
| Exact line item | `SKU-OAT-A-500`, quantity `2` | Merchant catalog and approved constraints |
| Substitution allowed | `false` | User consent |
| Maximum total | `SGD 24.00`, inclusive of shipping and tax | User consent, merchant total calculation |
| Delivery | `2026-11-17` | Merchant delivery capacity, timezone |
| Expiry | `2026-11-16T05:00:00Z` | Trusted consent service |
| Payment instrument | Scoped token reference, not raw PAN | Token/credential provider |
| Checkout version | Immutable hash or version ID | Merchant |
| Operation ID | `OP-1001` | Merchant/PSP idempotency scope |

**Non-goal:** The example does not create cryptographic mandates or issue payment credentials. It models pre-payment *intent preservation*. For real integrations, verify current protocol-specific signatures, lifecycle, challenge handling, and legal requirements.

## 2. Required deterministic checks

1. Check the consumer-approved merchant, item/variant, quantity and explicit substitution policy.
2. Check **total payable including fees/tax/shipping** in the approved currency; distinguish quote from final checkout.
3. Check delivery location and deadline; a cheaper item arriving later may still violate consent.
4. Check whether permission is expired, revoked or already consumed under its actual protocol/provider semantics.
5. Use one durable operation ID; a retried network call should not create another commercial payment intent.
6. After permission is validated, **separately** check the credential/provider/issuer outcome, merchant order state and aftercare.

## 3. Worked scenarios (HarborCart, fictional)

| Scenario | Cart total | Key change | Expected result |
|---|---:|---|---|
| Approved | S$22 | Exact SKU, qty 2, next-day | Permit *payment attempt*, not automatic payment success |
| Substitution | S$21 | Brand B SKU | Block: substitution forbidden |
| Overspend | S$26 | Shipping rises | Block: amount cap |
| Changed quantity | S$31 | Qty 3 | Block: item/quantity and amount |
| Delayed delivery | S$22 | Delivery two days later | Block: delivery condition |
| Merchant changed | S$22 | Different seller | Block: merchant scope |
| Expired consent | S$22 | Execution after expiry | Block: validity window |
| Payment unknown | S$22 | Valid intent; processor status unknown | Customer sees `PENDING`, no duplicate payment or confirmed order |

The [machine-readable scenario fixtures](../cases/data/agentic-intent-scenarios.json) and [verification script](../scripts/verify_agentic_cases.py) implement a **minimal toy policy**, sufficient to prevent accidental regression in these examples but not suitable for financial production.

## 4. Evidence and privacy checklist

Store: authorized customer principal reference, consent timestamp and trusted surface, consent version/expiry, approved constraints, merchant checkout hash/version, decision and rejection reason, scoped credential reference (never raw PAN), PSP attempt IDs, authorized/unknown/declined result, merchant order ID and refunds/dispute correlation IDs. Set lawful retention and access policies; redact sensitive data from analytic events and model prompts. Do not log private keys or full signed payment credential payloads in ordinary telemetry.

## 5. Payments PM acceptance criteria

- No restricted cart modification is silently accepted (tests for substitutions, amount, merchant, expiration, delivery).
- All duplicate requests reconcile to a known operation; no duplicate capture after timeout.
- A credential issuance response cannot advance an order to `PAID`.
- An issuer-approved payment without confirmed order is visible as an exception, not silently dropped.
- Customer can see what was approved and access merchant order/refund/support information.
- Risk, compliance, merchant operations and finance explicitly sign off on the launch scope.

**Related:** [Chapter 20](../book/05-new-and-emerging-payments/20-agentic-commerce-and-ai-payments.md) · [Checkout state](../book/03-checkout-authorization-and-fraud/10-checkout-and-payment-status-design.md) · [AP2 v0.2 reference](https://github.com/google-agentic-commerce/AP2/blob/main/docs/ap2/specification.md).
