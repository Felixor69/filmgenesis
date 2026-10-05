# Montaż i lektor AI (budżet 0 zł, jedna osoba)

## 1. Narzędzia

| Do czego | Narzędzie | Dlaczego |
|---|---|---|
| Trailer 16:9 | **DaVinci Resolve** (darmowa wersja) | Pełny montaż, korekcja barwna, dźwięk (Fairlight), napisy, eksport do 4K |
| Klipy pionowe 9:16 | **CapCut** (desktop) | Szybkie przycinanie, automatyczne napisy po polsku, gotowe proporcje pod TikTok i Reels |
| Nagrywanie gry | **OBS Studio** | Patrz [04-shotlista-gameplay.md](04-shotlista-gameplay.md) |
| Obrazy, wideo, muzyka, lektor | **ChatGPT, Gemini (Veo), Suno, Gemini TTS** | Kto do czego: [03-prompty-ai-wideo.md](03-prompty-ai-wideo.md), sekcja 0 |
| Czcionki | **Google Fonts**: `Cinzel` (tytuły, napisy typu „PÓŁ-ANIOŁ”), `Cormorant Garamond` (cytaty), `Inter` (plansza końcowa, linki) | Darmowe, także do użytku komercyjnego |

## 2. Kolejność pracy nad trailerem

1. **Najpierw lektor i muzyka.** Wygeneruj lektora (sekcja 5) i muzykę w Suno, potem ułóż je na osi czasu. Rytm muzyki wyznacza cięcia.
2. **Znaczniki na bitach.** W DaVinci odtwarzaj muzykę i na każdym mocnym uderzeniu wciskaj `M`, żeby wstawić znacznik. Na znacznikach tniesz ujęcia.
3. **Szkielet z gameplayu.** Wstaw wszystkie ujęcia GP zgodnie ze scenariuszem, bo są pewne. Brakujące ujęcia AI zastąp na razie czarnymi planszami z opisem („AI-05 Pół-Demon”).
4. **Ujęcia AI** wstawiaj w miarę generowania, bo przy dziennym limicie Veo to potrwa 2–3 tygodnie.
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
- Efekty: dźwięk otoczenia wygenerowany przez Veo razem z ujęciami AI (tętent, ogień, wiatr) oraz darmowe biblioteki (Pixabay Sound Effects, YouTube Audio Library): dzwon, szept, szron. Muzykę z plików Veo wyciszasz, bo muzyka jest z Suno.
- Głośność końcowa pod YouTube: ok. **-14 LUFS** (miernik Loudness w Fairlight).

**Eksport pod YouTube:** H.264 lub H.265, 1080p lub 4K, 24 fps, bitrate „Automatic – Best”. Wersja 4K dostaje na YouTube lepszą kompresję, nawet jeśli materiał z gry jest w 1080p.

**Wersja pionowa (CapCut):** import gotowych fragmentów, proporcje 9:16, gameplay przycięty do środka (postać jest zawsze w centrum ekranu). Automatyczne napisy z poprawką nazw (Eldoria, Orrena, Pół-Demon). **Strefa bezpieczna:** napisy nie mogą schodzić niżej niż ok. 20% od dołu i wchodzić na prawą krawędź, bo tam są przyciski TikToka.

## 5. Lektor AI

**Narzędzie: Gemini TTS w Google AI Studio.** Bezpośredni link: https://aistudio.google.com/generate-speech (od 23.09.2026 model Gemini 3.8 Flash TTS i biblioteka ponad 2000 głosów do odsłuchania i filtrowania po języku). Polski jest obsługiwany przez model, nawet jeśli nie ma go w filtrze języka głosów (filtr pokazuje język „rodzimy” głosu). Zapasowo: ElevenLabs (darmowy plan wymaga podpisu w opisie filmu i może ograniczać użycie komercyjne).

**Głos:** niski, dojrzały, spokojny: narrator legendy, nie spiker reklamy. W bibliotece ustaw Pitch: Low, przesłuchaj kilka głosów na pierwszym zdaniu i wybierz jeden na cały trailer.

