# 4. Payment economics: who earns, who pays, who bears risk?

**Part I — Understanding Payments** · Prerequisites: Chapters 1–3

## Learning outcomes

Explain the components of merchant payment cost, distinguish **MDR**, **interchange**, **network fees**, **processor fees**, and **take rate**, and calculate why a higher approval rate is not automatically a more profitable product.

## 4.1 Money movement is a business, not just infrastructure

Someone funds cardholder benefits, underwrites credit risk, maintains a network, builds a gateway, absorbs fraud exposure, handles disputes, and supplies merchant support. Commercial pricing reflects a mix of costs, risks, and bargaining power. The allocation differs by geography, merchant type, payment method, card product, and contract. No universal fixed fee table applies.

The **merchant discount rate (MDR)** is the fee a merchant pays to accept a card payment, typically stated as a percentage and sometimes a fixed fee. It may contain or be related to several components:

- **Interchange:** an amount associated with issuer/acquirer economics, under network and regional rules. It is *not* the same as the merchant's total fee.
- **Scheme/network assessment and processing fees:** may depend on network, transaction type, geography and services.
- **Acquirer/PSP/processor pricing:** includes their service margin, operations, fraud tooling, support or bundled features.
- **Other cost lines:** FX/cross-border charges, chargeback fees, payout fees, fraud losses, reserves, funding and working capital costs.

Two common pricing models are **blended** (one merchant-facing rate for a class of transactions) and **interchange++** (separate interchange, scheme fees, and markup). They change transparency and who absorbs variations in transaction mix.

## 4.2 Worked economics (illustrative, not market pricing)

A merchant processes **10,000 successful card transactions of S$50** each. This is **S$500,000 gross processed value**. Suppose the blended merchant fee is **2.5% + S$0.10** per transaction. The arithmetic is:

| Item | Calculation | Amount |
|---|---|---|
| Percentage charge | S$500,000 × 2.5% | S$12,500 |
| Fixed charge | 10,000 × S$0.10 | S$1,000 |
| Total merchant processing charge | Sum | **S$13,500** |
| Effective merchant fee | S$13,500 / S$500,000 | **2.7%** |

This is **merchant cost**, not the PSP's profit. To estimate PSP contribution, subtract the underlying network/interchange/acquiring costs, fraud/dispute losses and attributable variable operating costs; determine which party recognizes which revenue under the contract.

### Incremental approval is not free

Suppose a merchant has 100,000 legitimate card attempts, with approval improving from **90% to 92%** after a routing change. That's **2,000 additional approved attempts**, not automatically 2,000 additional completed orders. If each approved order has an average S$60 basket and 30% contribution margin *before incremental payment costs*, the theoretical maximum incremental contribution is **2,000 × S$60 × 30% = S$36,000**, assuming one additional converted order per approval and no later cancellations. If the change adds S$0.04 to *all* 100,000 attempts, that's S$4,000 of incremental attempt-level cost. You still must account for capture rate, duplicate attempts, fraud, refunds, adverse mix, and whether those attempts were actually eligible.

**PM mistake:** claiming "S$120K revenue recovered" while calling it profit and not accounting for provider fees or retries.

## 4.3 Take rate is a denominator choice

A PSP might report `net revenue / processed volume` as a take rate. Another business might report `gross payments revenue / total payment volume`, and a marketplace might use a separate commission take rate on **GMV**. Gross transaction value, net payment volume, merchant gross merchandise value and settled volume are not automatically the same.

Always label the numerator and denominator. To illustrate, **S$30,000 net payment revenue on S$2,000,000 processed volume = 1.5% net revenue take rate**. That cannot be compared directly with a marketplace's 15% merchandise commission without understanding the accounting model.

## 4.4 Merchant underwriting and reserves

The acquirer or payment facilitator can face exposure if a merchant receives payouts but later owes refunds or chargebacks, particularly for delayed delivery, travel, subscriptions or high-risk merchants. **Underwriting** evaluates the merchant's identity, business model, anticipated volume, ticket size, delivery delay, historical disputes, financial health and ability to meet future obligations. Controls might include rolling reserves, delayed payouts, caps, monitoring, guarantees, or suspension. These are **commercial risk tools**, not universally mandated deposits.

A PM designing merchant onboarding must balance conversion and time-to-first-payment with loss exposure and compliance. Asking for fewer documents can improve activation but may reduce the institution's ability to evaluate merchant risk. The right policy is segmented and reviewed by specialists.

## 4.5 Economics by product model

- **Issuing:** card programs may earn interchange-related revenue, fees or other income but incur processing, reward, funding, servicing and fraud costs. The exact economics depend on issuer relationships and regulation.
- **Acquiring:** value may come from processing margin, merchant services, value-added products and integrated distribution. Losses and reserves matter.
- **Gateway/orchestration:** pricing may be per transaction, tiered or bundled; multiple-provider coverage increases product value but also operational complexity.
- **Wallets:** closed-loop acceptance, stored balance, rewards and funding-source costs produce different unit economics from card acceptance.
- **Bank transfers:** often have different cost structures but introduce account validation, fraud/scam exposure, returns or payout tooling needs.

## 4.6 Product decisions grounded in economics
When evaluating "add another PSP," build a model with eligible volume by segment, expected approval uplift **at order level**, provider fixed/variable cost, engineering integration cost, reconciliation cost, operational complexity, and projected risk. Calculate both base case and downside. A more robust system is not automatically cheaper; the resilience benefit may justify some cost even without an immediate uplift.

## Check your understanding

1. Why isn't 2.5% MDR the same thing as 2.5% PSP margin?
2. Compute the effective merchant fee for 1,000 S$20 transactions at 2.0% + S$0.15.
3. How can a payment product increase GMV while reducing contribution margin?
4. What data would you request before setting payout delays for a newly onboarded merchant?

**Next:** [5. Merchant acquiring](../part-2/05-merchant-acquiring.md).

## Further reading

- [Visa — Interchange overview and regional documentation](https://www.visa.com/)
- [Adyen — Payments lifecycle and reconciliation](https://docs.adyen.com/reporting/reports-and-the-payments-lifecycle)
