# BİLGİ TABANI (cumulative knowledge — grows nightly)
Sistem "öğrenmesi" burada birikir. Her gecelik döngü yeni başlık ekler; bir sonraki gece bunu girdi alır.

## 2026-07-14 — Seed
- Repo kuruldu. Dikey odak: performans pazarlama & programatik.
- Denetim: 6 katman (structural/integrity/semantic/reference/patterns/review).
- Gelir: sponsorluk + featured + referral + premium pack + ajans inbound.

## 2026-07-17T02:06:27Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-17T08:04:07Z] gunluk-operasyon: standup+makale üretildi; nöbet tal/inf/prg; konu ctv-buying-checklist.
- [2026-07-17T08:04:07Z] liderlik-sync: tutanak toplantilar/2026-07-17-liderlik.md; açık P0=4, gelir aksiyonu=18.
- [] v2-ajans-insa: 600 ajanlik agency yapisi kuruldu; org tek kaynak data/org.json; 924 baslikli anayasa docs/MASTER-PROMPT-AJANS.md; gunluk/haftalik/aylik cron ritmi tanimlandi. Ogrenim: buyuk org uretimi = generator + assert(600) deseniyle idempotent tutulur.

- [] v2.1: segment-600 motoru kuruldu (her sekmede +600 gercek islem; Agents sekmesi Copilot yuzeyi oldugu icin alternatifle kapatildi) + gelir arastirmasi kaynakli emsallerle tamamlandi. Ogrenim: GitHub built-in GITHUB_TOKEN issues/PR/wiki/SARIF icin yeterli, Projects v2 icin PAT sart; secondary rate limit icin 1 islem/sn + 150lik PR batchleri guvenli bant.

- [2026-07-17T09:37:36Z] gunluk-operasyon: standup+makale üretildi; nöbet tal/inf/prg; konu ctv-buying-checklist.
- [2026-07-17T09:51:13Z] gunluk-operasyon: standup+makale üretildi; nöbet tal/inf/prg; konu ctv-buying-checklist.
- [] v2.3: 600 rol karti MAKSIMIZE edildi (15 bolum: kimlik/misyon/sorumluluk/RACI-karar-yetkileri/OKR/haftalik-ritim/toplanti/IO-DoD/arayuzler/araclar/eskalasyon-matrisi/ilk-30-gun/anti-desen/oz-denetim/baglantilar). KRITIK BUGFIX: frontmatter description tirnaksiz iki-nokta YAML hatasi (delivery: programmatic) tum kartlarda duzeltildi -> _yaml_q(). generate_docs curated dosyalari (GELIR-TAKIP, IS_LISTESI) artik W_seed ile koruyor. Ogrenim: jenerator collision-suffix disk durumunu okuyor -> yeniden uretimde once dizini temizle.

- [2026-07-17T10:51:10Z] gunluk-operasyon: standup+makale üretildi; nöbet tal/inf/prg; konu ctv-buying-checklist.
- [] v2.4: 600 kart 21 bolume genisletildi (+oz-ogrenim dongusu, +departman-ozel GERCEK kaynak URLleri, +panel/guncelleme takibi, +egitim&beta, +makale uretimi, +rol-ozel soru seti). 501-soruluk merkezi oz-denetim bankasi kuruldu (docs/OZ-DENETIM-SORU-BANKASI.md + data/soru_bankasi.json); gunluk dongu her kosumda bankadan 8 soru cekip standupta denetliyor. "500 soru/kart" 🚩 K-003 -> merkezi banka + kart alt-seti (gercekci esdeger).

- [] v2.5: kartlar role-ozellestirildi — §3a sorumluluk oz-denetimi (her sorumluluk+dept sorusu), §5 her KPI altina 3 tani sorusu, §20 tam kademe+departman blogu. Her kart ~50 KENDI KPI/biriminden turetilmis soru tasiyor. "+100 soru/bolum" 🚩 K-003 -> role-turetilmis gomulu sorular + 501 merkezi banka.

- [] v2.6: 79 GERCEK rol-modeli (disiplin basi dunya top isimleri, kaynakli arastirma) data/rol_modelleri.json + docs/ROL-MODELLERI.md; kartlara §16b Rol Modelleri gomuldu. HOLDING mimarisi umbrella'ya eklendi (7 repo tek cati, is birimi segmentasyonu). "her title top-5 + her title 500 soru" 🚩 K-003 -> disiplin-bazli gercek top-5 + 501 merkezi banka.

- [] v2.7: 22 rol-modeline 1 pratik ilke eklendi (Binet 60/40, Sharp penetrasyon, Kaushik STDC, Seufert LTV-once, vb; uydurma yok); O%27Kelley markdown link bug fix. Holding KOD olarak: umbrella data/holding.json + holding_report.py + holding-konsolide.yml (gunluk portfoy raporu). 3 marka alan-derinliginde org (Movea 34, VizaTrack 34, Cigkoftem 29 rol) DOKUMAN olarak (sahte issue YOK).

