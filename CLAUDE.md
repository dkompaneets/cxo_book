# CLAUDE.md

Working notes for the CXO novel ("The Vise").

## Layout

- `research/` — outlines, spine, character architecture, genre analysis. The working material.
  `research/canon.md` fixes the names/places/continuity the draft follows.
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

**Mick Herron's register, Elizabeth Strout's restraint at the peaks, no contempt anywhere.**

This is the governing style for the whole book. It is not a flavour applied on top — it is
what the strongest chapters already do, written down so the weak ones can be held to it.

- **Herron** — dry institutional comedy where the precision *is* the joke; professional
  competence and rot rendered exactly; the joke that conceals despair. Michael's whole
  characterisation ("his jokes always land, and that is the problem") is this move.
- **Strout** — at the four peak events and the ending, drop to plain declarative
  withholding and let the reader do the work.
- **No contempt** — Herron's narrator is sardonic *about* his people. Ours is not. The
  comedy comes from what a character believes about themselves, never from the narrator
  knowing better. This matters most for Nik and Marek, where a sardonic narrator curdles
  into caricature immediately.

Not Moriarty, not Backman, not Nicholls. Those were structural comps, not voice.

### Rules

- Close third, past tense, free indirect. One POV per chapter unless it is an ensemble chapter.
- Long accumulating sentences that **land on a flat concrete fact**. Elaboration, then thud.
- Comedy from institutional specificity, never from a character being stupid.
- **One aphorism per scene, maximum.** They are the book's best asset and they cheapen fast.
- **Emotion gets less language, not more.** At the peak, shorten.
- **No sentence that explains what the scene just did.** If a paragraph tells the reader how
  to feel about the preceding paragraph, cut it. Every score gain in revision came from this.
- Jokes must cost the joker something.
- British idiom throughout. The texture is where the credibility lives.

### Failure modes to watch

Named because the draft has drifted into each of them at least once: explanatory warmth
(ch16, ch22), sentiment on the last page (ch25, ch27), and the wise-immigrant-father cadence
in Marek's dialogue (ch13) — the one place the book risks condescending to a character.
