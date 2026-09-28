# Prompty AI wideo i biblia stylu

Prompty są **po angielsku**, bo generatory wideo i obrazu dają wtedy najlepsze wyniki. Opisy i uwagi są po polsku. Numeracja ujęć odpowiada [02-scenariusz-trailera.md](02-scenariusz-trailera.md).

## 0. Narzędzia (to, co już macie)

| Zadanie | Narzędzie | Jak |
|---|---|---|
| **Klatki kluczowe (obrazy)** | **ChatGPT** (generowanie obrazów) i **Gemini** (generowanie i edycja obrazów) | ChatGPT dobrze trzyma się złożonych opisów kompozycji. Gemini dobrze **edytuje istniejący obraz, zachowując tę samą postać** („ta sama postać, teraz w pełnej zbroi, na klifie”), co przydaje się przy bohaterach z Przystani i rasach. Wygeneruj w obu i wybierz lepszy obraz |
| **Wideo (animacja klatek)** | **Veo** w Gemini (oraz w Google Flow, jeśli wasz plan go obejmuje) | Tryb obraz → wideo: wgrywasz klatkę kluczową i dopisujesz prompt ruchu. Ujęcia ok. 8 s, 16:9 lub 9:16 |
| **Wideo (zapas)** | **Sora** w ChatGPT (jeśli jest w waszym planie) | Do ujęć, które w Veo nie wychodzą |
| **Muzyka** | **Suno** (płatny plan) | Patrz sekcja 5 |
| **Lektor** | Gemini TTS (Google AI Studio) | Patrz [07-montaz-i-lektor.md](07-montaz-i-lektor.md) |
| **Teksty** | ChatGPT lub Gemini | Warianty hooków, podpisów i opisów na bazie [05-teksty-postow.md](05-teksty-postow.md) |

**Do sprawdzenia w waszych planach, zanim zaczniecie:** dzienny limit filmów Veo, czy wideo ma **widoczny znak wodny** (jeśli tak, sprawdźcie, czy Flow albo wyższa rozdzielczość go nie usuwa, bo przycinanie kadru psuje kompozycję), dostępność Sory w waszym regionie i planie.

**Dźwięk z Veo:** Veo generuje też dźwięk. Muzyki z Veo nie używamy (mamy Suno), ale **odgłosy otoczenia z Veo mogą się przydać** (tętent, wiatr, ogień, szron). Dopisz do promptu linijkę `Audio: ...` (przykłady przy ujęciach), a w montażu zostaw tylko efekty.

## 1. Workflow (dla spójności ujęć)

0. **Limity Veo.** Dzienny limit filmów jest ograniczony, więc nie animujemy na ślepo. Klatkę kluczową dopracowujemy w ChatGPT lub Gemini (obrazy mają dużo większe limity) i dopiero gotowy kadr idzie do Veo. Kolejność: najpierw 11 ujęć trailera, potem serie klipów.
1. **Najpierw obraz, potem ruch (image-to-video).** Klatkę kluczową generujemy w ChatGPT lub Gemini, wybieramy najlepszą i dopiero ją animujemy w Veo. Daje to kontrolę nad kompozycją pod match cut.
2. **Arkusze postaci.** Wojownika i maga z Przystani (AI-03, AI-10) oraz rasy (AI-04–06) generujemy najpierw jako arkusze referencyjne: przód, profil, cała postać. Potem używamy ich jako referencji w każdym ujęciu.
3. **Referencja z gry.** Przed generowaniem robimy screenshot ujęcia GP, z którym łączymy AI (np. model Pół-Demona w grze), i dajemy go jako referencję kolorów i kostiumu. **Kolory stroju, skrzydeł czy płomieni w AI muszą się zgadzać z modelem w grze**, inaczej match cut nie zadziała.
4. **3–6 wariantów na ujęcie**, długość 4–8 s, przycinanie w montażu.
5. **Wspólny grading** na końcu: jeden LUT na AI i lekko na gameplay.

## 2. Biblia stylu Genesis

Doklejamy do każdego promptu:

