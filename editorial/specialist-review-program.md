# Independent specialist review program

**Review status, 16 November 2026: NOT STARTED.** Automated checks, author/editor desk review and public documentation review **do not count as an independent specialist review**. No reviewer name, credential or sign-off should be listed until a real reviewer has examined the exact commit and approved the stated scope. Ask reviewers before public attribution.

**Submit a review:** Use the [technical review issue form](https://github.com/aditti30-prog/pm-payments/issues/new?template=technical-review.yml) or provide a review against the exact commit SHA. The form collects the affected claim, counterexample, source date/version, severity and suggested correction; filing an issue is **not** an approval.

## How to review a chapter

1. Select a chapter, specific repo commit SHA, jurisdiction/rail and your competence area. State potential conflicts and whether you can review public material.
2. Validate **actors and accountabilities** (issuer, acquirer, PSP, merchant, risk/finance, regulator); **transaction state** (auth vs capture vs financial settlement vs payout); and **money and liability** (fees, reserves, losses, disputes).
3. Reproduce at least one worked calculation or event sequence. Look for mismatched denominators, missing IDs, impossible state transitions, sign errors or misplaced funds custody.
4. Check at least three claims against *dated primary sources* and identify where the claim must be qualified by scheme, country, program, contract or technical version.
5. Assess whether a PM can turn the chapter into a testable artifact: API behavior, exception workflow, RACI, metrics/guardrails, decision approval and rollback.
6. Submit comments as `file:line — issue — proposed wording — supporting source — severity`. Do not send PANs, customer/merchant details, internal partner credentials, proprietary scheme rules or confidential employer materials.
7. After corrections are merged, review the updated commit and mark **Approved / Approved with remaining caveats / Needs revision**. Record the review date and approved chapter revision.

## Review lanes and unresolved questions

For the specific claims to attack in each lane, with line locations and the source to check against, use the [specialist review packet](specialist-review-packet.md).

| Lane | Chapters to prioritize | Questions the reviewer should answer | Status |
|---|---|---|---|
| Card issuance, EMV tokenization | 7, 7A, 8A, 11 | Are FPAN/DPAN/device vs merchant token domains described accurately? What differs by issuer/TSP? Are cryptograms and 3DS/authorization correctly separated? | **Unassigned** |
| Acquiring, gateway and merchant risk | 4–6, 5A, 13A | Are acquirer/PayFac/MoR roles and contract liabilities accurate? Does payout reserve/negative balance logic reconcile? Is PCI responsibility overstated? | **Unassigned** |
| Disputes and fraud policy | 11, 13, 13B, 15 | Are chargeback status, deadlines, fraud-vs-scam distinctions, evidence and network-monitoring examples properly scoped and dated? | **Unassigned** |
| Payments finance, treasury and reconciliation | 3, 9A, 16, 16A, 17 | Is the accounting bridge correct across payouts, refunds, reserves, FX, timing and bank confirmations? Are multi-currency IDs and cutoff dates explicit? | **Unassigned** |
| Real-time/open banking and stablecoins | 9, 18, 19 | Are finality, refund/return, custody, redemption and regulatory controls described without universal assumptions? | **Unassigned** |
| Agentic-commerce architecture/security | 20 | Does protocol revision match current docs? Is signed merchant checkout, delegated consent, credential binding and payment-state recovery accurately separated? | **Unassigned** |

## Review record template

```text
Review ID:
Reviewer (display name by permission only):
Reviewer's relevant role/experience (optional):
Chapter(s) and Git commit SHA:
Geography / rail / provider scope:
Review date (UTC):
Primary sources verified, versions and dates:
Worked calculation or sequence replicated:
Critical issues resolved (linked commit/PR):
Remaining caveats or out-of-scope topics:
Decision: Approved / Approved with caveats / Needs revision
Permission granted to acknowledge publicly: yes / no
```

## Severity rubric

- **Blocker:** Might cause a reader to duplicate money movement, misstate regulatory/PCI duty, violate customer consent, misunderstand fraud liability or produce incorrect books.
- **Major:** Material actor, state, denominator, timing or funds-flow ambiguity; false universal claim; obsolete requirement presented as current.
- **Minor:** Poor explanation, missing reference, unclear diagram, case lacks assumption or intermediate calculation.
- **Editorial:** Grammar, navigation, formatting or repeated content without technical consequence.

**Release policy:** a working draft may be merged with clearly labeled unreviewed content; do **not** market the book as specialist-reviewed or production-authoritative until relevant lanes have accepted records. Critical findings require correction and retest before claiming the affected chapter is ready.
