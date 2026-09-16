#!/usr/bin/env bash
# Renders every image in assets/ from the HTML in tools/, in a dark and a light
# variant, using headless Chrome at 2x. The README picks the variant matching
# the viewer's GitHub theme through <picture>. Corners stay transparent.
#
#   ./tools/render.sh            # all images
#   ./tools/render.sh banner     # one image
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"

# name width height
IMAGES=(
  "banner 1280 440"
  "timeline 1280 520"
  "operating-model 1280 720"
)

shoot() { # page theme w h out
  "$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
    --default-background-color=00000000 --force-device-scale-factor=2 \
    --window-size="$3,$4" --virtual-time-budget=15000 \
    --screenshot="$5" "file://$ROOT/tools/$1.html#$2" >/dev/null 2>&1
}

for spec in "${IMAGES[@]}"; do
  read -r name w h <<<"$spec"
  [[ $# -gt 0 && "$1" != "$name" ]] && continue
  for theme in dark light; do
    out="$ROOT/assets/$name-$theme.png"
    shoot "$name" "$theme" "$w" "$h" "$out"
    printf '%-28s %s\n' "$(basename "$out")" "$(sips -g pixelWidth -g pixelHeight "$out" | tail -2 | awk '{printf "%s ", $2}')"
  done
done
