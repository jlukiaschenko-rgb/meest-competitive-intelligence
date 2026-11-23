# Zespół agentów — Meest Competitive Intelligence

Zatwierdzony docelowy skład: **5 ról**.

| Rola | Zadanie |
| --- | --- |
| Market Researcher | Wyszukiwanie zmian i nowych działań konkurentów |
| Marketing Strategist | Analiza reklam, komunikacji, grup docelowych i pozycjonowania |
| Analytics Reporter | Porównanie historii, priorytety i raporty |
| Growth Strategist | Rekomendacje marketingowe i eksperymenty |
| Trend Researcher | Wczesne trendy, wzorce, słabe sygnały i szanse rynkowe |

**Trend Researcher** jest oparty na rzeczywistym pliku [Product Trend Researcher w Agency Agents](https://github.com/msitarzewski/agency-agents/blob/main/product/product-trend-researcher.md). Pozostałe role oznaczone jako `custom` to nazwy funkcjonalne dostosowane do tego projektu, a nie gwarantowane nazwy agentów z upstream.

## Podział ról

Market Researcher identyfikuje **co się wydarzyło**. Trend Researcher analizuje **jakie wzorce z tego wynikają** — np. wzrost znaczenia dostaw transgranicznych czy nowego typu oferty w wielu firmach.

Przyszły przebieg: `zbieranie źródeł → nowe zdarzenia → weryfikacja → Marketing Strategist + Trend Researcher → Analytics Reporter → Growth Strategist → dashboard`.

## Status wdrożenia

To **konfiguracja i projekt ról**, nie uruchomiony system wieloagentowy. Dotychczasowy skaner Python i dashboard nie wywołują modeli AI. Integracja pięciu ról wymaga podłączenia wykonawcy modeli, ograniczeń budżetu i weryfikacji wyników. Nie wolno przedstawiać wygenerowanych rekomendacji jako potwierdzonych faktów bez źródeł.

Konfiguracja maszynowa: [config/agents.json](../config/agents.json).
