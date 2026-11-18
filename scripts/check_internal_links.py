#!/usr/bin/env python3
"""Check local Markdown links AND textbook semantics (headings, numbered references, Next chain).

Run from anywhere: python scripts/check_internal_links.py
No external dependencies. This is intentionally a structural checker, not a fact checker.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEAD = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)
NEXT = re.compile(r"^\*\*Next:\*\*\s*\[([^]]+)\]\(([^)]+)\)", re.MULTILINE)
NUMBERED_LINK = re.compile(r"^Chapter\s+(\d+[A-Za-z]?)\b", re.I)

# Explicit chapter order is intentional. New chapters must update the canonical reading path.
CHAPTERS = [
    "book/00-start-here-payments-pm-role/00-what-a-payments-pm-owns.md",
    "book/00-start-here-payments-pm-role/00a-your-first-90-days.md",
    "book/00-start-here-payments-pm-role/00b-prioritization-and-product-tradeoffs.md",
    "book/00-start-here-payments-pm-role/00c-selecting-payment-service-providers.md",
    "book/01-how-payments-work/01-understanding-a-payment.md",
    "book/01-how-payments-work/02-players-in-the-payments-ecosystem.md",
    "book/01-how-payments-work/03-how-card-payments-work.md",
    "book/01-how-payments-work/04-payment-fees-interchange-and-mdr.md",
    "book/02-payment-products-and-infrastructure/05-merchant-acquiring-and-onboarding.md",
    "book/02-payment-products-and-infrastructure/05a-marketplaces-payfacs-and-funds-flow.md",
    "book/02-payment-products-and-infrastructure/06-payment-gateways-routing-and-orchestration.md",
    "book/02-payment-products-and-infrastructure/07-card-issuing-and-tokenization.md",
    "book/02-payment-products-and-infrastructure/07a-network-tokens-and-card-credentials.md",
    "book/02-payment-products-and-infrastructure/08-wallets-qr-and-alternative-payment-methods.md",
    "book/02-payment-products-and-infrastructure/08a-in-store-pos-contactless-and-offline.md",
    "book/02-payment-products-and-infrastructure/09-bank-transfers-real-time-payments-and-bnpl.md",
    "book/02-payment-products-and-infrastructure/09a-cross-border-payments-fx-and-treasury.md",
    "book/03-checkout-authorization-and-fraud/10-checkout-and-payment-status-design.md",
    "book/03-checkout-authorization-and-fraud/10a-subscriptions-recurring-payments-and-dunning.md",
    "book/03-checkout-authorization-and-fraud/11-3d-secure-and-customer-authentication.md",
    "book/03-checkout-authorization-and-fraud/12-improving-payment-authorization-rates.md",
    "book/03-checkout-authorization-and-fraud/13-payment-fraud-and-risk-controls.md",
    "book/03-checkout-authorization-and-fraud/13a-compliance-pci-kyc-aml-and-ownership.md",
    "book/03-checkout-authorization-and-fraud/13b-scams-and-customer-protection.md",
    "book/03-checkout-authorization-and-fraud/14-how-to-manage-payment-products.md",
    "book/04-disputes-reconciliation-and-operations/15-chargebacks-and-dispute-management.md",
    "book/04-disputes-reconciliation-and-operations/16-payment-reconciliation-and-payouts.md",
    "book/04-disputes-reconciliation-and-operations/16a-payment-performance-metrics-and-dashboards.md",
    "book/04-disputes-reconciliation-and-operations/17-payment-outages-incidents-and-operations.md",
    "book/05-new-and-emerging-payments/18-instant-payments-open-banking-and-account-to-account.md",
    "book/05-new-and-emerging-payments/19-stablecoins-and-programmable-payments.md",
    "book/05-new-and-emerging-payments/20-agentic-commerce-and-ai-payments.md",
]

def slug(text: str) -> str:
    """Approximate GitHub heading anchor normalization for our English Markdown headings."""
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    text = text.lower().replace("`", "").strip()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return re.sub(r"\s", "-", text)

def chapter_id(path: Path) -> str | None:
    m = re.match(r"^(\d+[a-z]?)", path.name, flags=re.I)
    if not m:
        return None
    return m.group(1).lstrip("0").upper() or "0"

def resolve_path(from_md: Path, destination: str) -> Path:
    return (from_md.parent / unquote(destination.strip().strip("<>"))).resolve()

def check() -> tuple[list[str], int]:
    errors: list[str] = []
    local_links = 0
    files = list(ROOT.rglob("*.md"))
    texts = {file: file.read_text(encoding="utf-8") for file in files}

    # General link and explicitly numbered Chapter N label validation.
    for md, content in texts.items():
        for label, raw in MARKDOWN_LINK.findall(content):
            raw = raw.strip().split(' "', 1)[0]
            if raw.startswith(("http://", "https://", "mailto:")):
                continue
            file_dest, _, fragment = raw.partition("#")
            target = resolve_path(md, file_dest) if file_dest else md
            local_links += 1
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"BROKEN LINK: {md.relative_to(ROOT)} -> {raw}")
                continue
            if fragment and target.suffix.lower() == ".md":
                all_slugs = {slug(t) for t in HEAD.findall(texts.get(target, target.read_text(encoding='utf-8')))}
                if unquote(fragment).lower() not in all_slugs:
                    errors.append(f"BROKEN HEADING ANCHOR: {md.relative_to(ROOT)} -> {raw}")
            if target.suffix.lower() == ".md":
                m = NUMBERED_LINK.match(label)
                if m and chapter_id(target) != m.group(1).lstrip("0").upper():
                    errors.append(f"WRONG NUMBERED REFERENCE: {md.relative_to(ROOT)} says '{label}' -> {target.relative_to(ROOT)}")

    # Chapter file inventory and heading labels must match filename sequence.
    expected = {ROOT / name for name in CHAPTERS}
    actual = {p for p in (ROOT / "book").rglob("*.md") if p.name != "README.md"}
    for file in sorted(expected - actual):
        errors.append(f"MISSING CHAPTER: {file.relative_to(ROOT)}")
    for file in sorted(actual - expected):
        errors.append(f"UNLISTED CHAPTER (add to canonical path): {file.relative_to(ROOT)}")

    for idx, rel in enumerate(CHAPTERS):
        file = ROOT / rel
        if not file.exists():
            continue
        content = texts[file]
        first = content.splitlines()[0] if content else ""
        number = chapter_id(file)
        if file.parent.name == "part-0":
            if not first.startswith("# Part 0"):
                errors.append(f"WRONG CHAPTER HEADER: {rel} -> {first}")
        elif not re.match(rf"^# {re.escape(number)}\.\s", first):
            errors.append(f"WRONG CHAPTER HEADER: {rel} -> {first} (expected '{number}.')")

        if idx == len(CHAPTERS) - 1:
            # Final written chapter points to the roadmap and has no further chapter link.
            if "**Next:**" not in content:
                errors.append(f"MISSING NEXT-PLANNED MARKER: {rel}")
            continue
        found = NEXT.search(content)
        if not found:
            errors.append(f"MISSING NEXT LINK: {rel}")
            continue
        label, link = found.groups()
        dest = resolve_path(file, link.partition("#")[0])
        expected_next = ROOT / CHAPTERS[idx + 1]
        if dest != expected_next:
            errors.append(f"WRONG NEXT: {rel} -> {link}; expected {expected_next.relative_to(ROOT)}")
        next_number = chapter_id(expected_next)
        if next_number and expected_next.parent.name != "part-0":
            if not re.match(rf"^{re.escape(next_number)}(?:\b|\.)", label):
                errors.append(f"WRONG NEXT LABEL: {rel} uses '{label}'; expected chapter {next_number}")

    # README must expose every written chapter from the canonical path.
    readme = texts.get(ROOT / "book" / "README.md", "")
    for rel in CHAPTERS:
        if rel not in readme:
            errors.append(f"MISSING FROM BOOK INDEX: {rel}")
    return errors, local_links

if __name__ == "__main__":
    problems, count = check()
    for issue in problems:
        print(issue)
    if problems:
        print(f"FAILED: {len(problems)} issues, {count} local links inspected")
        sys.exit(1)
    print(f"OK: {count} local links; {len(CHAPTERS)} chapter headings and canonical Next links; numbered chapter references; README inventory")