```
STYLE: dark high-fantasy, painterly cinematic realism, the world of Eldoria, deep blue-black nights
where the only light comes from glowing souls and sacred relics, warm golden soul-light against cold
teal shadows, volumetric light, drifting motes of light, mist, anamorphic lens, shallow depth of field,
subtle film grain, 24fps cinematic motion, grounded and mysterious, no modern elements, no text, no logos
(short: dark fantasy, black night lit only by golden soul-light, teal mist, cinematic, film grain, no text)
```

**Paleta:**
- Światło dusz i reliktów: `#E8B04A` (złoto)
- Noc Eldorii: `#0B1A24` (prawie czerń z turkusem)
- Mgła i szron (Upiorni Jeźdźcy): `#9FC3CF`
- Ogień (Pół-Demon, kuźnia): `#D2542B`
- Tekst na ekranie: `#EDE3CC` (pergamin)

**Negative prompt:**
```
text, watermark, logo, modern clothing, guns, sci-fi, anime, cartoon, plastic skin, extra fingers,
deformed hands, morphing faces, blurry, low quality, bright daylight everywhere, Ultima Online logo
```

### Bohaterowie z Przystani (AI-03, AI-10)

```
WARRIOR: young adult, short dark hair, determined grey eyes, small scar on left cheek.
  START: brand-new plain steel breastplate slightly too light for them, round shield polished and spotless, simple sword.
  END: battle-worn dark steel armor, dented shield with painted crest, teal cloak, a glowing relic hanging at the belt.
MAGE: young adult, slim, curly auburn hair, shy smile, long coat with too many pockets,
  turning a small flickering crystal between the fingers.
```

---

## 3. Prompty trailera

### AI-01 · Dusze w ciemności (0:00–0:04) · statyczna, bardzo powolny najazd
```
Absolute darkness. A single tiny golden glowing soul appears and floats, then another, then dozens,
drifting like fireflies through the black void toward a hand holding a small silver crescent-moon amulet
on a gold chain. Only the souls give light. Very slow push-in. [STYLE]
```

### AI-02 · Relikt rozbłyska (0:04–0:08) · powolny odjazd
```
The souls flow into the crescent amulet which flares with warm golden light, the glow expanding outward
in a circle and revealing a dark ancient forest around a hooded adventurer. At the very edge of the light,
in the mist, a tall shadowy silhouette stands still, watching. Slow pull-back. [STYLE]
Audio: a soft resonant chime as the relic flares, quiet forest night ambience, no music.
```
**Match cut z GP-01:** krąg światła wokół postaci w centrum kadru, czarna reszta ekranu.

### AI-03 · Przystań Orrena (0:12–0:17) · kamera z pomostu, lekki ruch w bok
```
Dawn over a calm grey sea, a small island harbor town with wooden piers, stone walls and warm lanterns,
seagulls circling. A small boat docks; [WARRIOR, START] and [MAGE] step onto the wooden pier and look
toward the path leading inland into a green forest. Hopeful, peaceful, a new beginning.
Gentle lateral dolly. [STYLE, but golden dawn light instead of night]
```

### AI-04 · Pół-Anioł (0:22–0:24) · od dołu, kamera unosi się
```
A half-angel warrior stands in a shaft of divine light inside a ruined cathedral, then slowly unfurls
large luminous feathered wings, dust and light motes swirling around, calm solemn face, eyes glowing faintly.
Low angle, camera rising. [STYLE]
```
**Referencja:** kolor skrzydeł i zbroi z modelu Pół-Anioła w grze.

### AI-05 · Pół-Demon i płonący mustang (0:26–0:28) · orbita
```
A half-demon with small curved horns and ember-cracked skin raises a clawed hand; the ground splits
and a mustang made of living fire bursts out of the flames and rears up beside them, sparks and smoke
swirling. Night, ruined battlefield. Slow orbit. [STYLE]
Audio: roaring flames, a fiery horse neigh, crackling embers, no music.
```

### AI-06 · Nieumarły (0:30–0:32) · statyczna, zbliżenie na ziemię
```
Inside a dark crypt lit by cold green-blue light, a gaunt undead sorcerer in tattered robes points at the
stone floor; bony hands claw up through the cracked ground and a skeleton servant rises to its feet,
dust falling. Static camera, low angle. [STYLE]
```

