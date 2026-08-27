#!/usr/bin/env python3
"""Generate Security GIGA pack scaffolds (idempotent).

Defense-only. No exploit/PoC content. K-003: no 900k blob, no invented top-100.
Usage:
  python3 scripts/generate_security_giga_pack.py [--force]
  python3 scripts/generate_security_giga_pack.py --expand-refs
  python3 scripts/generate_security_giga_pack.py --expand-refs --depth-end 11
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TS = "2026-08-27T12:40:00Z"
EXPAND_TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Sourced ONLY from operator prompt (Dan Kaminsky historical note). No invention.
EXPERT_SEEDS = [
    {
        "name": "Dan Kaminsky",
        "role": "DNS/security researcher (historical reference)",
        "source_url": "https://en.wikipedia.org/wiki/Dan_Kaminsky",
        "note": "Historical public figure — defense lessons only; no exploit reproduction",
        "status": "sourced_historical",
    }
]

SECURITY_TITLES = [
    "ciso", "deputy-ciso", "v-ciso", "security-architect", "enterprise-security-architect",
    "cloud-security-architect", "zero-trust-architect", "application-security-lead",
    "product-security-engineer", "devsecops-lead", "secops-manager", "soc-manager",
    "detection-engineer", "threat-hunter", "incident-response-lead", "forensics-analyst",
    "vulnerability-manager", "penetration-test-coordinator", "red-team-liaison",
    "blue-team-lead", "purple-team-facilitator", "grc-manager", "compliance-officer",
    "privacy-officer", "dpo-liaison", "identity-access-manager", "privileged-access-admin",
    "crypto-engineer", "pqc-migration-lead", "sbom-provenance-owner", "supply-chain-security",
    "cloud-security-posture-analyst", "container-security-engineer", "network-security-engineer",
    "firewall-policy-owner", "data-protection-officer-ops", "security-awareness-lead",
    "security-qa-lead", "third-party-risk-manager", "business-continuity-security",
    "ot-ics-security-liaison", "ai-security-governance", "metrics-reporting-analyst",
]

SKILLS = [
    ("layers-engine", "Defense-in-depth layer controls and mapping templates."),
    ("firewall-engine", "Network/host/app firewall policy templates — defense only."),
    ("encryption-engine", "Crypto controls incl. PQC hybrid TLS — no attack material."),
    ("change-protocol-engine", "Secure change management and CAB security gates."),
    ("transparent-code-engine", "Transparent code review, SBOM, provenance checks."),
    ("conditional-policy-engine", "Conditional access and policy-as-code templates."),
    ("expert-engine", "Expert queue research — sourced seeds + pending_research only."),
    ("threat-modeling", "STRIDE/LINDDUN-style threat modeling — defend/detect focus."),
    ("compliance-mapper", "Map controls to NIST/ISO/CIS/OWASP — draft needs review."),
    ("incident-response", "IR playbooks aligned to detect/contain/recover."),
    ("secret-hygiene", "Secret scanning, vault patterns, redact-only handling."),
    ("zero-trust-architect", "NIST 800-207 / CISA ZTMM 2.0 architecture templates."),
    ("crypto-agility", "Crypto agility and PQC migration planning (FIPS 203/204/205)."),
    ("sbom-provenance", "SBOM, SLSA v1.0 provenance, supply-chain attestations."),
    ("iam-hardening", "IAM least-privilege, MFA, PAM hardening checklists."),
    ("cloud-security-posture", "CSPM baselines and misconfiguration defense."),
    ("detection-engineering", "Detection rules & ATT&CK→D3FEND mapping — no offense."),
    ("vulnerability-management", "Vuln intake, triage, SLA, exception workflow."),
    ("privacy-engineering", "Privacy-by-design controls and DPIA stubs."),
    ("security-qa", "Security QA gates for ASSESS/IMPLEMENT modes."),
]

CONTROL_FAMILIES = {
    "LAYERS": {
        "prefix": "LYR",
        "themes": [
            "perimeter", "network-seg", "host-hardening", "app-layer", "data-layer",
            "identity-layer", "endpoint", "cloud-control-plane", "ot-boundary", "people-process",
        ],
    },
    "FIREWALLS": {
        "prefix": "FW",
        "themes": [
            "ingress", "egress", "east-west", "waf", "host-fw",
            "dns-filter", "api-gw", "ot-fw", "cloud-sg", "policy-as-code",
        ],
    },
    "ENCRYPTION": {
        "prefix": "ENC",
        "themes": [
            "tls-baseline", "pqc-hybrid", "at-rest", "key-mgmt", "hsm",
            "transit", "messaging", "backup-crypto", "tokenisation", "crypto-agility",
        ],
    },
    "CHANGE": {
        "prefix": "CHG",
        "themes": [
            "cab-gate", "emergency-change", "rollback", "config-drift", "iac-review",
            "privileged-change", "vendor-change", "window-mgmt", "post-impl-verify", "audit-trail",
        ],
    },
    "TRANSPARENT_CODE": {
        "prefix": "TC",
        "themes": [
            "code-review", "sast", "dast-scope", "sbom", "slsa",
            "signing", "dependency-pin", "license-scan", "secrets-in-ci", "reproducible-build",
        ],
    },
    "CONDITIONAL": {
        "prefix": "COND",
        "themes": [
            "mfa-stepup", "device-trust", "geo-risk", "session-risk", "workload-attest",
            "just-in-time", "break-glass", "policy-exception", "continuous-auth", "context-acl",
        ],
    },
}

# Draft mapping pools — flagged needs_expert_review; not production-certified.
NIST_CSF = ["GV.OC", "GV.RM", "GV.RR", "ID.AM", "ID.RA", "PR.AA", "PR.DS", "PR.PS",
            "PR.IR", "DE.CM", "DE.AE", "RS.MA", "RS.AN", "RS.MI", "RC.RP"]
SP80053 = [f"AC-{i}" for i in range(1, 25)] + [f"SC-{i}" for i in range(1, 29)] + \
          [f"SI-{i}" for i in range(1, 21)] + [f"AU-{i}" for i in range(1, 17)] + \
          [f"CM-{i}" for i in range(1, 15)] + [f"IA-{i}" for i in range(1, 13)] + \
          [f"IR-{i}" for i in range(1, 11)] + [f"RA-{i}" for i in range(1, 10)] + \
          [f"SA-{i}" for i in range(1, 23)] + [f"SR-{i}" for i in range(1, 12)]
# Ensure pool length covers 1189–1196 range note via documentation, not claim of exact count.
ISO27001 = ["A.5.1", "A.5.15", "A.5.23", "A.8.2", "A.8.3", "A.8.8", "A.8.9", "A.8.15",
            "A.8.16", "A.8.20", "A.8.24", "A.8.25", "A.8.26", "A.8.28", "A.8.32"]
CIS = [f"CIS-{i}" for i in range(1, 19)]
OWASP = ["V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10",
         "V11", "V12", "V13", "V14"]

PQC_NOTE_IDS = {1, 2, 11, 12, 21, 22, 31, 32, 41, 42, 51, 52, 61, 62, 71, 72, 81, 82, 91, 92}


def write_if_needed(path: Path, content: str, force: bool) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        existing = path.read_text(encoding="utf-8")
        if existing == content:
            return False
        # Keep hand-authored richer files if longer and not force
        if len(existing) > len(content) + 200 and "HAND_AUTHORED" in existing:
            return False
    path.write_text(content, encoding="utf-8")
    return True


def skill_md(name: str, desc: str) -> str:
    return f"""---
