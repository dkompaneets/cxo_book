# CLAUDE.md

Working notes for the CXO novel ("The Vise").

## Layout

- `research/` — outlines, spine, character architecture, genre analysis. The working material.
- `audio/` — narrated mp3s of the research docs, for listening review.
- `scripts/` — tooling.
- `covers/` — cover concepts.
- `todo.md` — running list.

## Creating audio files

Research docs get narrated so they can be reviewed by ear. Kokoro TTS runs locally in
`.venv-kokoro` — no API, no network.

```sh
.venv-kokoro/bin/python scripts/tts.py research/outline2.md
```

Writes `audio/outline2.mp3` (output path derived from the input filename). Pass a second
argument to override it. Roughly 1 minute of audio per 1,000 characters; a 32-chapter
outline runs ~25 minutes and takes a few minutes to generate.

**How it works** — [scripts/tts.py](scripts/tts.py) converts markdown to narration text,
synthesises with Kokoro (`af_heart`, American English, 24 kHz), then pipes through ffmpeg
to mp3 and deletes the intermediate wav.

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
