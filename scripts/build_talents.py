#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ÖZEL YETENEKLER — kültür/sanat/spor + gelişim katalogu (+100).
Ajans rollerine takılabilen 'ek beceri' havuzu. Her yetenek bir gelişim döngüsü taşır:
incele → web araştır (rol-model) → uygula → arşivle(zaman damgalı) → geri oku → tekrarla.
Çıktı: data/ozel_yetenekler.json (research_loop ve prompt üreteci tüketir).
"""
import json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TS = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
OUT = os.path.join(ROOT, "data", "ozel_yetenekler.json")

KATEGORILER = {
    "sanat": ["Resim", "Heykel", "Fotoğrafçılık", "Grafik Tasarım", "İllüstrasyon", "Ebru",
              "Seramik", "Kaligrafi", "Dijital Sanat", "Kolaj", "Baskı Sanatı"],
    "muzik": ["Piyano", "Gitar", "Keman", "Vokal", "Beste", "DJ/Prodüksiyon", "Bağlama",
              "Ritim/Perküsyon", "Müzik Teorisi", "Ses Tasarımı", "Koro"],
    "sahne": ["Tiyatro", "Doğaçlama", "Dans", "Bale", "Modern Dans", "Halk Oyunları", "Gölge Oyunu",
              "Pandomim", "Sahne Yönetimi", "Stand-up", "Hitabet"],
    "yazi": ["Yaratıcı Yazarlık", "Şiir", "Senaryo", "Gazetecilik", "Deneme", "Mizah Yazarlığı",
             "Teknik Yazım", "Editörlük", "Çeviri", "Blog", "Storytelling"],
    "spor": ["Koşu", "Yüzme", "Bisiklet", "Futbol", "Basketbol", "Tenis", "Voleybol",
             "Yoga", "Pilates", "Tırmanış", "Dövüş Sanatları", "Satranç", "Triatlon", "Kürek"],
    "zanaat": ["Ahşap İşçiliği", "Örgü/Dokuma", "Takı Tasarımı", "Deri İşçiliği", "Cam İşçiliği",
               "Aşçılık", "Pastacılık", "Bahçıvanlık", "Origami", "Model Yapımı", "Kokoreç/Barista"],
    "zihin": ["Meditasyon", "Hızlı Okuma", "Hafıza Teknikleri", "Eleştirel Düşünme", "Zihin Haritalama",
              "Münazara", "Yabancı Dil", "Felsefe", "Mantık Bulmacaları", "Not Alma Sistemleri", "Stoacılık Pratiği"],
    "dijital": ["Video Kurgu", "3B Modelleme", "Animasyon", "Oyun Tasarımı", "Podcast Yapımı", "Motion Graphics",
                "UI/UX Eskizleme", "Veri Görselleştirme", "Drone Fotoğrafçılığı", "AR/VR Deneyimi", "No-Code Uygulama"],
    "liderlik": ["Koçluk", "Mentorluk", "Kolaylaştırıcılık (facilitation)", "Müzakere", "Karar Verme",
                 "Kültürlerarası İletişim", "Zaman Yönetimi", "Kriz İletişimi", "Topluluk Kurma", "Geri Bildirim Verme"],
}


def main():
    yetenekler = []
    idx = 0
    for kategori, items in KATEGORILER.items():
        for ad in items:
            idx += 1
            yetenekler.append({
                "id": f"yt-{idx:03d}",
                "ad": ad,
                "kategori": kategori,
                "gelisim_dongusu": ["incele", "web-arastir(rol-model)", "uygula",
                                    "arsivle(zaman-damgali)", "geri-oku", "tekrarla"],
                "rol_model_kaynak": "data/kaynaklar.json (aylık research_loop ile büyür)",
                "arsiv": "arsiv/ (zaman damgalı)",
                "durum": "aktif",
            })
    data = {"schema": "1", "guncelleme_utc": TS,
            "toplam": len(yetenekler),
            "not": "Ajans rollerine takılabilen ek beceri havuzu; her biri kültür/sanat/spor/zihin "
                   "gelişim döngüsüyle 7/24 LLM ajans yapısına bağlanır.",
            "kategoriler": list(KATEGORILER.keys()),
            "yetenekler": yetenekler}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"TALENTS WRITTEN: {len(yetenekler)} ({len(KATEGORILER)} kategori) -> {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
