set spineSize "1000x200"
set spineBackgroundColor "lightcyan"
set spineFont "'Noto-Serif-JP'"
set spineTitlePointsize 100
set spineTitleText 'サンプル'
set spineSubtitlePointsize 50
set spineSubtitleText 'Subtitle'
set spineStrokeColor "lightgray"
set spineStrokeWidth 10
set spineLineCoordinates "149,0 149,200"

# Generate a Spine Image
magick -size $spineSize xc:$spineBackgroundColor \
  -font $spineFont \
  -pointsize $spineTitlePointsize -gravity north -annotate +25+0 $spineTitleText \
  -pointsize $spineSubtitlePointsize -gravity south -annotate +0+0 $spineSubtitleText \
  -stroke $spineStrokeColor -strokewidth $spineStrokeWidth -draw "line $spineLineCoordinates" \
  -rotate -90 box_spine.png

set frontSize "750x1000"
set frontBackgroundColor "ghostwhite"
set frontFont "'Noto-Serif-JP'"
set frontTitleFill "black"
set frontTitlePointsize 100
set frontTitleText 'サンプル'
set frontAuthorFill "blue"
set frontAuthorPointsize 75
set frontAuthorText 'Author'
set frontPublishedByFill "black"
set frontPublishedByPointsize 75
set frontPublishedByText 'Published By'
set frontLineCoordinates "0,850 750,850"
set img "$img" # assuming img is already defined elsewhere

# Generate the front cover
magick -size $frontSize xc:$frontBackgroundColor \
  -font $frontFont \
  -fill $frontTitleFill -pointsize $frontTitlePointsize -gravity north -annotate +0+25 $frontTitleText \
  -fill $frontAuthorFill -pointsize $frontAuthorPointsize -gravity northeast -annotate +25+140 $frontAuthorText \
  -fill $frontPublishedByFill -pointsize $frontPublishedByPointsize -gravity south -annotate +0+25 $frontPublishedByText \
  -stroke $spineStrokeColor -strokewidth $spineStrokeWidth -draw "line $frontLineCoordinates" \
  \( $img -resize 500x500 \) \
  -gravity center -compose multiply -composite box_front.png

set spineDistortCoordinates "0,0 -150,100  0,1000 -150,895  200,1000 0,1000  200,0 0,0"
set frontDistortCoordinates "0,0 0,0  0,1000  0,1000  750,1000 500,780  750,0 500,150"

# Distort both images and merge using common points.
magick \
  \( box_spine.png -alpha set -virtual-pixel transparent \
     +distort Perspective "$spineDistortCoordinates" \) \
  \( box_front.png -alpha set -virtual-pixel transparent \
     +distort Perspective "$frontDistortCoordinates" \) \
  \
  -background black -compose plus -layers merge +repage \
  -bordercolor black -compose over -border 75x10 box_set.png
  
magick box_set.png box_spine.png box_front.png +append merged.png
