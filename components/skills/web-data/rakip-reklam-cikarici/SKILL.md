---
name: rakip-reklam-cikarici
description: Rakip markaların aktif reklamlarını reklam kütüphanelerinden (Meta Ad Library, Google Ads Şeffaflık Merkezi, TikTok) toplayıp mesaj/format/açı analizine çevirir. Kullanıcı "rakip reklamları", "rakip ne iletişim yapıyor", "reklam kütüphanesi", pitch/QBR için rakip kreatif taraması istediğinde aktifleş. Örnek: "müşterinin 3 rakibinin Meta reklamlarını çıkar, hangi vaatle satıyorlar?"
allowed-tools: Read, Write, WebFetch, WebSearch
model: sonnet
user-invocable: true
---
# Rakip Reklam Çıkarıcı
Rakip markaların yayındaki reklamlarını toplar, neyin işe yaradığını ayıklar; pitch argümanı ve kreatif brief girdisi üretir.

## Ne zaman aktifleş
Pitch öncesi rakip taraması, kreatif brief hazırlığı, QBR "pazar ne yapıyor" bölümü, yeni rakip agresifleştiğinde.

## Kaynaklar
- **Meta Ad Library** — aktif reklamlar, yayın tarihi, format, varyant sayısı (tempo göstergesi)
- **Google Ads Şeffaflık Merkezi** — arama/görüntülü/YouTube reklamları
- **TikTok Creative Center** — trend kreatifler ve sektör kıyası
Erişim engellenirse 🚩 bayrakla ve manuel tarama adımlarını listele; veri uydurma.

## Yordam
1. **Kapsamı kur** — rakip listesi + odak (mesaj mı, format mı, tempo mu) + dönem
2. **Topla** — her rakip için: aktif reklam sayısı, formatlar, ilk yayın tarihleri, LP hedefleri
3. **Ayıkla** — her reklamda: vaat (tek cümle), hedeflenen problem, CTA, kanıt öğesi (indirim/sosyal kanıt/özellik)
4. **Desenle** — tema kümeleri; uzun süredir yayında kalan reklam = muhtemel kazanan (harcama devam sinyali)
5. **Boşluk çıkar** — kimsenin sahiplenmediği vaat/segment → müşterinin fırsat açısı

## Çıktı formatı
- Rakip başına özet kart: tempo, baskın format, ana vaat
- Tema tablosu: tema → hangi rakipler → örnek metin (kısa alıntı) → yayın süresi
- **Fırsat bölümü**: 3 boşluk + her biri için önerilen açı ve test fikri
- Pitch/QBR'a gömülecek 3 cümlelik yönetici özeti

## Örnek
"Online eğitim müşterisi; 4 rakibin son 60 gün reklamları." → 2 rakip "sertifika" vaadinde yığılmış, 1'i fiyat kırıyor; boşluk: "iş bulma garantisi" açısı kimsede yok → müşteri için bu açıyla 2 kreatif test önerisi.

## Sınırlar
Sadece halka açık kütüphane verisi; harcama rakamları tahmindir, tahmin olduğu yazılır. Telif: rakip kreatifler analiz için kullanılır, kopyalanmaz.
