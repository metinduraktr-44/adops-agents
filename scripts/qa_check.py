#!/usr/bin/env python3
"""LATOS QA check — job card structure, title inventory diff, heading counts.

Exit 0 = pass (warnings ok); exit 1 = hard fail (title skip).
Usage: python3 scripts/qa_check.py [--hook]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOOK = "--hook" in sys.argv
WARNINGS: list[str] = []
ERRORS: list[str] = []


def load_inventory_slugs() -> set[str]:
    inv = ROOT / "ROSTER/TITLE_INVENTORY.md"
    if not inv.exists():
        return set()
    slugs = set(re.findall(r"\| `([a-z0-9-]+)` \|", inv.read_text(encoding="utf-8")))
    return slugs


def load_org_slugs() -> set[str]:
    org = json.loads((ROOT / "data/org.json").read_text(encoding="utf-8"))
    slugs: set[str] = set()
    for c in org.get("c_level", []):
        slugs.add(c["slug"])
    for dept in org.get("departments", []):
        for role in dept.get("roles", []):
            slugs.add(role["slug"])
    return slugs


def check_job_cards() -> None:
    cards_dir = ROOT / "JOB_CARDS"
    if not cards_dir.exists():
        return
    for card in cards_dir.glob("*/CARD.md"):
        slug = card.parent.name
        text = card.read_text(encoding="utf-8")
        if len(text) < 500:
            WARNINGS.append(f"[job-card] {slug}: CARD.md < 500 chars (scaffold ok, expand via /devam)")
        headings = list(card.parent.glob("H*.md"))
        if len(headings) < 1:
            WARNINGS.append(f"[job-card] {slug}: no H*.md heading files yet")
        for h in headings[:5]:
            ht = h.read_text(encoding="utf-8")
            if len(ht) < 200:
                WARNINGS.append(f"[heading] {slug}/{h.name}: < 200 chars (target 200+200+200 when expanded)")


def check_title_skip() -> None:
    org = load_org_slugs()
    inv = load_inventory_slugs()
    if not org:
        return
    if not inv:
        WARNINGS.append("[inventory] ROSTER/TITLE_INVENTORY.md missing or empty")
        return
    missing = org - inv
    extra = inv - org
    if missing:
        ERRORS.append(f"[title-skip] {len(missing)} org slugs missing from inventory (e.g. {list(missing)[:3]})")
    if extra and len(extra) > 20:
        WARNINGS.append(f"[inventory] {len(extra)} extra slugs in inventory vs org.json")


def main() -> None:
    check_title_skip()
    check_job_cards()
    if HOOK:
        for w in WARNINGS[:5]:
            print(f"QA_WARN: {w}", file=sys.stderr)
        if ERRORS:
            for e in ERRORS:
                print(f"QA_FAIL: {e}", file=sys.stderr)
            sys.exit(1)
        sys.exit(0)
    print("LATOS QA CHECK")
    for w in WARNINGS:
        print(" WARN:", w)
    for e in ERRORS:
        print(" FAIL:", e)
    if ERRORS:
        print("QA: KALDI")
        sys.exit(1)
    print("QA: GECTI")


if __name__ == "__main__":
    main()
