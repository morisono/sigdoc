## ffmpeg Basic Quick Start Guide
Also check: https://trac.ffmpeg.org/wiki

- init
`set video="path\to\input.mp4"`

- info
`ffmpeg -i video.mp4 -hide_banner`

- convert
`ffmpeg -i INPUT.mp4 OUTPUT.avi`

- convert all
`dir -r -Filter "2021*.mp4" -Name |%{ffmpeg -i "$_" "$_.mp3"}`

- crop
`ffmpeg -i INPUT.mp4 -vf "crop=800:800:560:140" -c:a copy out-800x.mp4`
orig_w=1920
orig_h=1080  
w=800
h=800
x=(1080-800)/2=140
y=(1920-800)/2=560


- resize
`ffmpeg -i INPUT.mp4 -s 300x300 out-300x.mp4`

- rotate
`ffmpeg -i INPUT.mp4 -vf "rotate=-90*PI/180" -scale=300:300 out-v.mp4`

- shrink (=resize ?)
`ffmpeg -i input.mp4 -vf "scale=1280:720" -c:a copy output.mp4`

- compress
`ffmpeg -i input.mp4 -vf scale=1280:-1 -c:v libx264 -preset veryslow -crf 24 output.mp4`
`ffmpeg -i input.mp4 -vcodec libx265 -crf 23 output.mp4`

- fps
`ffmpeg -i INPUT.mp4 -vf "fps=fps=30" out-30fps.mp4`
~~`ffmpeg -r 10 -i INPUT.mp4 out-10fps.mp4`~~

- merge audio (re-encoding)
`ffmpeg -i input.mp4 -i audio.wav -c:v copy -c:a aac output.mp4`

- merge audio (no-encoding)
`ffmpeg -i input.mp4 -i audio.wav -c copy output.mkv`

- replace audio
`ffmpeg -i input.mp4 -i audio.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4`

- (no-audiostream)
`ffmpeg -i audio.wav -i input.mp4 -acodec copy -vcodec copy -f mkv output.mkv`

- remove audio(video only)

- clip thumbnails
`ffmpeg -i input.mp4 -r 1 -f image2 image-%2d.png`

- trim (cut out 10 sec. from 00:01:00)
`ffmpeg -i input.mkv -c:av copy -ss 00:01:00 -t 10 output.mkv`
`ffmpeg -i input.mkv -c:av copy -ss 00:01:00 -to 00:01:10 output.mkv`

`ffmpeg -t 00:04:00 -i input.mp4 -ss 00:00:15 -async 1 output.mp4`

- remove video(audio only)
`ffmpeg -i input.mp4 -vn -acodec copy output.mp3`

- audio volume 
`ffmpeg -i input.mp3 -af 'volume=0.5' output.mp3`
`ffmpeg -i input.mp3 -af "volume=volume=10dB" output.mp3 `

- create gif
`ffmpeg -i input.mkv -s output.gif`

- change aspect
`ffmpeg -i input.mp4 -aspect 16:9 output.mp4`

- add poster image
`ffmpeg -loop 1 -i inputimage.jpg -i inputaudio.mp3 -c:v libx264 -c:a aac -strict experimental -b:a 192k -shortest output.mp4`

- split
`ffmpeg -i input.mp4 -t 00:00:30 -c copy part1.mp4 -ss 00:00:30 -codec copy part2.mp4`

- concat (make join.txt as path list)
```
file "part1.mp4"
file "part2.mp4"
file "part3.mp4"
```

~~`ffmpeg -i "concat：audio1.mp3 | audio2.mp3 | audio3.mp3" -c copy output.mp3`~~

`ffmpeg -f concat -safe 0 -i join.txt -c copy output.mp4`

`ffmpeg -f concat -i file.txt -c copy -fflags +genpts full.mp4`

`ffmpeg-safe 0 -fconcat-i join.txt -c:vcopy-c:acopy-c:scopy-map 0:v-map 0:a-map 0:s? dst`

`ffmpeg -i sample_1.mp4 -i sample_2.mp4 -filter_complex "concat=n=2:v=1:a=1" sample_1_2.mp4`

`ffmpeg -i input0.mp4 -i input1.mp4 -i input2.mp4 -filter_complex "[0:v] [0:a] [1:v] [1:a] [2:v] [2:a] concat=n=3:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" output.mp4`


- captions
`ffmpeg -i input.mp4 -isubtitle.srt -map 0 -map 1 -c copy -c：v libx264 -crf 23 -preset veryfast output.mp4`

- preview
`ffplay input.mp4`

- video speed 
`ffmpeg -i input.mp4 -vf "setpts = 0.5 * PTS" output.mp4`

- audio speed
`ffmpeg -i input.mp4 -filter：a "atempo = 2.0" -vn output.mp4`

- remove meta data
`ffmpeg -i input.mp4 -map_metadata -1 -c:v copy -c:a copy output.mp4`