name: {name}
description: {desc}
---

# {name}

> TR: Savunma-only skill. Keşfedilmezse inline path kullan.
> Damga: {TS}

## Guardrail
- **DEFENSE-ONLY** — no exploit, PoC, bypass, phishing, C2, ransomware.
- ATT&CK only for detect/defend mapping; prefer **D3FEND**.
- Secrets: `${{VAR}}`, `vault://`, `op://`, `<REDACTED>` only.
- K-003: no 900k blob; expand via `references/` + generator.

## If skill not discovered (inline path)
1. Read `docs/CURSOR-SECURITY-GIGA-MASTER-PROMPT.md`
2. Read `SECURITY_STATE.md` (MODE default ASSESS-ONLY)
3. Open `references/` in this skill folder
4. Prefer `/sec-*` commands over free-form offense requests

## Progressive disclosure
- `references/overview.md` — scope + ethics
- `references/control-templates.md` — control field schema
- `references/playbook.md` — operator steps for ASSESS→IMPLEMENT
- `references/standards.md` — version-pinned standards table
- `references/d3fend-map.md` — defense mapping stubs

## Outputs
- ASSESS-ONLY: gap notes under `ASSESSMENTS/`
- IMPLEMENT: only when `SECURITY_STATE.md` MODE=IMPLEMENT (stubs first)
"""


def ref_overview(name: str) -> str:
    return f"""# {name} — Overview

