# Master Plan — GIGA Creative Agency (7 Phases)

> From Bölüm 13 · Damga: 2026-08-27T00:35:00Z

## Phase 0 — Bootstrap ✅

- Rules, commands, MCP config, hooks, folder stubs, STATE.md
- Branch: `cursor/giga-creative-agency-50e1`

## Phase 1 — Context + Brand

- [ ] Populate `CONTEXT/brand.md`, audience, competitors
- [ ] Link holding OpCo brand kits where applicable
- [ ] Validate guardrails rule against sample brief

## Phase 2 — Experts Seed

- [ ] Create `EXPERTS/{title}/` for creative titles
- [ ] seed.json: ≤5 sourced profiles per title
- [ ] pending_research.json: empty slots, no invented bios

## Phase 3 — Brief Pipeline

- [ ] BRIEFS/ templates + `/brief-uret` smoke test
- [ ] SCENARIOS/ campaign examples
- [ ] critic-copy readonly review

## Phase 4 — Spec + Matrix

- [ ] MATRIX/ schema (format, dimensions, variant_id, brief_ref)
- [ ] spec_validate.py green on samples
- [ ] critic-spec pass

## Phase 5 — Canva BRIEF-ONLY

- [ ] CANVA_OPS/ job manifests without MCP
- [ ] Export intent documented in manifest
- [ ] QA/ checklist

## Phase 6 — Canva FULL

- [ ] Owner OAuth via Cursor MCP
- [ ] Live design create/edit/export
- [ ] tools/canva-client/ optional direct API path

## Phase 7 — QA + Archive

- [ ] critic-copy, critic-design, critic-spec workflow
- [ ] `/arsivle` → ARCHIVE/YYYY-MM/
- [ ] Monthly `/aylik-dongu` integration

## Blockers

| Item | Owner |
|---|---|
| Canva OAuth | Metin — Cursor MCP Authorize |
| Enterprise autofill | Confirm Canva plan before Phase 6 |
| Brand kit assets | CONTEXT/ population |
