# Statement of Applicability (SoA) — ISO/IEC 27001:2022 Annex A (DRAFT)

> HAND_AUTHORED · **DRAFT · needs_expert_review · NOT a certification claim**
> Damga: 2026-08-27T12:55:00Z · MODE=ASSESS-ONLY

## Document control
| Field | Value |
|---|---|
| Organization scope | Performance Growth / adops-agents component pack (repo) |
| Standard | ISO/IEC 27001:2022 Annex A (selected controls) |
| Status | Stub draft for gap analysis only |
| Owner | Compliance officer role (ORG/ROLES) — unassigned human |
| Related | `SECURITY_MATRIX/matrix.md`, `ASSESSMENTS/gap-2026-08-27.md` |

## Applicability legend
| Code | Meaning |
|---|---|
| A | Applicable — in scope for this repo |
| PA | Partially applicable |
| NA | Not applicable (justify) |
| I | Inherited (platform: GitHub/Cursor SaaS) |

## Selected Annex A rows (subset — expand later)

| Control | Title (short) | A/PA/NA/I | Implementation status | Evidence pointer | Notes |
|---|---|---|---|---|---|
| A.5.1 | Policies for information security | PA | Draft | `SECURITY_STATE.md`, rules `00-security-core` | MODE policy present |
| A.5.15 | Access control | PA | Draft | COND/*, iam-hardening | MCP/CI identity |
| A.5.23 | Information security for use of cloud services | PA | Draft | mcp.json, Actions | Canva MCP on; security MCP off |
| A.8.2 | Privileged access rights | PA | Draft | seed scripts env tokens | Document owners |
| A.8.3 | Information access restriction | PA | Draft | public repo vs secrets | |
| A.8.8 | Management of technical vulnerabilities | PA | Draft | vulnerability-management skill | CVE process note in RESEARCH |
| A.8.9 | Configuration management | PA | Draft | CHANGE/*, hooks | |
| A.8.15 | Logging | PA | Draft | AUDIT_LOG.jsonl | |
| A.8.16 | Monitoring activities | PA | Draft | security-audit.yml | |
| A.8.20 | Networks security | I/PA | Inherited | GitHub SaaS | FW templates only |
| A.8.24 | Use of cryptography | PA | Draft | ENC/*, PQC notes | Planning only |
| A.8.25 | Secure development life cycle | PA | Draft | TC/*, ethics_check | |
| A.8.26 | Application security requirements | PA | Draft | ASVS mapping draft | Component pack ≠ classic app |
| A.8.28 | Secure coding | PA | Draft | transparent-code-engine | |
| A.8.32 | Change management | PA | Draft | CHANGE/*, CALENDAR | |

## Exclusions (examples)
| Control area | Rationale |
|---|---|
| Physical office controls | Out of repo scope — organizational |
| OT/ICS detailed controls | Liaison role only; no OT assets in repo |

## Certification disclaimer
This SoA is a **working draft** for ASSESS-ONLY gap analysis. It does **not** assert ISO 27001 certification, audit readiness, or complete Annex A coverage. Human GRC expert review required before any external claim.

## Next
- Expand full Annex A table in later `/sec-compliance-paket` pass
- Link evidence once MODE=AUDIT
