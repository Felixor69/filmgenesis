# Prompty AI wideo i biblia stylu

Prompty są **po angielsku**, bo generatory (Veo, Kling, Runway, Sora, Hailuo, Luma) dają wtedy najlepsze wyniki. Opisy i uwagi są po polsku.

## 1. Workflow (dla spójności ujęć)

Największe ryzyko AI wideo to 13 ujęć, które wyglądają jak z 13 różnych filmów, i bohater, który w każdym ma inną twarz. Dlatego:

1. **Najpierw obrazy, potem ruch (image-to-video).** Każde ujęcie zaczynamy od klatki kluczowej wygenerowanej modelem obrazu (Midjourney, Flux, Imagen, GPT-image itp.). Wybieramy najlepszą i dopiero ją animujemy w generatorze wideo. Mamy wtedy kontrolę nad kompozycją, a match cuty z gameplayem da się ustawić co do kadru.
2. **Arkusz postaci bohatera.** Generujemy jedną postać (patrz „Bohater” niżej) w 3–4 ujęciach: przód, profil, pełna postać, zbroja końcowa. Używamy jej jako referencji (character reference / reference image) we wszystkich ujęciach z bohaterem: AI-03, AI-12, AI-13.
3. **Kompozycja pod match cut.** Przed generowaniem klatki robimy screenshot odpowiadającego ujęcia z gry (GP-xx) i dajemy go jako referencję kompozycji lub układamy klatkę AI tak, żeby postać była w tym samym miejscu kadru i patrzyła w tę samą stronę.
4. **Każde ujęcie w 3–6 wariantach**, wybieramy najlepsze. Długość 4–8 s, potem przycinamy w montażu.
5. **Grading na końcu.** W montażu nakładamy jeden LUT / korekcję na wszystkie ujęcia AI **i** lekko na gameplay, żeby się „kleiły”.

## 2. Biblia stylu Genesis

Doklejamy do każdego promptu (skrócona wersja w nawiasie, jeśli generator ma limit znaków):

```
STYLE: dark high-fantasy, painterly cinematic realism, medieval world of old gods and runes,
warm gold rune-light against deep teal-blue night shadows, volumetric light, drifting embers and dust,
anamorphic lens, shallow depth of field, subtle film grain, 24fps cinematic motion, epic but grounded,
no modern elements, no text, no logos
(short: dark high-fantasy, cinematic, gold rune-light vs teal shadows, volumetric, film grain, no text)
```

**Paleta:**
- Złoto run / światło dusz: `#E8B04A`
- Głęboki turkus nocy: `#0F2A33`
- Ciepłe ognie / kuźnia: `#D2542B`
- Kość / pergamin (tekst na ekranie): `#EDE3CC`

**Motywy przewodnie:** runy świecące złotem (bogowie), świecące dusze jak świetliki (dusze), otwarte krajobrazy (wolność).

**Negative prompt / unikać:**
```
text, watermark, logo, modern clothing, guns, sci-fi, anime style, cartoon, plastic skin,
extra fingers, deformed hands, morphing faces, blurry, low quality, Ultima Online logo
```

### Bohater (referencja dla AI-03, AI-12, AI-13)

```
Young adult adventurer, androgynous-leaning features, short dark messy hair, determined grey eyes,
small scar on left cheek, weathered skin.
START LOOK: plain undyed linen tunic, rope belt, barefoot, no weapon.
END LOOK: dark leather and steel armor with gold rune engravings on the pauldron, deep teal cloak, longsword on back.
```

---

## 3. Prompty ujęć

Format: **ID · czas w filmie · ruch kamery · prompt**. Wszystkie w 16:9. Wersje pionowe: dopisać `vertical 9:16 composition, subject centered`.

### AI-01 · Runy (0:00–0:04) · powolny najazd (slow push-in)
```
Total darkness, an ancient weathered standing stone monolith in a misty clearing at night.
One by one, carved runes on its surface ignite with glowing molten gold light, the light spreading
like veins across the stone. Tiny golden embers drift upward. Slow cinematic push-in toward the stone.
[STYLE]
```

### AI-02 · Dusze (0:04–0:08) · statyczna, lekki dryf
```
A black primeval forest at night, hundreds of small glowing golden souls float between the trees like
fireflies, slowly swirling together and gathering into the luminous silhouette of a human figure standing
in the center. Ethereal, sacred, quiet. Static camera with gentle drift. [STYLE]
```

### AI-03 · Przebudzenie (0:08–0:11) · kamera nisko, bohater wstaje
```
Dawn on a lonely grey beach, soft fog. [HERO, START LOOK] lies on wet sand, wakes up, slowly rises to
their feet and looks toward distant misty hills, the camera low behind their shoulder. Nothing in their
hands. Sense of beginning, vulnerability and freedom. [STYLE]
```
**Match cut:** kierunek patrzenia i pozycja w kadrze jak w GP-01 (postać w centrum, zwrócona w stronę, w którą w grze pójdzie).

