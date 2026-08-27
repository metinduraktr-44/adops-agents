#!/usr/bin/env python3
"""tools/security-scanners/control_validate.py — control mapping validator (scaffold).

GUARDRAIL AKTIF — savunma-only, secret-redakte, exploit-yok.

Turkce not: 6x100 kontrol cercevesi dosyalarindaki kontrol satirlarinin zorunlu
standart-eslemesi alanlarini tasiyip tasimadigini dogrular (bkz.
`.cursor/rules/20-control-mapping.mdc`). Bagimliliksiz, agsiz, salt-okur.

Required fields per control row: id, ad, NIST_CSF, 800-53, ISO27001,
doğrulama_yöntemi, savunma_gerekçesi (CIS/OWASP where applicable).

Usage:
    python3 tools/security-scanners/control_validate.py LAYERS/ FIREWALLS/ ...

TODO / DOC-VERIFY:
- This scaffold checks for field PRESENCE, not correctness of the mapped ids.
- VERIFY actual standard ids/versions against official sources before production.
"""
import os
import re
import sys

REQUIRED = ["id", "ad", "NIST_CSF", "800-53", "ISO27001", "doğrulama_yöntemi", "savunma_gerekçesi"]
FRAMEWORK_DIRS = ["LAYERS", "FIREWALLS", "ENCRYPTION", "CHANGE", "TRANSPARENT_CODE", "CONDITIONAL"]

# A control row is any markdown table row that looks like a control (starts with an id like ABC-001).
ROW_ID = re.compile(r"\b[A-Z]{2,4}-\d{2,4}\b")


def check_file(path):
    """Return list of (line_no, missing_fields) for suspicious control rows."""
    issues = []
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except Exception:
        return issues
    # Presence check is document-level here (schema stubs list fields once).
    # For real filled control files, extend to per-row parsing.
    lower = text
    missing = [f for f in REQUIRED if f not in lower]
    if ROW_ID.search(text) and missing:
        issues.append((0, missing))
    return issues


def main(argv):
    targets = argv[1:] or FRAMEWORK_DIRS
    any_issue = False
    for t in targets:
        if not os.path.exists(t):
            print(f"[control_validate] skip (missing): {t}")
            continue
        files = []
        if os.path.isdir(t):
            for root, _, fs in os.walk(t):
                files += [os.path.join(root, f) for f in fs if f.endswith(".md")]
        else:
            files = [t]
        for f in files:
            for line_no, missing in check_file(f):
                any_issue = True
                print(f"[control_validate] {f}: missing required field(s): {', '.join(missing)}")
    if not any_issue:
        print("[control_validate] OK — required mapping fields present (scaffold; verify ids vs official docs).")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
