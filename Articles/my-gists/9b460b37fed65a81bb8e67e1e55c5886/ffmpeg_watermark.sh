

# $inに透かしロゴ($image)をオーバーレイし、フェードイン/アウトと字幕($sub)を適用して$outを作成する
ffmpeg -y -i $in -i $image -lavfi "[0:v]overlay=W-w-10:H-h-10,fade=in:0:20[tmp_overlay]; [tmp_overlay]subtitles=$sub[out]" -map [out] -map 0:a -codec:v libx264 -crf 18 -preset slow -pix_fmt yuv420p -c:a aac -strict -2 $out

# $inに透かしロゴ($image)をオーバーレイし、フェードイン/アウトと字幕($sub)を適用して$outを作成する (filter_complexを使用)
ffmpeg -y -i $in -loop 1 -t 2 -i $image -filter_complex "[1]fade=0:1:alpha=1,setpts=PTS+N/TB[wm]; [0:v][wm]overlay=W-w-10:H-h-10,fade=in:0:20,subtitles=$sub[out]" -map [out] -map 0:a -c:v libx264 -crf 18 -preset slow -c:a aac $out

# $inにテキストオーバーレイを追加して$outを作成する
ffmpeg -i $in -vf "drawtext=fontfile=$font:text=$text:fontcolor=$fc:fontsize=$font_z:box=1:boxcolor=$bv@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2" -codec:a copy $out

# $inと$imageを合成し、オーバーレイにテキストを追加して$outを作成する
ffmpeg -i $in -i $image -lavfi "[0:v][1:v]overlay=10:10,drawtext=text='Hello World'" -c:a copy -movflags +faststart $out

# $inにテキストオーバーレイを追加して$outを作成する
ffmpeg -i $in -vf "drawtext=text='FFmpeg is the best'" -c:a copy $out

# ビデオとイメージを合成し、オーバーレイ位置を左下に指定して$outを作成する
ffmpeg -y -i $in -i $image -lavfi "overlay=x=main_w*0.01:y=main_h-overlay_h-(main_h*0.01)" -loglevel fatal $out

# $inに透明なループ再生ロゴをオーバーレイし、フェードイン/アウトを適用してプレビューする
ffmpeg -i $in -loop 1 -i $image -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1[a];[0][a]overlay=(W-w)/2:(H-h)/2:shortest=1" -f matroska - | ffplay -i -

# $inに透明なループ再生ロゴをオーバーレイし、フェードイン/アウトを適用して$outをエンコードする
ffmpeg -i $in -loop 1 -i $image -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1[a];[0][a]overlay=(W-w)/2:(H-h)/2:shortest=1" -movflags +faststart -pix_fmt yuv420p -c:v libx264 -crf 20 $out

# $inに透明なループ再生ロゴgifをオーバーレイし、フェードイン/アウトを適用してプレビューする
ffmpeg -i $in -ignore_loop 0 -i logo.gif -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1[a];[0][a]overlay=(W-w)/2:(H-h)/2:shortest=1" -f matroska - | ffplay -i -

# $inに透明なループ再生ロゴgifをオーバーレイし、フェードイン/アウトを適用して$outをエンコードする
ffmpeg -i $in -ignore_loop 0 -i logo.gif -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1[a];[0][a]overlay=(W-w)/2:(H-h)/2:shortest=1" -movflags +faststart -pix_fmt yuv420p -c:v libx264 -crf 20 $out

# $inにテキストオーバーレイを追加し、テキストの位置をランダムに変更して$outをエンコードする
ffmpeg -i $in -vf "drawtext=fontfile=$font:fontsize=$font_z:fontcolor=$fc@0.5:text=$text:x=if(eq(mod(t\,30)\,0)\,rand(0\,(W-tw))\,x):y=if(eq(mod(t\,30)\,0)\,rand(0\,(H-th))\,y)" -c:v libx264 -crf 23 -c:a copy $out