### AI-04 · Kowal (0:14–0:16) · zbliżenie, iskry w zwolnionym tempie
```
Close-up of a blacksmith's hammer striking a glowing orange blade on an anvil, sparks exploding in slow
motion, sweat and soot on muscular forearms, dark forge lit by the fire. Rhythmic, powerful. [STYLE]
```

### AI-05 · Mag (0:18–0:20) · orbita wokół postaci
```
A robed mage in a stone tower raises one hand, a glowing golden rune circle forms in the air in front of
the palm, then a crackling bolt of blue-white lightning erupts forward. Wind moves the robes.
Camera slowly orbits. [STYLE]
```

### AI-06 · Łowca (0:22–0:24) · profil, płytka głębia
```
A hunter in a green-grey hooded cloak in a misty pine forest at dawn, drawing a longbow, arrow nocked,
eye focused, breath visible in the cold air, shallow depth of field, a deer silhouette far in the fog.
Side profile. [STYLE]
```

### AI-07 · Złodziej (0:26–0:28) · kamera podąża za postacią
```
Night, narrow medieval alley lit by a single lantern. A hooded figure slips a stolen coin purse into
their cloak, glances back at the camera with a sly half-smile, and dissolves into the shadows.
Camera follows from behind, then stops. [STYLE]
```

### AI-08 · Nowy ląd (0:34–0:36) · przelot drona
```
Epic aerial drone flight over an unexplored fantasy continent at golden hour: jagged mountains, winding
rivers, dense forests, a walled stone city with tall towers in the distance, flocks of birds.
Fast forward flyover, sweeping and majestic. [STYLE]
```

### AI-09 · Potwór (0:38–0:40) · statyczna, potwór wychodzi z cienia
```
Inside a dark cave, glowing eyes appear in the blackness, then a massive horned reptilian beast steps out
into torchlight and roars toward the camera, dust and debris shaking from the ceiling. Terrifying,
huge scale. [STYLE]
```
**Uwaga:** jeśli w Genesis jest konkretny nowy potwór z charakterystycznym wyglądem, opiszcie go tutaj zamiast „horned reptilian beast”. Match cut z GP-08 będzie wtedy znacznie mocniejszy. `[DO UZUPEŁNIENIA: opis potwora]`

### AI-10 · Szarża armii (0:48–0:52) · szeroki kadr, kamera nisko
```
Two medieval fantasy armies charge at each other across a wide grassy plain under a stormy sky, banners
of gold and teal whipping in the wind, mages casting fire from the back lines, dust and thunder.
Wide shot, low camera, epic scale. [STYLE]
```

### AI-11 · Smok (0:56–0:58) · wolny odjazd w górę
```
A colossal dragon flies over a burning stone fortress at night, its wings blotting out the moon, fire
reflecting on its scales. At the foot of the walls a small party of five adventurers raises weapons and
shields. Slow upward tilt. [STYLE]
```

### AI-12 · Legenda (1:00–1:03) · orbita, bohater odwraca się
```
Sunset on a high cliff edge overlooking a vast fantasy valley. [HERO, END LOOK] stands at the edge,
cloak moving in the wind, then turns toward the camera with a calm confident look. Behind them a small
party of companions: a mage, a knight, an archer. Slow orbit. Triumphant, warm. [STYLE]
```
**Match cut:** drużyna ustawiona tak jak gracze w GP-14.

### AI-13 · Tło logo (1:05–1:10) · statyczna
```
The ancient rune stone from the opening, now in daylight mist, its runes glowing gold; golden light
particles rise from it and swirl in the empty upper center of the frame, leaving clean negative space
for a title. Static camera. [STYLE]
```
Logo GENESIS dokładamy w montażu (DaVinci / After Effects / CapCut). **Nie generujemy tekstu AI**, bo wychodzi krzywo.

---

## 4. Muzyka (jeśli generujecie AI, np. Suno/Udio z licencją komercyjną)

```
Epic cinematic fantasy trailer score, 95 BPM, 75 seconds. Starts with a low drone, a single bell and
whispered choir; at 0:14 tribal war drums and rhythmic celtic strings enter; builds with brass and
full choir to a massive climax at 0:48; sudden silence at 1:05 followed by one final orchestral hit
and a soft rune-like chime. No vocals with lyrics.
```
Zapiszcie i archiwizujcie dowód licencji (plan subskrypcji, data generowania). YouTube Content ID czasem się czepia.

## 5. Lektor AI (opcjonalnie)

Jeśli nie macie lektora: ElevenLabs i podobne robią dobry polski głos. Kierunek: **niski męski lub żeński głos, spokojny, lekko szepczący na początku, pewny na końcu**, jak narrator legendy, a nie spiker reklamy. Najlepiej jednak nagrać kogoś ze społeczności. To też świetny materiał do posta („głos trailera to nasz gracz X”).
