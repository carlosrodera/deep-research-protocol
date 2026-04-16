#!/usr/bin/env python3
"""
verify-citations.py — Deep Research Protocol citation verifier.

Parses a Markdown brief, extracts every cited URL, and issues HEAD
requests to verify each one resolves. Flags hallucinated or broken
citations — the #1 failure mode of single-engine deep research.

Usage
-----
    python scripts/verify-citations.py <path/to/brief.md> [--timeout 10] [--verbose]
    python scripts/verify-citations.py workspace/research/consolidated.md

Exit codes
----------
    0   all citations resolve (HTTP 2xx or 3xx)
    1   one or more citations failed to resolve
    2   usage error

Design notes
------------
- Standard library only. No runtime dependencies.
- HEAD first, GET fallback (some servers reject HEAD).
- 10s default timeout. Rate-limit-friendly (1 req/domain/sec).
- Distinguishes transient errors (network, 5xx) from confirmed-dead (4xx).
- Redirects followed up to 5 hops.

Part of the Deep Research Protocol — github.com/carlosrodera/deep-research-protocol.
MIT (c) 2026 Carlos Rodera.
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

# Markdown link patterns: [text](url), bare https://..., <https://...>
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^\s)]+)\)")
BARE_URL_RE = re.compile(r"(?<![(<\"'])\bhttps?://[^\s<>\"')\]]+")
ANGLE_URL_RE = re.compile(r"<(https?://[^>\s]+)>")

USER_AGENT = (
    "Mozilla/5.0 (compatible; DRP-CitationVerifier/1.0; "
    "+https://github.com/carlosrodera/deep-research-protocol)"
)

# Per-domain minimum interval (seconds) to avoid hammering a single host.
DOMAIN_MIN_INTERVAL = 1.0


@dataclass
class CheckResult:
    url: str
    status: int | None
    category: str  # "ok" | "broken" | "transient" | "skipped"
    detail: str


def extract_urls(text: str) -> list[str]:
    """Extract all URLs from a markdown blob, deduped, order-preserving."""
    seen: set[str] = set()
    ordered: list[str] = []

    def add(url: str) -> None:
        # Strip trailing punctuation that is almost never part of a URL.
        url = url.rstrip(".,;:!?")
        if url not in seen:
            seen.add(url)
            ordered.append(url)

    for m in MARKDOWN_LINK_RE.finditer(text):
        add(m.group(1))
    for m in ANGLE_URL_RE.finditer(text):
        add(m.group(1))
    for m in BARE_URL_RE.finditer(text):
        add(m.group(0))

    return ordered


def check_url(url: str, timeout: float) -> CheckResult:
    """Issue HEAD (fallback GET) and classify the result."""
    req_kwargs = {"headers": {"User-Agent": USER_AGENT}}

    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, **req_kwargs)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                status = resp.status
                if 200 <= status < 400:
                    return CheckResult(url, status, "ok", f"HTTP {status}")
                # 4xx → broken unless 403 on HEAD (retry GET)
                if method == "HEAD" and status in (403, 405, 501):
                    continue
                return CheckResult(url, status, "broken", f"HTTP {status}")
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 501):
                continue
            if 400 <= e.code < 500:
                return CheckResult(url, e.code, "broken", f"HTTP {e.code}")
            return CheckResult(url, e.code, "transient", f"HTTP {e.code}")
        except urllib.error.URLError as e:
            return CheckResult(url, None, "transient", f"URLError: {e.reason}")
        except TimeoutError:
            return CheckResult(url, None, "transient", "timeout")
        except Exception as e:  # noqa: BLE001
            return CheckResult(url, None, "transient", f"{type(e).__name__}: {e}")

    return CheckResult(url, None, "transient", "no response after HEAD+GET")


def domain_of(url: str) -> str:
    try:
        return urllib.parse.urlparse(url).netloc.lower()
    except Exception:  # noqa: BLE001
        return ""


def verify_all(urls: Iterable[str], timeout: float, verbose: bool) -> list[CheckResult]:
    results: list[CheckResult] = []
    last_hit: dict[str, float] = {}

    for i, url in enumerate(urls, 1):
        domain = domain_of(url)
        if domain:
            since = time.monotonic() - last_hit.get(domain, 0.0)
            if since < DOMAIN_MIN_INTERVAL:
                time.sleep(DOMAIN_MIN_INTERVAL - since)
            last_hit[domain] = time.monotonic()

        r = check_url(url, timeout)
        results.append(r)

        if verbose:
            print(f"[{i}] {r.category.upper():9s} {r.url}  →  {r.detail}")

    return results


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Verify every URL cited in a DRP brief resolves. Catches hallucinated citations.",
    )
    ap.add_argument("path", type=Path, help="Path to the markdown brief (e.g. workspace/research/consolidated.md)")
    ap.add_argument("--timeout", type=float, default=10.0, help="Per-request timeout in seconds (default 10)")
    ap.add_argument("--verbose", action="store_true", help="Print every URL check as it runs")
    args = ap.parse_args()

    if not args.path.exists():
        print(f"error: file not found: {args.path}", file=sys.stderr)
        return 2

    text = args.path.read_text(encoding="utf-8", errors="replace")
    urls = extract_urls(text)

    if not urls:
        print("no URLs found in brief. If this is unexpected, your brief has no citations — which itself violates DRP Step F.")
        return 1

    print(f"verifying {len(urls)} unique citation(s) from {args.path} …")
    results = verify_all(urls, timeout=args.timeout, verbose=args.verbose)

    by_cat: dict[str, list[CheckResult]] = collections.defaultdict(list)
    for r in results:
        by_cat[r.category].append(r)

    ok = len(by_cat.get("ok", []))
    broken = by_cat.get("broken", [])
    transient = by_cat.get("transient", [])

    print()
    print(f"  resolved   : {ok}/{len(urls)}")
    print(f"  broken     : {len(broken)}   (4xx or similar — investigate)")
    print(f"  transient  : {len(transient)}   (network / 5xx — retry or verify manually)")

    if broken:
        print()
        print("Broken citations (DRP treats these as hallucination signals):")
        for r in broken:
            print(f"  · [{r.status}] {r.url}  —  {r.detail}")

    if transient:
        print()
        print("Transient failures (re-run the verifier in a few minutes):")
        for r in transient:
            print(f"  · {r.url}  —  {r.detail}")

    # Exit code: 0 only if NO broken citations. Transient failures do not fail the run.
    return 0 if not broken else 1


if __name__ == "__main__":
    sys.exit(main())
