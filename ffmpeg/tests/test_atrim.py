import ffmpeg


def test_atrim_stream_method():
    args = (
        ffmpeg.input('in.mp4')['a']
        .atrim(start=1, end=2)
        .output('out.mp4')
        .get_args()
    )
    assert args == [
        '-i',
        'in.mp4',
        '-filter_complex',
        '[0:a]atrim=end=2:start=1[s0]',
        '-map',
        '[s0]',
        'out.mp4',
    ]


def test_atrim_function():
    args = (
        ffmpeg.atrim(ffmpeg.input('in.mp4')['a'], start=1, end=2)
        .output('out.mp4')
        .get_args()
    )
    assert args == [
        '-i',
        'in.mp4',
        '-filter_complex',
        '[0:a]atrim=end=2:start=1[s0]',
        '-map',
        '[s0]',
        'out.mp4',
    ]


def test_atrim_in_all():
    assert 'atrim' in ffmpeg.__all__
