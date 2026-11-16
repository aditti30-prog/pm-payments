#!/usr/bin/env python3
"""Parse every ```mermaid block with the real Mermaid CLI (mmdc), as GitHub would render it.

Text lints cannot see Mermaid syntax errors such as a ';' inside a sequence-diagram message
or a reserved word ('off') used as a participant ID; both show readers a red error box.

Needs: npm i -g @mermaid-js/mermaid-cli, plus Chrome or Chromium. Optional env:
MMDC (command, default 'mmdc'), PUPPETEER_EXECUTABLE_PATH (browser).
Pass --optional to skip quietly when mmdc is absent (local use); CI must not."""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def blocks(path):
    """Yield (first_line_number, source) for each ```mermaid block."""
    lines, start, buf = path.read_text(encoding="utf-8").splitlines(), None, []
    for n, line in enumerate(lines, 1):
        if start is None and re.match(r"^```mermaid\s*$", line):
            start, buf = n, []
        elif start is not None and line.startswith("```"):
            yield start, "\n".join(buf)
            start = None
        elif start is not None:
            buf.append(line)


def main(argv):
    optional = "--optional" in argv
    paths = [Path(a) for a in argv if not a.startswith("--")] or sorted(
        p for p in ROOT.rglob("*.md") if ".git" not in p.parts and "node_modules" not in p.parts)
    mmdc = shutil.which(os.environ.get("MMDC", "mmdc"))
    if not mmdc:
        if optional:
            print("SKIP: mmdc not installed (npm i -g @mermaid-js/mermaid-cli)")
            return
        sys.exit("FAIL: mmdc not found; npm i -g @mermaid-js/mermaid-cli")
    browser = os.environ.get("PUPPETEER_EXECUTABLE_PATH") or next(
        (shutil.which(b) for b in ("google-chrome", "chromium", "chromium-browser") if shutil.which(b)), None)
    work = Path(tempfile.mkdtemp(prefix="mermaid-check-"))
    config = work / "puppeteer.json"
    config.write_text(json.dumps({"args": ["--no-sandbox", "--disable-gpu"],
                                  **({"executablePath": browser} if browser else {})}))

    jobs = [(p, n, src) for p in paths for n, src in blocks(p)]

    def run(job):
        i, (path, line, src) = job
        mmd = work / f"{i}.mmd"
        mmd.write_text(src, encoding="utf-8")
        r = subprocess.run([mmdc, "-q", "-p", str(config), "-i", str(mmd), "-o", str(work / f"{i}.svg")],
                           capture_output=True, text=True, timeout=120)
        if r.returncode == 0:
            return None
        detail = [l.strip() for l in (r.stderr + r.stdout).splitlines()
                  if re.search(r"error|expecting|got ", l, re.I)][:2]
        try:
            shown = path.resolve().relative_to(ROOT)
        except ValueError:
            shown = path
        return f"{shown}:{line}: Mermaid parse error: {' | '.join(detail)[:300]}"

    with ThreadPoolExecutor(max_workers=4) as pool:
        errors = [e for e in pool.map(run, enumerate(jobs)) if e]
    shutil.rmtree(work, ignore_errors=True)
    for e in errors:
        print(e)
    if errors:
        sys.exit(f"FAIL: {len(errors)} of {len(jobs)} Mermaid diagram(s) do not parse")
    print(f"OK: {len(jobs)} Mermaid diagrams parsed by mmdc")


if __name__ == "__main__":
    main(sys.argv[1:])
