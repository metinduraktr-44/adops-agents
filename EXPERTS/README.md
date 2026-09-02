# EXPERTS — Roster & Monthly Loop

Türkçe not: Uzman bilgi tabanı ve **aylık döngü**. Seed isimler owner tarafından
verilen gerçek kamusal figürlerdir; **URL/biyografi uydurulmaz**. Kaynaklanmamış her
şey `araştırılacak / URL doğrulanmalı` olarak işaretlenir.

## Monthly loop: READ → DELTA → DIFF → WRITE → DIGEST
1. **READ** — read current `EXPERTS/DIGEST.md`.
2. **DELTA** — gather new, dated findings (only if research tools/network enabled).
3. **DIFF** — compare against the prior digest; keep only genuine changes.
4. **WRITE** — update roster/notes; mark unsourced items `araştırılacak / URL doğrulanmalı`.
5. **DIGEST** — write a concise dated summary section in `DIGEST.md`.

Run via `/aylik-dongu` or the `expert-engine` skill. No network side-effects unless
the owner explicitly enables research tools.

## Seed names (owner-supplied real public figures — research to verify)
These are seeds only. Do NOT invent URLs, quotes, dates, or biographical claims for any
of them; every factual claim must be sourced or marked to-verify.
- David Droga — araştırılacak / URL doğrulanmalı
- Susan Credle — araştırılacak / URL doğrulanmalı
- Paula Scher — araştırılacak / URL doğrulanmalı
- Piyush Pandey — **historical / memorial reference (deceased 23 Oct 2025)**; treat as
  memorial. araştırılacak / URL doğrulanmalı
- (owner may add more real figures here)

> No fabrication rule: names above are permitted as owner-supplied seeds; all
> supporting facts/links remain to-verify until sourced.

## Security queues (K-003)
- Sourced seeds only (prompt-listed). Current seed: **Dan Kaminsky** (historical).
- All other slots: `pending_research` to 100 — **never invent**.
- Security expert loop reads `EXPERTS/SECURITY_DIGEST.md` (see `security-expert-engine` skill).
- Damga: 2026-08-27T12:40:00Z

🚩 Live invent top-100 · hallucination · use sourced+pending queues