## 2026-07-18T01:55:15Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-18T06:26:20Z] gunluk-operasyon: standup+makale üretildi; nöbet inf/prg/sea; konu capi-signal-health.
## 2026-07-19T02:06:21Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-19T07:03:01Z] gunluk-operasyon: standup+makale üretildi; nöbet prg/sea/soc; konu retail-media-tr-landscape.
## 2026-07-20T02:26:59Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-20T07:39:42Z] gunluk-operasyon: standup+makale üretildi; nöbet sea/soc/mob; konu mmm-lite-for-smb.
- [2026-07-20T09:30:14Z] liderlik-sync: tutanak toplantilar/2026-07-20-liderlik.md; açık P0=6, gelir aksiyonu=19.
## 2026-07-21T02:05:16Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-21T07:03:50Z] gunluk-operasyon: standup+makale üretildi; nöbet soc/mob/ret; konu creative-fatigue-signals.
## 2026-07-22T02:03:31Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-22T07:06:02Z] gunluk-operasyon: standup+makale üretildi; nöbet mob/ret/seo; konu consent-mode-v2-pitfalls.
## 2026-07-23T02:10:27Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-23T06:44:21Z] gunluk-operasyon: standup+makale üretildi; nöbet ret/seo/cro; konu claude-code-agents-for-adops.
## 2026-07-24T02:06:42Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-24T06:44:20Z] gunluk-operasyon: standup+makale üretildi; nöbet seo/cro/ana; konu dco-feed-architecture.
## 2026-07-25T02:06:09Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-25T06:35:00Z] gunluk-operasyon: standup+makale üretildi; nöbet cro/ana/dsc; konu incrementality-geo-holdouts.
## 2026-07-26T02:10:45Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-26T07:08:32Z] gunluk-operasyon: standup+makale üretildi; nöbet ana/dsc/ops; konu sa360-bid-strategy-selection.
## 2026-07-27T02:24:26Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-27T07:59:27Z] gunluk-operasyon: standup+makale üretildi; nöbet dsc/ops/cre; konu amazon-acos-tacos-playbook.
- [2026-07-27T10:05:06Z] liderlik-sync: tutanak toplantilar/2026-07-27-liderlik.md; açık P0=6, gelir aksiyonu=19.
## 2026-07-28T01:58:56Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-28T07:06:56Z] gunluk-operasyon: standup+makale üretildi; nöbet ops/cre/str; konu agency-ai-org-design.
## 2026-07-29T02:02:12Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-29T07:12:22Z] gunluk-operasyon: standup+makale üretildi; nöbet cre/str/cls; konu programmatic-supply-path-2026.
## 2026-07-30T01:52:18Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-30T07:07:26Z] gunluk-operasyon: standup+makale üretildi; nöbet str/cls/nbd; konu skan-vs-sandbox-attribution.
## 2026-07-31T02:11:07Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-31T07:20:21Z] gunluk-operasyon: standup+makale üretildi; nöbet cls/nbd/prt; konu pmax-transparency-levers.
## 2026-08-01T02:12:31Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-01T06:44:47Z] gunluk-operasyon: standup+makale üretildi; nöbet nbd/prt/prd; konu ctv-buying-checklist.
- [2026-08-01T08:15:02Z] kurul: tutanak toplantilar/2026-08-01-kurul.md; açık P0=6, gelir aksiyonu=19.
## 2026-08-02T02:09:23Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-02T07:07:49Z] gunluk-operasyon: standup+makale üretildi; nöbet prt/prd/fin; konu capi-signal-health.
## 2026-08-03T02:11:31Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-03T07:54:09Z] gunluk-operasyon: standup+makale üretildi; nöbet prd/fin/leg; konu retail-media-tr-landscape.
- [2026-08-03T10:00:47Z] liderlik-sync: tutanak toplantilar/2026-08-03-liderlik.md; açık P0=6, gelir aksiyonu=19.
## 2026-08-04T01:57:19Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-04T07:06:34Z] gunluk-operasyon: standup+makale üretildi; nöbet fin/leg/tal; konu mmm-lite-for-smb.
## 2026-08-05T01:56:48Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-05T07:08:29Z] gunluk-operasyon: standup+makale üretildi; nöbet leg/tal/inf; konu creative-fatigue-signals.
## 2026-08-06T02:00:19Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-06T07:10:38Z] gunluk-operasyon: standup+makale üretildi; nöbet tal/inf/prg; konu consent-mode-v2-pitfalls.
## 2026-08-07T02:22:20Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-07T05:55:07Z] gunluk-operasyon: standup+makale üretildi; nöbet inf/prg/sea; konu claude-code-agents-for-adops.
## 2026-08-08T01:08:21Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-08T05:13:19Z] gunluk-operasyon: standup+makale üretildi; nöbet prg/sea/soc; konu dco-feed-architecture.
## 2026-08-09T01:13:15Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-09T05:27:38Z] gunluk-operasyon: standup+makale üretildi; nöbet sea/soc/mob; konu incrementality-geo-holdouts.
## 2026-08-10T01:15:07Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-10T05:51:48Z] gunluk-operasyon: standup+makale üretildi; nöbet soc/mob/ret; konu sa360-bid-strategy-selection.
- [2026-08-10T07:56:06Z] liderlik-sync: tutanak toplantilar/2026-08-10-liderlik.md; açık P0=6, gelir aksiyonu=19.
## 2026-08-11T01:13:37Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-11T05:32:36Z] gunluk-operasyon: standup+makale üretildi; nöbet mob/ret/seo; konu amazon-acos-tacos-playbook.
## 2026-08-12T01:21:25Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-12T05:51:49Z] gunluk-operasyon: standup+makale üretildi; nöbet ret/seo/cro; konu agency-ai-org-design.
## 2026-08-13T01:22:52Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-13T05:53:39Z] gunluk-operasyon: standup+makale üretildi; nöbet seo/cro/ana; konu programmatic-supply-path-2026.