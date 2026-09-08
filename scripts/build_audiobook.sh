#!/bin/sh
# Join the narrated chapters in audio/book/ into one audiobook file with chapter
# markers, so a player can jump between chapters and remember where you stopped.
#
#   scripts/build_audiobook.sh                 # -> audio/the-vise.m4b
#   scripts/build_audiobook.sh audio/other.m4b # custom output path
#
# Chapter titles come from the `# N. Title` heading of each book/chapter-*.md.
# Needs ffmpeg and ffprobe on PATH. Run scripts/narrate_book.sh first so every
# chapter mp3 is newer than its markdown.
set -e
cd "$(dirname "$0")/.."
out="${1:-audio/the-vise.m4b}"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

list="$tmp/list.txt"
meta="$tmp/meta.txt"
printf ';FFMETADATA1\ntitle=The Vise\nalbum=The Vise\ngenre=Audiobook\n' > "$meta"

start=0
for md in book/chapter-*.md; do
    stem=$(basename "$md" .md)
    mp3="audio/book/$stem.mp3"
    if [ ! -f "$mp3" ] || [ "$md" -nt "$mp3" ]; then
        echo "!! $mp3 is missing or older than $md; run scripts/narrate_book.sh first" >&2
        exit 1
    fi
    title=$(head -1 "$md" | sed 's/^# *//')
    ms=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$mp3" | awk '{printf "%d", $1*1000}')
    end=$((start + ms))
    printf "file '%s'\n" "$(pwd)/$mp3" >> "$list"
    printf '[CHAPTER]\nTIMEBASE=1/1000\nSTART=%d\nEND=%d\ntitle=%s\n' "$start" "$end" "$title" >> "$meta"
    start=$end
done

ffmpeg -y -loglevel error -f concat -safe 0 -i "$list" -i "$meta" -map_metadata 1 -map 0:a \
    -c:a aac -b:a 64k -ac 1 -ar 24000 -movflags +faststart "$out"

secs=$((start / 1000))
printf 'wrote %s  %d chapters  %dh %02dm  %s\n' "$out" "$(ls book/chapter-*.md | wc -l | tr -d ' ')" \
    $((secs / 3600)) $(((secs % 3600) / 60)) "$(du -h "$out" | cut -f1)"
