#!/usr/bin/env python3
"""Defense-only secret scanner. Stdlib. Exit 0 clean, 1 findings, 2 usage error.

Never prints full secret values — redacts matches.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# High-signal patterns; matches are redacted in output.
PATTERNS = [
    ("aws_access_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("generic_api_key_assign", re.compile(
        r"(?i)(api[_-]?key|secret|token|password|private[_-]?key)\s*[:=]\s*['\"][^'\"\n]{12,}['\"]"
    )),
    ("pem_private_key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("jwt_like", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
]

SKIP_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv",
    "data/arsiv",  # large archives — still scanned if explicitly passed
}
ALLOW_PLACEHOLDERS = ("${", "vault://", "op://", "<REDACTED>", "REDACTED")


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & {".git", "node_modules", "__pycache__", ".venv", "venv"}:
        return True
    if path.suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".pyc"}:
        return True
    return False


def is_placeholder_line(line: str) -> bool:
    return any(p in line for p in ALLOW_PLACEHOLDERS)


def redact(s: str) -> str:
    if len(s) <= 8:
        return "<REDACTED>"
    return s[:2] + "…" + "<REDACTED>"


def scan_file(path: Path) -> list[str]:
    findings: list[str] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return findings
    for i, line in enumerate(text.splitlines(), 1):
        if is_placeholder_line(line):
            continue
        for name, pat in PATTERNS:
            m = pat.search(line)
            if m:
                findings.append(f"{path}:{i}:{name}:{redact(m.group(0))}")
    return findings


def iter_paths(root: Path):
    if root.is_file():
        yield root
        return
    for p in root.rglob("*"):
        if p.is_file() and not should_skip(p):
            yield p


def main() -> int:
    ap = argparse.ArgumentParser(description="Secret scan (defense-only)")
    ap.add_argument("path", nargs="?", default=".", help="file or directory")
    ap.add_argument("--hook", action="store_true", help="hook mode: scan cwd lightly")
    ap.add_argument("--redact-check", metavar="FILE", help="check single file for hooks")
    args = ap.parse_args()

    if args.redact_check:
        findings = scan_file(Path(args.redact_check))
        for f in findings:
            print(f"[secret_scan] {f}", file=sys.stderr)
        return 1 if findings else 0

    target = Path(args.path)
    if args.hook:
        # Hook: prefer security-relevant trees to keep latency low
        targets = [
            ROOT / "SECURITY_CONTEXT",
            ROOT / "IMPLEMENTATION",
            ROOT / "ASSESSMENTS",
            ROOT / ".cursor",
            ROOT / "scripts",
        ]
        paths = []
        for t in targets:
            if t.exists():
                paths.extend(iter_paths(t))
    else:
        paths = list(iter_paths(target if target.is_absolute() else ROOT / target))

    all_findings: list[str] = []
    for p in paths:
        all_findings.extend(scan_file(p))

    if all_findings:
        print("SECRET_SCAN: KALDI")
        for f in all_findings[:50]:
            print(" -", f)
        if len(all_findings) > 50:
            print(f" - … {len(all_findings) - 50} more")
        return 1
    print("SECRET_SCAN: GECTI")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
