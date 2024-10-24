convert -virtual-pixel Transparent \
        cover.png -matte -resize 1600x1074\! \
        \( -clone 0 -crop 740x0+0+0\! \
                    +distort Perspective '0,0  62,80  0,1073  62,897  739,1073  628,912  739,0  628,64' \
        \) \
        \( -clone 0 -crop 84x0+758+0\! \
                    +distort Perspective '0,0 628,38  0,1073 628,922   83,1073  688,937   83,0  688,30' \
        \) \
        \( -clone 0 -crop 758x0+842+0\! \
                    +distort Perspective '0,0 688,30  0,1073 688,937  757,1073 1228,883  757,0 1228,80' \
        \) \
        -size 1700x1026 xc:black -swap 0,-1 +delete \
        \( label.jpg -resize 510x510\! label_opacity.png -alpha On -compose Copy_Opacity -composite \
                     -crop 410x0+100+0\! -repage +1232+229 \
        \) \
        -compose Over -layers merge \
        cover_label_light.png -compose HardLight -composite \
        cover_label_opacity.png -alpha On -compose Copy_Opacity -composite \
        -resize 1260x760\! -quality 95 -depth 8     preview.png