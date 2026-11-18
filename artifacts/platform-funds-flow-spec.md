# Platform Funds-Flow Specification — worked template

**System:** Fictional two-sided marketplace (not advice on legal status). **Owner:** Platform Payments PM. **Reviewed with:** Acquirer/PSP, finance, treasury, merchant operations, risk, compliance and legal. **Version:** Sample, 16 November 2026.

## 1. Commercial and licensing boundary

Before requesting any split API, document: contracting MoR, acquirer, PayFac (if applicable), sub-merchant, provider contract, permitted fund custody, beneficiary ownership, underwriting, KYB and sanctions controls. A platform that merely displays seller balances might still have legal obligations; specialist review is required.

## 2. Example allocation and accounting (fictional)

Buyer charge S$100; seller gross entitlement S$90 after 10% platform fee; platform absorbs processing cost S$2, leaving platform net fee proceeds S$8. **Reconcile:** `buyer amount 100 = seller payable 90 + platform gross fee 10`. And `platform net fee 8 = platform fee 10 - processing cost 2`. The S$2 is **an expense** of the platform, not an additional component added to the buyer's S$100.

| Step | Primary ID | Authoritative source | Required status | Exception |
|---|---|---|---|---|
| Customer charge | order ID, payment ID | Merchant + PSP | Captured and eligible | Unknown/duplicate |
| Settlement booking | settlement batch ID | PSP/acquirer report | Booked, not necessarily bank paid | Missing net item |
| Seller payable | seller ID, seller split ID | Platform finance ledger | S$90 obligation | Negative balance/hold |
| Platform fee | commission ID | Platform revenue ledger | S$10 gross | Commission misallocation |
| PSP expense | provider fee ID | PSP report and platform ledger | S$2 cost | Fee mismatch |
| Seller payout | payout operation ID | PSP/provider and bank | Bank-credited where confirmed | Rejection/return |

## 3. Operations that must balance

A partial refund can reverse seller payable, commission and/or fees according to contract. A chargeback may debit the platform before the seller is debited. A negative balance may persist after payout. A reserve is not revenue. **Every transfer must have an owner, reason, effective date, currency and reference.**

## 4. Example acceptance criteria

1. The sum of allocated amounts equals the captured amount under defined accounting treatment.
2. Unsupported or absent split instructions fail safely rather than booking unknown amounts silently.
3. Duplicate callbacks do not cause duplicate seller payable or payout operations.
4. All external payouts are matched to bank credit or a named, owned exception.
5. Negative balances, holds, reserves and chargebacks remain visible and auditable.
6. Refunds are reconciled to the original order and settlement event, including partially delivered orders.

## 5. Metrics and decision questions

Follow seller time to first paid order, payout-on-time rate, payout rejection/return by bank, seller-negative-balance exposure, disputed sales, fee variance and unexplained money. **PM decision:** Should a high-risk new seller be paid daily? Require underwriting/risk thresholds and customer/seller impact assessment; don't make it solely a UX preference.

**See:** [Chapter 5A](../book/02-payment-products-and-infrastructure/05a-marketplaces-payfacs-and-funds-flow.md) and [three-party recon](../book/04-disputes-reconciliation-and-operations/16-payment-reconciliation-and-payouts.md). [Adyen split documentation](https://docs.adyen.com/platforms/online-payments/split-transactions).