- generate test video 
`ffmpeg -f lavfi -i testsrc=duration=10:size=1280x720:rate=30 testsrc.mpg`
`ffmpeg -f lavfi -i testsrc=d=5:s=1920x1080:r=24,format=yuv420p -f lavfi -i sine=f=440:b=4 -shortest output.mp4`

- fade in/out 30fr/1sec
`ffmpeg -i sample.mp4 -vf "fade=in:0:30" input.mp4`
`ffmpeg -i sample.mp4 -vf "fade=t=out:st=10:d=1" output.mp4`
    - filter chain
`ffmpeg -i sample.mp4 -filter_complex "fade=in:0:30,fade=out:300:30" sample_fade-in_fade-out.mp4`
    - filter graph (needs link label)
     `ffmpeg -i sample_1.mp4 -vf "fade=in:0:30[a];[a]fade=out:300:30" sample_fade-in_fade-out.mp4`

- screenshot
`ffmpeg -i input.mp4 -map 0:v -ss 00:00:05 -frames:v 1 frame_1.png -map 0:v -ss 00:00:10 -frames:v 1 frame_2.png`

- keep quality
`ffmpeg -i input.mp4 -c:v libx264 output.mp4 `

- horizontal flip
`ffmpeg -i input.mp4 -vf "hflip" output.mp4`

- insert black at last
`ffmpeg -i input.mp3 -af "apad=packet_size=4096:pad_dur=2" output.mp3`

- binary 
ffmpeg -i input.mp4 -vf "hue=s=0" output.mp4

- blend
`ffmpeg -i input1.mp4 -i input2.mp4 -filter_complex "blend=difference" output.mp4`

- loop ( 1m = 30fps*60s = 1500fr)
`ffmpeg -i input.mp4 -filter_complex "loop=loop=10:size=1500:start=1500" -pix_fmt yuv420p output.mp4`
`ffmpeg -i input.mp4 -i input.mp4 -i input.mp4 -filter_complex "concat=n=3:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" output.mp4`


- side-by-side
- Holizontal Align 2
    - 16:9
    - preview
`ffmpeg -i input1.mp4 -i input2.mp4 -filter_complex "color=s=hd1080 [base];[0] setpts=PTS-STARTPTS, scale=960:-1 [left];[1] setpts=PTS-STARTPTS, scale=960:-1 [right];[base][left] overlay=0:h/2:shortest=1 [wh2];[wh2][right] overlay=w:h/2:shortest=1" -f matroska - | ffplay -i -`

    - encode
`ffmpeg -i input1.mp4 -i input2.mp4 -filter_complex "color=s=hd1080 [base];[0] setpts=PTS-STARTPTS, scale=960:-1 [left];[1] setpts=PTS-STARTPTS, scale=960:-1 [right];[base][left] overlay=0:h/2:shortest=1 [wh2];[wh2][right] overlay=w:h/2:shortest=1" -movflags +faststart -pix_fmt yuv420p -c:v libx264 -crf 20 "output.mp4"`

    - 4:3
    - preview
`ffmpeg -i input1.mp4 -i input2.mp4 -filter_complex "color=s=hd1080 [back_color];[0] setpts=PTS-STARTPTS, scale=960:-1 [left];[1] setpts=PTS-STARTPTS, scale=960:-1 [right];[back_color][left] overlay=0:h/4:shortest=1 [wh4];[wh4][right] overlay=w:h/4:shortest=1" -f matroska - | ffplay -i -`

    - encode
`ffmpeg -i input1.mp4 -i input2.mp4 -filter_complex "color=s=hd1080 [back_color];[0] setpts=PTS-STARTPTS, scale=960:-1 [left];[1] setpts=PTS-STARTPTS, scale=960:-1 [right];[back_color][left] overlay=0:h/4:shortest=1 [wh4];[wh4][right] overlay=w:h/4:shortest=1" -movflags +faststart -pix_fmt yuv420p -c:v libx264 -crf 20 "output.mp4"`


- Holizontal Align 3
    - preview
`ffmpeg -i input1.mp4 -i input2.mp4 -i input3.mp4 -filter_complex "color=s=hd1080 [back_color];[0] setpts=PTS-STARTPTS, scale=640:-1 [left];[1] setpts=PTS-STARTPTS, scale=640:-1 [middle];[2] setpts=PTS-STARTPTS, scale=640:-1 [right];[back_color][left] overlay=0:h:shortest=1 [w];[w][middle] overlay=w:h:shortest=1[w2];[w2][right] overlay=w*2:h:shortest=1" -f matroska - | ffplay -i -`

    - encode
`ffmpeg -i input1.mp4 -i input2.mp4 -i input3.mp4 -filter_complex "color=s=hd1080 [back_color];[0] setpts=PTS-STARTPTS, scale=640:-1 [left];[1] setpts=PTS-STARTPTS, scale=640:-1[middle];[2] setpts=PTS-STARTPTS, scale=640:-1 [right];[back_color][left] overlay=0:h/1.6:shortest=1 [w];[w][middle] overlay=w:h/1.6:shortest=1[w2];[w2][right] overlay=w*2:h/1.6:shortest=1" -f matroska - | ffplay -i -`

