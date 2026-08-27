# CURSOR SECURITY GIGA MASTER PROMPT — Defense-Only Security Operating System

> Damga: 2026-08-27T12:40:00Z · **In-repo apply** — Claude Code paste İPTAL (K-003).
> TR: Yoğun operatör promptu; tek 900k blob **üretilmez**. Progressive `references/` + generator.

---

## 0 — Amaç / Purpose

Performance Growth Holding / adops-agents altında **savunma odaklı** güvenlik işletim sistemi:

- ASSESS → (opsiyonel) IMPLEMENT → AUDIT döngüsü
- Kontrol aileleri: LAYERS · FIREWALLS · ENCRYPTION · CHANGE · TRANSPARENT_CODE · CONDITIONAL
- Standart çapraz yürüyüş (draft): NIST CSF 2.0, 800-53 Rev.5, ISO 27001:2022, CIS v8.1, OWASP ASVS 5.0.0, PQC FIPS 203/204/205, SLSA v1.0, NIST 800-207, CISA ZTMM 2.0
- Mevcut pack ile yan yana: Canva/GIGA creative kuralları silinmez; security pack co-exists

---

## 0.5 — BAŞLAT

```text
1. SECURITY_STATE.md oku → MODE (default ASSESS-ONLY)
2. docs/SECURITY-GIGA-BOOTSTRAP.md
3. /sec-baslat  (alias: güvenlik oturumu başlat)
4. Inventory: SECURITY_CONTEXT/inventory.md + attack-surface.md (defense perspective)
5. Gap: ASSESSMENTS/ · Matrix: SECURITY_MATRIX/matrix.md
6. Stamp AUDIT_LOG + BILGI_TABANI
```

**Cursor restart** after first pull of skills/rules. MCP security entries **off** until owner enables.

---

## 1 — MODE flags

| MODE | Flag | Behavior |
|---|---|---|
| **ASSESS-ONLY** | default | Inventory, gaps, risk notes, control draft review — **no live remediations** |
| **IMPLEMENT** | owner flip | IMPLEMENTATION/ stubs → reviewed changes; CAB via CHANGE controls |
| **AUDIT** | evidence | Compliance pack, crosswalk evidence, ARCHIVE snapshot |

Order: always **assess → implement → audit**. Never skip assess for production mutation.

---

## 2 — Ethics guardrail (HARD)

**DEFENSE-ONLY.** Refuse:
- Exploit code, PoCs, bypass recipes, phishing content, C2, ransomware, weaponization
- Credential exfil patterns, `rm -rf /`, `curl|bash` in executable scripts
- Real or dummy-realistic secrets — only `${VAR}`, `vault://`, `op://`, `<REDACTED>`

ATT&CK: **detect/defend mapping only**. Prefer **D3FEND**.

Ethics agent: `.cursor/agents/ethics-checker.md` · command `/sec-etik-denetim`

---

## 3 — Hybrid skill / inline rule

| Situation | Action |
|---|---|
| Skill discovered under `.cursor/skills/<name>/` | Follow SKILL.md + `references/` |
| Skill not discovered | Inline: this doc → SECURITY_STATE.md → family controls → ASSESSMENTS |
| Ambiguous offense request | ethics-checker refuse + offer defense alternative |

Skills (20): layers-engine, firewall-engine, encryption-engine, change-protocol-engine, transparent-code-engine, conditional-policy-engine, expert-engine, threat-modeling, compliance-mapper, incident-response, secret-hygiene, zero-trust-architect, crypto-agility, sbom-provenance, iam-hardening, cloud-security-posture, detection-engineering, vulnerability-management, privacy-engineering, security-qa.

---

## 4 — Phase plan (Faz 0 → partial 4)

| Faz | Ad | Durum hedefi |
|---|---|---|
| 0 | Bootstrap rules/commands/hooks/scripts | DONE (this pack) |
| 1 | Context ingestion + attack-surface (defense) | scaffold |
| 2 | 6×100 controls + matrix | generated draft |
| 3 | Experts queues + ORG/ROLES | sourced+pending |
| 4 | ASSESS gap template + scanner stubs | partial scaffold |
| 5+ | IMPLEMENT/AUDIT loops | blocked until MODE flip |

---

## 5 — Standards version table

| Standard | Pin |
|---|---|
| NIST CSF | **2.0** |
| NIST SP 800-53 | **Rev.5** — catalog size commonly cited **~1189–1196**; verify current NIST PDF before audit claims |
| ISO/IEC 27001 | **2022** |
| CIS Controls | **v8.1** |
| OWASP ASVS | **5.0.0** |
| PQC | **FIPS 203** (ML-KEM), **FIPS 204** (ML-DSA), **FIPS 205** (SLH-DSA); hybrid TLS planning |
| SLSA | **v1.0** |
| NIST SP 800-207 | Zero Trust Architecture |
| CISA ZTMM | **2.0** |

Mappings in controls = **draft / needs_expert_review** — not production-certified accuracy.

---

## 6 — File tree (canonical)

```
SECURITY_CONTEXT/   SECURITY_RESEARCH/   TASKS/
ORG/ROLES/          EXPERTS/
LAYERS/ FIREWALLS/ ENCRYPTION/ CHANGE/ TRANSPARENT_CODE/ CONDITIONAL/
SECURITY_MATRIX/    IMPLEMENTATION/   ASSESSMENTS/   COMPLIANCE/
ARCHIVE/ CALENDAR/ QA/ MEMORY/ REPORTS/
SECURITY_STATE.md   (pointer from STATE.md if creative STATE exists)
tools/security-scanners/
```

---

## 7 — Commands (sec-* to avoid Canva conflict)

| Command | Alias intent |
|---|---|
| `/sec-baslat` | `/baslat` security session |
| `/sec-devam` | `/devam` |
| `/sec-resume` | `/resume` |
| `/sec-faz-raporu` | phase report |
| `/sec-aylik-dongu` | monthly loop |
| `/sec-kontrol-uret` | control gen/refresh |
| `/sec-uzman-guncelle` | expert queue research |
| `/sec-gap-analizi` | gap analysis |
| `/sec-compliance-paket` | compliance pack |
| `/sec-arsivle` | archive |
| `/sec-etik-denetim` | ethics check |

---

## 8 — Experts (K-003)

- Seed **only** prompt-listed sourced names (incl. **Dan Kaminsky** historical note + public URL).
- Fill to 100 with `pending_research` slots — **never invent bios**.
- Pattern mirrors `data/title_top100_queues.json`.

---

## 9 — Org

Security titles live under `ORG/ROLES/` (≥40). **Do not** resize `data/org.json` 600 agency org unless owner explicitly runs `scripts/generate_org.py`.

---

## 10 — Red flags

🚩 **900k single-file prompt** · context impossible · **mega expander + phased refs** (this pack)
🚩 **Live invent top-100** · hallucination · **sourced + pending queues**
🚩 **Exploit/PoC generation** · ethics · **defense-only controls**

---

## 11 — Generator

```bash
python3 scripts/generate_security_giga_pack.py
python3 scripts/secret_scan.py .
python3 scripts/ethics_check.py .
python3 scripts/validate.py
```

---

## 12 — Agents

- `security-reviewer` — readonly assess of controls/gaps
- `compliance-auditor` — crosswalk evidence
- `ethics-checker` — refuse offense; secret hygiene

Hooks: afterFileEdit → secret_scan + ethics_check; beforeShellExecution dangerous-cmd failClosed; beforeReadFile redact; stop → phase-audit.
