#!/usr/bin/env fish

# Usage: fish script.fish $str $str2 $str3 $str4

# Set variables
set WIDTH_2_1 2048
set HEIGHT_2_1 1024
set WIDTH_16_9 1860
set HEIGHT_16_9 1024
set WIDTH_9_16 680
set HEIGHT_9_16 1200

set LEFT_10_PERCENT 186 # (math 1860 * 0.10)
set LEFT_20_PERCENT 372 # (math 1860 * 0.20)
set LEFT_25_PERCENT 465 # (math 1860 * 0.25)
set LEFT_30_PERCENT 558 # (math 1860 * 0.30)

set RIGHT_70_PERCENT 1302 # (math 1860 * 0.70)
set RIGHT_80_PERCENT 1488 # (math 1860 * 0.80)
set RIGHT_90_PERCENT 1674 # (math 1860 * 0.90)

set TOP_5_PERCENT 60 # (math 1200 * 0.05)
set TOP_10_PERCENT 120 # (math 1200 * 0.10)
set TOP_15_PERCENT 180 # (math 1200 * 0.15)
set TOP_20_PERCENT 240 # (math 1200 * 0.20)
set TOP_30_PERCENT 360 # (math 1200 * 0.30)

set BOTTOM_70_PERCENT 840 # (math 1200 * 0.70)
set BOTTOM_80_PERCENT 960 # (math 1200 * 0.80)
set BOTTOM_90_PERCENT 1080 # (math 1200 * 0.90)

set FONT_SIZE 100
set FONT_SIZE_SMALL 60
set FONT_SIZE_SMALLER 40
set FONT_SIZE_SMALLEST 40

set FONT 'Senobi-Gothic-Medium'

# Get the current timestamp
set TIMESTAMP (date +"%Y%m%d%H%M%S")

# Create a new folder with the timestamp
set OUTPUT_DIR "$TIMESTAMP"
mkdir -p $OUTPUT_DIR

# Check if the correct number of arguments is provided
if test (count $argv) -lt 4
    echo "Usage: $argv[0] text1 text2 text3 text4"
    exit 1
end

# Assign input arguments to variables
set str1 $argv[1]
set str2 $argv[2]
set str3 $argv[3]
set str4 $argv[4]

# Get the list of image files
set imgs (ls masterpiece/*.png)

# Check if the input folder is empty
if test (count $imgs) -eq 0
    echo "No image files found in the 'masterpiece' folder."
    exit 1
end

# Progress indication
echo "Processing images..."

# Loop through each image file in the masterpiece folder
for img in $imgs
    set out_path (basename $img .png)
    # Determine the most dominant color in the image
    set dominant_color (magick $img -format "%c" histogram:info: | sort -rnk 1 | head -n 1 | awk '{print $3}')

    # Determine font color based on background brightness
    set brightness (magick $img -colorspace Gray -format "%[mean]" info:)
    if test $brightness > 0.5
        set font_color '#555'
    else
        set font_color '#ddd'
    end

    # Create the 2:1 (2048x1024) image
    # for gravity in east west
    #     set annotate_x (if test $gravity = "east"; echo "-$LEFT_20_PERCENT"; else; echo "$LEFT_20_PERCENT"; end).
    #     magick $img -gravity $gravity -background $dominant_color -extent {$WIDTH_2_1}x{$HEIGHT_2_1} -fill $font_color -pointsize $FONT_SIZE -font $FONT -gravity center -annotate {$annotate_x}+0 $str1 -pointsize $FONT_SIZE_SMALL -annotate {$annotate_x}+-{$TOP_10_PERCENT} $str2 -pointsize $FONT_SIZE_SMALLEST -annotate {$annotate_x}+{$TOP_20_PERCENT} $str3 -annotate {$annotate_x}+{$TOP_15_PERCENT} $str4 $OUTPUT_DIR/$out_path-2x-$gravity.png
    # end

    # Create the 16:9 (1860x1024) image
    for gravity in east #west
        set annotate_x (if test $gravity = "east"; echo "-$LEFT_25_PERCENT"; else; echo "$LEFT_25_PERCENT"; end)
        magick $img -gravity $gravity -background $dominant_color -extent {$WIDTH_16_9}x{$HEIGHT_16_9} -fill $font_color -pointsize $FONT_SIZE -font $FONT -gravity center -annotate {$annotate_x}+0 $str1 -pointsize $FONT_SIZE_SMALL -annotate {$annotate_x}-{$TOP_10_PERCENT} $str2 -pointsize $FONT_SIZE_SMALLEST -annotate {$annotate_x}+{$TOP_10_PERCENT} $str3 -annotate {$annotate_x}+{$TOP_15_PERCENT} $str4 $OUTPUT_DIR/$out_path-16-9x-$gravity.png
    end

    # Create additional variations
    # Vertical banner (9:16)
    for gravity in north #south
        set annotate_y (if test $gravity = "south"; echo "$BOTTOM_80_PERCENT"; else; echo "$TOP_20_PERCENT"; end)
        magick $img -gravity $gravity -background $dominant_color -extent {$WIDTH_9_16}x{$HEIGHT_9_16} -fill $font_color -pointsize $FONT_SIZE_SMALL -font $FONT -annotate +0+1*{$annotate_y} $str1 -pointsize $FONT_SIZE_SMALLEST -annotate +0+1.2*{$annotate_y} $str2 -pointsize $FONT_SIZE_SMALLEST -annotate +0+1.3*{$annotate_y} $str3 -pointsize $FONT_SIZE_SMALLEST -annotate +0+1.4*{$annotate_y} $str4 $OUTPUT_DIR/$out_path-vertical-$gravity.png
    end
end

# Process completed
echo "Image processing completed. Output files are in '$OUTPUT_DIR' folder."
