#!/usr/bin/fish

# Function to display help
function show_help
    echo "Usage: script.fish [OPTIONS]"
    echo "Options:"
    echo "  -i, --input                     Input files (required)"
    echo "  --output-dir                    Output directory"
    echo "  --size-spine                    Spine size (default: 1000x100)"
    echo "  --size-cover                    Cover size (default: 750x1000)"
    echo "  --size-logo                     Logo size (default: 512x512)"
    echo "  --font                          Fonts (comma-separated list, default: 'CobraFontAdventure-Regular,Dela-Gothic-One-Regular,Noto-Serif-JP')"
    echo "  --fontsize-spine-1              Font size for spine title (default: 40)"
    echo "  --fontsize-spine-2              Font size for spine author (default: 40)"
    echo "  --fontsize-spine-3              Font size for spine publisher (default: 30)"
    echo "  --fontsize-cover-1              Font size for cover title (default: 80)"
    echo "  --fontsize-cover-2              Font size for cover subtitle (default: 40)"
    echo "  --fontsize-cover-3              Font size for cover publisher (default: 40)"
    echo "  --stroke-width                  Stroke width (default: 10)"
    echo "  --stroke-color                  Stroke color (default: lightgray)"
    echo "  --line-coord-spine              Line coordinates for spine (default: '250,0 250,200')"
    echo "  --line-coord-cover              Line coordinates for cover (default: '0,750 750,750')"
    echo "  --distortion-points-spine       Distortion points for spine (default: '-100,0 -150,100 -100,1000 -150,895 100,1000 0,1000 100,0 0,0')"
    echo "  --distortion-points-cover       Distortion points for cover (default: '0,0 0,0 0,1000 0,1000 750,1000 500,780 750,0 500,150')"
    echo "  --fontsize-banner-1             Font size for banner 1 (default: 40)"
    echo "  --fontsize-banner-2             Font size for banner 2 (default: 50)"
    echo "  --fontsize-banner-3             Font size for banner 3 (default: 20)"
    echo "  --text                          Text variables: title,subtitle,author,publisher (comma-separated list, default: 'title,subtitle,author,publisher')"
    echo "  --bc-banner                     Background color for banner (default: '#0d1117')"
    echo "  --bc-spine                      Background color for spine (default: '#f7931b')"
    echo "  --bc-cover                      Background color for cover (default: 'black')"
    echo "  --fc-banner                     Font color for banner (default: '#eaf2f9')"
    echo "  --fc-cover                      Font color for cover (default: '#eaf2f9')"
    echo "  --fc-spine                      Font color for spine (default: '#eaf2f9')"
    echo "  --line-color                    Line color (default: 'white')"
    echo "  --help                          Show this help message"
end

# Default values
set size_spine "1000x100"
set size_cover "750x1000"
set size_logo "512x512"
set fonts "CobraFontAdventure-Regular,Dela-Gothic-One-Regular,Noto-Serif-JP"
set fontsize_spine_1 40
set fontsize_spine_2 40
set fontsize_spine_3 30
set fontsize_cover_1 80
set fontsize_cover_2 40
set fontsize_cover_3 40
set stroke_width 10
set stroke_color "lightgray"
set line_coord_spine "250,0 250,200"
set line_coord_cover "0,750 750,750"
set distortion_points_spine "-100,0 -150,100 -100,1000 -150,895 100,1000 0,1000 100,0 0,0"
set distortion_points_cover "0,0 0,0 0,1000 0,1000 750,1000 500,780 750,0 500,150"
set fontsize_banner_1 40
set fontsize_banner_2 50
set fontsize_banner_3 20
set text "title,subtitle,author,publisher"
set bc_banner '#0d1117'
set bc_spine '#f7931b'
set bc_cover 'black'
set fc_banner '#eaf2f9'
set fc_cover '#eaf2f9'
set fc_spine '#eaf2f9'
set line_color 'white'

