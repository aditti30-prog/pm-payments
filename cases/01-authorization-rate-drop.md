# Worked case — Authorization falls from 94% to 89%

**Scenario type:** Hypothetical teaching exercise. **No real company, merchant, PSP, issuer, or production incident is represented.**

## The brief

You own card acceptance for a regional ecommerce merchant. The dashboard shows that attempt-based authorization rate moved from **94% last week to 89% this week**. Traffic volume is unchanged, checkout session conversion also deteriorated, and operations reports more "payment failed" contacts.

A payments engineer points out that some cross-border traffic was recently moved to a different PSP route. Sales asks you to revert all routing immediately. Fraud asks you not to loosen risk controls. What do you do in the first 24–48 hours?

## The synthetic evidence

Source CSV: [`authorization_cohorts.csv`](data/authorization_cohorts.csv)

| Cohort | Previous attempts | Previous approved | Current attempts | Current approved | Route changed? |
| --- | ---: | ---: | ---: | ---: | --- |
| Domestic credit | 4,000 | 3,800 | 4,000 | 3,760 | No |
| Cross-border credit | 3,000 | 2,850 | 3,000 | 2,550 | Yes |
| Domestic debit | 2,000 | 1,860 | 2,000 | 1,830 | No |
| Cross-border debit | 1,000 | 890 | 1,000 | 760 | Yes |
| **Total** | **10,000** | **9,400** | **10,000** | **8,900** | — |

Calculate the overall rate as total approved / total attempts, **not the unweighted average** of cohort percentages. The prior rate is **94.0%** and the current rate is **89.0%**. Both are illustrative.

### First-pass diagnosis

The overall decrease is **500 additional unsuccessful attempts**, holding attempt volume constant. By cohort:

| Cohort | Approval rate before → after | Change in approved count |
| --- | --- | ---: |
| Domestic credit | 95.0% → 94.0% | −40 |
| Cross-border credit | 95.0% → 85.0% | −300 |
| Domestic debit | 93.0% → 91.5% | −30 |
| Cross-border debit | 89.0% → 76.0% | −130 |

The two cross-border cohorts account for **430 / 500 = 86% of the added unsuccessful attempts**. This is strong **prioritization evidence**, not proof that rerouting caused the change. Perhaps the issuer mix, ticket size, fraud rules, merchant data quality, 3DS behavior or traffic acquisition changed at the same time.

## Your response as the PM

### 1. Protect customers and correctness first

If the rise includes **timeouts or unknown outcomes**, validate that customers are not wrongly encouraged to retry potentially approved transactions. Monitor duplicate authorization/capture complaints and pending orders. Confirm the PSP and merchant have consistent status/reconciliation records.

### 2. Validate the metric

Check that both weeks count the same kinds of submitted card authorization attempts. Inspect event completeness, retries, late provider responses, traffic mix and data transformation changes. Distinguish issuer declines from technical errors and merchant risk rejections.

### 3. Prioritize the cross-border cohorts

Create a segment-level breakdown by issuer/BIN group, currency, geography, route, 3DS result, card type, app version, refusal category and transaction-time window. Check whether route changes affected all eligible traffic or only a selected cohort.

### 4. Make a decision based on reversibility and risk

For an active severe incident with a preapproved rollback mechanism, engineering and risk may support reverting affected traffic quickly. But an indiscriminate global revert can create new problems. If outcomes and guardrails permit, a controlled comparison within the eligible affected cohorts can test the route hypothesis.

### 5. Specify success correctly

Do not stop at a higher attempt approval percentage. Track:

- Unique orders paid successfully and the time taken to confirm them.
- Issuer/PSP decline reason mix and technical unknown states.
- Duplicate authorizations, capture/reconciliation exceptions and customer complaints.
- Fraud losses and dispute signals over a suitable time window.
- Processing costs per successful paid order and routing availability.

## Hypothesis register

| Hypothesis | Evidence to seek | What would challenge it? |
| --- | --- | --- |
| New PSP route lowered acceptance for cross-border traffic | Drop begins at route rollout; comparable eligible traffic performs better on old route | Similar declines on unchanged route or entirely explained by issuer mix |
| More 3DS challenge failures | Challenge rate or abandonment spikes in affected cohorts | Authentication completion stable and issuer post-auth declines drive the change |
| Credential or request-data regression | Changed tokens, expiry handling, merchant/issuer data, specific error codes | No correlation with credential version or request fields |

**Important:** A rollback may be justified by risk management before causality is proven. The incident decision and the longer-term product hypothesis test are not the same exercise.

## A practical 30-minute exercise

1. Calculate the percentage-point change in each cohort and the total. Which cohort contributes most to the overall decline in **absolute approved attempts**?
2. Write three questions you would ask the PSP and three you would ask your analytics/engineering team.
3. Pick one experiment or controlled operational comparison. Specify eligibility, randomization (if appropriate), a primary outcome, three guardrails and a rollback trigger.
4. Draft a five-sentence executive update that distinguishes **observed facts**, **hypotheses** and **actions**.
5. Explain why a return to 94% attempt approval would not automatically prove the customer or merchant business outcome recovered.

## Answer key: what good reasoning looks like

- **Arithmetic:** 94% → 89% is a **5-percentage-point** change, approximately **5.32% relative decline** in approval rate (`5/94`). Cross-border credit contributes 300 of the 500 fewer approvals, or 60%; both cross-border cohorts together contribute 86%.
- **Partner questions:** Which refusal categories changed? Did route/merchant configuration change? Can provider references be mapped to final issuer decisions and capture records?
- **Engineering questions:** Did event definitions change? Are timeouts being recorded as declines? Did any release change tokens, 3DS fields, retry behavior or request payloads?
- **Experiment:** Restrict to eligible cross-border traffic; compare confirmed unique-order success and relevant costs/risks with stable assignment; monitor unknown outcomes and duplicate charges, and review longer-horizon risk signals.
- **Communication:** State that a route change is a **lead hypothesis**, not a confirmed cause. A different PSP route may also change traffic selection, costs, fraud screening and reporting categories.

## Verify the arithmetic

Run from the repository root:

```bash
python3 scripts/verify_case.py
```

The script reads the linked CSV and prints the weighted rates, percentage-point changes, and decline contribution by cohort. No external dependency is required.

**Read next:** [Sample PRD — safe recovery from uncertain payment outcomes](../artifacts/sample-prd-payment-recovery.md).
