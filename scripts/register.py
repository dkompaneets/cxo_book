#!/usr/bin/env python3
"""Measure whether the four POV registers are audible against each other.

    scripts/register.py                    # all four POVs against target
    scripts/register.py 4 24               # named chapters only
    scripts/register.py --blind            # unattributed paragraphs, for the ear test

Narration only: dialogue is cut out before measuring, so a register that lives in
the quotes cannot flatter prose that hasn't got one.

The targets come from the reference/ files. They are a floor, not a style — a
chapter can hit every number and still be dead, and the only real test is --blind,
read by a person. What the numbers catch is the one failure that is invisible from
inside a chapter: two POVs converging on the house mean.
"""

import argparse
import collections
import os
import difflib
import random
import re
import subprocess
import statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "book")

POV = {
    "Kate":    [1, 14, 15, 16, 22],
    "Alex":    [2, 17, 24],
    "Michael": [3, 19, 25],
    "Nik":     [4, 7, 18, 23],
}

# (low, high). See the "exclusives" section of each reference file.
#
# A plain numeral count is useless here: the house spells numbers out in prose, so digits
# measure Kate's timestamps and miss Nik's arithmetic completely — which is how his register
# went unwritten through two drafts. The two counts that separate cleanly are the two that are
# actually somebody's property. `money` is Nik seeing prices. `clock` is Kate's bar line.
# `tail` — the share of narration words living in sentences of 40+ words — is the statistic that
# actually separates these four, and mean sentence length is the one that does not. A mean is
# what a drafting pass moves by feel, which is how Kate and Alex both arrived at 11.7. Alex is
# short on average *and* owns the longest sentence in the book: room tone by the line, eruption
# by the word. Judge him on the tail and leave his mean alone.
# Calibrated from ch1, ch2 and ch3 — the three chapters that have been read and passed. They are
# the model, and where an earlier invented target disagreed with them the target was wrong: Michael
# was set at a mean of 25+ on nothing but ambition, and ch3 does 18.2 and works. Nik has no approved
# chapter, so his row is interpolated between Alex and Michael. His currency floor is provisional:
# what separates him is ~5 per thousand against everyone else's ~0.5, and the exact cut is not
# meaningful at one decimal place. Reset it once a Nik chapter has been read and passed.
TARGET = {
    #                 mean sent     st.dev       tail40 %    semicolon/1k   money/1k     clock/1k
    "Kate":    {"mean": (8.5, 12), "sd": (7, 12),  "tail": (0, 12),  "semi": (0, 0.5), "money": (0, 1.5), "clock": (3, 12)},
    "Alex":    {"mean": (11, 15),  "sd": (13, 45), "tail": (20, 45), "semi": (0, 0.5), "money": (0, 1.5), "clock": (0, 1.5)},
    "Nik":     {"mean": (13, 17),  "sd": (12, 20), "tail": (12, 25), "semi": (0, 0.5), "money": (4, 14),  "clock": (0, 1.5)},
    "Michael": {"mean": (16, 22),  "sd": (16, 28), "tail": (33, 55), "semi": (10, 20), "money": (0, 1.5), "clock": (0, 3)},
}

# Currency only. "Per cent" belongs to any technical speaker; a price belongs to Nik.
MONEY = r"(£|\bpounds?\b|\bpence\b|\blakh\b|\bquid\b|\bbasis points?\b|\brupees?\b)"
# Kate writes 9:24. Alex was drafted writing "twelve forty-four", which is the same bar line
# in words, and the numeral-only pattern scored his chapter at 0.00 while it carried seven of
# them. Bare hours ("three in the morning") are duration and stay uncounted; hour-plus-minute
# is a dial reading and is hers.
_H = r"(?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)"
_M = (r"(?:oh[- ](?:one|two|three|four|five|six|seven|eight|nine)"
      r"|(?:twenty|thirty|forty|fifty)(?:[- ](?:one|two|three|four|five|six|seven|eight|nine))?"
      r"|fifteen|ten|five)")