- Holizontal Align 4

- Vertical Align 2
`ffmpeg -i sample_1.mp4  -i sample_2.mp4 -filter_complex "[0:0]pad=iw:2*ih[a];[a][1:0]overlay=0:h" overlay.mp4`

- watermark
`ffmpeg -y -i $video -i $watermark -filter_complex "overlay=x=main_w-overlay_w-(main_w*0.01):y=main_h-overlay_h-(main_h*0.01)" -loglevel fatal out.mov`

- voice emulate(flitevox/flitelib)
    - install 
```
$ git clone https://github.com/festvox/flite.git
$ cd flite/
$ ./configure
$ make
$ sudo make install
```

    - enable
    `./configure --disable-indevs --enable-libflite --enable-cross-compile`

- sound (2000hz, 10s)
` ffmpeg -f lavfi -i "sine=frequency=2000:duration=10" output.mp3`

- change pitch/sample rate
`ffmpeg -i input.mp3 -af "asetrate=44100*0.5" output.mp3 `

- crossfade
`ffmpeg -i input1.mp3 -i input2.mp3 -filter_complex "acrossfade=duration=00:00:01:curve1=exp:curve2=exp" output.mp3`

- picture in picture
`ffmpeg -i sample_1.mp4  -i sample_2.mp4 -filter_complex"[1:0]scale=iw/2:ih/2[red];[0:0][red]overlay" -map 1:1 overlay.mp4`

- split 5
`ffmpeg -i input0.mp4 -i input1.mp4 -i input2.mp4 -i input3.mp4 -i input4.mp4 -filter_complex "[0]scale=-1:720[v0];[1]scale=-1:360[v1];[2]scale=-1:360[v2];[3]scale=-1:360[v3];[4]scale=-1:360[v4];[v0][v1][v2][v3][v4]xstack=inputs=5:layout=0_0|w0_0|w0+w1_0|w0_h1|w0+w1_h1[v]" -map "[v]" output.mp4`

- split 100 (10x10.sh, depend. ffmpeg,ffprobe,perl,seq)

```
ffmpeg -i "$1" -filter_complex '[0:a]asplit=100'`seq -s '' -f '[a%02g]' 0 99`';[0:v]scale=192:-1,split=100'`seq -s '' -f '[v%02g]' 0 99`';'`ffprobe "$1" -hide_banner -show_entries format=duration | perl -ne 'next if not m{^duration=(.*)$}; printf q([v%1$02d]trim=%2$f:%3$f,setpts=PTS-STARTPTS[v%1$02d];[a%1$02d]atrim=%2$f:%3$f,asetpts=PTS-STARTPTS[a%1$02d];), $_, $1*$_/100, $1*($_+1)/100 for (00 .. 99);'``seq -s '' -f '[v%02g]' 0 99`'xstack=inputs=100:layout='"`perl -e 'for $y (0 .. $ARGV[1] - 1) { $h = ($y ? qq($h+h0) : 0); for $x (0 .. $ARGV[0] - 1) { $w = ($x ? qq($w+w0) : 0); push @o, qq(${w}_$h) } } END { print join q(|), @o }' 10 10`"':shortest=1[v];'`seq -s '' -f '[a%02g]' 0 99`'amix=inputs=100:duration=shortest,loudnorm[a]' -map '[v]' -map '[a]' -shortest output.mp4 -y
```

`ffmpeg -i $video -loop 1 -i $image -filter_complex "[1]format=yuva420p,lut=a='val*0.9',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1[a];[0][a] overlay=(W-w)/2:(H-h)/2:shortest=1" out.mov`

- subtitle
`set x=filename; echo %x%.mp4 -vf "subtitles=%x%.srt" %x%.mp4`
`ffmpeg -i input.mp4 -vf "subtitles=subtitle.srt:force_style='FontName=Helvetica,FontSize=24'" out.mp4`

- subtitle manually
`
ffmpeg -i input.mp4 -i subtitle-eng.srt -i subtitle-jpn.srt \
  -map 0:v -map 0:a -map 1 -map 2 \
  -metadata:s:s:0 language=eng \
  -metadata:s:s:1 language=jpn \
  -c:v copy -c:a copy -c:s srt \
  multi-lang-subtitle.mkv
`

- HD to mobile
`ffmpeg -i ./HD.mov -vcodec libx264 -r 19 -b 120k -s 480x270 ./h264_480x270_r19_b120.mp4`

- Make a Null video
`ffmpeg -f lavfi -i color=black:s=3840x2160:r=24000/1001 -f lavfi -i anullsrc \
       -ar 48000 -ac 2 -t 5 empty4k5s.mp4`

