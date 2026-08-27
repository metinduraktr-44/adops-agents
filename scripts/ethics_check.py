#!/usr/bin/env python3
"""Cursor afterFileEdit hook — defense-only ethics guardrail (fail-open on error).

GUARDRAIL AKTIF — savunma-only, secret-redakte, exploit-yok.

Türkçe not: Düzenlenen dosyada saldırgan/silahlandırma (weaponization) desenleri
arar — çalışan exploit, C2, ransomware kripto rutini, veri sızdırma aracı,
phishing kiti, güvenlik-atlatma (bypass) kodu. İhlal bulursa hook JSON ile
"ask" döndürür (kullanıcı onayı ister) ve QA/ethics-check.log'a yazar. Hata
durumunda fail-open (allow). Salt savunma; ATT&CK yalnızca tespit/karşı-önlem
eşlemesi için, D3FEND önceliklidir.

Behavior
--------
- Reads the afterFileEdit hook payload as JSON from stdin.
- Scans the edited file for offensive/weaponization indicators.
- On a match: logs a REDACTED note and returns {"permission":"ask", ...} so a
  human confirms intent. This is conservative, not a hard block, to avoid false
  positives on legitimate defensive/detection content (which references these
  concepts descriptively).
- On no match or any error: {} / allow. Always exits 0 (fail-open).

Scope note: this hook exists to KEEP the security-governance OS defensive. It
flags content that reads like working attack tooling so it can be reviewed and
kept at an authorized, conceptual, detection-focused level.
"""
import sys
import os
import json
import re
import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(REPO_ROOT, "QA", "ethics-check.log")

# Indicators that a file may contain offensive / weaponized tooling rather than
# defensive, conceptual, or detection-oriented content. Kept intentionally
# high-signal to reduce false positives on legitimate defensive material.
OFFENSIVE_PATTERNS = [
    ("reverse_shell", re.compile(r"(?i)reverse[_\s-]?shell|bind[_\s-]?shell")),
    ("shellcode", re.compile(r"(?i)\bshellcode\b|msfvenom|\bmeterpreter\b")),
    ("c2_framework", re.compile(r"(?i)\b(cobalt\s?strike|command[_\s-]and[_\s-]control|c2\s+beacon|empire\s+agent)\b")),
    ("ransomware_routine", re.compile(r"(?i)\bransomware\b.*(encrypt|payload)|encrypt.*\bransom\b")),
    ("exfiltration_tool", re.compile(r"(?i)(data[_\s-]?exfiltration|exfiltrate).*(script|tool|payload|automate)")),
    ("phishing_kit", re.compile(r"(?i)phishing\s?(kit|page\s+clone|credential\s+harvest)")),
    ("exploit_weaponize", re.compile(r"(?i)(weaponize|weaponization)\b|working\s+exploit\s+for")),
    ("privilege_bypass_code", re.compile(r"(?i)(auth(entication)?|security|sandbox|kaspersky|edr|av)\s+bypass\s+(code|payload|technique\s+that\s+works)")),
]

# Defensive context that DOWNGRADES a flag (these terms indicate the mention is
# for detection / mapping / mitigation, i.e. allowed conceptual coverage).
DEFENSIVE_CONTEXT = re.compile(
    r"(?i)\b(D3FEND|detection|detect|mitigat|countermeasure|defen[sc]e|"
    r"blue\s?team|SIEM|SOC|EDR\s+rule|sigma\s+rule|yara|hunt|MITRE\s+ATT&CK\s+mapping)\b"
)


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
    if not isinstance(payload, dict):
        return None
    for key in ("file_path", "filePath", "path"):
        val = payload.get(key)
        if isinstance(val, str) and val:
            return val
    for outer in ("file", "edit", "arguments", "args"):
        sub = payload.get(outer)
        if isinstance(sub, dict):
            for key in ("file_path", "filePath", "path"):
                val = sub.get(key)
                if isinstance(val, str) and val:
                    return val
    return None


def _log(lines):
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
    """Return (violations, findings). Violations survive defensive-context downgrade."""
    findings = []
    abspath = path if os.path.isabs(path) else os.path.join(REPO_ROOT, path)
    rel = os.path.relpath(abspath, REPO_ROOT) if os.path.exists(abspath) else path
    if not os.path.isfile(abspath):
        return [], findings
    try:
        with open(abspath, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except Exception:
        return [], findings

    file_is_defensive = bool(DEFENSIVE_CONTEXT.search(text))
    for name, pat in OFFENSIVE_PATTERNS:
        for m in pat.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            # Look at the surrounding line for local defensive context.
            line_start = text.rfind("\n", 0, m.start()) + 1
            line_end = text.find("\n", m.end())
            line_end = len(text) if line_end == -1 else line_end
            local = text[line_start:line_end]
            downgraded = file_is_defensive or bool(DEFENSIVE_CONTEXT.search(local))
            tag = "REVIEW(defensive-context)" if downgraded else "VIOLATION"
            findings.append(f"{_now()} {tag} {name} {rel}:{line_no}")
            if not downgraded:
                findings.append(f"{_now()} -> flagged for human review (ask)")
                return [name], findings
    return [], findings


def main():
    violations = []
    findings = []
    try:
        payload = _read_stdin()
        path = _resolve_path(payload)
        if path:
            violations, findings = _scan_file(path)
            _log(findings)
    except Exception:
        # Fail-open: never block the agent because of a scanner error.
        violations = []

    try:
        if violations:
            msg = (
                "ethics_check: olası saldırgan/silahlandırma içeriği tespit edildi "
                f"({', '.join(violations)}). Savunma-only ilkesi gereği insan onayı "
                "gerekli. Yalnızca yetkili, kavramsal, tespit-odaklı içerik üretin."
            )
            sys.stdout.write(json.dumps({"permission": "ask", "userMessage": msg}))
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