> status: draft · needs_expert_review · damga: {TS}

## Purpose
Progressive reference for **{name}**. Defense posture only.

## Ethics
Refuse weaponization. Map threats to **controls, detections, recovery**.

## Related paths
- Controls: `LAYERS/` `FIREWALLS/` `ENCRYPTION/` `CHANGE/` `TRANSPARENT_CODE/` `CONDITIONAL/`
- Matrix: `SECURITY_MATRIX/matrix.md`
- State: `SECURITY_STATE.md`
"""


def ref_control_templates(name: str) -> str:
    return f"""# {name} — Control templates

Required fields per control markdown:

| Field | Required |
|---|---|
| id | yes |
| ad | yes |
| açıklama | yes |
| NIST_CSF | yes (draft) |
| 800-53 | yes (draft) |
| ISO27001 | yes (draft) |
| CIS | yes (draft) |
| OWASP | yes (draft) |
| doğrulama_yöntemi | yes |
| savunma_gerekçesi | yes |

All mappings flagged `needs_expert_review` — not production-certified.

## Example stub
```yaml
id: LYR-001
ad: Network segmentation baseline
NIST_CSF: PR.IR
800-53: SC-7
status: draft
```
"""


def ref_playbook(name: str) -> str:
    return f"""# {name} — Playbook

## MODE order
1. **ASSESS-ONLY** (default) — inventory, gap, risk notes
2. **IMPLEMENT** — only after owner flip in SECURITY_STATE.md
3. **AUDIT** — evidence pack + compliance crosswalk

## Steps
1. Read SECURITY_STATE.md
2. Load relevant controls (100× family)
3. Produce ASSESSMENTS/ gap row
4. If IMPLEMENT: write IMPLEMENTATION/ stub + CAB note (CHANGE)
5. Stamp AUDIT_LOG.jsonl + BILGI_TABANI.md

## Restart / MCP
- Cursor restart after new skills/rules
- MCP security catalog entries off until owner enables (`${{VAR}}` only)
"""


def ref_standards() -> str:
    return f"""# Standards version table (pinned)

| Standard | Version / note |
|---|---|
| NIST CSF | 2.0 |
| NIST SP 800-53 | Rev.5 (control catalog size range ~1189–1196 commonly cited; verify against current NIST PDF) |
| ISO/IEC 27001 | 2022 |
| CIS Controls | v8.1 |
| OWASP ASVS | 5.0.0 |
| PQC | FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA) |
| SLSA | v1.0 |
| NIST SP 800-207 | Zero Trust Architecture |
| CISA ZTMM | 2.0 |

> Damga: {TS} · draft crosswalk only
"""


def ref_d3fend() -> str:
    return f"""# D3FEND / ATT&CK usage

