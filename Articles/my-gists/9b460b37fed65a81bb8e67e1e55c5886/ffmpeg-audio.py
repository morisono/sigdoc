import ffmpeg

def audio_mix(input_files, output_file):
    filter_complex = 'amix=inputs={}:duration=longest'.format(len(input_files))
    ffmpeg.input(*input_files).output(output_file, filter_complex=filter_complex).run()


def audio_merge(input_files, output_file):
    filter_complex = 'amerge=inputs={}'.format(len(input_files))
    filter_complex += ' -ac 2'  # Set output to stereo
    ffmpeg.input(*input_files).output(output_file, filter_complex=filter_complex).run()


def join_mono_to_stereo(input_files, output_file):
    filter_complex = 'join=inputs={}:channel_layout=stereo'.format(len(input_files))
    ffmpeg.input(*input_files).output(output_file, filter_complex=filter_complex).run()


def merge_mono_to_mono(input_files, output_file):
    filter_complex = 'amerge=inputs={}'.format(len(input_files))
    ffmpeg.input(*input_files).output(output_file, filter_complex=filter_complex).run()
