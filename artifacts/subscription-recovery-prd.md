# Example PRD — Subscription collection recovery and truthful entitlements

**Status:** Fictional teaching PRD, v0.5 · **PM:** Recurring Payments · **Stakeholders:** Billing, Payments, Subscription Service, Support, Finance, Risk, Compliance and PSP Partner · **Date:** 16 November 2026.

## Problem

Billing teams collapse failed collection into `cancel_subscription`. Some card attempts fail transiently or require a customer action, while others time out but are actually authorized. Customers sometimes lose service despite payment, and careless retry logic risks duplicate charges.

## Goal and non-goals

Improve **matured paid-invoice rate** within approved retry rules and reduce unnecessary involuntary churn, without increasing fraud, duplicate captures, unpermitted retries or customer confusion. Non-goals: force issuer approvals, bypass applicable SCA, or keep entitlements forever without payment.

## Actors and canonical entities

`subscription_id`, `billing_cycle_id`, `invoice_id`, `payment_operation_id`, provider attempt ID, saved credential reference, customer permission, entitlement state, refund ID, and support case. A subscription has multiple invoices; an invoice can have multiple eligible attempts but must not be paid twice without an owned adjustment process.

## Functional requirements

| ID | Requirement | Acceptance check |
|---|---|---|
| R1 | Make invoice status independent of subscription entitlement | `invoice_pending`, `invoice_paid`, `invoice_uncollectible` can coexist with controlled grace period |
| R2 | Classify failed versus ambiguous payments | Timeout produces `outcome_unknown`; no immediate blind resubmission |
| R3 | Enforce retry eligibility based on current PSP/scheme rules | No retry on prohibited categories or beyond approved caps |
| R4 | Preserve idempotent operation references | Duplicate scheduler events do not create duplicate money movement |
| R5 | Notify customer respectfully | Clear failure, update-card and grace-period options without exposing issuer-sensitive detail |
| R6 | Track card renewal/token updates | Credential lifecycle is distinct from customer mandate and permission |
| R7 | Reconcile late PSP success to invoice and entitlement | One paid invoice and correct service restoration, no duplicate fulfillment |
| R8 | Permit safe cancellation and customer support | No hidden billing continuation after permitted cancellation |

## Example policy (hypothetical, not scheme defaults)

For eligible transient declines only: attempt up to two additional attempts over seven days, subject to actual issuer/PSP constraints, user disclosure, risk approval, and dynamic adjustment based on outcomes. Never blindly retry an unknown outcome; never retry a definitive prohibited response; request customer action when authentication is required. Test with holdout before making production claims about recovery uplift.

## Instrumentation

Record invoice due cohort/date, `attempt_no`, reason-class, provider result, final invoice/payment state, notification event, customer update event, entitlement restoration/cancellation, support case and eventual loss. Measure recovered *invoices*, not merely recovered attempts. Guardrails: attempts per invoice, disputed charges, complaints, incremental processing costs and access errors.

## Test matrix

- Timeout after issuer approval, callback late: same invoice paid once; no second capture.
- Hard decline: no automated retry outside approved policy.
- Updated card while a scheduled retry is pending: cancel/supersede stale retry, use current permission.
- Subscription cancelled during grace: no later unauthorized collection.
- Partial credit note: updated invoice amount and correct finance postings.
- End-of-month and timezone boundary: no duplicate invoice issue.

## PM launch plan

Shadow-mode cohort classification → test-only end-to-end retries and reconciliation → risk/legal-approved limited traffic → measure matured collection, invoice integrity and support contacts → rollback on fraud or duplicate-charge breaches.

**Reference:** [Chapter 10A](../book/part-3/10a-subscriptions-stored-credentials-and-dunning.md). [Adyen stored credentials](https://docs.adyen.com/online-payments/tokenization/make-token-payments).
