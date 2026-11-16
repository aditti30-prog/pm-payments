#!/usr/bin/env python3
"""Recompute the two synthetic operational case labs from JSON source inputs.

Each figure is recomputed from the fixture and must appear in the case text as a
whole token (see _match.present), so editing either the fixture or the prose
fails this check. These tests do NOT establish scheme or provider-rule correctness.
"""
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path

from _match import present

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "cases/data/operational-case-inputs.json").read_text(encoding="utf-8"))
assert DATA["schema_version"] == 1


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"))


def pct(numerator, denominator):
    assert denominator > 0
    return (Decimal(numerator) * 100 / Decimal(denominator)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


def shown(text, amount):
    """Amount appears as 12.34, S$12.34, or (if whole) S$12 -- as a whole token only."""
    a = money(amount)
    forms = [f"{a:,.2f}"]
    if a == a.to_integral_value():
        forms.append(f"S${int(a):,}")
    return any(present(text, f) for f in forms)


def table_row(text, label):
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.lstrip().startswith("|") and cells[0] == label:
            return cells
    raise AssertionError(f"failover: table row {label!r} missing")


def check_failover():
    d = DATA["failover"]
    case = (ROOT / "cases/02-ambiguous-authorization-routing.md").read_text(encoding="utf-8")
    assert 0 <= d["confirmed_paid_orders"] <= d["payment_initiated_orders"]
    assert 0 <= d["approved_auth_attempts"] <= d["submitted_auth_attempts"]
    assert d["challenges_completed"] <= d["challenges_started"]
    timeouts = d["original_psp_timeout_operations"]
    assert d["later_approved"] + d["definitively_declined"] + d["still_unknown"] == timeouts

    # Each metric row: label, numerator, denominator and rate must sit in the same row.
    rows = [
        ("Authorization attempts approved / submitted", d["approved_auth_attempts"], d["submitted_auth_attempts"]),
        ("Distinct paid orders / payment-initiated orders", d["confirmed_paid_orders"], d["payment_initiated_orders"]),
        ("Completed 3DS challenges / initiated challenges", d["challenges_completed"], d["challenges_started"]),
        ("Original A timeouts with a known issuer outcome at snapshot",
         d["later_approved"] + d["definitively_declined"], timeouts),
        ("Original A timeouts still unresolved", d["still_unknown"], timeouts),
    ]
    for label, num, den in rows:
        cells = table_row(case, label)
        want = [f"{num:,}", f"{den:,}", f"**{pct(num, den):.2f}%**"]
        assert cells[1:4] == want, f"failover row {label!r}: expected {want}, found {cells[1:4]}"

    # The 100-timeout partition is stated in prose; bind it to the fixture too.
    assert present(case, f"{timeouts} authorization requests"), "failover: timeout count missing"
    partition = (f"{d['later_approved']} were issuer-approved, {d['definitively_declined']} "
                 f"definitively declined, {d['still_unknown']} remain unresolved")
    assert present(case, partition), f"failover: partition text {partition!r} missing"
    print("OK: PSP failover rows, timeout partition and distinct metric grains")


def check_marketplace():
    d = DATA["marketplace"]
    assert d["currency"] == "SGD"
    a, b = money(d["seller_a_gross"]), money(d["seller_b_gross"])
    gross = a + b
    commission_rate = Decimal(d["platform_commission_rate"])
    processing_rate = Decimal(d["processing_fee_rate"])
    platform_commission_a = money(a * commission_rate)
    platform_commission_b = money(b * commission_rate)
    commission = platform_commission_a + platform_commission_b
    provider_fee = money(gross * processing_rate + Decimal(d["processing_fixed_fee"]))
    net_settlement = gross - provider_fee
    a_entitlement, b_entitlement = a - platform_commission_a, b - platform_commission_b
    a_reserve, b_reserve = money(d["seller_a_initial_reserve"]), money(d["seller_b_initial_reserve"])
    assert 0 <= a_reserve <= a_entitlement and 0 <= b_reserve <= b_entitlement
    a_payout, b_payout = a_entitlement - a_reserve, b_entitlement - b_reserve
    platform_net = commission - provider_fee
    assert net_settlement == a_payout + b_payout + a_reserve + b_reserve + platform_net

    refund = money(d["seller_a_later_refund"])
    assert 0 <= refund <= a
    refund_platform_share = money(refund * commission_rate)
    refund_seller_share = refund - refund_platform_share
    reserve_applied = min(a_reserve, refund_seller_share)
    seller_a_receivable = refund_seller_share - reserve_applied
    assert refund == reserve_applied + seller_a_receivable + refund_platform_share

    dispute = money(d["seller_b_final_dispute_principal"])
    assert 0 <= dispute <= b
    b_platform_reversal = money(dispute * commission_rate)
    b_seller_receivable = dispute - b_platform_reversal
    dispute_fee = money(d["seller_b_dispute_fee_platform"])
    assert b_platform_reversal + b_seller_receivable == dispute and dispute_fee >= 0

    case = (ROOT / "cases/03-marketplace-reserve-refund-dispute.md").read_text(encoding="utf-8")
    named = {
        "gross": gross, "provider fee": provider_fee, "net settlement": net_settlement,
        "A entitlement": a_entitlement, "B entitlement": b_entitlement,
        "A payout": a_payout, "B payout": b_payout, "platform net margin": platform_net,
        "reserve applied": reserve_applied, "A receivable": seller_a_receivable,
        "A refund commission reversal": refund_platform_share, "A refund seller share": refund_seller_share,
        "B commission reversal": b_platform_reversal, "B seller receivable": b_seller_receivable,
        "dispute fee": dispute_fee,
    }
    for name, amount in named.items():
        assert shown(case, amount), f"marketplace: {name} {money(amount)} is missing from case"

    # The one semantic guardrail worth pinning: reserve is held money, not earnings.
    assert "not platform earnings" in case.lower(), "marketplace: reserve-is-not-earnings caution removed"
    print("OK: Marketplace initial settlement, reserve, refund and dispute allocations")


if __name__ == "__main__":
    check_failover()
    check_marketplace()
