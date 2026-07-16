---
allowed-tools: Read, Write, WebFetch
argument-hint: <konu-veya-kaynak> [hedef-kitle]
description: Ajans düşünce liderliği içeriğini LinkedIn gönderi formatına çevirir — kanca + gövde + CTA + hashtag.
---
# /linkedin-yayinci
Girdi: konu, dosya yolu veya URL + opsiyonel hedef kitle ($ARGUMENTS). Amaç: Response DGA'nın programmatic/performance uzmanlığını görünür kılan, müşteri adayı çeken gönderi.

Süreç:
1. **Kaynağı oku** — dosya/URL ise içeriği çek; konu ise BILGI_TABANI'ndan ilgili sinyalleri al
2. **Tek içgörü seç** — gönderi başına 1 iddia; birden çok fikir varsa en tartışma yaratanı al
3. **Formatla**:
   - Kanca (ilk 2 satır): merak/karşıt görüş; "daha fazlasını gör" kırılmasından önce vurucu olmalı
   - Gövde: 3-5 kısa paragraf veya madde; en az 1 somut metrik/vaka; ajans deneyiminden örnek
   - CTA: tek soru veya tek davet ("QBR şablonunu isteyene gönderiyorum" gibi)
   - Hashtag: 2-4 adet, niş (#programmatic #performansPazarlama gibi); jenerik #marketing tek başına yasak
4. **Sınırlar** — ideal 900-1300 karakter; müşteri adı anonim (izin yoksa); rakip kötüleme yok

Çıktı: yayına hazır gönderi metni + 1 satır görsel önerisi (grafik/karusel fikri). API ile otomatik yayınlama YOK — taslak üretilir, onay Metin'de.
