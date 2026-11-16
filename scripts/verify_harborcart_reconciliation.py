#!/usr/bin/env python3
"""Verify synthetic HarborCart order's gross/net accounting and callback deduplication."""
import csv
from decimal import Decimal
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/'cases/data/harborcart-order-events.csv').open(newline='',encoding='utf8') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==6
assert len({(r['kind'],r['source_id']) for r in rows})==len(rows)
sums={r['kind']:Decimal(r['financial_amount_sgd']) for r in rows}
auth=sums['AUTHORIZATION'];capture=sums['CAPTURE'];refund=sums['REFUND'];fee=sums['PSP_FEE'];bank=sums['BANK_PAYOUT']
assert auth==Decimal('100.00')
assert capture==Decimal('80.00')
assert refund==Decimal('-10.00')
assert fee==-(capture*Decimal('0.02')+Decimal('0.20'))
assert capture+refund+fee==bank==Decimal('68.20'),(capture,refund,fee,bank)
assert sums['CAPTURE_WEBHOOK_REDELIVERY']==0
webhooks=[r for r in rows if r['delivery_id']=='EV1']
assert len(webhooks)==2 and len({r['source_id'] for r in webhooks})==1
assert bank != auth
print('OK: HarborCart S$100 authorization, S$80 capture, S$10 refund, S$1.80 fee, S$68.20 net payout; one financial capture despite duplicate webhook')