**Najważniejsza zasada:** model czyta pole tekstu **dosłownie, słowo w słowo**. Instrukcja tonu wpisana w tekst zostanie przeczytana na głos. Dlatego:
- w **polu tekstu** wpisujesz tylko polskie zdanie (kolumna „Tekst”);
- ton wpisujesz w **osobne pole stylu** przy danej kwestii (w edytorze to ustawienie stylu lub dostawy przy linijce mówcy), **po angielsku** (kolumna „Styl”);
- krótkie pauzy i oddechy wstawiasz w tekst jako znaczniki w nawiasach ostrych, np. `<pause>`, `<breath>`.

**Zasady:**
- Każdą linijkę generuj **osobno** i w kilku wersjach, potem wybierz najlepszą. Dłuższe pauzy robisz w montażu.
- Po wygenerowaniu **przesłuchaj nazwy własne**. Jeśli akcent jest zły, zapisz słowo fonetycznie (np. „Or-rena”) albo wstaw przecinek.

### Tekst do wygenerowania (linijka = osobny plik)

| Plik | Tekst (pole tekstu) | Styl (osobne pole, po angielsku) | Gdzie w filmie |
|---|---|---|---|
| L01 | `Bogowie patrzą... <pause>` | `deep low whisper, very slow, mysterious, like the narrator of a dark legend` | 0:00 |
| L02 | `...a dusze świecą w ciemności.` | `starts as a low whisper and rises into a calm deep voice, slow` | 0:04 |
| L03 | `Każda opowieść zaczyna się w Przystani Orrena.` | `warm, calm, deep storyteller voice, gentle pace` | 0:12 |
| L04 | `Wybierz krew... <pause>` | `firm, confident, deep and powerful, slow and deliberate` | 0:22 |
| L05 | `...wybierz boga.` | `firm, confident, deep, with solemn emphasis` | 0:38 |
| L06 | `Każda dusza, którą zbierzesz, rozświetli twoją drogę.` | `calm, serious, deep narrator voice, measured pace` | 0:43 |
| L07 | `Jeśli usłyszysz kopyta tam, gdzie nie ma drogi... <pause> nie odwracaj się.` | `quiet, tense, ominous, slow, almost a whisper, like telling a ghost story` | 0:48 |
| L08 | `Mapa, jakiej Ultima jeszcze nie widziała. Nie dla wygody. Dla odkrywców.` | `energetic, proud, epic trailer narrator, building intensity` | 0:58 |
| L09 | `Nie obiecamy ci zwycięstwa. <pause> Nie obiecamy ci nagrody.` | `very slow, heavy, grave, deep voice` | 1:02 |
| L10 | `Obiecamy ci tylko świat, który pamięta...` | `warm, hopeful, deep, slow` | 1:07 |
| L11 | `...i który zapamięta ciebie.` | `the quietest line, soft deep near-whisper, final and intimate` | 1:12 |
| L12 | `Genesis.` | `calm, dignified, deep, a single solemn word` | 1:16 |

### Teaser (osobno)
| Plik | Tekst |
|---|---|
| T01 | Bogowie patrzą... |

## 6. Plan pracy dla jednej osoby (orientacyjny)

| Tydzień | Zadania |
|---|---|
| 1 | Klatki kluczowe w ChatGPT i Gemini. Lektor L01–L12 w AI Studio. Muzyka w Suno. Nagranie GP-01, GP-02, GP-13, GP-14 |
| 2 | Sesja nagraniowa z drużyną (GP-03…GP-12). Animowanie ujęć w Veo w ramach dziennego limitu. Szkielet trailera |
| 3 | Ostatnie ujęcia AI. Nagranie eventu (GP-17). Montaż, kolor, dźwięk |
| 4 | Teaser, wersja pionowa, pierwsze klipy z serii. Start kampanii (T1) |

Klip „Jak zacząć w 5 minut” (GP-14) warto zmontować **w tygodniu 1** i od razu wstawić na stronę Instalacja. Przyda się niezależnie od kampanii.
