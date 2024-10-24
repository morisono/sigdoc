import ffmpeg
import ffmpeg


def preview_with_logo(in_file, image):
    (
        ffmpeg
        .input(in_file)
        .input(image, loop=1)
        .output('-', vf='format=yuva420p,lut=a=\'val*0.9\',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1', f='matroska')
        .run(cmd='ffplay', input='-')
    )

def preview_with_logo_gif(in_file, gif_file):
    (
        ffmpeg
        .input(in_file)
        .input(gif_file, ignore_loop=0)
        .output('-', vf='format=yuva420p,lut=a=\'val*0.9\',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1', f='matroska')
        .run(cmd='ffplay', input='-')
    )


def overlay_logo_bottom_left(in_file, image, out_file):
    (
        ffmpeg
        .input(in_file)
        .input(image)
        .output(out_file, vf='overlay=x=main_w*0.01:y=main_h-overlay_h-(main_h*0.01)', loglevel='fatal')
        .run()
    )

def overlay_logo_bottom_left_complex(in_file, image, out_file):
    (
        ffmpeg
        .input(in_file)
        .input(image, loop=1)
        .output(out_file, vf='overlay=x=main_w*0.01:y=main_h-overlay_h-(main_h*0.01)', loglevel='fatal')
        .run()
    )

def overlay_logo_center(in_file, image, out_file):
    (
        ffmpeg
        .input(in_file)
        .input(image, loop=1)
        .output(out_file, vf='overlay=(W-w)/2:(H-h)/2:shortest=1', loglevel='fatal')
        .run()
    )

def overlay_logo_with_gif(in_file, gif_file, out_file):
    (
        ffmpeg
        .input(in_file)
        .input(gif_file, ignore_loop=0)
        .output(out_file, vf='format=yuva420p,lut=a=\'val*0.9\',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1', movflags='+faststart', pix_fmt='yuv420p', c='libx264', crf=20)
        .run()
    )

def overlay_logo_with_gif_preview(in_file, gif_file):
    (
        ffmpeg
        .input(in_file)
        .input(gif_file, ignore_loop=0)
        .output('-', vf='format=yuva420p,lut=a=\'val*0.9\',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1')
        .run(cmd='ffplay', input='-')
    )

def overlay_video_with_text(in_file, image, out_file):
    (
        ffmpeg
        .input(in_file)
        .input(image)
        .output(out_file, vf='overlay=10:10,drawtext=text=\'Hello World\'')
        .output(out_file, acodec='copy', movflags='+faststart')
        .run()
    )

def overlay_logo_with_enable(in_file, image, out_file):
    (
        ffmpeg
        .input(in_file)
        .input(image)
        .output(out_file, vf='overlay=10:10:enable=between(t,0,30)', acodec='copy')
        .run()
    )


def encode_with_logo(in_file, image, out_file):
    (
        ffmpeg
        .input(in_file)
        .input(image, loop=1)
        .output(out_file, vf='format=yuva420p,lut=a=\'val*0.9\',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1', movflags='+faststart', pix_fmt='yuv420p', c='libx264', crf=20)
        .run()
    )

def encode_with_logo_gif(in_file, gif_file, out_file):
    (
        ffmpeg
        .input(in_file)
        .input(gif_file, ignore_loop=0)
        .output(out_file, vf='format=yuva420p,lut=a=\'val*0.9\',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1', movflags='+faststart', pix_fmt='yuv420p', c='libx264', crf=20)
        .run()
    )

def encode_with_logo_center(in_file, image, out_file):
    (
        ffmpeg
        .input(in_file)
        .input(image, loop=1)
        .output(out_file, vf='overlay=y=(H-h):shortest=1', movflags='+faststart', pix_fmt='yuv420p', c='libx264', crf=20, loglevel='fatal')
        .run()
    )

def encode_with_logo_random_position(in_file, image, out_file):
    (
        ffmpeg
        .input(in_file)
        .input(image, loop=1)
        .output(out_file, vf='overlay=shortest=1:x=if(eq(mod(n,200),0),sin(random(1))*W,x):y=if(eq(mod(n,200),0),sin(random(1))*H,y)', movflags='+faststart', pix_fmt='yuv420p', c='libx264', crf=20, loglevel='fatal')
        .run()
    )

