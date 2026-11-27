import ffmpeg


def test_output_filter_script_v():
    args = (
        ffmpeg.input('video.mp4')
        .output(
            'output.mp4',
            **{'filter_script:v': 'crop_filter.txt', 'c:v': 'h264_nvenc'}
        )
        .get_args()
    )
    assert args == [
        '-i',
        'video.mp4',
        '-c:v',
        'h264_nvenc',
        '-filter_script:v',
        'crop_filter.txt',
        'output.mp4',
    ]


def test_input_stream_specifier():
    args = ffmpeg.input('in.mp4', **{'c:v': 'h264_cuvid'}).output('out.mp4').get_args()
    assert args == ['-c:v', 'h264_cuvid', '-i', 'in.mp4', 'out.mp4']


def test_stream_specifier_numeric_value():
    args = ffmpeg.input('in.mp4').output('out.mp4', **{'qscale:v': 3}).get_args()
    assert args == ['-i', 'in.mp4', '-qscale:v', '3', 'out.mp4']