# Parse arguments
for arg in $argv
    switch $arg
        case '-i' '--input'
            set -l input_files
            set processing_input 1
        case '--output-dir'
            set processing_output_dir 1
        case '--size-spine'
            set processing_size_spine 1
        case '--size-cover'
            set processing_size_cover 1
        case '--size-logo'
            set processing_size_logo 1
        case '--font'
            set processing_fonts 1
        case '--fontsize-spine-1'
            set processing_fontsize_spine_1 1
        case '--fontsize-spine-2'
            set processing_fontsize_spine_2 1
        case '--fontsize-spine-3'
            set processing_fontsize_spine_3 1
        case '--fontsize-cover-1'
            set processing_fontsize_cover_1 1
        case '--fontsize-cover-2'
            set processing_fontsize_cover_2 1
        case '--fontsize-cover-3'
            set processing_fontsize_cover_3 1
        case '--stroke-width'
            set processing_stroke_width 1
        case '--stroke-color'
            set processing_stroke_color 1
        case '--line-coord-spine'
            set processing_line_coord_spine 1
        case '--line-coord-cover'
            set processing_line_coord_cover 1
        case '--distortion-points-spine'
            set processing_distortion_points_spine 1
        case '--distortion-points-cover'
            set processing_distortion_points_cover 1
        case '--fontsize-banner-1'
            set processing_fontsize_banner_1 1
        case '--fontsize-banner-2'
            set processing_fontsize_banner_2 1
        case '--fontsize-banner-3'
            set processing_fontsize_banner_3 1
        case '--text'
            set processing_text 1
        case '--bc-banner'
            set processing_bc_banner 1
        case '--bc-spine'
            set processing_bc_spine 1
        case '--bc-cover'
            set processing_bc_cover 1
        case '--fc-banner'
            set processing_fc_banner 1
        case '--fc-cover'
            set processing_fc_cover 1
        case '--fc-spine'
            set processing_fc_spine 1
        case '--line-color'
            set processing_line_color 1
        case '--help'
            show_help
            exit 0
        case '*'
            if test $processing_input
                set input_files $input_files $arg
                set processing_input 0
            else if test $processing_output_dir
                set output_dir $arg
                set processing_output_dir 0
            else if test $processing_size_spine
                set size_spine $arg
                set processing_size_spine 0
            else if test $processing_size_cover
                set size_cover $arg
                set processing_size_cover 0
            else if test $processing_size_logo
                set size_logo $arg
                set processing_size_logo 0
            else if test $processing_fonts
                set fonts (string split ',' $arg)
                set processing_fonts 0
            else if test $processing_fontsize_spine_1
                set fontsize_spine_1 $arg
                set processing_fontsize_spine_1 0
            else if test $processing_fontsize_spine_2
                set fontsize_spine_2 $arg
                set processing_fontsize_spine_2 0
            else if test $processing_fontsize_spine_3
                set fontsize_spine_3 $arg
                set processing_fontsize_spine_3 0
            else if test $processing_fontsize_cover_1
                set fontsize_cover_1 $arg
                set processing_fontsize_cover_1 0
            else if test $processing_fontsize_cover_2
                set fontsize_cover_2 $arg
                set processing_fontsize_cover_2 0
            else if test $processing_fontsize_cover_3
                set fontsize_cover_3 $arg
                set processing_fontsize_cover_3 0
            else if test $processing_stroke_width
                set stroke_width $arg
                set processing_stroke_width 0
            else if test $processing_stroke_color
                set stroke_color $arg
                set processing_stroke_color 0
            else if test $processing_line_coord_spine
                set line_coord_spine $arg
                set processing_line_coord_spine 0
            else if test $processing_line_coord_cover
                set line_coord_cover $arg
                set processing_line_coord_cover 0
            else if test $processing_distortion_points_spine
                set distortion_points_spine $arg
                set processing_distortion_points_spine 0
            else if test $processing_distortion_points_cover
                set distortion_points_cover $arg
                set processing_distortion_points_cover 0
            else if test $processing_fontsize_banner_1
                set fontsize_banner_1 $arg
                set processing_fontsize_banner_1 0
            else if test $processing_fontsize_banner_2
                set fontsize_banner_2 $arg
                set processing_fontsize_banner_2 0
            else if test $processing_fontsize_banner_3
                set fontsize_banner_3 $arg
                set processing_fontsize_banner_3 0
            else if test $processing_text
                set text (string split ',' $arg)
                set processing_text 0
            else if test $processing_bc_banner
                set bc_banner $arg
                set processing_bc_banner 0
            else if test $processing_bc_spine
                set bc_spine $arg
                set processing_bc_spine 0
            else if test $processing_bc_cover
                set bc_cover $arg
                set processing_bc_cover 0
            else if test $processing_fc_banner
                set fc_banner $arg
                set processing_fc_banner 0
            else if test $processing_fc_cover
                set fc_cover $arg
                set processing_fc_cover 0
            else if test $processing_fc_spine
                set fc_spine $arg
                set processing_fc_spine 0
            else if test $processing_line_color
                set line_color $arg
                set processing_line_color 0
            end
    end
end

if test -z "$input_files"
    echo "Error: Input files are required."
    show_help
    exit 1
end

if test -z "$output_dir"
    set output_dir "output/(date +%Y%m%dT%H%M%S)"
