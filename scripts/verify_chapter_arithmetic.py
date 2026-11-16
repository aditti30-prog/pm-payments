#!/usr/bin/env python3
"""Recompute the worked numbers printed in chapters and answer keys.

Each case lists literals that must appear in the named file AND an independent
recomputation, so editing either the prose or the math breaks CI.
Arithmetic only: says nothing about whether a rule, fee or process is real."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
B = "book/"
CASES = [
    # (file, literals that must appear, claim, computed value, expected value)
    (B + "part-3/11-3d-secure.md", ["9,600", "6,500", "3,100", "2,325", "8,825"],
     "3DS funnel: frictionless + completed challenges", 6500 + round(3100 * 0.75), 8825),
    (B + "part-4/16-three-way-reconciliation.md", ["S$8,750", "S$500", "S$200", "S$250", "S$300"],
     "payout bridge: 10,000 - refunds - dispute - fees - reserve", 10000 - 500 - 200 - 250 - 300, 8750),
    (B + "part-3/10a-subscriptions-stored-credentials-and-dunning.md", ["900", "60", "40"],
     "dunning cohort adds to 1,000 invoices", 900 + 60 + 40, 1000),
    (B + "part-4/16a-payment-metrics-and-observability.md", ["S$3,600", "S$3,600,000", "10 bps"],
     "fraud loss bps", round(3600 / 3_600_000 * 10_000), 10),
    (B + "part-2/05a-marketplaces-payfac-funds-flow.md", ["S$100", "S$88"],
     "seller entitlement = 100 - 10 fee - 2 processing", 100 - 10 - 2, 88),
    (B + "part-2/08a-card-present-pos-and-offline.md", ["80 attempted S$30", "S$2,400"],
     "offline outage sales at risk", 80 * 30, 2400),
    ("answers/chapter-exercises.md", ["S$550", "2.75%", "S$0.55"],
     "ch4 fee: 2% of 20,000 + 1,000 x 0.15", 2 * 20000 // 100 + 1000 * 15 // 100, 550),
    ("answers/chapter-exercises.md", ["S$5.30", "S$5.64"],
     "ch6 expected contribution A (cents)", round((0.85 * 8 - 1.50) * 100), 530),
    ("answers/chapter-exercises.md", ["S$5.30", "S$5.64"],
     "ch6 expected contribution B (cents)", round((0.93 * 8 - 1.80) * 100), 564),
    ("answers/chapter-exercises.md", ["S$33", "S$38", "S$45"],
     "ch10 new card amount: (60-12) - 10 - 5 points", (60 - 12) - 10 - 5, 33),
    ("answers/chapter-exercises.md", ["75%", "90%"],
     "ch12 attempt vs order success (percent)", 100 * (80 + 10) // (100 + 20), 75),
]


def main():
    bad = 0
    for rel, needles, claim, got, want in CASES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for n in needles:
            if n not in text:
                print(f"MISSING in {rel}: {n!r} ({claim})")
                bad += 1
        if got != want:
            print(f"WRONG MATH ({claim}): computed {got}, expected {want}")
            bad += 1
    if bad:
        sys.exit(f"FAIL: {bad} chapter arithmetic problem(s)")
    print(f"OK: {len(CASES)} worked chapter calculations recomputed and bound to chapter text")


if __name__ == "__main__":
    main()
