#!/usr/bin/env python3
"""Narrate a markdown file with Kokoro TTS (voice: af_heart).

Usage:
    .venv-kokoro/bin/python scripts/tts.py research/outline2.md
    .venv-kokoro/bin/python scripts/tts.py research/outline2.md audio/outline2.mp3

Writes an mp3 (via ffmpeg) and cleans up the intermediate wav.
"""
import os
import re
import subprocess
import sys
import tempfile

import numpy as np
import soundfile as sf
from kokoro import KPipeline

VOICE = "af_heart"          # Kokoro's top-graded (A) narrator voice
LANG = "a"                  # American English
SR = 24000
GAP_SEC = 0.35              # silence between segments
SCENE_GAP_SEC = 1.2         # silence at a scene break (--- in the markdown)
BREAK = "\x00SCENEBREAK\x00"

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}


def num_to_words(n):
    if n < 20:
        return ONES[n]
    if n < 100:
        tens, ones = divmod(n, 10)
        return TENS[tens] + ("-" + ONES[ones] if ones else "")
    return str(n)


def filename_to_words(name):
    """research/outline1.md -> 'outline one'; analysis_format_genre.md -> 'analysis format genre'."""
    stem = os.path.splitext(os.path.basename(name))[0]
    stem = stem.replace("_", " ").replace("-", " ")
    return re.sub(r"([a-zA-Z]) ?(\d+)",
                  lambda m: f"{m.group(1)} {num_to_words(int(m.group(2)))}", stem)


def build_text(md, title):
    out = []
    for ln in md.splitlines():
        s = ln.strip()
        if not s:
            continue
        if s == "---":                                      # scene break / rule
            out.append(BREAK)
            continue
        m = re.match(r"^#{1,6}\s*(\d+)\.\s*(.+)$", s)       # chapter heading
        if m:
            out.append(f"Chapter {num_to_words(int(m.group(1)))}. {m.group(2).strip()}.")
            continue
        if s.startswith("# "):                              # top title
            out.append(f"{title}.")
            continue
        m = re.match(r"^#{2,6}\s*(.+)$", s)                 # other heading
        if m:
            out.append(m.group(1).strip().strip("*") + ".")
            continue
        if re.match(r"^\d+\s+chapters", s):                 # skip the page-count meta line
            continue
        s = re.sub(r"^[-*]\s+", "", s)                      # bullet
        s = re.sub(r"^\d+\.\s+", "", s)                     # numbered list item
        out.append(s)

    text = "\n\n".join(out)

    # chapter refs, before the dash rewrite eats the ranges
    text = re.sub(r"\bch (\d+)\s*[–—-]\s*(\d+)",
                  lambda m: f"chapters {num_to_words(int(m.group(1)))} to {num_to_words(int(m.group(2)))}",
                  text)
    text = re.sub(r"\bch (\d+)", lambda m: f"chapter {num_to_words(int(m.group(1)))}", text)

    # markdown / punctuation cleanup for natural narration
    text = re.sub(r"`([^`]+\.md)`", lambda m: filename_to_words(m.group(1)), text)
    text = text.replace("`", "").replace("*", "").replace("~", "")
    text = text.replace("≈", "about ")
    text = text.replace(" / ", " and ")
    text = text.replace("—", ", ").replace("–", ", ")
    text = re.sub(r"\s+,", ",", text)
    text = re.sub(r",\s*,", ",", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    stem = os.path.splitext(os.path.basename(src))[0]
    out_mp3 = sys.argv[2] if len(sys.argv) > 2 else f"audio/{stem}.mp3"
    title = filename_to_words(src).title()

    with open(src, encoding="utf-8") as f:
        text = build_text(f.read(), title)
    print(f"[prepared {len(text)} chars from {src}]\n")
    print(text[:600] + "\n...\n")

    pipeline = KPipeline(lang_code=LANG)
    gap = np.zeros(int(SR * GAP_SEC), dtype=np.float32)
    scene_gap = np.zeros(int(SR * SCENE_GAP_SEC), dtype=np.float32)
    chunks = []
    i = 0
    scenes = [p.strip() for p in text.split(BREAK)]
    for n, scene in enumerate(scenes):
        if not scene:
            continue
        if n:
            chunks.append(scene_gap)
        for gs, ps, audio in pipeline(scene, voice=VOICE, split_pattern=r"\n+"):
            a = audio.detach().cpu().numpy() if hasattr(audio, "detach") else np.asarray(audio)
            chunks.append(a.astype(np.float32))
            chunks.append(gap)
            print(f"  seg {i:>3}: {gs[:60]!r}")
            sys.stdout.flush()
            i += 1

    full = np.concatenate(chunks)
    os.makedirs(os.path.dirname(out_mp3) or ".", exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        wav = tmp.name
    try:
        sf.write(wav, full, SR)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav,
                        "-codec:a", "libmp3lame", "-qscale:a", "3", out_mp3], check=True)
    finally:
        os.unlink(wav)

    dur = len(full) / SR
    print(f"\n[wrote {out_mp3}  {dur/60:.1f} min]")


if __name__ == "__main__":
    main()
