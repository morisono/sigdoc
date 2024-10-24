![merged](https://gist.github.com/assets/111455900/037bf4f9-aa5e-4448-b8be-e330ca4e1b34)


```sh
# 画像サイズを統一する x30
  for file in $base_dir/*.png
          convert $file -resize 200x -gravity center $file
  end

# Montageツールを使用して結合
  montage -resize 200x -background black -tile 6x5 -geometry +0+0 masterpieces/*.png -fill gra
y -pointsize 10 -annotate +10+190 %f -pointsize 40 -annotate +160+40 '©' merged.png
```