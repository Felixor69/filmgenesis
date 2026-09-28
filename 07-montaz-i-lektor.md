# Montaż i lektor AI (budżet 0 zł, jedna osoba)

## 1. Narzędzia

| Do czego | Narzędzie | Dlaczego |
|---|---|---|
| Trailer 16:9 | **DaVinci Resolve** (darmowa wersja) | Pełny montaż, korekcja barwna, dźwięk (Fairlight), napisy, eksport do 4K |
| Klipy pionowe 9:16 | **CapCut** (desktop) | Szybkie przycinanie, automatyczne napisy po polsku, gotowe proporcje pod TikTok i Reels |
| Nagrywanie gry | **OBS Studio** | Patrz [04-shotlista-gameplay.md](04-shotlista-gameplay.md) |
| Czcionki | **Google Fonts**: `Cinzel` (tytuły, napisy typu „PÓŁ-ANIOŁ”), `Cormorant Garamond` (cytaty), `Inter` (plansza końcowa, linki) | Darmowe, także do użytku komercyjnego |

## 2. Kolejność pracy nad trailerem

1. **Najpierw lektor i muzyka.** Wygeneruj lektora (sekcja 5), wybierz muzykę i ułóż je na osi czasu. Rytm muzyki wyznacza cięcia.
2. **Znaczniki na bitach.** W DaVinci odtwarzaj muzykę i na każdym mocnym uderzeniu wciskaj `M`, żeby wstawić znacznik. Na znacznikach tniesz ujęcia.
3. **Szkielet z gameplayu.** Wstaw wszystkie ujęcia GP zgodnie ze scenariuszem, bo są pewne. Brakujące ujęcia AI zastąp na razie czarnymi planszami z opisem („AI-05 Pół-Demon”).
4. **Ujęcia AI** wstawiaj w miarę generowania, bo przy darmowych kredytach to potrwa 2–3 tygodnie.
5. **Napisy i plansze.**
6. **Kolor.**
7. **Miks dźwięku.**
8. **Eksport**, potem wersja pionowa i teaser z tego samego materiału.

**Ścieżki na osi czasu:** V1 gameplay · V2 AI · V3 napisy · V4 znak „Grafika z gry” · A1 lektor · A2 muzyka · A3 efekty (dzwon, tętent, szept).

## 3. Match cut (przejście AI → gra)

To najważniejszy efekt w filmie. Jak go zrobić:

1. Ujęcie AI kładziesz na V2, a ujęcie z gry na V1, zaraz za nim.
2. Na ostatniej klatce AI ustaw krycie V2 na 50%, żeby widzieć oba obrazy naraz.
3. Przesuń i przeskaluj gameplay (Inspector → Transform), aż postać znajdzie się **w tym samym miejscu kadru** co w AI.
4. Wróć z kryciem do 100%. Cięcie **dokładnie na bicie muzyki**.
5. Opcjonalnie: 2–4 klatki białego błysku (Generator „Solid Color” z krótkim zanikiem) albo szybki zoom na przejściu. Sprawdź na żywo, co lepiej wygląda.

Znak `Grafika z gry` (mały, w rogu, `Inter`, 60% krycia) pojawia się przy pierwszym ujęciu z gry i przy ujęciu z eventu.

## 4. Kolor, dźwięk, eksport

**Kolor (strona Color):**
- Ujęcia AI: lekko obniżone nasycenie, cienie w stronę turkusu, światła w stronę złota.
- Gameplay: **tylko delikatnie** (kontrast +, nasycenie ±0). Gra ma wyglądać jak gra, bo obiecujemy „bez upiększeń”.
- Na koniec jeden wspólny node z lekkim ziarnem (Film Grain) na wszystkim, żeby całość się kleiła.

**Dźwięk (Fairlight):**
- Lektor ok. **-6 dB** szczytowo, muzyka ściszana pod lektorem (**ducking**) o ok. 8–10 dB.
- Na lektorze: lekki pogłos (Reverb, mały „hall”), podbicie niskich tonów (EQ, ok. +2 dB przy 120 Hz), kompresor. AI brzmi wtedy mniej „syntetycznie”, a bardziej jak narrator.
- Efekty z darmowych bibliotek (Pixabay Sound Effects, YouTube Audio Library): dzwon, tętent, szept, ogień, szron.
- Głośność końcowa pod YouTube: ok. **-14 LUFS** (miernik Loudness w Fairlight).

