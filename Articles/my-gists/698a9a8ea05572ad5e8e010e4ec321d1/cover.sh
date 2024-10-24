#!/bin/bash

# Creado por Carlos Celis Flen-Bers
wget http://img513.imageshack.us/img513/3228/imgrf9.jpg; img="imgrf9.jpg"
#img=$1;

identify -format "%w\x%h" $img
# imgrf9.jpg = 3213 px x 2125 px
# Width of spine = 213
# Width of covers 3213 - 213 = 3000; 3000 / 2 = 1500 px

# Back 1500 + Spine 213 + Front 1500 = 3213 px

# Cut front + spine = 1500 + 213 = 1713
#            East
# +______+---+------+
# |      |///|//////|
# |      |///|//////|
# |      |///|//////|
# |      |///|//////|
# +______+---+------+
convert "$img"  -gravity East -chop 1713x back.jpg
echo "Do back.jpg"

# Cut front y back = 1500 y 1500 por ambos lados
#   West       East
# +------+___+------+
# |//////|   |//////|
# |//////|   |//////|
# |//////|   |//////|
# |//////|   |//////|
# +------+___+------+
convert "$img"  -gravity East -chop 1500x  -gravity West -chop 1500x0 spine.jpg
echo "Do spine.jpg"

# Cut back + spine = 1500 + 213 = 1713
#     West
# +------+---+______+
# |//////|///|      |
# |//////|///|      |
# |//////|///|      |
# |//////|///|      |
# +------+---+______+
convert "$img"  -gravity West -chop 1713x0  front.jpg
echo "Do front.jpg"

# Transformar
# Puntos de perspectiva
# 1------2
# |      |
# |      |
# |      |
# |      |
# 3------4
# back 1500x2125
convert back.jpg -matte -virtual-pixel transparent \
 -distort Perspective '0,0 173,76   1500,0 1500,62   0,2125 173,1971   1500,2125 1500,1957' back_cover.png
echo "Creado back_cover.jpg"

# spine 213x2125
convert spine.jpg -matte -virtual-pixel transparent \
 -distort Perspective '0,0 0,62   213,0 143,76   0,2125 0,1957   213,2125 143,2013' spine_cover.png
echo "Creado spine_cover.jpg"

# front 1500x2125
convert front.jpg -matte -virtual-pixel transparent \
 -distort Perspective '0,0 0,76   1500,0 1200,47   0,2125 0,2013   1500,2125 1200,1910' front_cover.png
echo "Creado front_cover.jpg"

montage -geometry +0+0 back_cover.png \
\( spine_cover.png -crop 0x0-70+0 \) \
front_cover.png -background none caratula.png
# caratula.png 3143x2125

convert -size 16x16 -font CourierNew -pointsize 18 xc:none -annotate +3+12 '©' -flop cl.png

convert -size 150x16 -font CourierNew -pointsize 18 xc:none -annotate +3+12 'Carlos Celis' cc.png

montage -geometry +0+0 -background none cl.png cc.png carloscelis.png

ancho=`identify -format "%w" caratula.png`
anchowm=`expr $ancho / 3`; #echo $anchowm

composite \( carloscelis.png -geometry $anchowm -gravity southeast -dissolve 40% \)  caratula.png caratula-cpleft.png

#convert -trim img.png caratula.png
echo "Montage do"
