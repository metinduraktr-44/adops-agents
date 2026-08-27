# AGENTS.md

`adops-agents` is a Claude Code component pack + agency-automation repo (not a deployable web app). Content lives in `components/`, `docs/`, and `data/`; automation lives in `scripts/`. See `README.md` and `CONTRIBUTING.md` for the product overview and contribution rules.

## Security GIGA (defense-only)

In-repo Security GIGA bootstrap — Claude Code paste **cancelled** (K-003). Coexists with Canva/creative packs when present.

| Area | Location |
|---|---|
| Master prompt | `docs/CURSOR-SECURITY-GIGA-MASTER-PROMPT.md` |
| Bootstrap + usage | `docs/SECURITY-GIGA-BOOTSTRAP.md` |
| Phase / MODE | `SECURITY_STATE.md` (default **ASSESS-ONLY**; pointer in `STATE.md`) |
| Plan | `.cursor/plans/security-master-plan.md` |
| Controls | `LAYERS/` `FIREWALLS/` `ENCRYPTION/` `CHANGE/` `TRANSPARENT_CODE/` `CONDITIONAL/` |
| Matrix | `SECURITY_MATRIX/matrix.md` |
| Roles / experts | `ORG/ROLES/`, `EXPERTS/` (sourced + pending_research) |
| Commands | `.cursor/commands/sec-*.md` (`/sec-baslat`, `/sec-gap-analizi`, `/sec-etik-denetim`, …) |
| Hooks / scanners | `.cursor/hooks.json`, `scripts/secret_scan.py`, `scripts/ethics_check.py` |
| Generator | `scripts/generate_security_giga_pack.py` |

**Hard rules:** defense-only (no exploit/PoC); secrets only `${VAR}` / `vault://` / `op://` / `<REDACTED>`; no 900k prompt blob; no invented top-100 experts. MODE order: assess → implement → audit.

## Cursor Cloud specific instructions

### Runtime & dependencies
- Pure Python 3 stdlib + Bash, wrapped by npm scripts. There are **no** package dependencies: `package.json` has no `dependencies`, and there is no `requirements.txt`/lockfile. `npm install` is effectively a no-op, so no install step is required to start working.
- There is no application server, database, or GUI. "Running the app" means running the validator and the cron-style automation scripts below.

### Primary gate (lint/test/build equivalent)
- `npm run validate` (= `python3 scripts/validate.py`) is the single quality gate used by CI (`.github/workflows/validate-components.yml`). Success prints `VALIDATION: GECTI`; failure prints `VALIDATION: KALDI` and exits non-zero. Run this before committing (per `CONTRIBUTING.md`).

### Automation scripts write into the repo (important gotcha)
- The ops scripts (`scripts/daily_ops.py`, `scripts/weekly_board.py [--board]`, `scripts/nightly.sh`, `scripts/timestamp.sh`) and the generators (`scripts/generate_org.py`, `scripts/generate_docs.py`, `scripts/build_question_bank.py`) **write files** into `gundem/`, `makaleler/`, `toplantilar/`, `docs/`, `data/`, `components/`, and append to `AUDIT_LOG.jsonl` / `BILGI_TABANI.md` / `IS_LISTESI.md`. Running any of them dirties the working tree.
- Non-obvious: the generators can emit content (including new untracked `components/agents/agency/**` files) that differs from what is currently committed. Only run them if you intend to commit regenerated org/docs output. `generate_org.py` asserts exactly 600 agents.
- If you ran these only to smoke-test the environment, restore a clean tree with `git checkout -- . && git clean -fd` (safe here because these are regenerable outputs).
- `daily_ops.py` / the daily article step is skip-if-exists: it will not overwrite an already-present `makaleler/<date>-<topic>.md`.

### Optional LLM generation
- LLM-backed content generation is optional and requires the `ANTHROPIC_API_KEY` env var (paid API). Without it, every loop still runs deterministically (skeleton articles, real standups/minutes/validation). No key is needed for validation or normal development.

## Creative Agency OS (Cursor)

Türkçe not: Bu bölüm, "Otonom AI Creative Agency Operating System (Canva Dual-Mode)" master prompt'unun işletim iskeletidir. Şu an **CANVA:BRIEF-ONLY** (dry-run) modundadır — hiçbir gerçek Canva API çağrısı, hesap, anahtar veya ağ yan etkisi yoktur.