**Eksport pod YouTube:** H.264 lub H.265, 1080p lub 4K, 24 fps, bitrate „Automatic – Best”. Wersja 4K dostaje na YouTube lepszą kompresję, nawet jeśli materiał z gry jest w 1080p.

**Wersja pionowa (CapCut):** import gotowych fragmentów, proporcje 9:16, gameplay przycięty do środka (postać jest zawsze w centrum ekranu). Automatyczne napisy z poprawką nazw (Eldoria, Orrena, Pół-Demon). **Strefa bezpieczna:** napisy nie mogą schodzić niżej niż ok. 20% od dołu i wchodzić na prawą krawędź, bo tam są przyciski TikToka.

## 5. Lektor AI

**Narzędzie:** darmowy plan TTS z dobrymi polskimi głosami, np. ElevenLabs Free. **Przed publikacją sprawdź warunki darmowego planu.** Zwykle wymaga podpisu w opisie filmu (miejsce na to jest w opisie YouTube w [05-teksty-postow.md](05-teksty-postow.md)) i może ograniczać użycie komercyjne. Genesis jest non-profit, ale warto to potwierdzić w regulaminie narzędzia.

**Głos:** niski, dojrzały, spokojny: narrator legendy, nie spiker reklamy. Wybierz 2–3 głosy i porównaj je na pierwszym zdaniu.

**Ustawienia (ElevenLabs lub podobne):** Stability ok. 35–45% (więcej emocji) · Similarity ok. 75% · Style niski (0–20%). Wolniejsze tempo, jeśli narzędzie na to pozwala.

**Zasady:**
- Każdą linijkę generuj **osobno** i w kilku wersjach, potem wybierz najlepszą. Pauzy robisz w montażu, nie w TTS.
- Wielokropek „...” zwykle daje w TTS naturalne zawieszenie głosu. Jeśli nie, rozbij zdanie na dwa pliki.
- Po wygenerowaniu **przesłuchaj nazwy własne**. Jeśli akcent jest zły, zapisz słowo fonetycznie (np. „Or-rena”) albo wstaw przecinek.

### Tekst do wygenerowania (linijka = osobny plik)

| Plik | Tekst | Gdzie w filmie | Uwagi |
|---|---|---|---|
| L01 | Bogowie patrzą... | 0:00 | Szept, bardzo cicho |
| L02 | ...a dusze świecą w ciemności. | 0:04 | Szept przechodzący w głos |
| L03 | Każda opowieść zaczyna się w Przystani Orrena. | 0:12 | Ciepło, spokojnie |
| L04 | Wybierz krew... | 0:22 | Pewnie, na bębnach |
| L05 | ...wybierz boga. | 0:38 | |
| L06 | Każda dusza, którą zbierzesz, rozświetli twoją drogę. | 0:43 | |
| L07 | Jeśli usłyszysz kopyta tam, gdzie nie ma drogi... nie odwracaj się. | 0:48 | Cicho, z napięciem. Po generowaniu dodaj więcej pogłosu |
| L08 | Mapa, jakiej Ultima jeszcze nie widziała. Nie dla wygody. Dla odkrywców. | 0:58 | Dynamicznie |
| L09 | Nie obiecamy ci zwycięstwa. Nie obiecamy ci nagrody. | 1:02 | Wolno, z ciężarem |
| L10 | Obiecamy ci tylko świat, który pamięta... | 1:07 | |
| L11 | ...i który zapamięta ciebie. | 1:12 | Najcichsza, ostatnia linijka, na czarnym tle |
| L12 | Genesis. | 1:16 | Opcjonalnie, na logo |

### Teaser (osobno)
| Plik | Tekst |
|---|---|
| T01 | Bogowie patrzą... |

## 6. Plan pracy dla jednej osoby (orientacyjny)

| Tydzień | Zadania |
|---|---|
| 1 | Generowanie klatek kluczowych AI (obrazy są za darmo i bez limitu wideo). Lektor L01–L12. Wybór muzyki. Nagranie GP-01, GP-02, GP-13, GP-14 |
| 2 | Sesja nagraniowa z drużyną (GP-03…GP-12). Animowanie ujęć AI w ramach dziennych limitów. Szkielet trailera |
| 3 | Ostatnie ujęcia AI. Nagranie eventu (GP-17). Montaż, kolor, dźwięk |
| 4 | Teaser, wersja pionowa, pierwsze klipy z serii. Start kampanii (T1) |

Klip „Jak zacząć w 5 minut” (GP-14) warto zmontować **w tygodniu 1** i od razu wstawić na stronę Instalacja. Przyda się niezależnie od kampanii.
