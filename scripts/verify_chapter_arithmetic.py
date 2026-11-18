#!/usr/bin/env python3
"""Recompute the worked numbers printed in chapters and answer keys.

Each case lists a phrase that must appear in the named file (as a whole token, see
_match.present) AND an independent recomputation, so editing either the prose or the
math breaks CI. Phrases are long enough to be unique: a bare '75%' would be satisfied
by an unrelated 75% elsewhere in the file.
Arithmetic only: says nothing about whether a rule, fee or process is real."""
import sys
from pathlib import Path

from _match import present

ROOT = Path(__file__).resolve().parents[1]
B = "book/"
KEY = "answers/chapter-exercises.md"
CASES = [
    # (file, phrases that must appear, claim, computed value, expected value)
    (B + "03-checkout-authorization-and-fraud/11-3d-secure-and-customer-authentication.md",
     ["9,600 initiate 3DS → 6,500 frictionless, 3,100 challenged → 2,325 challenges completed (75%) → 8,825 authenticated outcomes"],
     "3DS funnel: frictionless + completed challenges", 6500 + round(3100 * 0.75), 8825),
    (B + "04-disputes-reconciliation-and-operations/16-payment-reconciliation-and-payouts.md",
     ["Provider payout S$8,750", "S$500 refunds, S$200 dispute debit, S$250 fees, and S$300 reserve"],
     "payout bridge: 10,000 - refunds - dispute - fees - reserve", 10000 - 500 - 200 - 250 - 300, 8750),
    (B + "03-checkout-authorization-and-fraud/10a-subscriptions-recurring-payments-and-dunning.md",
     ["900 invoices are paid, 60 decline with final results, and 40 remain temporarily unresolved"],
     "dunning cohort adds to 1,000 invoices", 900 + 60 + 40, 1000),
    (B + "04-disputes-reconciliation-and-operations/16a-payment-performance-metrics-and-dashboards.md",
     ["S$3,600 / S$3,600,000 = 0.10% = 10 bps"],
     "fraud loss bps", round(3600 / 3_600_000 * 10_000), 10),
    (B + "02-payment-products-and-infrastructure/05a-marketplaces-payfacs-and-funds-flow.md",
     ["Buyer pays S$100; platform fee S$10; processing cost S$2; seller entitlement S$88"],
     "seller entitlement = 100 - 10 fee - 2 processing", 100 - 10 - 2, 88),
    (B + "02-payment-products-and-infrastructure/08a-in-store-pos-contactless-and-offline.md",
     ["80 attempted S$30 card transactions", "S$2,400"],
     "offline outage sales at risk", 80 * 30, 2400),
    (KEY, ["Total **S$550**, equivalent to **2.75%** of S$20,000 and **S$0.55 per transaction**"],
     "ch4 fee: 2% of 20,000 + 1,000 x 0.15", 2 * 20000 // 100 + 1000 * 15 // 100, 550),
    (KEY, ["0.85 × 8 − 1.50 = S$5.30"],
     "ch6 expected contribution A (cents)", round((0.85 * 8 - 1.50) * 100), 530),
    (KEY, ["0.93 × 8 − 1.80 = S$5.64"],
     "ch6 expected contribution B (cents)", round((0.93 * 8 - 1.80) * 100), 564),
    (KEY, ["New pre-tender payable = 48 − 10 = **S$38**"],
     "ch10 new payable: (60 - 12) - 10 coupon", (60 - 12) - 10, 38),
    (KEY, ["5 points + S$33 card"],
     "ch10 new card amount: 38 payable - 5 points", 38 - 5, 33),
    (KEY, ["(80 + 10)/(100 + 20) = 75%"],
     "ch12 attempt approval (percent)", 100 * (80 + 10) // (100 + 20), 75),
    (KEY, ["unique paid-order success improves from 80% to 90%"],
     "ch12 paid-order success (percent)", 100 * (80 + 10) // 100, 90),
]


def main():
    bad = 0
    for rel, phrases, claim, got, want in CASES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for p in phrases:
            if not present(text, p):
                print(f"MISSING in {rel}: {p!r} ({claim})")
                bad += 1
        if got != want:
            print(f"WRONG MATH ({claim}): computed {got}, expected {want}")
            bad += 1
    if bad:
        sys.exit(f"FAIL: {bad} chapter arithmetic problem(s)")
    print(f"OK: {len(CASES)} worked chapter calculations recomputed and bound to chapter text")


if __name__ == "__main__":
    main()