CLOCK = (r"\b\d{1,2}[:.]\d{2}\b"
         rf"|\b{_H}[- ]{_M}\b"
         rf"|\b(?:quarter|half|five|ten|twenty|twenty[- ]five)[- ](?:past|to)[- ]{_H}\b"
         rf"|\b{_H}\s+o'clock\b")


def load(n):
    with open(os.path.join(BOOK, f"chapter-{n:02d}.md")) as f:
        text = f.read()
    text = re.sub(r"^# .*\n", "", text)
    # Blockquoted lines are rendered artefacts — a Slack thread, a pasted email. They are not the
    # POV's prose, and counting their timestamps as his clock is measuring the screenshot.
    text = re.sub(r"^>.*$", "", text, flags=re.M)
    return text.replace("---\n", "")


def narration(text):
    """Narration fragments, split at every quoted span.

    Deleting quotes outright would weld the sentence before a line of dialogue to the one
    after it — `said:` + `And Nik felt…` reads as a single 60-word sentence, which is how a
    chapter of short prose can be reported as having Michael's tail.
    """
    return [f for f in re.split(r'"[^"]*"', text) if f.strip()]


def sentences(text):
    text = re.sub(r"\*+", "", text)
    text = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def narration_sentences(text):
    return [s for frag in narration(text) for s in sentences(frag)]


def retained(n):
    """Share of the current chapter that is word-for-word what it was at HEAD.

    A chapter can pass every target while four fifths of it is untouched, because two inserted
    passages move the whole distribution. Conformance without this number means nothing.
    """
    try:
        old = subprocess.run(["git", "show", f"HEAD:book/chapter-{n:02d}.md"],
                             capture_output=True, text=True, cwd=ROOT, check=True).stdout.split()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    new = load(n).split()
    if not new:
        return None
    kept = sum(b.size for b in difflib.SequenceMatcher(None, old, new).get_matching_blocks())
    return round(kept / len(new) * 100, 1)


def measure(chapters):
    raw = "".join(load(n) for n in chapters)
    lens = [len(s.split()) for s in narration_sentences(raw)]
    words = sum(lens)
    # Narration only, like the sentence stats. Counting these in dialogue charges a POV for the
    # way other characters speak — Michael's semicolons inside a Kate chapter are his voice
    # rendered correctly, and reading them as her drift would delete the contrast on purpose.
    prose = " ".join(narration(raw))
    per_k = lambda pat: len(re.findall(pat, prose, re.I)) / max(words, 1) * 1000
    return {
        "words": words,
        "mean": round(statistics.mean(lens), 1),
        "sd": round(statistics.pstdev(lens), 1),
        "tail": round(sum(l for l in lens if l >= 40) / max(words, 1) * 100, 1),
        "longest": max(lens),
        "frag": round(sum(l <= 4 for l in lens) / len(lens) * 100, 1),
        "semi": round(per_k(r";"), 2),
        "money": round(per_k(MONEY), 2),
        "clock": round(per_k(CLOCK), 2),
    }


LABEL = {"mean": "mean sentence", "sd": "st. dev", "tail": "words in 40w+ %", "longest": "longest sentence", "frag": "fragments %",
         "semi": "semicolons /1k", "money": "money /1k", "clock": "timestamps /1k"}
STATS = ("mean", "sd", "tail", "longest", "frag", "semi", "money", "clock")


def verdict(pov, stat, value):
    bounds = TARGET[pov].get(stat)
    if bounds is None:
        return " "
    lo, hi = bounds
    return "ok" if lo <= value <= hi else ("lo" if value < lo else "hi")


