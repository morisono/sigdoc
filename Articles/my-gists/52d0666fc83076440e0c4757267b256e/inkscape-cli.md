```sh
alias inkscape='/mnt/c/Program\ Files/Inkscape/bin/inkscape.com'

# add rect before <defs>
for f in *.svg; sed -i '0,/<defs/s/<defs/<rect width="100%" height="100%" fill="#ffffff" fill-opacity="0" \/>\n <defs/' $f; end

# convert
inkscape monolith.svg -D --export-filename=monolith.png

# 


```