# LLM ENV — OpenRouter anahtarı (başlangıç rehberi)
> TR: Bu dosya, API key’in ne olduğunu ve nasıl güvenli kullanılacağını anlatır.
> Anahtarlar sadece lokal `.env.local` dosyasındadır — **asla GitHub’a / commit’e koyma**.

---

## 1) Bu ne? Neden lazım?

**API key** = OpenRouter’a “ben hesabın sahibiyim, faturalı çağrı yapabilirim” diyen gizli şifre.

Bu projede günlük makale üretimi (`scripts/daily_ops.py`) LLM çağırır.
- Key **varsa** → gerçek makale yazılır.
- Key **yoksa** → sistem yine çalışır ama makale “iskelet” kalır (döngü kırılmaz).

**OpenRouter** bir aracıdır: tek key ile Claude / GPT vb. modellere bağlanırsın.
Site: https://openrouter.ai

---

## 2) “Rotate” ne demek? Neden öneriyoruz?

**Rotate** = eski key’i iptal edip **yeni** key üretmek.

Neden?
- Key bir yere (chat, e-posta, ekran görüntüsü) yazıldıysa başkası kullanabilir → kredin yanar.
- Bu sohbette bir key paylaşıldı → güvenlik için yenilemek iyi pratiktir.
- Zorunlu değil; ama önerilir.

Eski key çalışmaya devam eder **ta ki** OpenRouter’da sildiğin / revoke ettiğin ana kadar.

---

## 3) Adım adım: yeni key al

1. Tarayıcıda aç: **https://openrouter.ai/settings/keys**
2. Giriş yap (Google / e-posta hesabınla).
3. Hesabında kredi / bakiye olduğundan emin ol (Keys sayfası veya Billing).
   - Boş bakiyede key çalışır ama çağrı **ücret hatası** verebilir.
4. **Create API Key** (veya “New key”) de.
5. İsmi isteğe bağlı yaz (ör. `adops-agents-local`).
6. Oluşan key’i **hemen kopyala**.
   - Biçim genelde: `sk-or-v1-` ile başlar, uzun bir metin.
   - Sayfayı kapattıktan sonra tam key çoğu zaman **bir daha gösterilmez** → bir yere güvenli yapıştırana kadar kaybetme.
7. (Öneri) Eski / sızmış key’in yanındaki **Delete / Revoke** ile iptal et.
   - Böylece eski key artık çalışmaz.

🚩 Key’i tekrar chat’e, PR’a, commit’e, Slack’e yapıştırma.

---

## 4) Key’i projeye koy (yalnızca `.env.local`)

### `.env.local` nedir?
Proje kökündeki gizli ayar dosyası. Git **bilerek görmez** (`.gitignore` → `.env.*`).
Yani GitHub’a push edilmez.

### Dosya yolu
Repo kökü:
```text
adops-agents/
  .env.local          ← burası (gizli)
  docs/LLM-ENV.md     ← bu rehber
  scripts/llm_client.py
```

### Dosya içeriği (örnek)
Cursor / VS Code ile `.env.local` aç, **şuna benzer** olsun:

```bash
# Local secrets — gitignored. DO NOT COMMIT.
OPENROUTER_API_KEY=sk-or-v1-BURAYA_YENİ_KEYİ_YAPIŞTIR
OPENROUTER_MODEL=anthropic/claude-sonnet-4
LLM_PROVIDER=openrouter
```

Kurallar:
- `=` işaretinin sağında **boşluk olmasın** (yanlış: `KEY = sk-...`).
- Key’i tırnak içine almak şart değil.
- Eski `sk-or-v1-...` satırını sil / değiştir; iki key yan yana bırakma.
- Dosyayı kaydet.

### Terminal ile (isteğe bağlı)
Proje klasöründeyken:

```bash
# Mac/Linux — dosyayı oluştur/güncelle (key’i kendin yaz)
nano .env.local
# veya
code .env.local
```

Kaydettikten sonra **yeni terminal** aç veya live loop’u yeniden başlat ki env yüklensin.

---

## 5) Doğru mu diye test et

Proje kökünde:

```bash
python3 scripts/llm_client.py
```

Beklenen:
```text
openrouter=set anthropic=missing
reply: PONG
```

- `PONG` → key çalışıyor.
- `LLM SKIPPED` / `HTTP 401` → key yanlış, silinmiş veya eksik kopyalanmış.
- `HTTP 402` / credit → OpenRouter bakiyesi yetersiz: https://openrouter.ai/settings/credits

Makaleyi zorla yeniden üretmek için:

```bash
FORCE_LLM_ARTICLE=1 python3 scripts/daily_ops.py
```

Başarılıysa `makaleler/YYYY-MM-DD-....md` içinde `source: daily-ops llm (openrouter)` görünür.

---

## 6) Sık yapılan hatalar

| Hata | Ne olur | Düzeltme |
|---|---|---|
| Key’i `README` / commit’e yazmak | Sızıntı | Commit’ten çıkar, key’i rotate et |
| `.env` yerine yanlış klasör | Script key görmez | Dosya **repo kökünde** `.env.local` olmalı |
| `ANTHROPIC_API_KEY` sanmak | Bu key Anthropic formatı değil | OpenRouter → `OPENROUTER_API_KEY` |
| Eski key’i silmeden yenisini koymamak (sızıntı sonrası) | Eski key hâlâ çalışır | OpenRouter’da eskiyi **Revoke** |
| Live tmux hâlâ eski env ile | Eski key kullanılır | `live_ops` oturumunu yeniden başlat |

Live yeniden başlat (Cloud / tmux kullanan ortam):

```bash
bash scripts/live_ops.sh --loop 120
```

---

## 7) Öncelik sırası (sistem nasıl seçer?)

1. `OPENROUTER_API_KEY` → OpenRouter (tercih)
2. `ANTHROPIC_API_KEY` → doğrudan Anthropic (yedek)
3. Hiçbiri yok → iskelet makale (döngü yine çalışır)

Kod: `scripts/llm_client.py`

---

## 8) Metin için 30 saniyelik kontrol listesi

- [ ] https://openrouter.ai/settings/keys → yeni key oluşturdum
- [ ] Eski/sızmış key’i sildim (revoke)
- [ ] Key’i yalnızca `.env.local` içine yazdım
- [ ] Chat / PR / commit’e yapıştırmadım
- [ ] `python3 scripts/llm_client.py` → `PONG` aldım

Hazır. Başka bir şey yapmana gerek yok; ajan / `daily_ops` / live loop key’i buradan okur.
