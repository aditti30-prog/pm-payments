#!/usr/bin/env python3
"""Catch Markdown that renders wrongly on GitHub: junk fence info strings,
merged Mermaid lines, odd fence counts, glued labels/lazy list continuation,
and tables glued to the paragraph above. Pass paths to lint; default: whole repo."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
INFO_OK = re.compile(r"^[A-Za-z0-9_+-]*$")
LIST = re.compile(r"^\s*([-*+]|\d+[.)])\s")
BLOCK = re.compile(r"^(\s*([-*+]|\d+[.)])\s|#|>|\||<|---|\*\*\*|___|\s*$)")
# closing bracket, space, new node id: two statements merged on one Mermaid line
MERGED_NODE = re.compile(r"[\]\)\}]\s+[A-Za-z_]\w*\s*[\[\(\{]")


def lint(path):
    errs, fence, kind, opened = [], None, "", 0
    prev = ""
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        m = FENCE.match(line)
        if m and fence is None:
            info = m.group(3).strip()
            fence, kind, opened = m.group(2)[0], info, n
            if not INFO_OK.match(info):
                errs.append((n, f"fence info string {m.group(3).strip()!r} looks like merged text"))
        elif m and fence is not None:
            if m.group(2)[0] == fence and m.group(3).strip() == "":
                fence = None
            elif m.group(2)[0] == fence:
                errs.append((n, f"text after closing fence {m.group(3).strip()!r}"))
        elif fence is not None:
            if kind == "mermaid" and MERGED_NODE.search(re.sub(r'"[^"]*"|\|[^|]*\|', "", line)) \
                    and not re.match(r"\s*(subgraph|classDef|class|style|click|%%|note|participant)", line):
                errs.append((n, "Mermaid line looks like two statements merged"))
        else:
            if line.strip() and not BLOCK.match(line) and prev.strip():
                hard = prev.endswith("  ") or prev.endswith("\\")
                if LIST.match(prev) and not line.startswith((" ", "\t")):
                    errs.append((n, "unindented text directly after list item (lazy continuation)"))
                elif line.startswith("**") and not hard and not BLOCK.match(prev):
                    errs.append((n, "bold label glued to paragraph above (missing blank line)"))
            if line.startswith("|") and prev.strip() and not prev.startswith("|"):
                errs.append((n, "table not preceded by a blank line"))
        prev = line
    if fence is not None:
        errs.append((opened, "unclosed code fence"))
    return errs


def main(argv):
    files = [Path(a) for a in argv] or sorted(
        p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    bad = 0
    for f in files:
        for n, msg in lint(f):
            print(f"{f}:{n}: {msg}")
            bad += 1
    if bad:
        sys.exit(f"FAIL: {bad} Markdown structure problem(s)")
    print(f"OK: {len(files)} Markdown files: fences, Mermaid lines, labels and tables")


if __name__ == "__main__":
    main(sys.argv[1:])