- Prefer **D3FEND** techniques for hardening, detection, isolation, deception (defense).
- ATT&CK may appear as **threat coverage labels** only — never as attack how-to.
- Output format: `threat_id → detect_control → prevent_control → recover_control`

Damga: {TS}
"""


def control_md(family: str, prefix: str, n: int, theme: str) -> str:
    idx = n - 1
    csf = NIST_CSF[idx % len(NIST_CSF)]
    sp = SP80053[idx % len(SP80053)]
    iso = ISO27001[idx % len(ISO27001)]
    cis = CIS[idx % len(CIS)]
    owasp = OWASP[idx % len(OWASP)]
    cid = f"{prefix}-{n:03d}"
    pqc = ""
    if family == "ENCRYPTION" and n in PQC_NOTE_IDS:
        pqc = (
            "\n## PQC note\n"
            "- Plan hybrid TLS with classical + ML-KEM (FIPS 203).\n"
            "- Signature agility: ML-DSA (FIPS 204) / SLH-DSA (FIPS 205) migration path.\n"
            "- Defense planning only — no cryptanalysis attack material.\n"
        )
    return f"""# {cid} — {theme} control {n}

| Field | Value |
|---|---|
| id | {cid} |
| ad | {theme.replace('-', ' ').title()} control {n:03d} |
| açıklama | Defense control for {theme} in {family}. Draft template for ASSESS-ONLY gap analysis. |
| NIST_CSF | {csf} |
| 800-53 | {sp} |
| ISO27001 | {iso} |
| CIS | {cis} |
| OWASP | ASVS {owasp} (map refine in review) |
| doğrulama_yöntemi | Config review + evidence sample + negative test of secure behavior (no exploit payload) |
| savunma_gerekçesi | Reduces attack surface / improves detectability / supports recovery for {theme} |
| status | draft · needs_expert_review |
| damga | {TS} |
{pqc}
## Notes
- Crosswalk is **template-reasonable**, not certified.
- MODE=ASSESS-ONLY by default; do not auto-remediate production.
"""


DEPTH_TOPICS = [
    "governance-and-ownership",
    "asset-and-data-classification",
    "identity-and-least-privilege",
    "network-and-segmentation",
    "logging-and-detection",
    "incident-readiness",
    "change-and-cab-gates",
    "supply-chain-and-sbom",
    "crypto-and-key-lifecycle",
    "privacy-and-retention",
    "cloud-posture-baselines",
    "secure-defaults-review",
    "evidence-and-audit-trail",
    "vendor-and-third-party",
    "recovery-and-continuity",
    "metrics-and-kris",
    "exception-and-risk-accept",
    "training-and-awareness",
    "policy-as-code-checks",
    "continuous-improvement",
]


def depth_module_body(name: str, i: int, expand: bool = False) -> str:
    topic = DEPTH_TOPICS[(i - 1) % len(DEPTH_TOPICS)]
    damga = EXPAND_TS if expand else TS
    # Richer progressive modules for expand mode — still per-file, never one blob.
    checklist_n = 28 if expand else 20
    lines = [
        f"# {name} depth module {i:02d} — {topic}\n",
        f"\n> progressive disclosure · defense-only · damga: {damga}\n",
        f"\n## Purpose\n",
        f"Deepen ASSESS-ONLY coverage for `{name}` on topic **{topic}**.\n",
        f"Produce gap rows and evidence pointers — do **not** auto-remediate production.\n",
        f"\n## Ethics\n",
        f"- Refuse weaponization, exploit how-to, phishing lure templates, C2 setup.\n",
        f"- Prefer D3FEND-style detect / harden / isolate / recover wording.\n",
        f"- Secrets: `${{VAR}}` / `vault://` / `<REDACTED>` only.\n",
        f"\n## Operator steps\n",
        f"1. Read `SECURITY_STATE.md` (MODE default ASSESS-ONLY).\n",
        f"2. Sample related controls in family folders; note draft mapping status.\n",
        f"3. Record gaps in `ASSESSMENTS/` with severity + defense recommendation.\n",
        f"4. Stamp learning to `BILGI_TABANI.md` + `AUDIT_LOG.jsonl` when closing a pass.\n",
        f"\n## Checklist\n",
    ]
    for j in range(1, checklist_n + 1):
        lines.append(
            f"- [ ] {topic} item {i}.{j:02d}: verify evidence exists; if missing, open gap; "
            f"document owner; no offensive steps.\n"
        )
    lines += [
        f"\n## Mapping hint\n",
        f"| Framework | Draft pin |\n|---|---|\n",
        f"| NIST CSF 2.0 | {NIST_CSF[i % len(NIST_CSF)]} |\n",
        f"| NIST SP 800-53 Rev.5 | {SP80053[i * 3 % len(SP80053)]} |\n",
        f"| ISO/IEC 27001:2022 | {ISO27001[i % len(ISO27001)]} |\n",
        f"| CIS Controls v8.1 | {CIS[i % len(CIS)]} |\n",
        f"| OWASP ASVS 5.0.0 | {OWASP[i % len(OWASP)]} |\n",
        f"\n## Evidence examples (non-secret)\n",
        f"- Config screenshot / export path (redact tokens)\n",
        f"- CI job name + run id proving gate ran\n",
        f"- Policy markdown link under `docs/` or control id\n",
        f"- Ticket / CAB id for exceptions\n",
        f"\n## Negative tests (secure behavior only)\n",
        f"- Confirm unauthorized path is **denied** in staging (no payload crafting).\n",
        f"- Confirm secret scanner hooks fire on staged files.\n",
        f"- Confirm ethics_check.py clean on authored security content.\n",
        f"\n## Out of scope (forbidden)\n",
        f"Refuse: exploit how-to, credential harvest, auth bypass instructions, malware generation.\n",
        f"\n## K-003\n",
        f"This is one progressive module — aggregate coverage via many files, never a 900k single prompt.\n",
    ]
    if expand:
        lines += [
            f"\n## Scenario notes ({topic})\n",
            f"For AdOps Agents (markdown/Python component pack + GitHub Actions):\n",
            f"- Map `{topic}` to repo surfaces: `.github/workflows/`, `scripts/`, `.cursor/`, `data/`.\n",
            f"- Holding OpCos inherit shared controls; country LLM agencies need privacy overlays.\n",
            f"- Canva/creative GIGA files coexist — do not delete; security uses `SECURITY_STATE.md`.\n",
            f"- MCP security catalog stays **off** until owner Authorize with `${{VAR}}` only.\n",
            f"\n## Review flags\n",
            f"- status: draft · needs_expert_review\n",
            f"- MODE: ASSESS-ONLY unless owner flips `SECURITY_STATE.md`\n",
        ]
    return "".join(lines)


def generate_skills(force: bool, depth_end: int = 5) -> int:
    n = 0
    for name, desc in SKILLS:
        base = ROOT / ".cursor" / "skills" / name
        refs = base / "references"
        for rel, body in [
            ("SKILL.md", skill_md(name, desc)),
            ("references/overview.md", ref_overview(name)),
            ("references/control-templates.md", ref_control_templates(name)),
            ("references/playbook.md", ref_playbook(name)),
            ("references/standards.md", ref_standards()),
            ("references/d3fend-map.md", ref_d3fend()),
        ]:
            if write_if_needed(base / rel if rel == "SKILL.md" else refs / Path(rel).name, body, force):
                n += 1
        for i in range(1, depth_end + 1):
            extra = refs / f"depth-{i:02d}.md"
            expand = i > 5
            body = depth_module_body(name, i, expand=expand)
            if write_if_needed(extra, body, force):
                n += 1
    return n


def expand_skill_refs(force: bool, depth_start: int, depth_end: int) -> int:
    """Add progressive depth modules (K-003: many files, no single 900k blob)."""
    n = 0
    for name, _desc in SKILLS:
        refs = ROOT / ".cursor" / "skills" / name / "references"
        refs.mkdir(parents=True, exist_ok=True)
        for i in range(depth_start, depth_end + 1):
            path = refs / f"depth-{i:02d}.md"
            body = depth_module_body(name, i, expand=True)
            if write_if_needed(path, body, force):
                n += 1
    return n


def generate_controls(force: bool) -> int:
    n = 0
    for family, meta in CONTROL_FAMILIES.items():
        themes = meta["themes"]
        prefix = meta["prefix"]
        for i in range(1, 101):
            theme = themes[(i - 1) % len(themes)]
            path = ROOT / family / f"{prefix}-{i:03d}.md"
            if write_if_needed(path, control_md(family, prefix, i, theme), force):
                n += 1
        readme = ROOT / family / "README.md"
        body = (
            f"# {family}\n\n100 draft controls (`{prefix}-001`…`{prefix}-100`).\n"
            f"Mappings: needs_expert_review. Damga: {TS}\n"
        )
        if write_if_needed(readme, body, force):
            n += 1
    return n


def generate_roles(force: bool) -> int:
    n = 0
    roles_dir = ROOT / "ORG" / "ROLES"
    for title in SECURITY_TITLES:
        path = roles_dir / f"{title}.md"
        body = f"""# Role: {title}

