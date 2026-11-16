#!/usr/bin/env python3
"""Validate answer coverage and chapter-to-answer-key navigation.

Structure/completeness only. Does not verify legal, commercial or payment truth.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_internal_links import CHAPTERS

KEY = ROOT / "answers" / "chapter-exercises.md"


def check() -> list[str]:
    errors=[]
    text=KEY.read_text(encoding="utf-8") if KEY.exists() else ""
    anchors=set(re.findall(r"^## ([a-z0-9-]+)$",text,re.M))
    expected={Path(p).stem for p in CHAPTERS}
    for missing in sorted(expected - anchors):
        errors.append(f"MISSING SOLUTIONS SECTION: {missing}")
    for extra in sorted(anchors - expected):
        errors.append(f"ORPHAN SOLUTIONS SECTION: {extra}")
    for chapter in CHAPTERS:
        path=ROOT/chapter
        raw=path.read_text(encoding="utf-8")
        token=f"../../answers/chapter-exercises.md#{path.stem}"
        if f"[Worked solutions]({token})" not in raw:
            errors.append(f"NO CHAPTER-TO-KEY LINK: {chapter}")
        key_title=re.search(rf"^## {path.stem}\n\n\*\*Chapter:\*\* \[(.+?)\]",text,re.M)
        h1=raw.splitlines()[0].lstrip("# ").strip()
        if key_title and key_title.group(1)!=h1:
            errors.append(f"STALE CHAPTER TITLE IN KEY: {path.stem}: {key_title.group(1)!r} != {h1!r}")
        headings=[m for m in re.finditer(r"^## ([a-z0-9-]+)$",text,re.M) if m.group(1)==path.stem]
        if len(headings)!=1:
            errors.append(f"SOLUTION HEADING COUNT != 1: {path.stem}")
        elif len(text[headings[0].end():].split("\n---\n",1)[0].split())<55:
            errors.append(f"THIN SOLUTION: {path.stem} (under 55 words)")
        if not (re.search(r"^## .*?(?:exercise|practice|check your understanding|questions?)",raw,re.I|re.M) or re.search(r"^\*\*Exercise:\*\*",raw,re.I|re.M)):
            errors.append(f"NO CHAPTER EXERCISE: {chapter}")
    return errors


if __name__ == "__main__":
    errors=check()
    for error in errors:print(error)
    if errors:
        raise SystemExit(f"FAILED: {len(errors)} answer coverage issues")
    print(f"OK: {len(CHAPTERS)} chapter exercises, linked worked solutions and stable anchors")