def report(chapters=None):
    if chapters:
        for n in sorted(chapters):
            owner = next((p for p, cs in POV.items() if n in cs), None)
            m = measure([n])
            head = f"ch{n:02d}" + (f"  {owner}" if owner else "  (ensemble)")
            keep = retained(n)
            kept = f" | {keep}% unchanged from HEAD" if keep is not None else ""
            print(f"\n{head}   {m['words']} narration words{kept}")
            for k in STATS:
                mark = verdict(owner, k, m[k]) if owner else " "
                want = TARGET[owner][k] if owner and k in TARGET[owner] else ""
                want = f"want {want[0]}–{want[1]}" if want else ""
                print(f"    {LABEL[k]:<16} {m[k]:>7}   {mark:<3} {want}")
        return

    rows = {p: measure(cs) for p, cs in POV.items()}
    width = max(len(v) for v in LABEL.values()) + 2
    print(f"{'':{width}}" + "".join(f"{p:>16}" for p in rows))
    for k in STATS:
        line = f"{LABEL[k]:{width}}"
        for p in rows:
            line += f"{rows[p][k]:>12}{verdict(p, k, rows[p][k]):>4}"
        print(line)

    print("\nconvergence — the pair that must never be closest:")
    pairs = []
    for a in rows:
        for b in rows:
            if a < b:
                d = abs(rows[a]["mean"] - rows[b]["mean"]) + abs(rows[a]["sd"] - rows[b]["sd"])
                pairs.append((d, a, b))
    for d, a, b in sorted(pairs):
        print(f"    {a:<8} / {b:<8} distance {d:5.1f}")



# Every proper noun that would give the answer away. Without this the test measures whether you
# can read a name, not whether the prose has a voice.
NAMES = r"""Kate|Merrick|Katherine|Aleksander|Alex|Alek|Wójcik|Wojcik|Michael|Halloway|
Nikhil|Nik|Raghavan|Ben|Farrow|Meera|Anaya|Rohan|Shobha|Marek|Ewa|Dawn|Fowler|Ruth|Claire|
Danny|Iris|Sam|Gus|Delaney|Wilf|Tanner|Harriet|Nash|Tom|Ferreira|Gareth|Pryce|Priyesh|Bridget|
Fiona|Redgrave|Terry|Nwosu|Callum|Deitch|Saul|Fenella|Velum|Bellwether|Lauriston|Lodestone|
Sunward|Marrowbone|Arcus|Meridian|Ardenne|Bea|Sasha|Sofia|Colin|Denny|Vasyl|Otis|Priyanka"""
NAMES = re.compile(r"\b(" + NAMES.replace("\n", "") + r")('s)?\b")


def blind(seed=0, per_chapter=2):
    """Print unattributed paragraphs. Read them and name the POV before checking the key."""
    rng = random.Random(seed)
    picked = []
    for pov, chs in POV.items():
        for n in chs:
            paras = [p.strip() for p in load(n).split("\n\n")
                     if len(p.split()) > 45 and not p.strip().startswith('"')]
            for p in rng.sample(paras, min(per_chapter, len(paras))):
                picked.append((pov, n, NAMES.sub("—", re.sub(r"\s+", " ", p))))
    rng.shuffle(picked)
    for i, (_, _, para) in enumerate(picked, 1):
        print(f"\n[{i}]  {para}\n")
    print("\n--- key ---")
    print(", ".join(f"{i}:{pov} ch{n}" for i, (pov, n, _) in enumerate(picked, 1)))


# Section-level ownership for the ensemble chapters. Every POV section is that character's prose,
# so it is measured against that character's target — the house has no voice of its own. `None`
# marks the few sections that belong to the hotel rather than to a person.
SECTIONS = {
    5:  [None, "Kate", "Alex", "Michael", "Nik", None],
    6:  [None, "Nik", "Kate", "Alex", "Michael", None],
    8:  ["Kate", "Kate", "Kate", "Kate"],
    9:  ["Alex", "Alex", "Alex", "Alex", "Alex"],
    10: ["Kate", "Kate", "Kate", "Kate", "Kate"],
    11: ["Kate", "Kate", "Alex", "Kate", "Kate", "Nik", "Michael", "Kate"],
    12: ["Michael", "Alex", "Michael", "Alex", "Alex", "Michael", "Alex"],
    13: ["Alex", "Alex", "Nik", "Alex", "Alex", "Alex"],
    20: ["Nik", "Kate", "Alex", "Nik", "Michael", "Nik"],
    21: ["Michael", "Kate", "Nik", "Nik", "Alex", None, "Nik"],
    26: [None, "Kate", "Nik", "Alex", None, "Kate"],
    27: ["Nik", "Nik", "Kate", "Alex", "Alex", "Kate"],
}


