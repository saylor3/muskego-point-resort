#!/bin/bash
# audit-images.sh — read-only. Reports sizes of git-TRACKED images only (what actually deploys).
echo "Scanning tracked images..."
git ls-files -z -- '*.jpg' '*.jpeg' '*.png' '*.JPG' '*.JPEG' '*.PNG' | \
while IFS= read -r -d '' f; do
  bytes=$(stat -f%z "$f")
  mb=$(echo "scale=2; $bytes/1048576" | bc)
  flag=""
  if [ "$bytes" -gt 1048576 ]; then flag="  <-- OVER 1MB"; fi
  printf "%8s MB  %s%s\n" "$mb" "$f" "$flag"
done | sort -rn
echo ""
echo "Anything flagged OVER 1MB should be compressed before deploy."
