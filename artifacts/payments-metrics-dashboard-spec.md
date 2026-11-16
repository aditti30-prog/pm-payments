# Artifact — Payments Metrics & Observability Dashboard Specification

**Status:** Adaptable teaching artifact · **Owner:** Payments PM (fictional HarborCart) · **Reviewers:** Data/analytics, payments engineering, fraud/risk, finance/reconciliation, provider operations  
**Last reviewed:** 16 November 2026 · Companion: [Chapter 16A](../book/part-4/16a-payment-metrics-and-observability.md)

## Problem and user

Leadership sees conflicting “payment success” numbers in checkout analytics and PSP reporting. Support cannot explain whether a timeout eventually succeeded; finance only sees variances after settlement. Build one metric contract and related views that maintain **distinct grains** rather than forcing a single blended success number.

**Users:** Payments PM for product decisions; engineering/SRE for incidents; finance for financial integrity; risk for lagged loss feedback. Each view may have different access permissions and freshness requirements.

## Metric dictionary — define these before writing SQL

| Metric ID | Population and formula | Event clock | Owner | Decision enabled |
| --- | --- | --- | --- | --- |
| `checkout_paid_rate_v1` | Distinct eligible checkout sessions with paid order / distinct eligible checkout sessions; fixed 24h conversion window | Checkout start cohort | Product analytics | Checkout changes |
| `payment_order_success_v1` | Distinct orders initiating payment and confirmed paid within 24h / orders initiating payment | Initiation cohort | Payments PM | Recovery/failed-payment UX |
| `auth_attempt_approval_v1` | Eligible approved auth attempts / submitted eligible auth attempts; exclude pre-PSP invalid request and test activity, report excluded volumes separately | Submission UTC | PSP analytics | Authorization diagnostics |
| `unknown_15m_v1` | Unknown payment operations still unresolved after 15m / operations entering unknown state | First unknown event timestamp | SRE/payments ops | Pending-state escalation |
| `payment_cost_per_paid_order_v1` | Cohort-attributable processing fees / distinct confirmed paid orders | Cohort with finance allocation | Finance | Routing and provider economics |
| `recon_unexplained_value_v1` | Signed absolute unexplained variance after cutoff by legal entity and currency | Settlement/payout value date | Finance | Exception management |
| `fraud_loss_bps_v1` | Confirmed fraud loss amount / captured sales amount on aligned mature cohort × 10,000 | Mature transaction cohort | Fraud/risk | Risk-adjusted product decisions |

**Non-negotiable dimensional filters:** market, legal entity, payment rail/method, channel, PSP/acquirer route, card-brand and issuing-country cohorts where permitted, token type, 3DS status, merchant type, currency, product version, control/treatment assignment, and timestamps. Aggregate securely; do not expose PAN/CVV or secrets.

## Data contracts

- **Order table**: `order_id`, `checkout_session_id`, `merchant_id`, `market`, `payment_started_at`, `paid_at`, `order_status`.
- **Payment operation**: `payment_operation_id`, `order_id`, `status`, `first_attempt_at`, `final_status_at`, `idempotency_scope`.
- **Attempt**: `attempt_id`, `payment_operation_id`, `psp_id`, `psp_payment_id`, `submitted_at`, `response_at`, `response_category`, `approved_bool`, `provider_result_code`.
- **Financial events**: `financial_event_id`, `capture_id` or `refund_id`, `settlement_line_id`, `payout_id`, `legal_entity`, `currency`, `signed_minor_units`, `value_date`.
- **Risk/dispute**: `dispute_id`, `payment_operation_id`, `label_finalized_at`, `loss_minor_units`, `case_status`.

**Join rule:** attempt-level data joins upward to payment operation and order before counting distinct orders. Never count retries as new orders. Financial data joins on stable provider/capture/settlement references, not amount plus time alone.

## Dashboard layout

1. **Outcome strip:** eligible checkout sessions, paid orders, payment-start success, attempt approval, cost per paid order, confirmed duplicate capture count (each with denominator and freshness tooltip).
2. **Funnel:** checkout → payment initiated → authentication → authorization → capture → paid order; stage and time basis labelled, and alternate-rail events handled separately.
3. **Diagnostic drill-down:** decline taxonomy by issuer/country/PSP, trend baseline, traffic mix, first attempt vs retries, recent release annotations.
4. **Reliability:** request latency p50/p95/p99, timeouts, webhook lag, unknown >15m, recovery time, incident markers.
5. **Financial integrity:** captured vs settled signed amounts; payout-bank match; aged unexplained variance by entity and currency; reserve/fee bridge.
6. **Control view:** fraud/dispute outcomes only for mature cohorts; exposure to false-positive controls; risk sign-off for experiments.

## Worked fictional acceptance tests

- **AT1:** 100,000 eligible sessions and 72,000 paid session results show exactly **72%**, with the eligible population visible.
- **AT2:** 82,000 eligible attempts and 73,800 approvals show **90%** regardless of how many orders those attempts belong to.
- **AT3:** A missing PSP response classified as `OUTCOME_UNKNOWN` is **not** counted as an issuer decline; it enters the unresolved queue.
- **AT4:** A webhook delivered twice produces one authoritative event processing effect; events are not assumed ordered.
- **AT5:** Paid-order counts never increase when a duplicate capture occurs for an already paid order; financial-integrity monitoring records the duplicate.
- **AT6:** Unsettled authorizations are absent from the settlement/payout gross-to-net bridge.
- **AT7:** Risk dashboard does not compare this week's captured volume with last quarter's finally labeled fraud loss without a maturity warning.
- **AT8:** Every displayed percentage has a populated definition link, time window, last updated timestamp and responsible team.

## Sample diagnostic SQL sketch (not deployable without schema mapping)

```sql-- First establish a de-duplicated eligible authorization-attempt cohort.
-- Do not use this result as unique-order success.
SELECT
  DATE(submitted_at) AS auth_date_utc,
  market,
  psp_id,
  COUNT(DISTINCT attempt_id) AS eligible_attempts,
  COUNT(DISTINCT CASE WHEN approved_bool THEN attempt_id END) AS approved_attempts
FROM payment_attempts
WHERE eligible_for_auth_rate = TRUE
  AND is_test = FALSE
GROUP BY 1, 2, 3;
```

**Alerting contract:** link each actionable alert to a runbook (Chapter 17), explicit severity rules, on-call owner, suppression/data-quality checks, and protected financial actions. Threshold values are business decisions, not generic industry defaults.

## Rollout and ownership

Phase 1: dictionary + batch validation against PSP and finance exports. Phase 2: segment drilldown and read-only dashboards. Phase 3: alerting only for actionable unresolved outcomes and financial-integrity problems. Hold a weekly discrepancy review with sign-off from PM, data and finance.

**Known limitations:** Provider taxonomies and network/scheme monitoring definitions vary; payment methods have different state clocks; refunds/chargebacks arrive with lag. This artifact deliberately does not pretend to be a universal provider dashboard.
