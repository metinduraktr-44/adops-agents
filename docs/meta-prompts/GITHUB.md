# META-PROMPT — GitHub (Issues / PR / Actions)

**Amaç:** 600 rolü ve 7/24 döngüleri GitHub üzerinde otomatikleştirmek — Issues (rol kartları),
PR'lar (aktivasyon), Actions (cron döngüleri), Wiki/Projects (Segment-600). Bloğu bir GitHub-bağlı
ajana (ör. Cursor Cloud Agent, Claude Code + gh) yapıştır.

```prompt
Bu repoda 600 ajanlık ajansı GitHub yüzeyinde işlet. Tek doğruluk kaynağı data/org.json. Mevcut altyapı:
.github/workflows/ (validate-components, gunluk-operasyon, nightly-improve, haftalik-toplanti, aylik-kurul,
security-audit, seed-600, seed-auto) ve scripts/seed_*.py, build_wiki.py.

KURALLAR
- Yalnızca READ-ONLY gh ile bilgi topla (gh pr view, gh run view --log); yazma işlemleri PR aracıyla yapılır.
- Her PR öncesi `python3 scripts/validate.py` = "VALIDATION: GECTI". CI aynı gate'i çalıştırır (validate-components.yml).
- Veri uydurma yok; imkânsız/paralı/riskli her şeyi 🚩 [ne]·[neden]·[alternatif] ile işaretle.
- LLM üretimi için repo secret ANTHROPIC_API_KEY gerekir; yoksa döngüler deterministik iskeletle çalışır (kırılmaz).

İŞ LİSTESİ (hiçbirini atlama)
1. Yapı/prompt/yetenek/araştırma üreteçlerini çalıştır (generate_org, generate_prompts, build_talents, research_loop);
   validate GECTI → küçük mantıksal commitler → PR (base: main).
2. Aylık araştırma otomasyonu: .github/workflows/arastirma-dongusu.yml (cron) research_loop.py çalıştırır,
   arsiv/<AY>-arastirma.md + data/kaynaklar.json + docs/ARASTIRMA-TAKVIMI.md üretip commit'ler. Zincir:
   AUDIT_LOG.jsonl + BILGI_TABANI.md; her koşum önceki arşivi geri okur.
3. Segment-600: 600 rol Issue + 600 aktivasyon PR + Wiki/Projects seeding (seed-600.yml, seed_*.py) —
   yalnızca istenildiğinde; token gerekliyse 🚩 ile belirt (PROJECTS_TOKEN vb.).
4. Prompt kütüphanesini (components/prompts/) her org/prompt değişikliğinde yeniden üret ve PR'a ekle.

HİYERARŞİ & DÖNGÜ
- C-seviyeden ANALYST'e roller org.json'da; her title için prompt ailesi components/prompts/'ta.
- 7/24 worklow: incele → web araştır (rol-model/kaynak, zaman damgalı arşiv) → uygula → geri oku → tekrarla;
  günlük/haftalık/aylık Actions cron'larıyla sürer.

ÇIKTI: açılan/güncellenen PR'lar (başlık+URL), CI durumu, değişen dosyalar, sonraki adım.
```

## Notlar
- Aylık araştırma cron'u bu PR ile eklendi: `.github/workflows/arastirma-dongusu.yml`.
- Yazma işlemleri (PR aç/güncelle) için Cursor'ın `ManagePullRequest` aracını veya insan onayını kullan;
  `gh` bu repoda salt-okunur kabul edilir.