An additive scaffold that turns this repo into a runnable creative-agency operating system. It does **not** replace the existing agency corpus under `components/**` or `data/**` — it lives alongside it in `.cursor/`, `tools/`, and new top-level output folders.

### Architecture / where things live
- `.cursor/rules/*.mdc` — always-on and scoped behavior rules (identity, brand guardrails, spec validation, file structure, Canva ops). Behavior rules go here, **not** in AGENTS.md (avoid duplication).
- `.cursor/commands/*.md` — slash commands (`/baslat`, `/devam`, `/canva-uret`, …). Each has Objective / Requirements / Output.
- `.cursor/skills/<name>/SKILL.md` — progressive-disclosure skills (Canva ops + agency workflow). Folder name equals frontmatter `name`.
- `.cursor/agents/*.md` — read-only critic subagents (`critic-copy`, `critic-design`, `critic-spec`).
- `.cursor/mcp.json` — references the Canva MCP URL only. **OAuth is a user action** (see `.cursor/skills/*/references` and `CANVA_OPS/MCP_TOOLS.md`); no secrets live in-repo.
- `.cursor/hooks.json` (v1) — `afterFileEdit` → `scripts/spec_validate.py`; optional `stop` phase-completion check. stdio JSON in/out, fail-open.
- `.cursor/plans/master-plan.md` — Faz 0..7 phase plan (Bölüm 13).
- `STATE.md` — resume state (current phase + flags). Read this on `DEVAM`/`RESUME`.
- `tools/canva-client/` — TypeScript Canva Connect API client scaffold (Bölüm 9 Mod A2). Stubs only; no deps installed, no network.

### Output folders (Bölüm 12)
`CONTEXT/`, `RESEARCH/`, `TASKS/`, `ORG/`, `EXPERTS/`, `SCENARIOS/`, `MATRIX/`, `BRIEFS/`, `CANVA_OPS/`, `QA/`, `ARCHIVE/`. Generated artifacts (designs, exports, logs) land under `CANVA_OPS/` and `ARCHIVE/`.

### How to run (owner commands)
- `BAŞLAT` — cold start from `.cursor/plans/master-plan.md` Faz 0.
- `DEVAM` / `RESUME` — resume from `STATE.md` at the last completed phase.
- `CANVA:BRIEF-ONLY` — **default/current** dry-run: produce briefs, specs, and registries but do **not** call Canva. No side-effects.
- `CANVA:ON` — enable real Canva MCP / Connect API operations. Requires the user to complete Canva OAuth first (user action). Do not enable autonomously.

### Quality gate
Same as the rest of the repo: `python3 scripts/validate.py` must print `VALIDATION: GECTI`. `validate.py` only scans `components/**`, so Creative Agency OS files do not affect it — but always run it before committing.

## Security Governance OS (Cursor)

Türkçe not: Bu bölüm, "Güvenlik Odaklı GIGA MASTER PROMPT — Otonom AI Security Architecture & Governance Operating System" master prompt'unun işletim iskeletidir. **MODE=ASSESS-ONLY**, **savunma-only (defense-only)** modundadır — hiçbir exploit, hesap, anahtar veya ağ yan etkisi yoktur. Bu OS, Creative Agency OS ile aynı `.cursor/` altında **additive** olarak yaşar (STACKS on `cursor/creative-agency-os-c8d4`, PR #616).

### Defense-only principle (kesin sınır)
Never produce exploits, weaponization, C2, ransomware, phishing, bypass code, or data-exfiltration tooling. Pen-test/red-team topics stay authorized, conceptual, and detection-focused. Prioritize **D3FEND** (defense); reference **MITRE ATT&CK** only to design detections/countermeasures. Enforced by `.cursor/rules/05-ethics-guardrail.mdc` + `scripts/ethics_check.py`.

### No plaintext secrets (kesin sınır)
Never write real or realistic-format secret values anywhere (including examples/dummies). Only `${VAR}`, `vault://…`, `op://…`, or `<REDACTED>`. `.cursor/mcp.json` uses `${VAR}` env only; security MCP servers (Semgrep, Snyk, SonarQube, Trivy, JFrog, Endor Labs) default **OFF** — enable in Cursor Settings > MCP. Enforced by `.cursor/rules/10-secret-hygiene.mdc` + `scripts/secret_scan.py`.