### AI-07 · Krąg ośmiu bóstw (0:38–0:43) · kamera obraca się wewnątrz kręgu
```
Inside a vast ancient open-air temple at night, eight colossal stone statues of gods stand in a circle,
each lit by its own divine light: radiant gold (creation), sickly pale green (death), lush green (nature),
arcane violet (magic), pure white with diamonds (art), blood red (war), silver moonlight (night),
pitch black with a single glowing eye (shadow). A lone small figure stands at the center.
Camera spins slowly around the figure, looking up at the gods. Epic scale. [STYLE]
```
Ten sam prompt nadaje się do klipów „Bogowie Eldorii” (osobne ujęcie na każdy posąg, patrz sekcja 4).

### AI-08 · Upiorni Jeźdźcy (0:48–0:52) · statyczna, mgła się rozsuwa
```
A frozen northern swamp at night, the old road swallowed by bog. Thick mist parts like a torn bandage and
reveals a column of spectral cavalry riding in formation: dark shields without heraldry, sunken helmets
with a cold pale glow in the visor slits, armor rustling like old parchment. The ghostly horses' hooves
never touch the ground, leaving trails of frost that form letters of an unknown alphabet.
Breath turns to vapor, torches die out. Static camera, riders approach toward it. Eerie, silent. [STYLE,
cold teal and frost-blue palette]
Audio: muffled ghostly hoofbeats, creaking frost, cold wind, faint whispers, no music.
```
To najlepszy potwór do trailera: ma gotową legendę na wiki („Orszak z Drugiej Strony”). **Referencja kolorów:** model Upiornego Jeźdźca z gry.

### AI-09 · Wilk Alfa (0:55–0:58) · statyczna, potwór wyskakuje w kamerę
```
A dark forest at dusk; animals flee, lights flicker out. Out of the undergrowth leaps a massive alpha wolf,
twice the normal size, scarred, with glowing amber eyes and an unnatural aura, snarling at the camera.
Static camera, sudden motion. [STYLE]
```
Jeśli w grze łatwiej trafić na inne stworzenie Alfa (np. Golem), zmieńcie opis na nie.

### AI-10 · Legenda (1:02–1:07) · orbita, bohater się odwraca
```
Sunrise on a high cliff above the vast unexplored land of Eldoria: jagged mountains, misty valleys, a
walled city far away. [WARRIOR, END] stands at the edge, a glowing relic at the belt, cloak moving in
the wind, then turns toward the camera with a calm confident look. Beside them [MAGE], now older and
confident, and three companions of different races: a dwarf, a dark elf, a half-angel.
Slow orbit. Triumphant, warm. [STYLE, golden sunrise]
```
**Match cut z GP-12:** drużyna ustawiona tak samo jak gracze w grze.

### AI-11 · Dusze układają się w logo (1:12–1:16) · statyczna
```
Pure black void. Hundreds of small golden glowing souls drift in from all sides and gather in the
center of the frame into a horizontal band of light, leaving clean empty space. Static camera. [STYLE]
```
Napis **GENESIS** dokładamy w montażu. **Nie generujemy tekstu przez AI**, bo wychodzi krzywo.

---

## 4. Prompty do serii klipów

### „Bogowie Eldorii”: relikty (po jednym ujęciu na bóstwo)
Wspólny początek: `Extreme close-up of a sacred relic hanging at a belt in darkness, it begins to glow as golden souls flow into it, [RELIC], slow push-in. [STYLE]`

| Bóstwo | [RELIC] |
|---|---|
| Osirion | `a solid gold censer on an ornate chain releasing milky smoke with sparks of light` |
| Mortis | `a small obsidian skull with pale sparks flickering in its eye sockets` |
| Verdana | `a carved wooden tree-shaped amulet with tiny hand-carved leaves` |
| Arcanus | `a glass vial of shimmering living liquid that shifts colors and pulses` |
| Valoria | `a solid gold necklace set with small diamonds and a radiant divine symbol` |
| Bellum | `a raw dark-grey stone on a leather cord, cracked like battle scars, pulsing red within` |
| Lunara | `a gold chain with a silver crescent-moon pendant shimmering with cold light` |
| Umbra | `a dark eye-shaped gem whose pupil moves and watches` |
| Ateista | `a plain brass symbol on a simple chain, no ornaments, unlit, cold` |

