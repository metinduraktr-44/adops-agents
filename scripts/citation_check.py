#!/usr/bin/env python3
"""LATOS citation check — EXPERTS/RESEARCH require URL/timestamp or unverified flag.

Exit 0 = pass; exit 1 = hard fail on sourced claim without citation.
Usage: python3 scripts/citation_check.py [--hook]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOOK = "--hook" in sys.argv
ERRORS: list[str] = []
WARNINGS: list[str] = []

SCAN_DIRS = ["EXPERTS", "EXPERTS_TALENT", "RESEARCH", "FORECASTS"]
URL_RE = re.compile(r"https?://[^\s\)|>]+")
OK_FLAGS = ("unverified", "pending_research", "null", "sourced_historical", "scaffold")


def check_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = path.relative_to(ROOT)
    has_url = bool(URL_RE.search(text))
    has_flag = any(f in text.lower() for f in OK_FLAGS)
    has_timestamp = bool(re.search(r"\d{4}-\d{2}-\d{2}", text))
    # Named expert without url/unverified
    if re.search(r"\| \d+ \| sourced \| [A-Z]", text) and not has_url:
        ERRORS.append(f"[citation] {rel}: sourced row without URL")
    if "status: sourced" in text.lower() and not has_url and "pending" not in text.lower():
        WARNINGS.append(f"[citation] {rel}: sourced status but no URL found")
    if not has_url and not has_flag and path.suffix == ".md" and "top100" in path.name:
        WARNINGS.append(f"[citation] {rel}: expert file lacks URL and explicit pending/unverified")


def main() -> None:
    for d in SCAN_DIRS:
        base = ROOT / d
        if not base.exists():
            continue
        for md in base.rglob("*.md"):
            check_file(md)
    if HOOK:
        for w in WARNINGS[:5]:
            print(f"CITE_WARN: {w}", file=sys.stderr)
        if ERRORS:
            for e in ERRORS:
                print(f"CITE_FAIL: {e}", file=sys.stderr)
            sys.exit(1)
        sys.exit(0)
    print("LATOS CITATION CHECK")
    for w in WARNINGS:
        print(" WARN:", w)
    for e in ERRORS:
        print(" FAIL:", e)
    if ERRORS:
        print("CITATION: KALDI")
        sys.exit(1)
    print("CITATION: GECTI")


if __name__ == "__main__":
    main()
