---
description: Son sektör sinyallerinden müşteriye özel pitch brifi üretir — yönetici özeti + sinyal→etki tablosu + konuşma noktaları.
---
# /pitch-brifi
Girdi: müşteri/prospect adı, sektör, pitch bağlamı ($ARGUMENTS). Kaynak: BILGI_TABANI.md + varsa güncel tarama çıktıları.

Çıktı (bu sırayla, başka bölüm ekleme):
1. **Yönetici özeti** — 3 cümle: müşterinin durumu, en kritik sinyal, önerilen açı
2. **Sinyal → Etki tablosu** — satır başına: sinyal (kaynaklı) | müşteriye etkisi | önerilen hamle. En fazla 5 satır, en güçlü sinyal üstte
3. **Konuşma noktaları** — toplantıda söylenecek 5 madde; her biri tek cümle, metrik veya kanıt içerir

Kurallar: kaynağı olmayan sinyal yazma; 90 günden eski sinyali damgala; jenerik sektör klişesi ("dijitalleşme artıyor") yasak. Çıktı doğrudan pitch-deck-uretici ajanına girdi olacak kalitede olmalı.
