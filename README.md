# Meest Competitive Intelligence

Publiczny dashboard monitorowania 8 konkurentów Meest Post, uruchamiany przez GitHub Actions.

**Dashboard:** https://jlukiaschenko-rgb.github.io/meest-competitive-intelligence/ *(dostępny dopiero po włączeniu Pages i poprawnym wdrożeniu)*

## Zakres MVP
- 8 konkurentów, 19 publicznych stron: promocje, aktualności, blogi i strony główne
- Wykrywanie nowych linków publikacji oraz raportowanie z dowodem (źródłowy URL)
- Pierwsze skanowanie buduje punkt odniesienia; nie produkuje sztucznych alertów
- Historia dziennych kontroli i znalezionych zdarzeń w plikach `data/*.json`
- Dashboard: priorytety, wyszukiwarka, filtrowanie po firmie i kategorii, historia skanów
- Publikacja przez GitHub Pages

## Uruchomienie
1. GitHub → **Settings → Pages → Build and deployment → Source: GitHub Actions**.
2. GitHub → **Settings → Actions → General → Workflow permissions: Read and write permissions** (jeśli jest wymagane).
3. GitHub → **Actions → Daily competitive scan and Pages → Run workflow**. Kolejne uruchomienia zaplanowano raz dziennie.
4. W zakładce Actions sprawdź logi skanów i wdrożenia. Dashboard nie będzie dostępny do momentu udanej publikacji.

Uruchomienie lokalne: `python3 scripts/scan.py`, następnie serwowanie repozytorium `python3 -m http.server 8000` i otwarcie `http://localhost:8000`.

## Uczciwość danych i ograniczenia
- Narzędzie wykrywa nowe linki pojawiające się na monitorowanych stronach. **Nie jest pełnym systemem inteligentnego scrapingu**, nie gwarantuje uchwycenia każdej obniżki ceny ani zmian w treści istniejących podstron.
- Pierwsze uruchomienie nie generuje zdarzeń, tylko zapisuje stan bazowy. Brak zdarzeń przy błędach źródeł nie oznacza braku aktywności konkurenta.
- Dynamiczne strony / blokady botów / zmiany układu HTML mogą ograniczać wyniki. Błędy są widoczne w historii.
- Meta Ad Library, Google Ads Transparency Center i LinkedIn Ad Library **nie są automatycznie odczytywane**. To kolejny etap integracji.
- Odczyt i zapis źródłowych URL nie potwierdza początku kampanii. Priorytety są heurystyczne, a daty wykrycia różnią się od dat publikacji.
- Repozytorium i historia są **publiczne**. Nie dodawaj poufnych danych ani tokenów do plików.

## Konfiguracja
Lista źródeł: `config/sources.json`; kod skanera: `scripts/scan.py`; dzienne skanowanie i publikacja: `.github/workflows/daily.yml`.

Opracowanie: wersja początkowa do dalszej rozbudowy o porównania cen, deduplikację i weryfikację kampanii reklamowych.
