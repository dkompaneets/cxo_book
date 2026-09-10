#!/bin/sh
# Build the novel as one EPUB and one PDF from book/chapter-*.md.
#   scripts/build_ebook.sh            -> ebook/the-vise.epub, ebook/the-vise.pdf
# EPUB via pandoc (one chapter per section, cover from covers/). PDF via pandoc HTML
# printed by headless Chrome, so no TeX install is needed.
set -eu
cd "$(dirname "$0")/.."

TITLE="The Vise"
AUTHOR="Dmitriy Kompaneets and Mikhael Podgortsev"
COVER="covers/the-vise-cover-v1.png"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT=ebook
mkdir -p "$OUT"

CSS="$OUT/.style.css"
cat > "$CSS" <<'CSS'
@page { size: 6in 9in; margin: 0.9in 0.8in; }
html, body { margin: 0; padding: 0; }
body { font-family: Georgia, "Times New Roman", serif; font-size: 11.5pt; line-height: 1.45; }
h1 { font-size: 1.5em; font-weight: normal; margin: 3em 0 1.5em; page-break-before: always; text-align: center; }
h1.title { font-size: 2.4em; margin-top: 35vh; page-break-before: auto; }
p.author { text-align: center; font-style: italic; }
p { margin: 0; text-indent: 1.4em; text-align: justify; hyphens: auto; }
h1 + p, hr + p { text-indent: 0; }
hr { border: 0; text-align: center; margin: 1.6em 0; }
hr::after { content: "\2022\2003\2022\2003\2022"; }
em { font-style: italic; }
nav#TOC { page-break-before: always; text-align: center; margin-top: 30vh; }
nav#TOC h2 { font-size: 1.5em; font-weight: normal; margin-bottom: 1.5em; }
nav#TOC ul { list-style: none; padding: 0; margin: 0; }
nav#TOC li { margin: 0.35em 0; }
nav#TOC a { color: inherit; text-decoration: none; }
@page cover { margin: 0; }
div.cover { page: cover; width: 6in; height: 9in; overflow: hidden; page-break-after: always; }
div.cover img { display: block; width: 100%; height: 100%; object-fit: cover; }
CSS

# shellcheck disable=SC2012
CHAPTERS="$(ls book/chapter-*.md | sort -V)"

pandoc $CHAPTERS -o "$OUT/the-vise.epub" \
  --metadata title="$TITLE" --metadata author="$AUTHOR" --metadata lang=en-GB \
  --epub-cover-image="$COVER" --css="$CSS" --split-level=1 --toc --toc-depth=1
echo "wrote $OUT/the-vise.epub"

HTML="$OUT/.the-vise.html"
COVERHTML="$OUT/.cover.html"
printf '<div class="cover"><img src="%s" alt="Cover"></div>\n' "$COVER" > "$COVERHTML"
pandoc $CHAPTERS -o "$HTML" --standalone --embed-resources \
  --metadata title="$TITLE" --metadata author="$AUTHOR" --metadata lang=en-GB \
  --css="$CSS" --toc --toc-depth=1 --metadata toc-title=Contents --include-before-body="$COVERHTML"
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$(pwd)/$OUT/the-vise.pdf" "file://$(pwd)/$HTML" 2>/dev/null
rm -f "$HTML" "$CSS" "$COVERHTML"
echo "wrote $OUT/the-vise.pdf"
