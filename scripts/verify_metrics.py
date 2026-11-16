#!/usr/bin/env python3
"""Verify all HarborCart synthetic funnel and cohort arithmetic from CSV inputs.

This is a reproducible textbook fixture test, not a production KPI calculator.
Changing a source value must affect the computed metric and may fail the
explicit teaching expectations below.
"""
from pathlib import Path
from decimal import Decimal
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "cases" / "data"


def load_funnel(path):
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    required = {
        "eligible_checkout_sessions",
        "payment_initiated_orders",
        "confirmed_paid_orders",
        "captured_sales_sgd",
        "processing_cost_sgd",
        "mature_captured_sales_sgd",
        "mature_confirmed_fraud_loss_sgd",
    }
    values = {row["metric"]: Decimal(row["value"]) for row in rows}
    assert len(values) == len(rows), "duplicate funnel metric"
    assert values.keys() == required, "missing or unexpected funnel metric"
    assert all(value >= 0 for value in values.values()), "negative amount/count"
    return values


def load_cohorts(path):
    with path.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    assert {r["cohort"] for r in rows} == {"domestic", "cross_border"}, "cohort coverage"
    assert len(rows) == 2, "duplicated cohorts"
    return {
        r["cohort"]: (
            Decimal(r["eligible_authorization_attempts"]),
            Decimal(r["approved_authorization_attempts"]),
        )
        for r in rows
    }


def divide(numerator, denominator):
    assert denominator > 0, "undefined metric: denominator cannot be zero"
    return numerator / denominator


def calculate(funnel, cohorts):
    total_attempts = sum(row[0] for row in cohorts.values())
    approved_attempts = sum(row[1] for row in cohorts.values())
    assert all(0 <= approved <= attempts for attempts, approved in cohorts.values())
    assert funnel["confirmed_paid_orders"] <= funnel["payment_initiated_orders"]
    assert funnel["payment_initiated_orders"] <= funnel["eligible_checkout_sessions"]
    assert funnel["mature_confirmed_fraud_loss_sgd"] <= funnel["mature_captured_sales_sgd"]
    return {
        "submitted_attempts": total_attempts,
        "approved_attempts": approved_attempts,
        "attempt_auth_rate": divide(approved_attempts, total_attempts),
        "checkout_paid_conversion": divide(funnel["confirmed_paid_orders"], funnel["eligible_checkout_sessions"]),
        "initiated_order_success": divide(funnel["confirmed_paid_orders"], funnel["payment_initiated_orders"]),
        "cost_per_paid_order_sgd": divide(funnel["processing_cost_sgd"], funnel["confirmed_paid_orders"]),
        "fraud_loss_bps": divide(funnel["mature_confirmed_fraud_loss_sgd"], funnel["mature_captured_sales_sgd"]) * 10000,
        "domestic_auth_pct": divide(cohorts["domestic"][1], cohorts["domestic"][0]) * 100,
        "cross_border_auth_pct": divide(cohorts["cross_border"][1], cohorts["cross_border"][0]) * 100,
    }


def verify():
    funnel = load_funnel(DATA / "harborcart-funnel.csv")
    cohorts = load_cohorts(DATA / "harborcart-metrics.csv")
    actual = calculate(funnel, cohorts)
    expected = {
        "submitted_attempts": Decimal("82000"),
        "approved_attempts": Decimal("73800"),
        "attempt_auth_rate": Decimal("0.90"),
        "checkout_paid_conversion": Decimal("0.72"),
        "initiated_order_success": Decimal("0.90"),
        "cost_per_paid_order_sgd": Decimal("0.98"),
        "fraud_loss_bps": Decimal("10"),
        "domestic_auth_pct": Decimal("91.93548387096774193548387097"),
        "cross_border_auth_pct": Decimal("84"),
    }
    for name, expected_value in expected.items():
        observed = actual[name]
        if name == "domestic_auth_pct":
            assert round(observed, 2) == Decimal("91.94"), (name, observed)
        else:
            assert observed == expected_value, (name, observed, expected_value)

    # Mutation checks make sure the calculation responds to input changes.
    altered = dict(funnel)
    altered["confirmed_paid_orders"] -= 1
    changed = calculate(altered, cohorts)
    assert changed["checkout_paid_conversion"] != actual["checkout_paid_conversion"]
    assert changed["cost_per_paid_order_sgd"] != actual["cost_per_paid_order_sgd"]

    try:
        divide(Decimal(1), Decimal(0))
        raise AssertionError("zero denominator was accepted")
    except AssertionError as err:
        assert "denominator" in str(err), str(err)

    print("OK: data-backed HarborCart funnel, segment rates, fee and mature-fraud arithmetic")


if __name__ == "__main__":
    verify()
