# Autoryzacja ChatGPT i codzienna analiza

## Obecny tryb: ChatGPT + połączony GitHub

ChatGPT wykonuje codzienny raport za pomocą zaplanowanego zadania ChatGPT, używając istniejącego połączenia GitHub. **Nie uruchamia OAuth wewnątrz GitHub Actions**. Nie jest potrzebny `OPENAI_API_KEY`. Zadanie jest skonfigurowane na około **09:00 Europe/Warsaw**.

1. GitHub Actions wykonuje techniczny skan 20 publicznych stron i zapisuje `data/events.json`, `data/history.json` i `data/state.json`.
2. Zaplanowane zadanie ChatGPT po skanowaniu czyta źródła i historię przez połączony GitHub i opracowuje raport według pięciu ról: Market Researcher, Marketing Strategist, Trend Researcher, Analytics Reporter, Growth Strategist.
3. ChatGPT zwraca raport użytkownikowi. Gdy dostępna jest operacja zapisu plików podczas uruchomienia zadania, może również dopisać zweryfikowane analizy do `data/analysis.json`. **Automatyczny zapis z harmonogramu nie jest jeszcze potwierdzony testem**.
4. Wszystkie ważne twierdzenia muszą mieć źródła; pojedynczy nowy URL to nie dowód nowej kampanii.

## Czego to nie robi

- Nie istnieje mechanizm wykorzystania sesji ChatGPT w anonimowym/efemerycznym GitHub-hosted Actions. Nie przechowuj `~/.codex/auth.json` ani tokenów OAuth w repozytorium lub publicznych plikach.
- Pięć ról oznacza pięć kroków analizy podczas zadania ChatGPT, a nie pięć oddzielnie zalogowanych usług.
- Wersja `scripts/analyze.py` wykorzystująca API pozostaje w repozytorium jako **nieaktywna**, nie jest wywoływana w workflow. Nie jest potrzebna do obecnego trybu.
- Monitoring reklam Meta/Google/LinkedIn oraz pełnych treści dynamicznych stron wymaga dodatkowych, dopuszczonych źródeł.
- Repozytorium jest publiczne: publikowane raporty też będą publiczne.

## Publikacja

Włącz `Settings → Pages → Build and deployment → Source → GitHub Actions` w repozytorium. Pierwszy workflow nie opublikował Pages, ponieważ strona Pages nie była włączona. Następnie uruchom workflow lub wykonaj commit zmieniający jego kod, by ponowić wdrożenie.

GitHub Pages: https://jlukiaschenko-rgb.github.io/meest-competitive-intelligence/ (link zadziała dopiero po poprawnym wdrożeniu).