# $inに透かしロゴ($image)をオーバーレイし、フェードイン/アウトと字幕($sub)を適用し、左下に配置して$outを作成する
ffmpeg -i $in -loop 1 -i $image -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=0:d=3:alpha=1,fade=out:st=60:d=3:alpha=1[a];[0][a]overlay=x=main_w*0.01:y=main_h-overlay_h-(main_h*0.01)" -loglevel fatal $out

# $inに透かしロゴ($image)をオーバーレイし、フェードイン/アウトを適用し、中央に配置して$outを作成する
ffmpeg -i $in -loop 1 -i $image -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=0:d=3:alpha=1,fade=out:st=7:d=5:alpha=1[a];[0][a]overlay=(W-w)/2:(H-h)/2:shortest=1" -loglevel fatal $out

# $inに透かしロゴ($image)をオーバーレイし、フェードイン/アウトを適用し、中央に配置して$outをエンコードする
ffmpeg -i $in -i $image -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=1:d=2:alpha=1[a];[0][a]overlay=y=(H-h):shortest=1" -movflags +faststart -pix_fmt yuv420p -c:v libx264 -crf 20 -loglevel fatal $out

# $inに透かしロゴ($image)をオーバーレイし、フェードイン/アウトを適用し、ランダムな位置に配置して$outをエンコードする
ffmpeg -y -i $in -loop 1 -i $image -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=1:d=2:alpha=1[a];[0][a]overlay=shortest=1:x=if(eq(mod(n\,200)\,0)\,sin(random(1))*W\,x):y=if(eq(mod(n\,200)\,0)\,sin(random(1))*H\,y)" -movflags +faststart -pix_fmt yuv420p -c:v libx264 -crf 20 -loglevel fatal $out

# $inに透かしロゴ($image)をオーバーレイし、フェードイン/アウトを適用し、左下に配置して$outを作成する
ffmpeg -loglevel fatal -i $in -loop 1 -i $image -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=1:d=2:alpha=1,fade=out:st=60:d=2:alpha=1[a];[0][a]overlay=10:(H-h)-10:shortest=1" -movflags +faststart -pix_fmt yuv420p -c:v libx264 -crf 20 $out

# $inに透明なループ再生ロゴをオーバーレイし、フェードイン/アウトを適用し、最速の再生を持つ$outをエンコードする
ffmpeg -y -i $in -loop 1 -i $image -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=1:d=2:alpha=1[a];[0][a]overlay=y=(H-h):shortest=1" -movflags +faststart -pix_fmt yuv420p -c:v libx264 -crf 20 -loglevel fatal $out

# $inに透かしロゴ($image)をオーバーレイし、フェードイン/アウトを適用し、ランダムな位置に配置して$outをエンコードする
ffmpeg -y -i $in -loop 1 -i $image -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=1:d=2:alpha=1[a];[0][a]overlay=shortest=1:x=if(eq(mod(n\,200)\,0)\,sin(random(1))*W\,x):y=if(eq(mod(n\,200)\,0)\,sin(random(1))*H\,y)" -movflags +faststart -pix_fmt yuv420p -c:v libx264 -crf 20 -loglevel fatal $out

# $inに透明なループ再生ロゴgifをオーバーレイし、フェードイン/アウトを適用し、最速の再生を持つ$outをエンコードする
ffmpeg -y -i $in -ignore_loop 0 -i logo.gif -lavfi "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1[a];[0][a]overlay=(W-w)/2:(H-h)/2:shortest=1" -movflags +faststart -pix_fmt yuv420p -c:v libx264 -crf 20 -loglevel fatal $out

# $inにテキストオーバーレイを追加し、テキストの位置をランダムに変更し、最速の再生を持つ$outをエンコードする
ffmpeg -i $in -framerate 30000/1001 -loop 1 -i $image -filter_complex "[1:v]fade=out:st=30:d=1:alpha=1[ov];[0:v][ov]overlay=10:10[v]" -map "[v]" -map 0:a -c:v libx264 -c:a copy -shortest $out

# $inに透明なループ再生ロゴをオーバーレイし、フェードイン/アウトを適用し、最速の再生を持つ$outをエンコードする
ffmpeg -i $in -loop 1 -i $image -lavfi "[1:v]overlay=10:10:enable=between