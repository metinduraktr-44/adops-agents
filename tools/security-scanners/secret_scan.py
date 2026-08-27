#!/usr/bin/env python3
"""tools/security-scanners/secret_scan.py — offline secret scan wrapper (scaffold).

GUARDRAIL AKTIF — savunma-only, secret-redakte, exploit-yok.

Turkce not: Verilen dosya/dizinde olasi gizli-bilgi desenlerini arar ve REDAKTE
bulgular yazar (deger asla yazilmaz). Bagimliliksiz (stdlib), agsiz. CLI kullanim
icin; hook surumu icin `scripts/secret_scan.py`e bakin.

Usage:
    python3 tools/security-scanners/secret_scan.py [PATH ...]

TODO / DOC-VERIFY:
- Extend patterns from an authoritative source (e.g. gitleaks/trufflehog rulesets)
  and VERIFY against official docs before production.
- This scaffold intentionally installs nothing and makes no network calls.
"""
import os
import re
import sys

# Reuse the same conservative pattern set as the hook version.
SECRET_PATTERNS = [
    ("aws_access_key_id", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("private_key_block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")),
    ("gh_token", re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}")),
    ("slack_token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("google_api_key", re.compile(r"AIza[0-9A-Za-z_\-]{35}")),
    ("generic_secret_assignment", re.compile(
        r"(?i)(api[_-]?key|secret|password|passwd|token|access[_-]?key|client[_-]?secret)"
        r"\s*[:=]\s*[\"']?([^\s\"']{6,})")),
]
SAFE_REF = re.compile(r"\$\{[^}]+\}|vault://|op://|<REDACTED>|process\.env|os\.environ")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".cache", "dist"}


def scan_file(path):
    findings = []
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh, 1):
                if SAFE_REF.search(line):
                    continue
                for name, pat in SECRET_PATTERNS:
                    if pat.search(line):
                        # REDACTED: path:line + pattern name only, never the value.
                        findings.append(f"{name} {path}:{i} <REDACTED>")
                        break
    except Exception:
        pass
    return findings


def walk(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for f in files:
                    yield os.path.join(root, f)


def main(argv):
    paths = argv[1:] or ["."]
    total = []
    for f in walk(paths):
        total.extend(scan_file(f))
    if total:
        print(f"[secret_scan] {len(total)} finding(s) (REDACTED — no values shown):")
        for ln in total:
            print("  -", ln)
        print("Fix: reference ${VAR} / vault:// / op://; rotate any exposed secret.")
        # Non-zero so CI can gate; but never leak values.
        return 1
    print("[secret_scan] no findings (scaffold, stdlib-only, offline).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
