#!/usr/bin/env python3
"""Recompute the synthetic authorization-case numbers using only stdlib."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "cases" / "data" / "authorization_cohorts.csv"

with DATA.open(newline="", encoding="utf-8") as stream:
    rows = list(csv.DictReader(stream))

assert rows, "Expected synthetic cohort data"
for row in rows:
    for field in ("baseline_attempts", "baseline_approved", "current_attempts", "current_approved"):
        row[field] = int(row[field])
    assert 0 <= row["baseline_approved"] <= row["baseline_attempts"]
    assert 0 <= row["current_approved"] <= row["current_attempts"]

old_attempts = sum(r["baseline_attempts"] for r in rows)
new_attempts = sum(r["current_attempts"] for r in rows)
old_approved = sum(r["baseline_approved"] for r in rows)
new_approved = sum(r["current_approved"] for r in rows)
old_rate = 100 * old_approved / old_attempts
new_rate = 100 * new_approved / new_attempts
additional_unsuccessful = (new_attempts - new_approved) - (old_attempts - old_approved)

print(f"Previous: {old_approved:,}/{old_attempts:,} = {old_rate:.1f}%")
print(f"Current:  {new_approved:,}/{new_attempts:,} = {new_rate:.1f}%")
print(f"Change:   {new_rate - old_rate:+.1f} percentage points")
print(f"Additional unsuccessful attempts: {additional_unsuccessful:,}")
print("Cohort differences:")
for r in rows:
    delta = r["current_approved"] - r["baseline_approved"]
    print(f"  {r['cohort']}: {delta:+,} approvals")

cross_border_fewer = sum(
    r["baseline_approved"] - r["current_approved"]
    for r in rows if r["cohort"].startswith("Cross-border")
)
if additional_unsuccessful:
    print(f"Cross-border contribution: {cross_border_fewer:,}/{additional_unsuccessful:,} = {100 * cross_border_fewer / additional_unsuccessful:.1f}%")

assert (old_attempts, old_approved, new_attempts, new_approved) == (10000, 9400, 10000, 8900)
assert additional_unsuccessful == 500
assert cross_border_fewer == 430