def sections(n):
    """(owner, text) for each --- separated section of an ensemble chapter."""
    with open(os.path.join(BOOK, f"chapter-{n:02d}.md")) as f:
        body = re.sub(r"^# .*\n", "", f.read())
    body = re.sub(r"^>.*$", "", body, flags=re.M)
    parts = [p.strip() for p in re.split(r"\n---\n", body) if p.strip()]
    owners = SECTIONS.get(n, [])
    return list(zip(owners + [None] * (len(parts) - len(owners)), parts))


def measure_text(text):
    lens = [len(s.split()) for s in narration_sentences(text)] or [0]
    words = max(sum(lens), 1)
    prose = " ".join(narration(text))
    per_k = lambda pat: len(re.findall(pat, prose, re.I)) / words * 1000
    return {"words": words, "mean": round(statistics.mean(lens), 1),
            "sd": round(statistics.pstdev(lens), 1),
            "tail": round(sum(l for l in lens if l >= 40) / words * 100, 1),
            "semi": round(per_k(r";"), 2), "money": round(per_k(MONEY), 2),
            "clock": round(per_k(CLOCK), 2)}


# Phrases that mark machine-written prose, plus the three narrator tics CLAUDE.md says were
# stripped once already and which creep back on every pass. Rates are per 10,000 words.
TELLS = {
    # Narration only: interrupted *speech* is deliberate here, so dialogue dashes are not a tell.
    "em-dash (narration)":        (r"—", 30),
    "genuinely/entirely/completely": (r"\b(?:genuinely|entirely|completely)\b", 5),
    "polysyndeton (and X, and Y, and Z)": (r"\band [^.,;]{2,30}, and [^.,;]{2,30}, and ", 1.5),
    "specific/particular/precise": (r"\b(?:specific|particular|precise)\b", 1.5),
    "the way you/they <verb>":    (r"the way (?:you|they|people|one) \w+", 2),
    ", which was …":              (r", which was (?:the |a |an )?[a-z]+[,.]", 1),
    "exactly the/what/how":       (r"\bexactly (?:the|what|how|why)\b", 2),
    "a small/little <noun>":      (r"\ba (?:small|tiny|little) [a-z]+\b", 2),
    "of a man/woman who":         (r"of a (?:man|woman|person|girl|boy)\b", 1.5),
    "that was the thing":         (r"[Tt]hat was the (?:thing|part|point)\b", 1),
    "nothing at all":             (r"\bnothing at all\b", 0.7),
    "sat/stood/went very still":  (r"(?:sat|stood|went) very still\b", 0.4),
}


def tells(chapters=None):
    chapters = chapters or range(1, 28)
    texts = {n: " ".join(narration(load(n))) for n in chapters}
    total = " ".join(texts.values())
    words = len(total.split())
    print(f"{'':38}{'count':>7}{'/10k':>8}{'budget':>8}   worst chapters")
    for name, (pat, budget) in TELLS.items():
        n = len(re.findall(pat, total))
        rate = n / words * 10000
        worst = sorted(((len(re.findall(pat, t)) / max(len(t.split()), 1) * 10000, c)
                        for c, t in texts.items()), reverse=True)[:3]
        worst = " ".join(f"ch{c:02d}({r:.0f})" for r, c in worst if r > budget)
        flag = "  " if rate <= budget else "!!"
        print(f"{flag}{name:36}{n:>7}{rate:>8.1f}{budget:>8}   {worst}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("chapters", nargs="*", type=int)
    ap.add_argument("--blind", action="store_true")
    ap.add_argument("--tells", action="store_true")
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    if a.tells:
        tells(a.chapters or None)
    elif a.blind:
        blind(a.seed)
    else:
        report(a.chapters)
