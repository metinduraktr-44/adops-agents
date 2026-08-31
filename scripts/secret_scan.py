#!/usr/bin/env python3
"""Cursor afterFileEdit hook — secret hygiene scanner (fail-open, advisory).

GUARDRAIL AKTIF — savunma-only, secret-redakte, exploit-yok.

Türkçe not: Düzenlenen dosyada olası gizli anahtar/kimlik bilgisi desenlerini
arar; bulgularını SECURITY_STATE.md yanındaki QA/secret-scan.log'a REDAKTE ederek
yazar ve ajanı uyarır. Gerçek/dummy secret değeri ASLA log'a yazılmaz — yalnızca
dosya + satır + desen adı. Ajanı bloklamaz (fail-open); her zaman exit 0.

Behavior
--------
- Reads the afterFileEdit hook payload as JSON from stdin.
- Resolves the edited file path from common payload shapes.
- Scans the file for well-known secret/credential patterns (API keys, private
  keys, tokens, connection strings, generic assigned secrets).
- Skips values that are already safe references: ${VAR}, vault://, op://, or
  <REDACTED>.
- Appends REDACTED findings (path:line + pattern name only, never the value) to
  QA/secret-scan.log.
- Emits advisory hook JSON on stdout; NEVER blocks (allow). Always exits 0.

This is a defensive skeleton. It detects and warns; it does not exfiltrate,
transmit, or store real secret material.
"""
import sys
import os
import json
import re
import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(REPO_ROOT, "QA", "secret-scan.log")

# Files whose mere presence (by name) warrants a warning.
SENSITIVE_NAMES = re.compile(
    r"(^|/)(\.env(\..+)?|credentials|.*\.pem|.*\.key|id_rsa|id_dsa|id_ecdsa|id_ed25519)$",
    re.IGNORECASE,
)

# Detection patterns. Names only are logged, never captured values.
SECRET_PATTERNS = [
    ("aws_access_key_id", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("private_key_block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")),
    ("gh_token", re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}")),
    ("slack_token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("google_api_key", re.compile(r"AIza[0-9A-Za-z_\-]{35}")),
    ("jwt", re.compile(r"eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}")),
    ("bearer_token", re.compile(r"(?i)bearer\s+[A-Za-z0-9._\-]{20,}")),
    ("connection_string_pw", re.compile(r"(?i)(?:postgres|mysql|mongodb(?:\+srv)?|redis)://[^\s:@/]+:[^\s@/]+@")),
    ("generic_secret_assignment", re.compile(
        r"(?i)(api[_-]?key|secret|password|passwd|token|access[_-]?key|client[_-]?secret)"
        r"\s*[:=]\s*[\"']?([^\s\"']{6,})"
    )),
]

# Safe references that must NOT be treated as secrets.
SAFE_REF = re.compile(r"\$\{[^}]+\}|vault://|op://|<REDACTED>|process\.env|os\.environ")


def _now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _read_stdin():
    try:
        raw = sys.stdin.read()
    except Exception:
        return {}
    raw = (raw or "").strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except Exception:
        return {}


def _resolve_path(payload):
    """Best-effort extraction of the edited file path from the hook payload."""
    if not isinstance(payload, dict):
        return None
    for key in ("file_path", "filePath", "path"):
        val = payload.get(key)
        if isinstance(val, str) and val:
            return val
    # Nested shapes: {"file": {"path": ...}} or {"edit": {"file_path": ...}}
    for outer in ("file", "edit", "arguments", "args"):
        sub = payload.get(outer)
        if isinstance(sub, dict):
            for key in ("file_path", "filePath", "path"):
                val = sub.get(key)
                if isinstance(val, str) and val:
                    return val
    return None


def _log(lines):
    """Append REDACTED finding lines to the scan log; never raise."""
    if not lines:
        return
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as fh:
            for ln in lines:
                fh.write(ln + "\n")
    except Exception:
        pass


def _scan_file(path):
    """Return a list of REDACTED finding strings (path:line pattern), no values."""
    findings = []
    abspath = path if os.path.isabs(path) else os.path.join(REPO_ROOT, path)
    rel = os.path.relpath(abspath, REPO_ROOT) if os.path.exists(abspath) else path

    if SENSITIVE_NAMES.search(path):
        findings.append(f"{_now()} WARN sensitive-filename {rel} <REDACTED>")

    if not os.path.isfile(abspath):
        return findings

    try:
        with open(abspath, encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh, start=1):
                if SAFE_REF.search(line):
                    continue
                for name, pat in SECRET_PATTERNS:
                    if pat.search(line):
                        # Log ONLY path:line + pattern name. Never the value.
                        findings.append(f"{_now()} FINDING {name} {rel}:{i} <REDACTED>")
                        break
    except Exception:
        return findings
    return findings


def main():
    findings = []
    try:
        payload = _read_stdin()
        path = _resolve_path(payload)
        if path:
            findings = _scan_file(path)
            _log(findings)
    except Exception:
        findings = []

    # Advisory only. Fail-open: always allow, never block on secret scan.
    try:
        if findings:
            msg = (
                f"secret_scan: {len(findings)} potansiyel gizli-bilgi bulgusu "
                f"(REDAKTE) → QA/secret-scan.log. ${{VAR}}/vault://op:// kullanın."
            )
            sys.stdout.write(json.dumps({"permission": "allow", "userMessage": msg}))
        else:
            sys.stdout.write("{}")
    except Exception:
        try:
            sys.stdout.write("{}")
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
