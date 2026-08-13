# CLAUDE.md

Working notes for the CXO novel ("The Vise").

## Layout

- `research/` — outlines, spine, character architecture, genre analysis. The working material.
  `research/canon.md` fixes the names/places/continuity the draft follows.
- `reference/` — one file per POV character: voice register, authors, prosody. Read the
  relevant file before writing or editing that character's chapters. See the style section.
- `book/` — the draft itself: one file per chapter, `chapter-01.md` … `chapter-27.md`.
  A chapter file holds the chapter and nothing else (see below). **27 chapters, not the
  outline's 32** — see the structure section of [research/canon.md](research/canon.md) for
  which outline chapters were merged and why. Don't "restore" the missing five.
- `audio/` — narrated mp3s of the research docs. `audio/book/` — narrated chapters.
- `scripts/` — tooling.
- `covers/` — cover concepts.
- `todo.md` — running list.

## Chapter conventions

A chapter file is prose and nothing else: a `# N. Title` heading, then the chapter, with
scene breaks marked by `---` on their own line. Nothing before the heading, nothing after
the last line — same discipline as the outline files. `research/canon.md` is the source of
truth for names, places, dates, and the rules the prose keeps (e.g. Michael's deep breath
is never explained, and he alone is never given a vantage on himself).

## Creating audio files

Research docs get narrated so they can be reviewed by ear. Kokoro TTS runs locally in
`.venv-kokoro` — no API, no network.

```sh
.venv-kokoro/bin/python scripts/tts.py research/outline2.md
```

Writes `audio/outline2.mp3` (output path derived from the input filename). Pass a second
argument to override it. Roughly 1 minute of audio per 1,000 characters; a 32-chapter
outline runs ~25 minutes and takes a few minutes to generate.

**Narrating the whole book** — [scripts/narrate_book.sh](scripts/narrate_book.sh) runs
`tts.py` over every `book/chapter-*.md` into `audio/book/`. It skips any chapter whose mp3
is newer than its markdown, so it's safe to re-run after editing a chapter — only the
changed ones regenerate. Pass file paths to narrate a subset.

```sh
scripts/narrate_book.sh                 # all chapters (skips up-to-date ones)
scripts/narrate_book.sh book/chapter-05.md
```

**How it works** — [scripts/tts.py](scripts/tts.py) converts markdown to narration text,
synthesises with Kokoro (`af_heart`, American English, 24 kHz), then pipes through ffmpeg
to mp3 and deletes the intermediate wav. It handles both the outlines and the prose
chapters: `# N. Title` → *"Chapter N. Title."*, and a `---` scene break becomes a longer
pause in the narration.

The markdown→speech conversion handles:

- `### 7. Why We Do This` → *"Chapter seven. Why We Do This."*
- `ch 5–8` → *"chapters five to eight"*; `ch 17` → *"chapter seventeen"*
- Backticked filenames → spoken names (`analysis_format_genre.md` → *"analysis format genre"*)
- Strips `**bold**`, `---` rules, and the `NN chapters, ~N pages` meta line
- Em dashes → commas, so the narrator pauses instead of running sentences together

If a new doc has markup the converter mangles, extend `build_text()` rather than editing
the source markdown — the markdown is the artifact, the audio is a rendering of it.

**Requirements:** `.venv-kokoro` (already set up), plus `ffmpeg` and `lame` on PATH
(`brew install ffmpeg lame`). First run downloads the Kokoro model to the HF cache.

`scripts/tts_outline1.py` is the original single-purpose version, kept for reference.
Use `scripts/tts.py` for anything new.

## Outline conventions

**An outline file contains the outline and nothing else.** Match the shape of
[research/outline1.md](research/outline1.md): a title, a one-line page count, then
`### N. Title` followed by one dense paragraph per chapter. Nothing before the first
chapter, nothing after the last.

- **No Parts or Acts.** The structural rhythm lives inside the chapters, not in headers above them.
- **No commentary.** No "what changed and why", no notes blocks, no open questions, no
  rationale for the structure, no asides pointing at the machinery ("this is the fuse").
  If that thinking is worth keeping, it goes in chat or a separate file — never in the outline.

