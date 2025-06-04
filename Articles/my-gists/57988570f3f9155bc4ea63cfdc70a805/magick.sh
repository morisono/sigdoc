# create watermark
magick convert -size 500x500 xc:none -font 'Freestyle-Script' -pointsize 50 -draw "gravity center fill rgba(0,0,0,0.5) rotate -30 text 0,0 'Sample'" watermark.png

# add watermark
mogrify -gravity center -draw "image over 0,0 0,0 'watermark.png'" *.png
# -alpha set -channel RGBA -evaluate set 50%

## shutterstock style
magick convert input.png \( -size 100x -background none -fill white -gravity center label:"watermark" -trim -rotate -30 -bordercolor none -border 10 -write mpr:wm +delete +clone -fill mpr:wm  -draw 'color 0,0 reset' \) -compose over -composite out_watermark.png

## yellow tape
magick convert input.png \( -pointsize 30 -background none -undercolor '#ffff0040' -fill black -font 'Freestyle-Script' -gravity center label:"Sample Sample Sample Sample Sample Sample " -trim -rotate -30 -bordercolor none -border 0 -write mpr:wm +delete +clone -fill mpr:wm  -draw 'color 0,0 reset' \) -compose over -composite out_watermark.png


# at random
mogrify -gravity center -draw "image over %[fx:int(w/2)],%[fx:int(h/2)] watermark.png" *.png

# crop resize
convert input.png -gravity center -crop 50% -resize 200% input_center.png

# blur
magick convert input.png  -blur 0x8 +mask output_Blur.png


# make mask
magick -size 500x500 radial-gradient: sb_mask.png
magick convert sb_mask.png -negate sb_mask_n.png

magick convert input.png -mask sb_mask.png -blur 0x18 +mask output_maskedBlur.png

# faster way
convert -scale 10% -blur 0x2.5 -resize 1000% sample.jpg blurred_fast.jpg


magick input.png sb_mask_n.png -composite output_maskedBlur.png

magick convert input.png -blur 0x10 -gravity center -crop 50% -resize 200% -alpha on -channel a -evaluate set 50% -compose dissolve -composite output.png

magick input.png -background "rgba(0, 0, 0, 0)" -virtual-pixel transparent -blur 0x10 -define compose:args="0,-100%" -compose DstIn -composite output.png

# mosaic
convert input.png -scale 10% -scale 1000% output.png

# gauss
convert input.png -gaussian-blur 20x10 output.png

# fade
convert input.png \
\( -size 1920x1080 radial-gradient:black-white -gravity center -crop 50%x100%+0+0 \) \
-alpha off -compose copy_opacity -composite output.png

# crop
convert input.png -gravity center -crop 60%x60%+0+0 output.png

# greyed out
magick input.png -colorspace Gray gray_input.png
magick input.png gray_input.png -compose blend -define compose:args=50x50 -composite output.png

# remove metadata
magick convert input.png -strip output.png
