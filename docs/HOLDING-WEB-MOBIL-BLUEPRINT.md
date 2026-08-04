# HOLDING WEB / iOS / ANDROID BLUEPRINT
> Damga: 2026-08-04T09:40:15Z · TR: Ürün kodu değil; mimari + workflow iskeleti.

## Katmanlar
1. **HoldCo Console (Web)** — portföy KPI, sermaye zarfı, ülke ajans durumu
2. **OpCo Dashboards (Web)** — Permergrowth / VizaTrack / Movea / Cigkoftem
3. **Consumer apps (iOS + Android)** — VizaTrack, Movea, Cigkoftem (+ opsiyonel Permergrowth client)
4. **Shared Platform API** — auth, flags, notifications, analytics, CI

## Stack ipuçları
- Web: Next.js, Vercel, Clerk/WorkOS auth via HoldCo platform
- iOS: SwiftUI, TestFlight, shared API
- Android: Kotlin, Play Console, shared API

## Workflow entegrasyonu
Her app yüzeyi için:
- Kişisel: standup · todo · eğitim · self-inquiry · up/down/lateral
- Grup: dept sync · release train · incident · localization review
- Gece: ülke + rakip top-5 arşiv döngüsü (`scripts/nightly_holding_research.py`)

## Title özelleştirme
App surface title'ları OpCo ladder'ına map edilir; HoldCo CTO sponsor.
Prompt genişletme: `data/prompt_bank/*` + rol kartı §1–21 (AdOps) veya iştirak MD ladder.

## DoD (blueprint)
- [x] holding.json apps bloğu
- [x] OpCo surfaces listelenmiş
- [ ] Gerçek native repo scaffold (ayrı PR; bu pakette yok — sahte commit yok)
