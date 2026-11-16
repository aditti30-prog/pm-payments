#!/usr/bin/env python3
"""Scheduled audit of external URLs in Markdown.

Not a compliance/source-accuracy checker. 404/410 are confirmed dead; 401/403,
429, network errors and robots restrictions are reported as UNVERIFIED rather
than incorrectly marked valid. Run weekly, outside PR CI.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL = re.compile(r"https?://[^\s<>)\]]+")
REPORT = ROOT / "external-link-report.txt"
USER_AGENT = "pm-payments-handbook-link-audit/1.0 (+https://github.com/aditti30-prog/pm-payments)"


def find_urls():
    found = set()
    for path in ROOT.rglob("*.md"):
        for match in URL.findall(path.read_text(encoding="utf-8")):
            link = match.rstrip(".,;:")
            parsed = urllib.parse.urlsplit(link)
            if parsed.netloc and parsed.scheme in {"http", "https"}:
                found.add(urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, parsed.query, "")))
    return sorted(found)


def check(url):
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            status = response.status
    except urllib.error.HTTPError as error:
        status = error.code
        if status in (405, 501):
            try:
                request = urllib.request.Request(url, method="GET", headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(request, timeout=12) as response:
                    status = response.status
            except urllib.error.HTTPError as second:
                status = second.code
            except (urllib.error.URLError, TimeoutError, OSError) as second:
                return ("UNVERIFIED", url, type(second).__name__)
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        return ("UNVERIFIED", url, type(error).__name__)
    if status in (404, 410):
        return ("BROKEN", url, f"HTTP {status}")
    if 200 <= status < 400:
        return ("OK", url, f"HTTP {status}")
    return ("UNVERIFIED", url, f"HTTP {status}")


def main():
    urls = find_urls()
    results = []
    # Keep load modest and do not test multiple anchors on the same web page.
    with ThreadPoolExecutor(max_workers=4) as pool:
        jobs = [pool.submit(check, url) for url in urls]
        for future in as_completed(jobs):
            results.append(future.result())
    results.sort(key=lambda item: (item[0], item[1]))
    lines = [f"External URL audit: {len(urls)} distinct URLs"]
    for state in ("BROKEN", "UNVERIFIED", "OK"):
        group = [item for item in results if item[0] == state]
        lines.append(f"\n{state}: {len(group)}")
        lines.extend(f"{reason}  {link}" for _, link, reason in group)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Checked {len(urls)} unique links; BROKEN={sum(x[0]=='BROKEN' for x in results)}; UNVERIFIED={sum(x[0]=='UNVERIFIED' for x in results)}")
    return 1 if any(item[0] == "BROKEN" for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