end

set title (echo $text[1])
set subtitle (echo $text[2])
set author (echo $text[3])
set publisher (echo $text[4])

# Function to create directories
function create_dir
    mkdir -p $argv
end

# Function to generate spine image
function generate_spine_image
    magick convert -size $size_spine xc:$bc_spine \
        -font $argv[1] -fill $fc_spine \
        -pointsize $fontsize_spine_1 -gravity center -annotate +100+0 "$argv[2] $argv[3]" \
        -gravity west -pointsize $fontsize_spine_2 -annotate +270+0 $argv[4] \
        -pointsize $fontsize_spine_3 -annotate +20+0 $argv[5] \
        -stroke $stroke_color -strokewidth $stroke_width -draw "line $line_coord_spine" \
        -rotate -90 \( -size $size_spine gradient:white-transparent -rotate 90 -alpha on -channel a -evaluate subtract 80% +channel \) \
        -gravity west -compose over -composite $argv[6]/box_sp.png
end

# Function to generate front cover
function generate_front_cover
    magick convert -size $size_cover xc:$bc_cover \
        \( $argv[1] -resize $size_logo \) -gravity center -compose over -composite \
        -font $argv[2] -fill $fc_cover -pointsize $fontsize_cover_1 -gravity north -annotate +0+25 $argv[3] \
        -pointsize $fontsize_cover_2 -annotate +0+120 $argv[4] \
        -fill $fc_cover -pointsize $fontsize_cover_2 -gravity northeast -annotate +25+140 $argv[5] \
        -fill $fc_cover -pointsize $fontsize_cover_3 -gravity south -annotate +0+25 $argv[6] \
        -stroke $stroke_color -strokewidth $stroke_width -fill $line_color -draw "line $line_coord_cover" $argv[7]/box_fr.png
end

# Function to distort and merge images
function distort_and_merge_images
    magick convert \( $argv[1]/box_sp.png -virtual-pixel transparent +distort Perspective "$distortion_points_spine" \) \
           \( $argv[1]/box_fr.png -virtual-pixel transparent +distort Perspective "$distortion_points_cover" \) \
           -background $bc_banner -compose over -layers merge +repage -bordercolor $bc_banner -compose over -border 75x10 $argv[1]/box_set.png
end

# Function to generate annotated image
function generate_annotated_image
    magick convert -size 1024x1024 xc:none -font $argv[1] -fill white -gravity northwest \
        -pointsize $fontsize_banner_1 -annotate +50+250 $banner \
        -pointsize $fontsize_banner_1 -annotate +50+300 $banner1 \
        -gravity north -font $argv[2] -pointsize $argv[3] -annotate +50+500 $banner2 \
        -pointsize $argv[3] -annotate +50+600 $banner3 \
        -gravity southwest -font $argv[1] -pointsize $fontsize_banner_3 -annotate +50+300 $banner4 \
        -pointsize $fontsize_banner_3 -annotate +50+100 $banner5 $argv[4]
end

# Function to create banners
function create_banners
    magick convert $argv[1]/box_set.png -gravity west -extent 1820x1024 $argv[1]/temp_banner_h.png
    magick convert $argv[1]/temp_banner_h.png $argv[1]/annotate_image.png -gravity east -composite $argv[1]/banner_h.png

    magick convert $argv[1]/box_set.png -gravity north -extent 1024x1820 $argv[1]/temp_banner_v.png
    magick convert $argv[1]/temp_banner_v.png $argv[1]/annotate_image.png -gravity south -composite $argv[1]/banner_v.png

    magick convert $argv[1]/box_set.png -gravity center -extent 1024x1024 -modulate 30 $argv[1]/temp_banner_o.png
    magick convert $argv[1]/temp_banner_o.png $argv[1]/annotate_image2.png -fill white -gravity center -composite $argv[1]/banner_o.png
end

# Main script execution
set out_dir_created 0

for img in $input_files
    set base (basename $img .png)
    set ts (date +%Y%m%dT%H%M%S)
    set out "$output_dir/$base/$ts"

    if test $out_dir_created -eq 0
        create_dir $out
        set out_dir_created 1
    end

    generate_spine_image $fonts[1] $title $subtitle $author $publisher $out
    generate_front_cover $img $fonts[1] $title $subtitle $author $publisher $out
    distort_and_merge_images $out
    generate_annotated_image $fonts[3] $fonts[2] $fontsize_banner_1 $out/annotate_image.png
    generate_annotated_image $fonts[3] $fonts[2] $fontsize_banner_1 $out/annotate_image2.png
    create_banners $out
end
