
set sw 1920
set sh 1080
set size '1920x1080'
set sc red
set strw 10
set phw 2275x1280
set phw 1920x1080
set phq 900x1280
set phq 960x1080
set phm 720x1280
set phm 607x1080
set ciw 2.39



# fr
mkdir fr_$strw
cat ../color/colorlist | while read c;
  convert -size 1920x1080 xc:none -stroke $c -strokewidth $strw -fill transparent -draw "rectangle 0,0 1920,1080" fr_$strw/$c.png;
end

# fr rr
mkdir fr_rr_$strw
cat ../color/colorlist | while read c;
  convert -size 1920x1080 xc:$c -fill '#333' -draw "roundrectangle 100,100 1820,980,200,200" fr_rr_$strw/$c.png
end

# fr sq rr
mkdir fr_sq_rr_$strw
cat ../color/colorlist | while read c;
  convert -size 800x800 xc:$c -fill '#333' -draw "roundrectangle 50,50 750,750,100,100" fr_sq_rr_$strw/$c.png
end

# fr rr mob
mkdir fr_rr_mob_$strw
cat ../color/colorlist | while read c;
  convert -size 720x1280 xc:$c -fill '#333' -draw "roundrectangle 50,50 670,1230,100,100" fr_rr_mob_$strw/$c.png
end

# fr sq
mkdir fr_sq_$strw
cat ../color/colorlist | while read c
  convert -size 800x800 xc:none -stroke $c -strokewidth $strw -fill transparent -gravity center -draw "rectangle 0,0,800,800" fr_sq_$strw/$c.png
end

# fr mob
mkdir fr_mob_$strw
cat ../color/colorlist | while read c
  convert -size 720x1280 xc:none -stroke $c -strokewidth $strw -fill transparent -gravity center -draw "rectangle 0,0,720,1280" fr_mob_$strw/$c.png
end

# fr r
mkdir fr_r_$strw
cat ../color/colorlist | while read c
    convert -size 800x800 xc:none -stroke $c -strokewidth $strw -fill transparent -gravity center -draw "circle 400,400 100,0" fr_r_$strw/$c.png
end
# photo wide
mkdir ph_wide_$phw
cat ../color/colorlist | while read c
  convert -size 2275x1280 xc:none -stroke $c -strokewidth 50 -fill transparent -gravity center -draw "rectangle 0,0,2275,1280" -fill $c -draw "rectangle 0,880,2275,1280" ph_wide_$phw/$c.png
end

# photo wide rr
mkdir ph_wide_rr
cat ../color/colorlist | while read c
    convert -size 1920x1080 xc:none -stroke $c -strokewidth 25 -fill transparent -draw "rectangle 0,0,1920,1080" -strokewidth 50 -fill transparent -gravity center -draw "roundrectangle  0,0 1920,960,50,50" -fill $c -draw "rectangle 0,960,1920,1080" ph_wide_rr/$c.png
end

# photo square
mkdir ph_sq_$phq
cat ../color/colorlist | while read c
    convert -size 960x1080 xc:none -stroke $c -strokewidth 50 -fill transparent -gravity center -draw "rectangle 0,0,960,960" -fill $c -draw "rectangle 0,880,960,1080" ph_sq_$phq/$c.png
end

# photo square rr
mkdir ph_sq_rr_$phq
cat ../color/colorlist | while read c
    convert -size 960x1080 xc:none -stroke $c -strokewidth 25 -fill transparent -draw "rectangle 0,0,960,1080" -strokewidth 50 -fill transparent -gravity center -draw "roundrectangle  0,0 960,960,50,50" -fill $c -draw "rectangle 0,960,960,1080" ph_sq_rr_$phq/$c.png
end

# photo mini
mkdir ph_mini_$phm
cat ../color/colorlist | while read c
  convert -size 607x1080 xc:none -stroke $c -strokewidth 50 -fill transparent -gravity center -draw "rectangle 0,0,607,1080" -fill $c -draw "rectangle 0,880,607,1080" ph_mini_$phm/$c.png
end


# cinema frame 2.39:1
mkdir ci_$ciw
cat ../color/colorlist | while read c
  convert -size 1920x1080 xc:none -fill $c -draw "rectangle 0,0,1920,140" -fill $c -draw "rectangle 0,940,1920,1080" ci_$ciw/$c.png
end
# cinema frame 2.35:1
mkdir ci_$ciw
cat ../color/colorlist | while read c
  convert -size 1920x1080 xc:none -fill $c -draw "rectangle 0,0,1920,132" -fill $c -draw "rectangle 0,948,1920,1080" ci_$ciw/$c.png
end
# cinema frame 2:1
ls ci_50/ | while read f
    magick ci_50/$f $f.svg
end

# convert png to svg
set dir ci_2.35
set dir_to {$dir}_svg
mkdir $dir_to
find $dir | while read f
  magick $f $f.pnm
  potrace -s -o $dir_to/$f.svg $f.pnm
  rm $f.pnm
end
# Alternate command:

find $dir | while read f
  magick $f pnm:- | potrace -s -o $f.svg
end

# montage
montage ph_mini/* -background none -geometry +0+0 montage_mini.png

# ph kbs
spline -s kbs -t 0.6 -e close -d 1920x1080 -c black -i black -sw 2 "100,50 100,910 1820,910 1820,50" ph_kbs_0.png

# ph bspline
spline -s bspline -t 0.6 -e close -d 1920x1080 -c black -i black -sw 2 "5,5 5,1075 1915,1075 1915,5" ph_bspline_2.png

# ph aapl
convert ph_sq_bl.png icon_910x.png -geometry +0+50 -gravity north -compose over -composite output.png
convert ph_aapl.n.png -fuzz 95% -fill none -opaque white ph_aapl_white.png
cat ../color/colorlist | while read c
    convert ph_aapl_white.png -fill $c -colorize 100 tmp/ph_aapl_$c.png
end
montage ph_aapl/* -background none -geometry +0+0 -tile x1 seq_aapl.png
convert -rotate 90 -append $(yes ph_aapl_center.png | head -n 9) tmp1.png


# shoten

# set mask ../ph_mini_607x1080/black.png
cat list.csv | while IFS=',' read mask path name desc
    convert "$path" -resize 607^x1080 -gravity north -crop 607x1080+0+0 "out-$path"
    convert out-$path $mask -compose over -composite out_$path
    convert -fill white -stroke black -strokewidth 1 -font 'Noto-Sans-JP-Bold' -gravity south \
     -pointsize 50 -annotate +0+150 $name \
     -pointsize 40 -annotate +0+100 $desc out_$path out$path
    rm out-$path out_$path
end
for i in (seq 1 12)
    set files $files "out$i.jpg"
end
convert $files +append merged.jpg
set --erase files

# frame
montage -geometry +0 -background black $(yes bicolor.png | head -n 28) -tile 4x mobile.png
montage -geometry +0 -background none $(yes 760x/bicolor.png | head -n 75) -tile 15x5 xd75.png