### Owner commands
- `/sec-baslat` — cold start from `.cursor/plans/security-master-plan.md` Faz 0.
- `/sec-devam` · `/sec-resume` — resume from `SECURITY_STATE.md`.
- `/sec-faz-raporu` — phase report. `/sec-aylik-dongu` — monthly experts/standards loop. `/sec-uzman-guncelle` — update expert digest. `/sec-arsivle` — archive a phase.
- `/kontrol-uret` — generate mapped controls for a framework. `/gap-analizi` — gap analysis. `/compliance-paket` — ISO 27001 SoA / evidence package. `/etik-denetim` — defense-only + secret audit.

### 6×100 control framework
Six defense-in-depth frameworks, ~100 controls each: `LAYERS/` (defense-in-depth), `FIREWALLS/` (exposure policy), `ENCRYPTION/` (crypto + PQC), `CHANGE/` (change/CI-CD), `TRANSPARENT_CODE/` (secure SDLC/SBOM), `CONDITIONAL/` (conditional access / zero-trust). Every control row carries `id, ad, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi` (see `.cursor/rules/20-control-mapping.mdc`). Scaffold ships the schema + template rows only — full controls are produced in phased runs via `/kontrol-uret`.

### File map (security-namespaced)
- `.cursor/rules/{00-security-core,05-ethics-guardrail,10-secret-hygiene,20-control-mapping,30-security-file-structure,40-secops}.mdc`.
- `.cursor/commands/{sec-*, kontrol-uret, gap-analizi, compliance-paket, etik-denetim}.md`.
- `.cursor/skills/<name>/SKILL.md` — 20 security skeletons (engines + threat-modeling, compliance-mapper, incident-response, zero-trust-architect, crypto-agility, sbom-provenance, iam-hardening, cloud-security-posture, detection-engineering, vulnerability-management, privacy-engineering, security-qa, security-expert-engine).
- `.cursor/agents/{security-reviewer,compliance-auditor,ethics-checker}.md` — read-only critics.
- `.cursor/hooks.json` — merged: `afterFileEdit` → `scripts/{secret_scan,ethics_check}.py`; `beforeShellExecution` → `.cursor/hooks/block-dangerous.sh` (fail-closed); `beforeReadFile` → `.cursor/hooks/redact-secrets.sh`; `stop` → `.cursor/hooks/phase-audit.sh`.
- `tools/security-scanners/` — offline, dependency-free validation wrappers (`secret_scan.py`, `control_validate.py`, `opa_test.sh`).
- Bölüm 12 folders: `SECURITY_CONTEXT/`, `SECURITY_RESEARCH/`, `ORG/ROLES/`, `EXPERTS/SECURITY_DIGEST.md`, `LAYERS/ FIREWALLS/ ENCRYPTION/ CHANGE/ TRANSPARENT_CODE/ CONDITIONAL/`, `SECURITY_MATRIX/`, `IMPLEMENTATION/`, `ASSESSMENTS/`, `COMPLIANCE/`, `CALENDAR/`, `QA/findings.md`, `MEMORY/`, `REPORTS/`. State: `SECURITY_STATE.md`; plan: `.cursor/plans/security-master-plan.md`.

### Standards (reproduce with a "verify against official source before production" banner)
NIST CSF 2.0 · NIST SP 800-53 Rev.5 (~1,189–1,196 controls) · ISO/IEC 27001:2022 (93 Annex A controls) · CIS Controls v8.1 · OWASP ASVS 5.0.0 · PQC FIPS 203/204/205 · SLSA v1.0 · NIST SP 800-207 / CISA ZTMM 2.0. Never fabricate facts/URLs; mark unknowns `araştırılacak / URL doğrulanmalı`.

### Quality gate
Same as the rest of the repo: `python3 scripts/validate.py` must print `VALIDATION: GECTI`. Security OS files live under `.cursor/`, `tools/`, `scripts/`, and new top-level SECURITY dirs — `validate.py` only scans `components/**`, so they do not affect it, but always run it before committing.