Opisy reliktów pochodzą z wiki „System Wiary”.

### „Rasy Eldorii”: portrety (po jednym ujęciu na rasę)
Wspólny szablon: `Cinematic portrait of a [RACE] adventurer in Eldoria, [DETAIL], turning to face the camera, [STYLE]`

| Rasa | [DETAIL] |
|---|---|
| Człowiek | `versatile traveler, practical gear, city gate behind` |
| Elf | `graceful, longbow, ancient forest, leaves drifting` |
| Krasnolud | `stocky, braided beard, mining pick, glowing ore in a mountain tunnel` |
| Pół-Elf | `between two worlds, half in elven forest, half in human village` |
| Niziołek | `small, clever grin, squeezing through a narrow rock crevice toward hidden treasure` |
| Pół-Anioł | `faint luminous wings, calm, holy light` |
| Upadły Pół-Anioł | `blackened wings, cold eyes, ash falling` |
| Nieumarły | `gaunt, cold blue glow, skeleton servant rising beside` |
| Pół-Demon | `small horns, ember skin, fire mustang behind` |
| Jaszczuroczłowiek | `scaled reptilian humanoid in a misty swamp, claws, swamp creatures ignoring it` |
| Pół-Ork | `muscular, tusks, berserker rage, red eyes` |
| Mroczny Elf | `pale grey skin, white hair, underground cave with glowing fungi` |

---

## 5. Muzyka (Suno)

Na płatnym planie Suno utwory wygenerowane w czasie aktywnej subskrypcji można wykorzystywać komercyjnie (sprawdźcie aktualne warunki swojego planu). **Zapiszcie datę generowania i zrzut ekranu planu** na wypadek zgłoszenia Content ID na YouTube.

**Tryb:** Custom · **Instrumental: włączony**

**Style of Music:**
```
dark cinematic fantasy trailer, orchestral, epic, war drums, wordless choir, celtic strings,
ethereal bells, brooding, building intensity, 95 bpm
```

**Pole Lyrics (znaczniki struktury, bez słów):**
```
[Intro]
[low drone, single distant bell, breathing textures]

[Verse]
[gentle hopeful strings, soft flute, sea ambience]

[Build]
[tribal war drums enter, heavy hits on every beat]

[Pre-Chorus]
[wordless choir rises]

[Bridge]
[sudden tension, cold high strings, ghostly whispers, distant hoofbeats]

[Chorus]
[full orchestra and choir climax, massive]

[Outro]
[silence, one final deep orchestral hit, soft shimmering chime]

[End]
```

**Wskazówki:**
- Wygeneruj 6–10 wersji i wybierz tę, której **narastanie najlepiej pasuje do scenariusza**. Utwór nie musi mieć dokładnie 80 s, bo docinasz go w montażu (skracasz środek, zostawiasz intro i finał).
- Jeśli plan to umożliwia, pobierz **ścieżki osobno (stems)**, np. perkusję osobno. Łatwiej wtedy przyciszyć melodię pod lektora i zostawić bębny.
- **Osobne krótkie utwory** do klipów pionowych (15–30 s, mocny start od pierwszej sekundy):
  - „Rasy Eldorii”: `epic fantasy percussion, fast hybrid trailer drums, heroic brass stabs, 120 bpm, instrumental`
  - „Bogowie Eldorii”: `sacred dark ambient, choir pads, temple bells, mysterious, slow, instrumental`
  - „Orszak z Drugiej Strony”: `dark horror ambient, cold wind, ghostly choir, distant hoofbeats, dread, instrumental`
- Jeden **motyw przewodni Genesis** (krótka melodia) warto powtarzać we wszystkich materiałach. W Suno możesz przedłużać (Extend) albo przerabiać (Cover) wybrany utwór, żeby zachować motyw w różnych wersjach.

## 6. Lektor

Lektor AI. Tekst przygotowany pod syntezę mowy i ustawienia głosu są w [07-montaz-i-lektor.md](07-montaz-i-lektor.md).
