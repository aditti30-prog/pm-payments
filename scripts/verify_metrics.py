#!/usr/bin/env python3
"""Verify the fictional HarborCart metrics case; not a production KPI calculator."""
from pathlib import Path
import csv
from decimal import Decimal

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / 'cases/data/harborcart-metrics.csv').open(newline='') as f:
    cohorts = list(csv.DictReader(f))
assert {r['cohort'] for r in cohorts} == {'domestic', 'cross_border'}
submitted = sum(int(r['eligible_authorization_attempts']) for r in cohorts)
approved = sum(int(r['approved_authorization_attempts']) for r in cohorts)
assert (submitted, approved) == (82_000, 73_800)
assert Decimal(approved) / submitted == Decimal('0.9')
assert Decimal('72000') / Decimal('100000') == Decimal('0.72')
assert Decimal('72000') / Decimal('80000') == Decimal('0.9')
assert Decimal('70560') / Decimal('72000') == Decimal('0.98')
assert Decimal('3600') / Decimal('3600000') == Decimal('0.001')
assert Decimal(16800) / Decimal(20000) == Decimal('0.84')
assert round(Decimal(57000) / Decimal(62000) * 100, 2) == Decimal('91.94')
assert 73_800 <= 82_000 and 72_000 <= 80_000
print('OK: HarborCart synthetic metrics, cohort rollup, cost and fraud arithmetic')
