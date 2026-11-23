# Meest Competitive Intelligence — pierwsza analiza
**Data wykonania:** 2026-11-23  
**Typ:** baseline + weryfikacja publicznych źródeł; **nie** alert nowych zmian z ostatnich 24 h.  
**Konkurenci:** Nova Post, epaka.pl, Furgonetka.pl, GlobKurier, Przesyłarka.pl, Poczta Polska, Apaczka, Sendit.

## Analytics Reporter — wynik skanera
- 3 zapisane skany w repozytorium: 20:48, 20:50, 20:51 UTC.
- Każdy skan: **20/20 źródeł bez błędów pobierania**; **0 nowych linków**.
- Pierwszy skan ustanowił baseline; brak nowego linku nie jest dowodem braku nowych reklam, promocji czy zmian ceny.
- `data/events.json` było puste w chwili analizy, dlatego `data/analysis.json` pozostaje bez wpisów o nowych zdarzeniach.

## Market Researcher — publicznie potwierdzone informacje (materiały zastane)
- **Nova Post**: opublikowany program poleceń z terminem do 31.12.2026. Źródło: https://novapost.com/pl-pl/more/referral-program/ . Brak dowodu, że program rozpoczął się dziś.
- **Sendit**: informacja o aktualizacji cennika FedEx i Ambro Express od 01.11.2026. Źródło: https://www.sendit.pl/aktualnosci . Jest to wcześniejsza zmiana.
- **Furgonetka**: przegląd zmian produktowych z 14.10.2026. Źródło: https://furgonetka.pl/blog/pazdziernikowy-przeglad-zmian/ . Nie jest nową publikacją z dzisiaj.
- **GlobKurier**: na blogu wzmianka o sobotnich nadaniach w sezonie przedświątecznym 2026. Źródło: https://www.globkurier.pl/blog . Data rozpoczęcia oferty wymaga odrębnej weryfikacji.
- **Poczta Polska**: komunikaty prasowe dostępne w https://media.poczta-polska.pl/releases ; bez potwierdzenia nowej promocji w badanym oknie.
- **epaka.pl**, **Przesyłarka.pl** i **Apaczka**: dostępne oficjalne blogi; brak zweryfikowanego nowego działania z ostatnich 24 h w tym przeglądzie: https://www.epaka.pl/blog-kurierski/ , https://przesylarka.pl/blog , https://www.apaczka.pl/blog/ .

## Marketing Strategist — interpretacja
- Program poleceń Nova Post może wskazywać na rozwijanie pozyskiwania klientów przez rekomendacje; nie znamy efektów ani budżetu.
- Treści poradnikowe i aktualizacje platform kurierskich uzasadniają monitorowanie wartości komunikowanych klientom, ale nie potwierdzają nowej kampanii reklamowej.

## Trend Researcher — hipotezy do obserwacji
- **Ułatwianie wysyłki i rozwój e-commerce**: pojawiające się aktualizacje funkcjonalne warto zestawiać z działaniami innych platform w kolejnych tygodniach.
- **Promocje retencyjne i polecenia**: program Nova Post należy porównać z mechanikami rabatowymi konkurencji; pojedynczy przypadek nie wystarcza do stwierdzenia trendu.

## Growth Strategist — propozycje działań
1. Porównać mechanikę programu poleceń Nova Post z istniejącymi programami Meest Post.
2. Zbierać przez 14 dni promocje i zmiany cen dla porównywalnych tras i gabarytów, zanim zarekomendujemy reakcję cenową.
3. Rozbudować skaner o zmiany treści istniejących stron i osobną integrację źródeł reklam; samo wykrywanie nowych URL nie wystarcza.

## Ograniczenia
Jest to **pierwszy ręcznie wykonany raport pięciu ról w ChatGPT**, a nie pięć samodzielnie działających procesów. Źródła internetowe zostały zweryfikowane, jednak bez historycznych zrzutów treści nie da się wykazać, kiedy dokładnie zaszła każda zmiana. Nie należy traktować informacji zastanych jako alertów dziennych. Brak weryfikacji Meta Ad Library, Google Ads Transparency i pełnych social mediów. Raport jest publiczny w repozytorium.
