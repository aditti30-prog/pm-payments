#!/usr/bin/env python3
"""Basic checker for relative Markdown links; ignores external links/anchors."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
missing = []
count = 0
for md in root.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    for raw in pattern.findall(text):
        target = raw.split("#", 1)[0].strip().strip('<>')
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        count += 1
        relative = unquote(target.split(' "', 1)[0])
        candidate = (md.parent / relative).resolve()
        if not candidate.is_relative_to(root.resolve()) or not candidate.exists():
            missing.append((md.relative_to(root), raw))

if missing:
    for source, destination in missing:
        print(f"BROKEN: {source} -> {destination}")
    sys.exit(1)
print(f"OK: {count} local links across {len(list(root.rglob('*.md')))} Markdown files")
