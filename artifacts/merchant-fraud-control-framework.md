
# Merchant fraud risk — customer, transaction and context worksheet

**Scope:** Merchant-side checkout, order and fulfilment fraud controls. Not issuer authorization/risk rules or a PSP's proprietary model. **Policy thresholds and regulated actions require Risk/Compliance approval.** The PM owns observable product behavior, integrated signals, checkout/recovery UX and measured trade-offs.

**Read:** [Chapter 13](../book/03-checkout-authorization-and-fraud/13-payment-fraud-and-risk-controls.md).

## 1. Threat and exposure

Name the **specific threat** before choosing a rule: stolen card, account takeover, card testing, voucher/rewards abuse, returns/refund abuse, fulfilment/delivery manipulation or first-party misuse. Do not equate these with 3DS abandonment, issuer declines, unknown PSP outcomes or authorized-transfer scams. Write who bears loss under the applicable merchant/provider contract and what customer rights remain.

## 2. Three-pillar signal matrix

| Pillar | Candidate merchant-side signals | False-positive challenge |
|---|---|---|
| **Customer behavior** | Account tenure, login/security events, change of device or delivery address, stored-credential changes, recent order and return history | New customer, family usage, travel, legitimate account recovery |
| **Transaction behavior** | Basket size versus baseline, repeated low-value attempts, distinct payment credentials, payment-retry velocity, high-resale item concentration, return/refund frequency | Processor outage, customer testing a valid alternate card, flash sale |
| **Transaction context** | Time, channel/device/app version, campaign, shipping/pickup/drop-off patterns, currency and issuer geography where legally available, PSP health | Late-night shopping, legitimate travel, campaigns and infrastructure incidents |

Every feature needs an approved source, grain (customer/order/attempt), event-time window, privacy purpose and retention, data-quality fallback, cohort baseline and owner. **No single geography, hour or new card is evidence of fraud.**

## 3. Risk decision record

| Field | Fill in |
|---|---|
| Risk policy and version | ___ |
| Threat hypothesis and source evidence | ___ |
| Relevant pillars and justified combinations | ___ |
| Eligible merchant segment and exclusions | ___ |
| Decision | Allow / eligible step-up / bounded manual review / hold fulfilment / risk-approved decline |
| Safety and customer path | Missing data, unknown payment state, safe messaging, appeals/recovery, review deadline |
| Financial and UX guardrails | Mature fraud loss, good paid orders, conversion, 3DS completion/latency, support contacts, false-positive proxies |
| Approvals | Risk, Payments PM, Engineering, Legal/Privacy/Compliance where needed |
| Rollout | Shadow test, approved limited launch, kill switch, owner and review date |
| Review maturity | Payment and dispute outcome window; label bias and holdout limitations |

## 4. Illustrative threat-to-action examples

- **Possible card testing:** Numerous distinct credentials plus repeated small authorization attempts and weak purchase intent may warrant approved rate limits and investigation. Verify the pattern is not repeated merchant technical retries during a PSP outage.
- **Possible account takeover:** Newly changed credentials/device plus unusually large resalable basket and unfamiliar delivery destination can trigger a reversible fulfilment hold and bounded review, not automatic permanent suspension.
- **Possible voucher abuse:** Abnormal redemption across linked orders can trigger promotion-eligibility investigation independently from card fraud rules.
- **Higher-risk first order:** A first-time cross-border buyer should not be universally blocked. Consider permitted authentication, cohort risk, margin and manual review capacity with a legitimate customer recovery path.

## 5. Test and measurement

Compare **loss prevented** with good orders lost, customer friction, review cost and later chargebacks—not fraud rate alone. Rejected transactions do not subsequently produce observed chargebacks, so a model trained only on approved orders has **selection bias**. Use appropriate risk-approved shadow scoring, appeals, mature loss labels and controlled tests. Distinguish merchant pre-PSP rejects from issuer authorization declines and 3DS failure.

**Practice:** A loyal customer changes password, device and shipping address, then orders high-priced electronics at 2 a.m. Meanwhile PSP timeouts spike. Classify every signal into one of the three pillars, separate merchant technical retries from genuine multiple-card testing, propose a safe reversible decision, and define falsification criteria.
