import ffmpeg

def init(video):
    ffmpeg.input(video)


def info(video):
    ffmpeg.input(video).output("-hide_banner").run()


def convert(input_file, output_file):
    ffmpeg.input(input_file).output(output_file).run()


def convert_all(input_directory, output_directory, pattern):
    ffmpeg.input(f'{input_directory}/{pattern}', pattern_type='glob').output(f'{output_directory}/%filename%.mp3').run()


def crop(input_file, output_file, width, height, x, y):
    ffmpeg.input(input_file).filter('crop', width, height, x, y).output(output_file, c='copy').run()


def resize(input_file, output_file, width, height):
    ffmpeg.input(input_file).output(output_file, s=f'{width}x{height}').run()


def rotate(input_file, output_file, angle, scale):
    ffmpeg.input(input_file).filter('rotate', angle).output(output_file, vf=f'scale={scale}').run()


def shrink(input_file, output_file, width, height):
    ffmpeg.input(input_file).output(output_file, vf=f'scale={width}:{height}', c='copy').run()


def compress(input_file, output_file, crf):
    ffmpeg.input(input_file).output(output_file, vf='scale=1280:-1', vcodec='libx264', preset='veryslow', crf=crf).run()


def fps(input_file, output_file, fps):
    ffmpeg.input(input_file).output(output_file, vf=f'fps=fps={fps}').run()


def merge_audio(input_video, input_audio, output_file):
    ffmpeg.input(input_video).input(input_audio).output(output_file, c='copy', shortest=None).run()


def merge_audio_no_encoding(input_video, input_audio, output_file):
    ffmpeg.input(input_video).input(input_audio).output(output_file, c='copy').run()


def replace_audio(input_video, input_audio, output_file):
    ffmpeg.input(input_video).input(input_audio).output(output_file, c='copy', map='0:v:0', map='1:a:0').run()


def remove_audio(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, an=None, vcodec='copy').run()


def clip_thumbnails(input_file, output_pattern):
    ffmpeg.input(input_file).output(output_pattern, vf='fps=1').run()


def trim(input_file, output_file, start_time, end_time):
    ffmpeg.input(input_file).output(output_file, c='copy', ss=start_time, to=end_time).run()


def remove_video(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, vn=None, acodec='copy').run()


def audio_volume(input_file, output_file, volume):
    ffmpeg.input(input_file).output(output_file, af=f'volume={volume}').run()


def create_gif(input_file, output_file):
    ffmpeg.input(input_file).output(output_file).run()


def change_aspect_ratio(input_file, output_file, aspect_ratio):
    ffmpeg.input(input_file).output(output_file, aspect=aspect_ratio).run()


def add_poster_image(input_image, input_audio, output_file):
    ffmpeg.input(input_image, loop=1).input(input_audio).output(output_file, c='copy', shortest=None).run()


def split(input_file, output_files, durations):
    in_stream = ffmpeg.input(input_file)
    outputs = []
    for i, duration in enumerate(durations):
        outputs.append(in_stream.output(output_files[i], c='copy', t=duration))

    ffmpeg.merge_outputs(*outputs).run()


def concat(input_files, output_file):
    inputs = [ffmpeg.input(file) for file in input_files]
    ffmpeg.concat(*inputs).output(output_file, c='copy').run()

    

def captions(input_file, subtitle_file, output_file):
    ffmpeg.input(input_file).output(output_file, srt=subtitle_file, c='copy', vcodec='libx264', crf=23, preset='veryfast').run()


def preview(input_file):
    ffmpeg.input(input_file).output("-").run(overwrite_output=True)


def video_speed(input_file, output_file, speed):
    ffmpeg.input(input_file).output(output_file, vf=f"setpts={speed}*PTS").run()


def audio_speed(input_file, output_file, speed):
    ffmpeg.input(input_file).output(output_file, af=f"atempo={speed}", vn=None).run()


def remove_meta_data(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, map_metadata='-1', c='copy').run()


def generate_test_video(output_file, duration, size, rate):
    ffmpeg.input('testsrc', f'duration={duration}', f'size={size}', f'rate={rate}').output(output_file).run()


def fade(input_file, output_file, fade_in_duration, fade_out_duration):
    ffmpeg.input(input_file).output(output_file, vf=f"fade=in:0:{fade_in_duration},fade=out:st=10:d={fade_out_duration}").run()


def screenshot(input_file, timestamps, output_prefix):
    for i, timestamp in enumerate(timestamps):
        output_file = f"{output_prefix}_{i+1}.png"
        ffmpeg.input(input_file).output(output_file, ss=timestamp, vframes=1).run()


def keep_quality(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, c='copy', vcodec='libx264').run()


def horizontal_flip(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, vf='hflip').run()


def insert_black_last(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, af='apad=packet_size=4096:pad_dur=2').run()
    


def binary(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, vf='hue=s=0').run()


def blend(input_file1, input_file2, output_file):
    ffmpeg.input(input_file1).input(input_file2).output(output_file, filter_complex='blend=difference').run()


def loop(input_file, loop_count, output_file):
    ffmpeg.input(input_file).output(output_file, filter_complex=f'loop=loop={loop_count}:size=1500:start=1500', pix_fmt='yuv420p').run()


