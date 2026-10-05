#!/usr/bin/env python3
"""Wstępny montaż trailera Genesis (wersja kinowa) z plików w material/.

Uruchomienie:  python3 montaz/build.py [katalog_wyjściowy]
Wymaga ffmpeg oraz czcionek Cinzel.ttf i Inter.ttf w katalogu FONTS (domyślnie obok wyjścia).
Brakujące nagrania z gry (GP-xx.mp4) zastępowane są planszami z opisem.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAT = os.path.join(ROOT, "material")
OUT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "montaz", "out"))
FONTS = os.environ.get("FONTS", OUT)
os.makedirs(OUT, exist_ok=True)

W, H, FPS = 1920, 1080, 24
XF = 0.5  # długość przenikania między ujęciami (s)
CINZEL = os.path.join(FONTS, "Cinzel.ttf")
INTER = os.path.join(FONTS, "Inter.ttf")
CREAM = "0xEDE3CC"

# (id, źródło, start w źródle, długość, opis planszy dla GP, napisy, lektor)
# napisy: (tekst, od, do, rozmiar, czcionka) w czasie segmentu
# lektor: (plik, od) w czasie segmentu
SEGMENTS = [
    ("AI-01", "AI-01.mp4", 0, 10, None, [], [("L01.wav", 2.0)]),
    ("AI-02", "AI-02.mp4", 0, 10, None, [], [("L02.wav", 1.0)]),
    ("GP-01", "GP-01.mp4", 0, 4, "Relikt Wiary w nocy: krąg światła wokół postaci",
     [("W ELDORII NOC JEST PRAWDZIWA", 0.5, 3.8, 64, "c")], []),
    ("AI-03a", "AI-03a.mp4", 0, 5.5, None, [], [("L03.wav", 2.0)]),
    ("AI-03b", "AI-03b.mp4", 2, 5.5, None, [], []),
    ("GP-02", "GP-02.mp4", 0, 5, "Przystań Orrena: nowe postacie, pomost, manekiny",
     [("BEZPIECZNY START · BEZ PvP · 168 H OCHRONY", 0.5, 4.8, 52, "c")], []),
    ("AI-04", "AI-04.mp4", 0, 10, None, [("PÓŁ-ANIOŁ", 4.0, 9.5, 96, "c")], [("L04.wav", 2.0)]),
    ("GP-03", "GP-03.mp4", 0, 3, "Model Pół-Anioła w grze", [], []),
    ("AI-05", "AI-05.mp4", 0, 10, None, [("PÓŁ-DEMON", 3.5, 9.5, 96, "c")], []),
    ("GP-04", "GP-04.mp4", 0, 3, "Pół-Demon przyzywa ognistego mustanga", [], []),
    ("AI-06", "AI-06.mp4", 0, 10, None, [("NIEUMARŁY", 3.5, 9.5, 96, "c")], []),
    ("GP-05", "GP-05.mp4", 0, 3, "Nieumarły przyzywa sługę", [], []),
    ("GP-06", "GP-06.mp4", 0, 4, "Seria ras: Mroczny Elf, Krasnolud, Jaszczuroczłowiek, Niziołek…",
     [("11 RAS · KAŻDA Z WŁASNYM WYGLĄDEM", 0.4, 3.8, 56, "c")], []),
    ("AI-07", "AI-07.mp4", 0, 10, None,
     [(n, 3.0 + i * 0.8, 3.0 + i * 0.8 + 0.75, 72, "c") for i, n in enumerate(
         ["OSIRION", "MORTIS", "VERDANA", "ARCANUS", "VALORIA", "BELLUM", "LUNARA", "UMBRA"])],
     [("L05.wav", 1.5)]),
    ("GP-07", "GP-07.mp4", 0, 5, "Ołtarz: składanie dusz, relikt rozbłyska", [], [("L06.wav", 0.5)]),
    ("AI-08", "AI-08.mp4", 0, 10, None, [("UPIORNI JEŹDŹCY", 5.5, 9.6, 84, "c")], [("L07.wav", 1.8)]),
    ("GP-08", "GP-08.mp4", 0, 4, "Upiorny Jeździec atakuje drużynę", [], []),
    ("BLACK", None, 0, 3, None,
     [("Czujesz, że coś potężnego zbliża się do tej okolicy...", 0.4, 2.9, 40, "i")], []),
    ("AI-09", "AI-09.mp4", 0, 8, None, [], []),
    ("GP-10", "GP-10.mp4", 0, 3, "Stworzenie [Alfa] w walce", [("STWORZENIA ALFA", 0.3, 2.8, 72, "c")], []),
    ("GP-11", "GP-11.mp4", 0, 5, "Kuźnia, osadzanie runy, loch oświetlony reliktami", [], [("L08.wav", 0.0)]),
    ("AI-10", "AI-10.mp4", 0, 10, None, [], [("L09a.wav", 4.3), ("L09b.wav", 7.6)]),
    ("GP-12", "GP-12.mp4", 0, 4, "Drużyna różnych ras pozuje, ukłon", [], [("L10.wav", 0.6)]),
    ("AI-12", "AI-12.mp4", 0, 10, None, [], []),
    ("GP-17", "GP-17.mp4", 0, 4, "Ognisty Portal: bitwa o wejście (sobota 20:00)",
     [("OGNISTY PORTAL · KAŻDA SOBOTA 20:00", 0.4, 3.8, 52, "c")], []),
    ("AI-11", "AI-11.mp4", 0, 10, None, [("GENESIS", 6.0, 10.0, 150, "c")],
     [("L11.wav", 1.0), ("L12.wav", 6.3)]),
    ("END", None, 0, 7, None, [], []),
]

END_LINES = [
    ("GENESIS", 120, -230, "c"),
    ("Darmowy serwer Ultima Online · Po polsku", 40, -70, "i"),
    ("uogenesis.pl", 64, 20, "c"),
    ("discord.gg/dhrwsxWyHf", 40, 110, "i"),
    ("Zacznij w Przystani Orrena", 38, 200, "i"),
    ("Ognisty Portal: soboty 20:00 · Deathmatch: nd, pn, śr 21:00", 34, 270, "i"),
]


def run(cmd):
    subprocess.run(cmd, check=True)


def textfile(name, text):
    p = os.path.join(OUT, "txt_" + name + ".txt")
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)
    return p


def fade_alpha(t0, t1, f=0.3):
    return (f"if(lt(t,{t0}),0,if(lt(t,{t0+f}),(t-{t0})/{f},"
            f"if(lt(t,{t1-f}),1,if(lt(t,{t1}),({t1}-t)/{f},0))))")


def drawtext(path, size, font, x, y, alpha, shadow=True, outline=False):
    fontfile = CINZEL if font == "c" else INTER
    s = (f"drawtext=fontfile='{fontfile}':textfile='{path}':fontsize={size}:fontcolor={CREAM}"
         f":x={x}:y={y}:alpha='{alpha}'")
    if shadow:
        s += ":shadowcolor=black@0.7:shadowx=3:shadowy=3"
    if outline:
        s += ":borderw=4:bordercolor=0x1a1208@0.85"
    return s


def build_segment(i, seg):
    sid, src, ss, dur, desc = seg[:5]
    out = os.path.join(OUT, f"seg_{i:02d}.mp4")
    norm = f"scale={W}:{H}:flags=lanczos,fps={FPS},format=yuv420p,setsar=1"
    srcpath = os.path.join(MAT, src) if src else None
    if srcpath and os.path.exists(srcpath):
        grade = "eq=saturation=0.92:contrast=1.04" if sid.startswith("AI") else "eq=contrast=1.05"
        # tpad: klipy Veo mają ~10 s, więc dociągamy ostatnią klatkę na czas przenikania
        vf = f"{norm},{grade},tpad=stop_mode=clone:stop_duration=1"
        run(["ffmpeg", "-v", "error", "-y", "-ss", str(ss), "-i", srcpath, "-t", str(dur + XF),
             "-an", "-vf", vf, "-c:v", "libx264", "-crf", "14", "-preset", "fast", out])
    else:
        filters = [norm]
        if desc:  # plansza zastępcza za nagranie z gry
            t1 = textfile(f"ph{i}a", f"[ NAGRANIE Z GRY ]  {sid}")
            t2 = textfile(f"ph{i}b", desc)
            t3 = textfile(f"ph{i}c", "do podmiany w Vegasie")
            filters += [drawtext(t1, 54, "c", "(w-text_w)/2", "h*0.30", "0.85", False),
                        drawtext(t2, 36, "i", "(w-text_w)/2", "h*0.30+90", "0.85", False),
                        drawtext(t3, 26, "i", "(w-text_w)/2", "h*0.30+150", "0.5", False)]
            color = "0x15181c"
        else:
            color = "black"
        if sid == "END":
            for k, (txt, size, dy, font) in enumerate(END_LINES):
                p = textfile(f"end{k}", txt)
                filters.append(drawtext(p, size, font, "(w-text_w)/2", f"h/2+({dy})",
                                        fade_alpha(0.3 + k * 0.25, dur + 1), True))
        run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i",
             f"color=c={color}:s={W}x{H}:r={FPS}:d={dur + XF}",
             "-vf", ",".join(filters), "-c:v", "libx264", "-crf", "14", "-preset", "fast", out])
    return out


def main():
    files, starts = [], []
    t = 0.0
    for i, seg in enumerate(SEGMENTS):
        files.append(build_segment(i, seg))
        starts.append(t)
        t += seg[3]
    total = t + XF

    # łączenie z przenikaniem
    inputs = []
    for f in files:
        inputs += ["-i", f]
    chain, prev = [], "[0:v]"
    for k in range(1, len(files)):
        lab = f"[x{k}]"
        chain.append(f"{prev}[{k}:v]xfade=transition=fade:duration={XF}:offset={starts[k]:.3f}{lab}")
        prev = lab

    # napisy w czasie globalnym
    texts = []
    n = 0
    for seg, st in zip(SEGMENTS, starts):
        for (txt, a, b, size, font) in seg[5]:
            p = textfile(f"t{n}", txt)
            n += 1
            # napisy w dolnej części kadru, żeby nie zasłaniać postaci; logo i czarne plansze na środku
            y = "(h-text_h)/2" if seg[0] in ("AI-11", "BLACK") else "h*0.80-text_h/2"
            texts.append(drawtext(p, size, font, "(w-text_w)/2", y, fade_alpha(st + a, st + b),
                                  outline=seg[0] == "AI-11"))
    # znacznik "Grafika z gry" na ujęciach z gry (prawdziwych, nie planszach)
    for seg, st in zip(SEGMENTS, starts):
        if seg[0].startswith("GP") and os.path.exists(os.path.join(MAT, seg[1])):
            p = textfile(f"gz{n}", "Grafika z gry")
            n += 1
            texts.append(drawtext(p, 28, "i", "w-text_w-40", "h-text_h-36",
                                  f"0.6*({fade_alpha(st, st + seg[3])})", False))
    vlast = prev
    if texts:
        chain.append(f"{prev}{','.join(texts)},noise=alls=3:allf=t[vout]")
        vlast = "[vout]"
    video = os.path.join(OUT, "video.mp4")
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(chain),
         "-map", vlast, "-c:v", "libx264", "-crf", "16", "-preset", "medium", video])

    # dźwięk: lektor (z pogłosem) + muzyka ściszana pod lektorem
    vo = [(os.path.join(MAT, f), st + off) for seg, st in zip(SEGMENTS, starts) for f, off in seg[6]]
    ain = ["-i", os.path.join(MAT, "muzyka.mp3")]
    for f, _ in vo:
        ain += ["-i", f]
    parts = []
    for k, (_, at) in enumerate(vo, start=1):
        ms = int(at * 1000)
        parts.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms}[v{k}]")
    labels = "".join(f"[v{k}]" for k in range(1, len(vo) + 1))
    fade_start = total - 6
    parts += [
        f"{labels}amix=inputs={len(vo)}:normalize=0,volume=1.6,"
        f"aecho=0.85:0.6:60|110:0.18|0.10,apad,atrim=0:{total:.3f},asplit=2[vo][sc]",
        f"[0:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{total:.3f},volume=0.55,"
        f"afade=t=out:st={fade_start:.3f}:d=6[mus]",
        "[mus][sc]sidechaincompress=threshold=0.03:ratio=8:attack=30:release=600[duck]",
        "[duck][vo]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[aout]",
    ]
    audio = os.path.join(OUT, "audio.wav")
    run(["ffmpeg", "-v", "error", "-y", *ain, "-filter_complex", ";".join(parts),
         "-map", "[aout]", "-ar", "48000", audio])

    final = os.path.join(OUT, "Genesis_trailer_robocza.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", video, "-i", audio, "-c:v", "copy",
         "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", final])
    print(f"Gotowe: {final}  ({total:.1f} s)")
    for seg, st in zip(SEGMENTS, starts):
        print(f"{int(st // 60)}:{st % 60:05.2f}  {seg[0]}")


if __name__ == "__main__":
    main()