## Tone

Research-backed fiction, tragicomic. The target reader is a real CXO with a fine nose for
falseness. Credibility comes from precise detail and the absence of moralising; it is
destroyed by sentimentality and tidy endings. See
[research/analysis_format_genre.md](research/analysis_format_genre.md).

## Style — decided

**Four registers, one restraint. Strout at every peak. No contempt anywhere.**

This replaces the earlier single-register brief (Herron for the whole house). One narrator
voice across four POVs is what made the first draft read as background music: the four leads
were statistically indistinguishable in sentence length, sentence openers and dialogue.
Herron is now Nik's property, not the house's. Not Moriarty, not Backman, not Nicholls —
those were structural comps, never voice.

### The house floor — what all four share

- Close third, past tense, free indirect. One POV per chapter unless it is an ensemble chapter.
- **Strout at the peaks.** All four collapse toward plain declarative at their worst moment,
  and each loses something different: Michael his subordination, Kate her clock, Nik his
  jokes, Alex his flow. Four different silences. This is the only thing they share, which is
  what makes it mean something.
- **No contempt.** The comedy comes from what a character believes about themselves, never
  from the narrator knowing better. Matters most for Nik and Marek, where a sardonic narrator
  curdles into caricature immediately.
- British idiom throughout — except Alex, deliberately (see below).

### The four registers

One file each, in [reference/](reference/). **Read the character's file before writing or
editing any of their chapters.** Each carries the music, the authors and what to steal from
them, the prosody rules, what that character loses at the peak, their chapter list, and the
failure mode specific to them.

| POV | Register | |
|---|---|---|
| Michael Halloway | Classical — Ishiguro, Bennett, Trevor | [reference/michael.md](reference/michael.md) |
| Kate Merrick | Ostinato, the Soviet news intro — Mantel, Offill, Levy | [reference/kate.md](reference/kate.md) |
| Nikhil Raghavan | Comic patter — Herron, Heller, Coe | [reference/nik.md](reference/nik.md) |
| Aleksander Wójcik | Norwegian rock — Motorpsycho, Petterson, Knausgård, Baker | [reference/alex.md](reference/alex.md) |

The registers are only worth having if they are audible against each other. When two of them
share a scene, the contrast is the point — and the ensemble chapters are where all four meet.

### Rules

- **The narrator has no tics of its own.** Three were stripped: spelled-out numbers, the
  `, which was` appositive, and the polysyndetic close (*and X, and Y, and Z*). Reissue them
  unevenly, as character property — counting belongs to Nik and to Kate's clock, never to
  Alex or Michael.
- Comedy from institutional specificity, never from a character being stupid.
- **One aphorism per scene, maximum.** They are the book's best asset and they cheapen fast.
- **Emotion gets less language, not more.** At the peak, shorten.
- **No sentence that explains what the scene just did.** If a paragraph tells the reader how
  to feel about the preceding paragraph, cut it. Every score gain in revision came from this.
- Jokes must cost the joker something — and **some must fail.** A comedy about status in which
  every joke lands has no social risk in it.
- Dysfluency, distraction and collapse are **enacted in the syntax**, never described in
  fluent narration.
- Ensemble chapters (6, 11, 20, 21, 26, 27) are where the four registers collide. They should
  be the loudest chapters in the book, not the flattest.

### Failure modes to watch

- **One narrator wearing four names** — the failure this rewrite exists to fix. Test: strip
  the names from a paragraph and see whether you can still tell who it is.
- **Mannered registers** — the opposite failure. If a reader can *name the device*, pull back.
- Detail of a single register. The first draft ran 292 meeting-words against 5 smells and
  2 tastes. Weather, food, body, noise.
- Explanatory warmth (ch16, ch22).
- Sentiment on the last page (ch25, ch27).
- The wise-immigrant-father cadence in Marek's dialogue (ch13) — the one place the book risks
  condescending to a character. His dialect must not do work the prose should be doing.