| Field | Value |
|---|---|
| title | {title} |
| responsibility | Own defense outcomes for `{title}` scope; escalate ethics/secret risks |
| outputs | ASSESSMENTS notes, control evidence pointers, IR/compliance artifacts as applicable |
| mode_default | ASSESS-ONLY |
| reports_to | ciso (logical; not org.json resize) |
| damga | {TS} |

## Notes (TR)
ORG/ROLES güvenlik unvanları — `data/org.json` 600 boyutu değiştirilmez.
"""
        if write_if_needed(path, body, force):
            n += 1
    idx = roles_dir / "README.md"
    body = (
        f"# ORG/ROLES — Security titles\n\n"
        f"Count: {len(SECURITY_TITLES)} · Not part of org.json 600 resize.\n"
        f"Damga: {TS}\n\n"
        + "\n".join(f"- `{t}.md`" for t in SECURITY_TITLES)
        + "\n"
    )
    if write_if_needed(idx, body, force):
        n += 1
    return n


def generate_experts(force: bool) -> int:
    n = 0
    # Shared security expert queue + per-discipline thin folders
    disciplines = [
        "sec-architecture", "sec-appsec", "sec-cloud", "sec-iam", "sec-crypto",
        "sec-detection", "sec-ir", "sec-grc", "sec-privacy", "sec-supply-chain",
    ]
    for disc in disciplines:
        d = ROOT / "EXPERTS" / disc
        seed = {
            "title": disc,
            "policy": "sourced_only_plus_pending_research",
            "seeds": EXPERT_SEEDS if disc == "sec-architecture" else [],
            "note": "Only prompt-listed sourced names. Empty preferred over invention.",
            "damga": TS,
        }
        pending = {
            "title": disc,
            "target_slots": 100,
            "filled_sourced": len(seed["seeds"]),
            "slots": [
                {"slot": i, "status": "pending_research", "query_hint": f"{disc} public expert source needed"}
                for i in range(len(seed["seeds"]) + 1, 101)
            ],
            "damga": TS,
        }
        for name, obj in [("seed.json", seed), ("pending_research.json", pending)]:
            path = d / name
            body = json.dumps(obj, indent=2, ensure_ascii=False) + "\n"
            if write_if_needed(path, body, force):
                n += 1
    readme = ROOT / "EXPERTS" / "README.md"
    body = f"""# EXPERTS — Security queues (K-003)