def side_by_side(input_file1, input_file2, output_file, alignment='horizontal', aspect_ratio='16:9'):
    if alignment == 'horizontal':
        scale = '960:-1'
        overlay = 'overlay=0:h/2:shortest=1 [wh2];[wh2][right] overlay=w:h/2:shortest=1'
    elif alignment == 'vertical':
        scale = '-1:540'
        overlay = 'overlay=w/2:0:shortest=1 [wh2];[wh2][right] overlay=w/2:h:shortest=1'

    if aspect_ratio == '16:9':
        base_size = 'hd1080'
    elif aspect_ratio == '4:3':
        base_size = 'hd1080'

    ffmpeg.input(input_file1).input(input_file2).output(output_file, filter_complex=f"color=s={base_size} [base];[0] setpts=PTS-STARTPTS, scale={scale} [left];[1] setpts=PTS-STARTPTS, scale={scale} [right];[base][left] {overlay}", movflags='+faststart', pix_fmt='yuv420p', c='libx264', crf=20).run()


def horizontal_align_3(input_file1, input_file2, input_file3, output_file, aspect_ratio='16:9'):
    if aspect_ratio == '16:9':
        base_size = 'hd1080'
        scale = '640:-1'
        overlay = 'overlay=0:h:shortest=1 [w];[w][middle] overlay=w:h:shortest=1[w2];[w2][right] overlay=w*2:h:shortest=1'
    elif aspect_ratio == '4:3':
        base_size = 'hd1080'
        scale = '640:-1'
        overlay = 'overlay=0:h/1.6:shortest=1 [w];[w][middle] overlay=w:h/1.6:shortest=1[w2];[w2][right] overlay=w*2:h/1.6:shortest=1'

    ffmpeg.input(input_file1).input(input_file2).input(input_file3).output(output_file, filter_complex=f"color=s={base_size} [back_color];[0] setpts=PTS-STARTPTS, scale={scale} [left];[1] setpts=PTS-STARTPTS, scale={scale}[middle];[2] setpts=PTS-STARTPTS, scale={scale} [right];[back_color][left] {overlay}", movflags='+faststart', pix_fmt='yuv420p', c='libx264', crf=20).run()


def vertical_align_2(input_file1, input_file2, output_file):
    ffmpeg.input(input_file1).input(input_file2).output(output_file, filter_complex="[0:0]pad=iw:2*ih[a];[a][1:0]overlay=0:h").run()


def sound(frequency, duration, output_file):
    ffmpeg.input('sine=frequency={}:duration={}'.format(frequency, duration)).output(output_file).run()


def change_pitch(input_file, sample_rate, output_file):
    ffmpeg.input(input_file).output(output_file, af='asetrate={}'.format(sample_rate)).run()


def crossfade(input_file1, input_file2, duration, output_file):
    ffmpeg.input(input_file1).input(input_file2).output(output_file, filter_complex='acrossfade=duration={}:curve1=exp:curve2=exp'.format(duration)).run()


def picture_in_picture(input_file1, input_file2, output_file):
    ffmpeg.input(input_file1).input(input_file2).output(output_file, filter_complex="[1:0]scale=iw/2:ih/2[red];[0:0][red]overlay").run()


def split_5(input_files, output_file):
    filter_complex = ''
    for i, input_file in enumerate(input_files):
        filter_complex += '[{}:v]scale=-1:720[v{}];[{}:a]'.format(i, i, i)
    filter_complex += 'amix=inputs={}:duration=shortest,loudnorm[a]'.format(len(input_files))
    filter_complex += ''.join('[v{}]'.format(i) for i in range(len(input_files)))
    filter_complex += 'xstack=inputs={}:layout=0_0|w0_0|w0+w1_0|w0_h1|w0+w1_h1[v]'.format(len(input_files))
    ffmpeg.input(*input_files).output(output_file, filter_complex=filter_complex).run()


def split_100(input_file, output_file, rows, cols):
    duration = ffmpeg.probe(input_file)['format']['duration']
    filter_complex = ''
    for i in range(rows):
        for j in range(cols):
            index = i * cols + j
            filter_complex += '[0:a]atrim=start={}*{}:end={}*{}[a{:02d}];'.format(duration, index/100, duration, (index+1)/100, index)
            filter_complex += '[0:v]trim=start={}*{}:end={}*{},setpts=PTS-STARTPTS[v{:02d}];'.format(duration, index/100, duration, (index+1)/100, index)
    filter_complex += ''.join('[v{:02d}]scale=-1:720[v{:02d}];'.format(i, i) for i in range(rows*cols))
    filter_complex += 'xstack=inputs={}:layout='.format(rows*cols)
    filter_complex += '|'.join('{}_{}'.format(j, i) for i in range(rows) for j in range(cols))
    filter_complex += '[v]'
    ffmpeg.input(input_file).output(output_file, filter_complex=filter_complex).run()


def subtitle(input_file, subtitle_file, output_file):
    ffmpeg.input(input_file).input(subtitle_file).output(output_file, vf="subtitles={}".format(subtitle_file)).run()


def subtitle_manually(input_file, subtitle_files, output_file):
    filter_complex = ''
    for i, subtitle_file in enumerate(subtitle_files):
        filter_complex += '-i {} '.format(subtitle_file)
    filter_complex += '-map 0:v -map 0:a '
    for i in range(len(subtitle_files)):
        filter_complex += '-map {} '.format(i+1)
    filter_complex += '-c:v copy -c:a copy -c:s srt '
    for i in range(len(subtitle_files)):
        filter_complex += '-metadata:s:s:{} language={} '.format(i, subtitle_files[i].split('-')[1].split('.')[0])
    filter_complex += output_file
    ffmpeg.input(input_file).output(output_file, filter_complex=filter_complex).run()


def hd_to_mobile(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, vcodec='libx264', r=19, b='120k', s='480x270').run()


def make_null_video(duration, output_file):
    ffmpeg.input('color=black:s=3840x2160:r=24000/1001').output(output_file).run()
