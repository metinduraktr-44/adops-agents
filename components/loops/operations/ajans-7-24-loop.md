---
name: ajans-7-24-loop
description: 7/24 agency heartbeat — chains nightly-improve, daily standup/work-list/article, weekly leadership + revenue reviews, monthly board into one unbroken loop.
---
# Ajans 7/24 Döngüsü
**TR:** Ajansın kalp atışı. Cron zinciri: 03:00 nightly → 07:30 standup → 07:35 iş listesi → 07:40 makale → hafta içi review'lar → ayın 1'i kurul.

## Chain
1. nightly-improve (00:00 UTC) — read→distill→produce→validate→stamp→commit
2. gunluk-operasyon (04:30 UTC) — standup + IS_LISTESI + article + tracking
3. haftalik-toplanti (Mon 06:00 UTC) — leadership minutes + weekly consolidation
4. aylik-kurul (1st, 06:00 UTC) — OKR scoring + phase-gate decisions

## Invariants
- Every run appends AUDIT_LOG.jsonl and one learning line to BILGI_TABANI.md.
- A red run must be triaged within 24h (INF on-call), escalated to cto-platform at 48h.
