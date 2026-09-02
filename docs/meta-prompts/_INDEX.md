# META-PROMPT KÜTÜPHANESİ — platformlara yapıştırılabilir ajans kurulum promptları

Bu klasör, **600 ajanlık AI ajans**ı (bkz. `docs/MASTER-PROMPT-AJANS.md`) dört farklı platformda
kurup 7/24 çalıştırmak için kopyala-yapıştır-hazır **master promptlar** içerir.

| Platform | Dosya | Ne zaman |
|---|---|---|
| Claude Code | [`CLAUDE-CODE.md`](CLAUDE-CODE.md) | Reponun içinde ajanları/skilleri/komutları çalıştırıp döngüleri işletmek |
| Cursor | [`CURSOR.md`](CURSOR.md) | Cursor'da (IDE / Cloud Agent) aynı yapıyı sürdürmek |
| Lovable | [`LOVABLE.md`](LOVABLE.md) | Ajans için web arayüzü/dashboard üretmek |
| GitHub | [`GITHUB.md`](GITHUB.md) | Issues/PR/Actions ile 600 operasyonu otomatikleştirmek |

## Kullanım
1. İlgili dosyanın içindeki ` ```prompt ` bloğunu **olduğu gibi** kopyala.
2. Hedef platforma yapıştır.
3. Ajan; org.json → promptlar → döngüler → araştırma arşivi zincirini kurar/sürdürür.

## Üreteçler (bu promptların dayandığı kod)
- `scripts/generate_prompts.py` — her title/ekip/uygulama için prompt (`components/prompts/`).
- `scripts/research_loop.py` — top-100 kişi kaydı (`data/kaynaklar.json`) + zaman damgalı `arsiv/` + `docs/ARASTIRMA-TAKVIMI.md`.
- `scripts/build_talents.py` — kültür/sanat/spor +100 özel yetenek (`data/ozel_yetenekler.json`).
- Mevcut: `generate_org.py`, `generate_docs.py`, `daily_ops.py`, `weekly_board.py`, `nightly.sh`.

## 🚩 Gerçekçilik notu
İstenen "prompt başına 900.000.000.000 karakter" / "title başına 122 prompt" hedefleri fiziksel olarak
imkânsızdır (tek LLM çıktısı yüz KB mertebesindedir; 600×122×3 ≈ 220.000 dosya). Bunun yerine bu sistem
**yüksek-sinyalli + üreteçle ölçeklenen** promptlar kullanır (reponun ilkesi: *signal over length*).
Modül/prompt sayısını büyütmek için: `python3 scripts/generate_prompts.py --modules N`.