def encode_with_logo_gif_random_position(in_file, gif_file, out_file):
    (
        ffmpeg
        .input(in_file)
        .input(gif_file, ignore_loop=0)
        .output(out_file, vf='format=yuva420p,lut=a=\'val*0.9\',fade=in:st=1:d=2:alpha=1,fade=out:st=7:d=2:alpha=1', movflags='+faststart', pix_fmt='yuv420p', c='libx264', crf=20, loglevel='fatal')
        .run()
    )


def add_text_overlay(in_file, font, text, font_color, font_size, box_color, box_opacity, out_file):
    (
        ffmpeg
        .input(in_file)
        .output(out_file, vf=f'drawtext=fontfile={font}:text={text}:fontcolor={font_color}:fontsize={font_size}:box=1:boxcolor={box_color}@{box_opacity}:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2')
        .output(out_file, acodec='copy')
        .run()
    )

def add_text_overlay_simple(in_file, text, out_file):
    (
        ffmpeg
        .input(in_file)
        .output(out_file, vf='drawtext=text=\'FFmpeg is the best\'')
        .output(out_file, acodec='copy')
        .run()
    )

def add_random_text_overlay(in_file, font, font_size, font_color, text, out_file):
    (
        ffmpeg
        .input(in_file)
        .output(out_file, vf=f'drawtext=fontfile={font}:fontsize={font_size}:fontcolor={font_color}@0.5:text={text}:x=if(eq(mod(t,30),0),rand(0,(W-tw)),x):y=if(eq(mod(t,30),0),rand(0,(H-th)),y)')
        .output(out_file, c='libx264', crf=23, acodec='copy')
        .run()
    )

def add_random_text_overlay_encode(in_file, font, font_size, font_color, text, out_file):
    (
        ffmpeg
        .input(in_file, framerate='30000/1001')
        .input('test.png', loop=1)
        .output(out_file, vf='fade=out:st=30:d=1:alpha=1[ov];[0:v][ov]overlay=10:10[v]', acodec='copy', shortest=None)
        .run()
    )


def apply_watermark_and_effects(in_file, image, sub, out_file):
    (
        ffmpeg
        .input(in_file)
        .output(image, vf=f'fade=in:0:20,subtitles={sub}')
        .output(out_file, vf=f'overlay=W-w-10:H-h-10,fade=in:0:20')
        .output(out_file, vf='format=yuv420p', crf=18, preset='slow', c='aac', strict='-2')
        .run()
    )

def apply_watermark_and_effects_complex(in_file, image, sub, out_file):
    (
        ffmpeg
        .input(in_file)
        .output(image, vf='fade=0:1:alpha=1,setpts=PTS+N/TB')
        .output(out_file, vf=f'overlay=W-w-10:H-h-10,fade=in:0:20,subtitles={sub}')
        .output(out_file, vf='format=yuv420p', crf=18, preset='slow', c='aac')
        .run()
    )

def apply_watermark_and_effects(in_file, image, sub, out_file):
    (
        ffmpeg
        .input(in_file)
        .output(out_file, vf=f'overlay=W-w-10:H-h-10,fade=in:0:20[tmp_overlay];[tmp_overlay]subtitles={sub}')
        .output(out_file, codec='libx264', crf=18, preset='slow', pix_fmt='yuv420p', c='aac', strict='-2')
        .run()
    )

def apply_watermark_and_effects_complex(in_file, image, sub, out_file):
    (
        ffmpeg
        .input(in_file)
        .output(out_file, loop=1, t=2, vf='fade=0:1:alpha=1,setpts=PTS+N/TB[wm];[0:v][wm]overlay=W-w-10:H-h-10,fade=in:0:20,subtitles=' + sub)
        .output(out_file, codec='libx264', crf=18, preset='slow', c='aac')
        .run()
    )
