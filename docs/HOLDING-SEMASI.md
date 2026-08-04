# HOLDING ŞEMASI
> Üretim: 2026-08-04T08:35:51Z · Kaynak: data/holding.json

```mermaid
flowchart TD
  OWNER([Metin Durak — Owner])
  OWNER --> permergrowth-holding([PermerGrowth Holding])
  permergrowth-holding --> grp-ceo[Group CEO]
  permergrowth-holding --> grp-coo[Group COO]
  permergrowth-holding --> grp-cfo[Group CFO]
  permergrowth-holding --> grp-cto[Group CTO]
  permergrowth-holding --> grp-clo[Group Chief Legal Officer]
  permergrowth-holding --> grp-cpo[Group Chief People Officer]
  permergrowth-holding --> permergrowth-performance([PermerGrowth Performance])
  permergrowth-holding --> permergrowth-legal([PermerGrowth Hukuk])
  permergrowth-holding --> vizatrack([VizaTrack])
  permergrowth-holding --> permergrowth-tech([PermerGrowth Tech (App iOS/Android)])
```

## İştirakler ve roller

### PermerGrowth Performance (`permergrowth-performance`) — Performans Pazarlama & Programatik (600-ajanlık ajans buraya bağlanır: data/org.json)
- **C** CEO — Performance (`perf-ceo`) → `grp-ceo`
- **C** COO — Delivery (`perf-coo-delivery`) → `perf-ceo`
- **EVP** EVP — Programmatic (`perf-evp-programmatic`) → `perf-coo-delivery`
- **EVP** EVP — Paid Social (`perf-evp-paid-social`) → `perf-coo-delivery`
- **DIRECTOR** Director — Analytics (`perf-dir-analytics`) → `perf-coo-delivery`
- **LEAD** Lead — Activation (`perf-lead-activation`) → `perf-evp-programmatic`
- **SPECIALIST** Specialist — Campaign (`perf-spec-campaign`) → `perf-lead-activation`
- **ANALYST** Analyst — Data (`perf-anl-data`) → `perf-dir-analytics`

### PermerGrowth Hukuk (`permergrowth-legal`) — Hukuk, Uyum, Sözleşme, KVKK/GDPR
- **C** Managing Partner — Legal (`leg-ceo`) → `grp-clo`
- **DIRECTOR** Director — Compliance (`leg-dir-compliance`) → `leg-ceo`
- **LEAD** Lead — Contracts (`leg-lead-contracts`) → `leg-dir-compliance`
- **SPECIALIST** Specialist — Privacy (KVKK/GDPR) (`leg-spec-privacy`) → `leg-lead-contracts`
- **ANALYST** Analyst — Legal Research (`leg-anl-research`) → `leg-dir-compliance`

### VizaTrack (`vizatrack`) — Vize/seyahat takibi ürünü — başvuru izleme, randevu, uyum
- **C** CEO — VizaTrack (`vt-ceo`) → `grp-ceo`
- **C** CPO — Product (`vt-cpo-product`) → `vt-ceo`
- **DIRECTOR** Director — Operations (`vt-dir-ops`) → `vt-ceo`
- **LEAD** Lead — Consulate Integrations (`vt-lead-integrations`) → `vt-dir-ops`
- **SPECIALIST** Specialist — Customer Success (`vt-spec-support`) → `vt-dir-ops`
- **ANALYST** Analyst — Appointment Data (`vt-anl-data`) → `vt-lead-integrations`

### PermerGrowth Tech (App iOS/Android) (`permergrowth-tech`) — Web + Mobil (iOS/Android) uygulama platformu; holding yapısını taşıyan ürün
- **C** CTO — Platform (`tech-cto`) → `grp-cto`
- **DIRECTOR** Director — Mobile (iOS/Android) (`tech-dir-mobile`) → `tech-cto`
- **DIRECTOR** Director — Backend/API (`tech-dir-backend`) → `tech-cto`
- **LEAD** Lead — iOS (`tech-lead-ios`) → `tech-dir-mobile`
- **LEAD** Lead — Android (`tech-lead-android`) → `tech-dir-mobile`
- **SPECIALIST** Specialist — DevOps/SRE (`tech-spec-devops`) → `tech-dir-backend`
- **ANALYST** Analyst — QA (`tech-anl-qa`) → `tech-dir-mobile`

## Ülkeler
- Hedef: TR, DE, NL, AE, SA, UK, US
- Pazar: TR, DE, NL, AE, SA, UK, US, FR, ES, PL

> Her iştirak her ülke için yerelleştirilir (dil + hukuk); gece araştırma worklow'u top-5'i tazeler.
