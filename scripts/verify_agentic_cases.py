#!/usr/bin/env python3
"""Toy deterministic consent-policy examples. Not AP2/ACP/UCP implementation or security verification."""
from datetime import datetime, timezone
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'cases/data/agentic-intent-scenarios.json').read_text())
assert DATA['fictional'] is True

def utc(s):
    dt = datetime.fromisoformat(s.replace('Z', '+00:00'))
    assert dt.tzinfo is not None
    return dt.astimezone(timezone.utc)

def check(intent, candidate):
    errors = []
    if candidate['merchant'] != intent['merchant']:
        errors.append('merchant_mismatch')
    if candidate['sku'] != intent['sku'] and not intent['substitution_allowed']:
        errors.append('sku_mismatch')
    if candidate['quantity'] != intent['quantity']:
        errors.append('quantity_mismatch')
    if candidate['currency'] != intent['currency']:
        errors.append('currency_mismatch')
    if candidate['total_minor'] > intent['max_total_minor']:
        errors.append('amount_over_cap')
    if candidate['delivery_date'] != intent['delivery_date']:
        errors.append('delivery_mismatch')
    if utc(candidate['evaluated_at']) > utc(intent['expires_at']):
        errors.append('permission_expired')
    return errors

for scenario in DATA['scenarios']:
    actual = check(DATA['intent'], scenario)
    assert actual == scenario['expected'], f"{scenario['id']}: {actual} != {scenario['expected']}"
print(f"OK: {len(DATA['scenarios'])} fictional agentic-intent constraint checks")
