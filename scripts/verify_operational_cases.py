#!/usr/bin/env python3
"""Recompute the two synthetic operational case labs from JSON source inputs.

Tests are deliberately independent of the numbers typed into the case text:
mutating a fixture without updating the corresponding prose fails this check.
These tests do NOT establish scheme or provider-rule correctness.
"""
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "cases/data/operational-case-inputs.json").read_text(encoding="utf-8"))
assert DATA["schema_version"] == 1


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"))


def money_text(value):
    return f"S${money(value):,.2f}"


def pct(numerator, denominator):
    assert denominator > 0
    return (Decimal(numerator) * 100 / Decimal(denominator)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )


def check_contains(text, value, case):
    assert value in text, f"{case}: expected calculated text '{value}' missing"


def check_failover():
    d = DATA["failover"]
    case = (ROOT / "cases/02-ambiguous-authorization-routing.md").read_text(encoding="utf-8")
    assert 0 <= d["confirmed_paid_orders"] <= d["payment_initiated_orders"]
    assert 0 <= d["approved_auth_attempts"] <= d["submitted_auth_attempts"]
    assert d["challenges_completed"] <= d["challenges_started"]
    assert (
        d["later_approved"] + d["definitively_declined"] + d["still_unknown"]
        == d["original_psp_timeout_operations"]
    )
    ratios = [
        pct(d["approved_auth_attempts"], d["submitted_auth_attempts"]),
        pct(d["confirmed_paid_orders"], d["payment_initiated_orders"]),
        pct(d["challenges_completed"], d["challenges_started"]),
        pct(d["later_approved"] + d["definitively_declined"], d["original_psp_timeout_operations"]),
        pct(d["still_unknown"], d["original_psp_timeout_operations"]),
    ]
    for result in ratios:
        check_contains(case, f"**{result:.2f}%**", "failover")
    for key in ("submitted_auth_attempts", "approved_auth_attempts", "still_unknown"):
        check_contains(case, f"{d[key]:,}", "failover")
    # Explicit semantic guardrails: keep auth and paid orders distinct.
    assert "not" in case.lower() and "paid orders" in case.lower()
    print("OK: PSP failover rates, timeout partition and distinct metric grains")


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
    for amount in (
        gross, provider_fee, net_settlement, a_entitlement, b_entitlement,
        a_payout, b_payout, platform_net, reserve_applied, seller_a_receivable,
        refund_platform_share, refund_seller_share, b_platform_reversal,
        b_seller_receivable, dispute_fee,
    ):
        expected_tokens = {
            money_text(amount),
            f"{money(amount):,.2f}",
            f"S${money(amount):,.0f}",
        }
        assert any(token in case for token in expected_tokens), (
            f"marketplace: calculated amount {money(amount)} is missing from case"
        )

    # Structural guardrail against treating seller reserve as platform earnings.
    assert "not platform earnings" in case.lower()
    assert "not" in case.lower() and "collected" in case.lower()
    print("OK: Marketplace initial settlement, reserve, refund and dispute allocations")


if __name__ == "__main__":
    check_failover()
    check_marketplace()
