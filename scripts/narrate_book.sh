#!/bin/sh
# Narrate book chapters with Kokoro. Skips a chapter whose mp3 is newer than its
# markdown, so it is safe to re-run after adding chapters, editing one, or after
# an interrupted run.
#
#   scripts/narrate_book.sh                       # every chapter
#   scripts/narrate_book.sh book/chapter-0*.md    # a subset
set -e
cd "$(dirname "$0")/.."
mkdir -p audio/book

if [ $# -gt 0 ]; then
    files="$*"
else
    files=$(ls book/chapter-*.md)
fi

for f in $files; do
    stem=$(basename "$f" .md)
    out="audio/book/$stem.mp3"
    if [ -f "$out" ] && [ "$out" -nt "$f" ]; then
        echo "=== skip $out (up to date)"
        continue
    fi
    echo "=== $f -> $out"
    .venv-kokoro/bin/python scripts/tts.py "$f" "$out"
done
echo "=== done"