- Sourced seeds only (prompt-listed). Current seed: **Dan Kaminsky** (historical).
- All other slots: `pending_research` to 100 — **never invent**.
- Damga: {TS}

🚩 Live invent top-100 · hallucination · use sourced+pending queues
"""
    if write_if_needed(readme, body, force):
        n += 1
    return n


def generate_matrix(force: bool) -> int:
    path = ROOT / "SECURITY_MATRIX" / "matrix.md"
    body = f"""# SECURITY_MATRIX — Crosswalk (draft)

> status: draft · needs_expert_review · damga: {TS}

## Coverage

| Family | Count | Prefix | Notes |
|---|---|---|---|
| LAYERS | 100 | LYR | Defense-in-depth |
| FIREWALLS | 100 | FW | Policy templates |
| ENCRYPTION | 100 | ENC | Includes PQC hybrid TLS controls |
| CHANGE | 100 | CHG | Secure change |
| TRANSPARENT_CODE | 100 | TC | SBOM/SLSA |
| CONDITIONAL | 100 | COND | Conditional access |

**Total:** 600 draft controls.

## Standards pins
See skill `references/standards.md` — NIST CSF 2.0, 800-53 Rev.5 (~1189–1196 range note),
ISO 27001:2022, CIS v8.1, OWASP ASVS 5.0.0, FIPS 203/204/205, SLSA v1.0, NIST 800-207, CISA ZTMM 2.0.

