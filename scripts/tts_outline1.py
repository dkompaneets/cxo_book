#!/usr/bin/env python3
"""Narrate research/outline1.md with Kokoro TTS (voice: af_heart)."""
import re
import sys
import numpy as np
import soundfile as sf
from kokoro import KPipeline

SRC = "research/outline1.md"
OUT_WAV = "audio/outline1.wav"
VOICE = "af_heart"          # Kokoro's top-graded (A) narrator voice
LANG = "a"                  # American English
SR = 24000

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
TENS = {30: "thirty"}

def num_to_words(n):
    if n <= 20:
        return ONES[n]
    if n < 30:
        return "twenty-" + ONES[n - 20]
    return str(n)

def build_text(md):
    lines = md.splitlines()
    out = []
    for ln in lines:
        s = ln.strip()
        if not s:
            continue
        if s.startswith("# "):                       # top title
            out.append("Outline one.")
            continue
        m = re.match(r"^#{2,6}\s*(\d+)\.\s*(.+)$", s)  # chapter heading
        if m:
            n = int(m.group(1))
            title = m.group(2).strip()
            out.append(f"Chapter {num_to_words(n)}. {title}.")
            continue
        if s.startswith("#"):
            continue
        if re.match(r"^\d+\s+chapters", s):            # skip meta line
            continue
        out.append(s)
    text = "\n\n".join(out)
    # markdown / punctuation cleanup for natural narration
    text = text.replace("*", "")
    text = text.replace("—", ", ").replace("–", ", ")
    text = re.sub(r"\s+,", ",", text)
    text = re.sub(r",\s*,", ",", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text

def main():
    with open(SRC, encoding="utf-8") as f:
        md = f.read()
    text = build_text(md)
    print(f"[prepared {len(text)} chars]\n")
    print(text[:600] + "\n...\n")

    pipeline = KPipeline(lang_code=LANG)
    gap = np.zeros(int(SR * 0.35), dtype=np.float32)
    chunks = []
    for i, (gs, ps, audio) in enumerate(pipeline(text, voice=VOICE, split_pattern=r"\n+")):
        a = audio.detach().cpu().numpy() if hasattr(audio, "detach") else np.asarray(audio)
        chunks.append(a.astype(np.float32))
        chunks.append(gap)
        print(f"  seg {i:>3}: {gs[:60]!r}")
        sys.stdout.flush()

    full = np.concatenate(chunks)
    import os
    os.makedirs("audio", exist_ok=True)
    sf.write(OUT_WAV, full, SR)
    dur = len(full) / SR
    print(f"\n[wrote {OUT_WAV}  {dur/60:.1f} min]")

if __name__ == "__main__":
    main()
