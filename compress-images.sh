#!/bin/bash
# Safe image compressor. Resizes to max edge, re-encodes JPEGs at quality,
# writes to a temp file, and replaces the original ONLY if smaller.
MAX_EDGE=2000
QUALITY=80
total_before=0; total_after=0; shrunk=0; kept=0; failed=0
compress_one() {
  f="$1"; [ -f "$f" ] || return
  ext="${f##*.}"; before=$(stat -f%z "$f"); tmp="$(mktemp -t mpcompress).${ext}"
  case "$ext" in
    jpg|jpeg|JPG|JPEG) sips -Z "$MAX_EDGE" -s format jpeg -s formatOptions "$QUALITY" "$f" --out "$tmp" >/dev/null 2>&1 ;;
    png|PNG) sips -Z "$MAX_EDGE" "$f" --out "$tmp" >/dev/null 2>&1 ;;
    *) rm -f "$tmp"; return ;;
  esac
  if [ ! -s "$tmp" ]; then printf 'FAILED  %s\n' "$f"; rm -f "$tmp"; failed=$((failed+1)); return; fi
  after=$(stat -f%z "$tmp"); total_before=$((total_before+before))
  if [ "$after" -lt "$before" ]; then
    mv "$tmp" "$f"; total_after=$((total_after+after)); shrunk=$((shrunk+1))
    printf 'shrunk  %-55s %9d -> %9d\n' "$f" "$before" "$after"
  else
    rm -f "$tmp"; total_after=$((total_after+before)); kept=$((kept+1))
    printf 'kept    %-55s %9d (already efficient)\n' "$f" "$before"
  fi
}
if [ "$#" -gt 0 ]; then
  for f in "$@"; do compress_one "$f"; done
else
  while IFS= read -r -d '' f; do compress_one "$f"; done < <(find . -type f \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' \) -not -path './.git/*' -not -path './node_modules/*' -print0)
fi
echo "------------------------------------------------------------"
printf 'shrunk: %d   kept: %d   failed: %d\n' "$shrunk" "$kept" "$failed"
printf 'before: %d bytes\nafter:  %d bytes\nsaved:  %d bytes\n' "$total_before" "$total_after" "$((total_before-total_after))"
