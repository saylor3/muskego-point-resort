#!/bin/bash
# Moves and renames the Kelly Berg cabin photos from ~/Downloads
# into ~/Desktop/NEW Muskego/images/cabins/
#
# Usage: bash ~/Desktop/NEW\ Muskego/install_photos.sh
#
# Run this after all 21 attachments have finished downloading.

set -e

DEST=~/Desktop/"NEW Muskego"/images/cabins
DL=~/Downloads

echo "Creating directories..."
mkdir -p "$DEST/norway"
mkdir -p "$DEST/spruce"
mkdir -p "$DEST/lumberjack"

echo "Filing Norway photos..."
cp "$DL/_IrXHFNg.jpeg"   "$DEST/norway.jpeg"       # card image
cp "$DL/3-jMvpaw.jpeg"   "$DEST/norway/1.jpeg"
cp "$DL/BPkgnF8w.jpeg"   "$DEST/norway/2.jpeg"
cp "$DL/eGXGR8Qw.jpeg"   "$DEST/norway/3.jpeg"
cp "$DL/KgczQmnQ.jpeg"   "$DEST/norway/4.jpeg"
cp "$DL/Obp_wCTg.jpeg"   "$DEST/norway/5.jpeg"
cp "$DL/Q_IkWuBg.jpeg"   "$DEST/norway/6.jpeg"
cp "$DL/QO5zySPA.jpeg"   "$DEST/norway/7.jpeg"

echo "Filing Spruce photos..."
cp "$DL/IMG_3059.jpeg"   "$DEST/spruce.jpeg"        # card image
cp "$DL/IMG_3062.jpeg"   "$DEST/spruce/1.jpeg"
cp "$DL/IMG_6291.jpeg"   "$DEST/spruce/2.jpeg"
cp "$DL/IMG_6300.jpeg"   "$DEST/spruce/3.jpeg"
cp "$DL/IMG_6302.jpeg"   "$DEST/spruce/4.jpeg"

echo "Filing Lumberjack photos..."
cp "$DL/Bi.jpg"                      "$DEST/lumberjack.jpeg"    # card image
cp "$DL/Ludlow's Resort-0047.jpg"    "$DEST/lumberjack/1.jpeg"
cp "$DL/Ludlow's Resort-0058.jpg"    "$DEST/lumberjack/2.jpeg"
cp "$DL/Ludlows_2019_5-26.jpg"       "$DEST/lumberjack/3.jpeg"
cp "$DL/Ludlows_2019_5-28.jpg"       "$DEST/lumberjack/4.jpeg"
cp "$DL/Ludlows_2019_5-35.jpg"       "$DEST/lumberjack/5.jpeg"
cp "$DL/Ludlows_2019_5-40.jpg"       "$DEST/lumberjack/6.jpeg"
cp "$DL/Ludlows_2019_5-41.jpg"       "$DEST/lumberjack/7.jpeg"

echo ""
echo "Done! Final structure:"
echo "  images/cabins/norway.jpeg          (card)"
echo "  images/cabins/norway/1-7.jpeg      (gallery)"
echo "  images/cabins/spruce.jpeg          (card)"
echo "  images/cabins/spruce/1-4.jpeg      (gallery)"
echo "  images/cabins/lumberjack.jpeg      (card)"
echo "  images/cabins/lumberjack/1-7.jpeg  (gallery)"
