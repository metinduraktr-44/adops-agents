---
name: persembe-pilot-deliverable-loop
description: Her Perşembe Response DGA pilotu için 1 deliverable (pitch deck taslağı veya pitch brifi) üretir, DENETÇİ rubric'ten geçirir ve damgalayarak teslim eder. GELIR_MOTORU haftalık ritminin Perşembe adımıdır.
category: operations
interval: 7d
stop-condition: Bu haftanın deliverable'ı DENETÇİ rubric'ten GEÇTİ aldı, uretim/ klasörüne kaydedildi ve AUDIT_LOG.jsonl'a damgalı satır eklendi. Maksimum 3 iterasyon; 3. iterasyonda hâlâ KALDI ise 🚩 bayrakla durur, ertesi haftaya devreder.
components: [agent:performance-marketing/pitch-deck-uretici, command:marketing/pitch-brifi, hook:quality-gates/denetci-rubric, hook:audit/timestamp-audit]
tags: [pilot, deliverable, pitch, response-dga, gelir-motoru, loop]
---

# Perşembe Pilot Deliverable Döngüsü

> GELIR_MOTORU sözleşmesi: "Per: pilot deliverable (dogfooding kanıtı)". Bu döngü o kuralı otomatikleştirir — dış satıştan önce iç kanıt üretir. Kanıt metriği: **pitch başına hazırlık süresi ↓**.

## 🎯 Amaç
Her Perşembe, Response DGA'nın gerçek işine giden 1 deliverable: aktif bir prospect için pitch deck taslağı, yoksa güncel sinyallerden pitch brifi.

## ⏱️ Zamanlama
`7d` — Perşembe gecesi koşacak şekilde başlat (gecelik pencere, Cilt 1 takvimi).

## ▶️ Çalıştır
```
/loop 7d "Bu haftanın Response DGA pilot deliverable'ını üret: aktif pitch varsa pitch-deck-uretici ile konuşma notlu deck taslağı, yoksa /pitch-brifi ile en güncel prospect brifi. DENETÇİ rubric'e vur; KALDI ise düzelt (maks 3 iterasyon). GEÇTİ'yi uretim/[tarih]-[ad].md olarak kaydet, hazırlık süresini ölç ve AUDIT_LOG.jsonl'a damgala."
```

## 🔁 İterasyon adımları
1. **Algıla** — BILGI_TABANI.md + haftanın sinyalleri + aktif pitch/prospect listesi; ts_start damgası al
2. **Karar ver** — aktif pitch var → deck taslağı; yok → pitch brifi (boş Perşembe yasak)
3. **Üret** — `pitch-deck-uretici` veya `/pitch-brifi`; müşteriye özel, kaynaklı, metrikli
4. **Denetle** — `denetci-rubric` 6 katman; KALDI → eksiği düzelt, 3'e dön (maks 3 tur)
5. **Kaydet & damgala** — `uretim/` klasörüne yaz; hazırlık süresini (ts_start→ts_end) ölç; `timestamp-audit` AUDIT_LOG satırını basar; öğrenimi BILGI_TABANI'na ekle (zincir: gelecek Perşembe'nin girdisi)

## 🛑 Durma koşulu
GEÇTİ + kayıt + damga tamamsa dur. 3 iterasyonda GEÇTİ yoksa 🚩 ile dur, KALDI nedenini logla (kural: KALDI olan teslim edilmez).

## 🧩 Referans bileşenler
- `agent:performance-marketing/pitch-deck-uretici` — deck taslağını yazar
- `command:marketing/pitch-brifi` — pitch yoksa haftanın brifini üretir
- `hook:quality-gates/denetci-rubric` — teslim öncesi 6 katman hatırlatıcısı
- `hook:audit/timestamp-audit` — her üretime gerçek zaman damgası

## 💡 Örnek
Perşembe gecesi: aktif prospect "X perakende zinciri" → döngü 10 bölümlük konuşma notlu deck taslağını 1 iterasyonda GEÇTİ ile üretir, `uretim/2026-07-16-x-perakende-pitch.md` kaydeder; hazırlık süresi 40 dk olarak loglanır (önceki manuel süre ~4 saat → kanıt metriği işledi).
