# Pięcioagentowa analiza AI — uruchomienie

Workflow GitHub Actions uruchamia skaner, a następnie `scripts/analyze.py` dla pięciu ról: Market Researcher, Marketing Strategist, Trend Researcher, Analytics Reporter i Growth Strategist.

Każda rola otrzymuje informacje o wykrytym zdarzeniu oraz wyniki poprzednich ról. Wyniki są zapisywane w `data/analysis.json` i pokazywane na dashboardzie. Każda rola to osobne wywołanie API modelu, a nie autonomiczny agent z dostępem do pełnego internetu. Konfiguracja ról: `config/agents.json`.

## Wymagany sekret
Repozytorium → **Settings → Secrets and variables → Actions → New repository secret**:
- Nazwa: `OPENAI_API_KEY`
- Wartość: prywatny klucz OpenAI API. **Nigdy nie wpisuj go do kodu ani w czacie.**

Bez sekretu skaner i strona mogą działać, ale analiza AI zostaje pominięta, a `data/ai_status.json` pokaże `waiting_for_api_key`.

## Jak uruchomić
1. **Settings → Pages → Source → GitHub Actions**
2. **Actions → Daily competitive scan and Pages → Run workflow**
3. Sprawdź status w **Actions**, a po sukcesie stronę https://jlukiaschenko-rgb.github.io/meest-competitive-intelligence/

Workflow ma też trigger `push` dla zmian w kodzie, oraz codzienne uruchomienie o 06:12 UTC. Godzina lokalna w Polsce zmienia się z czasem letnim.

## Ograniczenia
- Pierwszy skan jest bazą odniesienia i nie generuje sztucznych „nowości”.
- Skaner wykrywa linki, a nie wszystkie zmiany cen lub treści.
- AI analizuje metadane zdarzeń i poprzednie wyniki, **nie czyta w całości stron źródłowych**; dlatego oceny mają charakter hipotez i wymagają weryfikacji.
- Biblioteki reklam i profile social media nie są automatycznie integrowane.
- Repozytorium jest publiczne, więc raporty AI również są publiczne.
- Wykonywane jest maksymalnie 12 nowych zdarzeń dziennie × 5 wywołań modelu. Opłaty API zależą od użycia; nie ma automatycznego twardego limitu kosztów.
