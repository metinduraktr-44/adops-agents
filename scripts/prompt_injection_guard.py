#!/usr/bin/env python3
"""Defense-only heuristic: flag instruction-override strings in trusted instruction files.

Does not generate attacks. Exit 0 clean, 1 findings, 2 usage error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Phrases we refuse to obey if they appear as directives in instruction surfaces.
PATTERNS = [
    ("ignore_previous", re.compile(r"(?i)ignore\s+(all\s+)?previous\s+instructions")),
    ("disable_safety", re.compile(r"(?i)disable\s+(all\s+)?(safety|guardrail)s?")),
    ("exfil_directive", re.compile(r"(?i)(exfiltrate|send\s+secrets?\s+to)\b")),
    ("skip_permissions", re.compile(r"(?i)dangerously-skip-permissions")),
]

SCAN_PATHS = [
    ROOT / "CLAUDE.md",
    ROOT / "AGENTS.md",
    ROOT / ".cursor" / "rules",
    ROOT / ".cursor" / "commands",
    ROOT / ".cursor" / "hooks.json",
    ROOT / "docs" / "CLAUDE-CODE-AKTIVASYON.md",
]

SKIP_HINTS = (
    "refuse",
    "do not",
    "don't",
    "forbidden",
    "defense-only",
    "owner-gated",
    "do not enable",
    "flag",
    "heuristic",
)


def should_skip_line(line: str) -> bool:
    low = line.lower()
    return any(h in low for h in SKIP_HINTS)


def scan_text(path: Path, text: str) -> list[str]:
    out: list[str] = []
    for i, line in enumerate(text.splitlines(), 1):
        if should_skip_line(line):
            continue
        for name, pat in PATTERNS:
            if pat.search(line):
                out.append(f"{path}:{i}:{name}")
    return out


def iter_files() -> list[Path]:
    files: list[Path] = []
    for p in SCAN_PATHS:
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            files.extend([x for x in p.rglob("*") if x.is_file() and x.suffix in {".md", ".mdc", ".json"}])
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description="Prompt-injection heuristic (defense-only)")
    ap.add_argument("--hook", action="store_true")
    ap.add_argument("--prompt-hook", action="store_true")
    args = ap.parse_args()

    if args.prompt_hook:
        raw = sys.stdin.read() if not sys.stdin.isatty() else ""
        try:
            payload = json.loads(raw) if raw.strip().startswith("{") else {"text": raw}
        except json.JSONDecodeError:
            payload = {"text": raw}
        text = str(payload.get("text") or payload.get("prompt") or raw)
        findings = scan_text(Path("<prompt>"), text)
        if findings:
            print("PROMPT_INJECTION_GUARD: KALDI (prompt)", file=sys.stderr)
            for f in findings:
                print(f" - {f}", file=sys.stderr)
            return 1
        return 0

    findings: list[str] = []
    for path in iter_files():
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        findings.extend(scan_text(path, text))

    if findings:
        print("PROMPT_INJECTION_GUARD: KALDI")
        for f in findings[:50]:
            print(" -", f)
        return 1
    print("PROMPT_INJECTION_GUARD: GECTI")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