## Coverage gaps (initial)
- [ ] Exact 800-53 Rev.5 control-to-enhancement enumeration (verify NIST PDF)
- [ ] ASVS 5.0.0 chapter-level binding per app tier
- [ ] ZTMM 2.0 pillar maturity scoring
- [ ] Expert review of PQC hybrid deployment assumptions

## Red flags
🚩 900k single-file prompt · mega expander + phased refs
🚩 Invented top-100 experts · sourced+pending only
🚩 Exploit/PoC · ethics · defense-only
"""
    return 1 if write_if_needed(path, body, force) else 0


def ensure_dirs() -> None:
    dirs = [
        "SECURITY_CONTEXT", "SECURITY_RESEARCH", "TASKS", "ORG/ROLES", "EXPERTS",
        "LAYERS", "FIREWALLS", "ENCRYPTION", "CHANGE", "TRANSPARENT_CODE", "CONDITIONAL",
        "SECURITY_MATRIX", "IMPLEMENTATION", "ASSESSMENTS", "COMPLIANCE", "ARCHIVE",
        "CALENDAR", "QA", "MEMORY", "REPORTS",
        "tools/security-scanners",
        ".cursor/hooks", ".cursor/commands", ".cursor/agents", ".cursor/plans",
    ]
    for d in dirs:
        (ROOT / d).mkdir(parents=True, exist_ok=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument(
        "--expand-refs",
        action="store_true",
        help="Write progressive depth-NN.md modules toward ~900k aggregate skill refs",
    )
    ap.add_argument("--depth-start", type=int, default=6, help="First depth module for --expand-refs")
    ap.add_argument("--depth-end", type=int, default=11, help="Last depth module (inclusive); ~900k aggregate target")
    ap.add_argument("--scaffold-only", action="store_true", help="Skip controls/roles when expanding")
    args = ap.parse_args()
    ensure_dirs()
    counts: dict = {}
    if args.expand_refs:
        counts["expand_refs"] = expand_skill_refs(args.force, args.depth_start, args.depth_end)
        # Also refresh base depth 1-5 bodies if force
        if args.force:
            counts["skills_base"] = generate_skills(True, depth_end=5)
    if not args.expand_refs or not args.scaffold_only:
        if not args.expand_refs:
            counts["skills"] = generate_skills(args.force, depth_end=5)
            counts["controls"] = generate_controls(args.force)
            counts["roles"] = generate_roles(args.force)
            counts["experts"] = generate_experts(args.force)
            counts["matrix"] = generate_matrix(args.force)
    print(json.dumps({"ok": True, "written_or_updated": counts, "damga": EXPAND_TS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
