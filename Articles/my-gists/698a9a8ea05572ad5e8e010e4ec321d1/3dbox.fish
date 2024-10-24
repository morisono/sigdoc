iWidth=1024
iHeight=1024
adjX=$(echo "$iWidth * 0.2 / 2" | bc)      # Scaling factor that works for me
adjY=$(echo "$iHeight * 0.1" | bc)
frameWidth=15       # width of the frame side

magick "$input" \
  -virtual-pixel white -distort Perspective \
          "0,0,$adjX,0" \
          ",0,$iHeight,$adjX,$iHeight" \
          ",$iWidth,0,$(echo "$iWidth - $adjX" | bc),$adjY" \
          ",$iWidth,$iHeight,$(echo "$iWidth - $adjX" | bc),$(echo "$iHeight - $adjY" | bc)" \
\( +clone -crop 1x"$iHeight"+$adjX+0 \
-fill black -colorize 40% -write mpr:line +delete \) \
-draw "image over $(echo "$adjX - $frameWidth" | bc),0 $frameWidth,$iHeight 'mpr:line'" \
\( +clone -crop "${frameWidth}x$iHeight"+$((adjX-frameWidth))+0 \
-virtual-pixel white -distort Perspective \
            "0,0,0,10," \
            "0,$iHeight,0,$(echo "$iHeight - 10" | bc)," \
            "$frameWidth,0,$frameWidth,0," \
            "$frameWidth,$iHeight,$frameWidth,$iHeight" \
  -write mpr:side +delete \) \
  -draw "image over $(echo "$adjX - $frameWidth" | bc),0 $frameWidth,$iHeight 'mpr:side'" \
"$output"