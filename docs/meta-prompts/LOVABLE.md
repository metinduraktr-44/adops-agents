# META-PROMPT — Lovable

**Amaç:** Ajans için bir **web dashboard/arayüz** üretmek — 600 rolü, hiyerarşiyi, prompt kütüphanesini,
araştırma arşivini ve 7/24 döngü durumunu görselleştiren bir uygulama. Bloğu Lovable'a yapıştır.

```prompt
600 ajanlık bir AI performans-pazarlama ajansı için modern, minimal bir yönetim paneli (dashboard) kur.
Veri modeli reponun JSON dosyalarından beslenir (statik import veya API): data/org.json (10 C-level +
20 departman + 600 rol, 6 kademe), data/kaynaklar.json (disiplin başına top-100 kişi), data/ozel_yetenekler.json
(+100 kültür/sanat/spor yetenek), arsiv/*.md (zaman damgalı araştırma arşivi), docs/ARASTIRMA-TAKVIMI.md.

SAYFALAR
1. Org Şeması — C-seviyeden ANALYST'e kırılabilir hiyerarşi ağacı; departman filtreleri; headcount/KPI kartları.
2. Rol Detayı — seçilen title için (A)TITLE (B)EKİP (C)UYGULAMA prompt ailelerini gösteren kopyala butonlu panel
   (kaynak: components/prompts/<dept>/<slug>.md).
3. Rol-Modeller & Araştırma — disiplin başına top isimler (kaynaklar.json), her ay büyüyen sayaç (x/100),
   zaman damgalı arşiv zaman çizelgesi (arsiv/), aylık takvim (ARASTIRMA-TAKVIMI).
4. Yetenekler — kültür/sanat/spor +100 katalog, kategori filtreleri, gelişim döngüsü rozetleri.
5. Operasyon — günlük standup, haftalık liderlik, aylık kurul çıktıları; AUDIT_LOG zinciri (GEÇTİ/KALDI).

TASARIM
- Düz, minimal, amaca yönelik. Gradient/emoji/box-shadow/rainbow YOK. Net görsel hiyerarşi.
- Her grafik/tablo kendini açıklasın: başlık + eksen etiketleri + kaynak + zaman aralığı.
- Boş durum render etme; verisi olmayan bölümü gizle.

KURALLAR
- Veri uydurma yok; eksik veriyi "araştırılacak (x/100) 🚩" olarak göster.
- Kopyalanabilir promptlar birebir dosya içeriğinden gelsin.

ÇIKTI: çalışan dashboard + veri bağlama katmanı + bir örnek rol için uçtan uca akış (org → rol → prompt kopyala).
```

## Notlar
- Lovable tarafında canlı veri istiyorsan, repo JSON'larını sunan küçük bir statik API veya doğrudan
  JSON import kullan; dosya şemaları yukarıda listelendi.
- Prompt içeriği `components/prompts/` üreteçle güncellenir; dashboard bu dosyaları kaynak alsın.
