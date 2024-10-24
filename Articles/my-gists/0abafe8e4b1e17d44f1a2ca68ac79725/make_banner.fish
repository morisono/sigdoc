#!/usr/bin/env fish

# set colors white black red green blue yellow
# function generate_colorlist
# set _colorlist []
# for c1 in $colors
#     for c2 in $colors
#         if test "$c1" != "$c2"
#             set _colorlist (echo $_colorlist $c1 $c2)
#         end
#     end
# end

set colorlist "\
white red
yellow red
black red
white black
yellow black
red black
yellow white
red white
black white
white yellow
red yellow
black yellow"

set wordlist "\
泌尿器科医になる 理由
蟹を家で食べる 意味"


set current_time (date +%Y%m%d_%H%M%S)
set ext png
set f Dela-Gothic-One-Regular
set w 1024
set h 512
set p1 100
set p2 500
set size (echo {$w}x{$h})
set out_path (echo outputs/$current_time/$size)
set filelist ""

function generate_banner
    set i 0
    echo $wordlist | while read c1 c2
        mkdir -p $out_path/{$c1}_{$c2}
        echo $colorlist | while read bc fc
            set out {$c1}_{$c2}/(printf "%05d\n" $i).{$ext}
            convert -size {$w}x{$h} xc:$bc -fill $fc \
                -font $f -gravity center \
                -pointsize $p1 -annotate +0-200 $c1 \
                -pointsize $p2 -annotate +0+20 $c2 \
                $out_path/$out
            set i (math $i + 1)
        end
    end
end

function generate_gif
    convert -delay 1 -loop 0 (find $out_path -name "*.$ext") \
        "$out_path/output.gif"
end

generate_banner
generate_gif
