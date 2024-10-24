# blur float
# -modulateは明度（Brightness）、彩度（Saturation）、色相（Hue）を調整
magick $img \
        \( -clone 0 -resize 150% -blur 0x50 -alpha set -channel A -evaluate set 50% -modulate 50,100,100 \) \
        -delete 0 \
        \( $img -set page "+%[fx:(w*1.5-w)/2]+%[fx:(h*1.5-h)/2]" \) \
        -flatten +repage "$(basename "$img" .png)-2.png"
        
# Fixed SIZE ver. (1024x)
magick $img \
          \( -clone 0 -resize 1024x1024^ -gravity center -crop 1024x1024+0+0! -blur 0x50 -alpha set -channel A -evaluate set 50% -modulate 50,100,100 \
          -fill white -font 'Senobi-Gothic-Medium' -pointsize 40 -annotate +0+440 %t\
          -pointsize 40 -annotate +0-440 'NOW ON SALE!'  \) \
          -delete 0 \
          \( $img -resize 75% -set page "+%[fx:(1024-w)/2]+%[fx:(1024-h)/2]" \) \
        -flatten +repage "$(basename "$img" .png)-2.png"
        
# With shadow float
magick xc:white \
  \( $img -resize 1024x1024^ -gravity center -crop 1024x1024+0+0! -blur 0x50 -alpha set -channel A -evaluate set 50% \
  -fill white -font 'Senobi-Gothic-Medium'\
  -pointsize 40 -annotate +0+440 %t\
  -pointsize 40 -annotate +0-440 'NOW ON SALE!'  \) \
  \( $img -resize 75% -set page "+%[fx:(1024-w)/2]+%[fx:(1024-h)/2]" \) \
  \( +clone -background black -shadow 80x3+5+5 -geometry +0+0 \) \
  +swap -background none -layers merge +repage \
  "$(basename "$img" .png)-3.png"
  
✦ ➜ magick -list font | grep Font: | fzf