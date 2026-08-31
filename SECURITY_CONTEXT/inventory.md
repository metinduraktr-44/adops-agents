# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

# Security Context — Asset Inventory (skeleton)

Türkçe not: Faz 0 girdisi. Varlık envanteri (sistemler, veri, kimlikler, bağımlılıklar). MODE=ASSESS-ONLY.

> No secrets here. Reference credentials/config only via `${VAR}` / `vault://` / `op://`.

## Assets (fill in Faz 0)
| asset_id | tür (system/data/identity/dependency) | sahibi | kritiklik (L/M/H) | veri_sınıfı | notlar |
|---|---|---|---|---|---|
| (template) | system | araştırılacak | H | araştırılacak | example row — replace |

## Data classes
- Public / Internal / Confidential / Restricted (define per org; verify against policy).

## Dependencies
- Third-party services, libraries, cloud accounts — list by name; no tokens. Mark unknowns `araştırılacak`.
