#!/usr/bin/env python3
"""Ethics check — block exploit-oriented keywords in generated security content.

Defense-only. Exit 0 clean, 1 findings.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Keyword heuristics for *generated* offensive content. Mentions in ethics/refuse
# docs are allowlisted via context patterns.
BLOCK = [
    re.compile(r"(?i)\bexploit\s+poc\b"),
    re.compile(r"(?i)\bproof[- ]of[- ]concept\s+exploit\b"),
    re.compile(r"(?i)\bweaponiz(?:e|ation)\b"),
    re.compile(r"(?i)\bransomware\s+payload\b"),
    re.compile(r"(?i)\bc2\s+server\s+setup\b"),
    re.compile(r"(?i)\bphishing\s+lure\s+template\b"),
    re.compile(r"(?i)\bcredential\s+exfil"),
    re.compile(r"(?i)\bcurl\s*[^\n]*\|\s*(?:ba)?sh\b"),
    re.compile(r"(?i)\brm\s+-rf\s+/"),
    re.compile(r"(?i)\bbypass\s+authentication\s+by\b"),
    re.compile(r"(?i)\bgenerate\s+malware\b"),
]

ALLOW_HINTS = (
    "refuse",
    "defense-only",
    "do not",
    "forbidden",
    "forbid",
    "no exploit",
    "ethics",
    "d3fend",
    "detect/defend",
    "hooks block",
    "out of scope",
)

SCAN_ROOTS = [
    "LAYERS", "FIREWALLS", "ENCRYPTION", "CHANGE", "TRANSPARENT_CODE", "CONDITIONAL",
    "IMPLEMENTATION", "ASSESSMENTS", "COMPLIANCE", "SECURITY_CONTEXT", "SECURITY_RESEARCH",
    "ORG/ROLES", "EXPERTS", "REPORTS", "QA", "MEMORY",
    ".cursor/skills", ".cursor/commands", ".cursor/agents",
]


def check_text(path: Path, text: str) -> list[str]:
    findings = []
    for i, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        if any(h in low for h in ALLOW_HINTS):
            continue
        for pat in BLOCK:
            if pat.search(line):
                findings.append(f"{path}:{i}:{pat.pattern}")
    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=".")
    ap.add_argument("--hook", action="store_true")
    args = ap.parse_args()

    paths: list[Path] = []
    if args.hook or args.path == ".":
        for rel in SCAN_ROOTS:
            p = ROOT / rel
            if p.exists():
                paths.extend([x for x in p.rglob("*") if x.is_file() and x.suffix in {".md", ".py", ".sh", ".json", ".yml", ".yaml"}])
    else:
        target = Path(args.path)
        if target.is_file():
            paths = [target]
        else:
            paths = [x for x in target.rglob("*") if x.is_file()]

    findings: list[str] = []
    for p in paths:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        findings.extend(check_text(p, text))

    if findings:
        print("ETHICS_CHECK: KALDI")
        for f in findings[:40]:
            print(" -", f)
        return 1
    print("ETHICS_CHECK: GECTI")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
