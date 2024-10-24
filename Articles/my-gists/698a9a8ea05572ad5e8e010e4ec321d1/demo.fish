#!/usr/bin/env fish

set input "input.png"
set depth 1
set edge (math "$depth * 72")

set width (magick "$input" -ping -format "%w" info:)
set height (magick "$input" -ping -format "%h" info:)

set shrink (math "($edge * 0.7)")
set angle 30
set radian (math "($angle * 3.14159265358979323846 / 180)")
set alpha (math "abs(tan($radian)) * $shrink")
set shortSide (math "($height - $alpha)")

set topLong (math "($width + $shrink)")

set widthMinusEdge (math "$width-$edge")
set heightMinusEdge (math "$height-$edge")

# Central part
magick "$input" -crop "$widthMinusEdge x $heightMinusEdge+0+0" +repage "central.png"

# Right corner
magick "$input" -crop "$edge x $height+$widthMinusEdge+0" -virtual-pixel transparent -distort Perspective "0,0 0,0 $edge,0 $shrink,$alpha $edge,$height $shrink,$height 0,$height 0,$height" +repage "right.png"

# Top part
magick "$input" -crop "$widthMinusEdge x $edge+0+$heightMinusEdge" -virtual-pixel transparent -distort Perspective "0,0 0,0 $widthMinusEdge,0 $widthMinusEdge,0 $width,$edge $topLong,$alpha 0,$edge $shrink,$alpha" +repage "top.png"

# Composite image
magick -size "$widthx$height" xc:none -draw "image over 0,0 0,0 'central.png'" -draw "image over $widthMinusEdge,0 0,0 'right.png'" -draw "image over 0,$heightMinusEdge 0,0 'top.png'" +repage "composite.png"

# Create shadow
magick "composite.png" -background black -virtual-pixel transparent -shadow 80x3+5+5 "wrap1.png"

# Output
magick "wrap1.png" "png:-"

# Cleanup
rm central.png right.png top.png composite.png wrap1.png