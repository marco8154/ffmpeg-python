import ffmpeg


def test_hstack_function():
    args = (
        ffmpeg.hstack(ffmpeg.input('a.mp4'), ffmpeg.input('b.mp4'))
        .output('o.mp4')
        .get_args()
    )
    assert args == [
        '-i',
        'a.mp4',
        '-i',
        'b.mp4',
        '-filter_complex',
        '[0][1]hstack=inputs=2[s0]',
        '-map',
        '[s0]',
        'o.mp4',
    ]


def test_hstack_stream_method():
    args = (
        ffmpeg.input('a.mp4')
        .hstack(ffmpeg.input('b.mp4'))
        .output('o.mp4')
        .get_args()
    )
    assert args == [
        '-i',
        'a.mp4',
        '-i',
        'b.mp4',
        '-filter_complex',
        '[0][1]hstack=inputs=2[s0]',
        '-map',
        '[s0]',
        'o.mp4',
    ]


def test_vstack_three_inputs_with_shortest():
    a = ffmpeg.input('a.mp4')
    b = ffmpeg.input('b.mp4')
    c = ffmpeg.input('c.mp4')
    args = ffmpeg.vstack(a, b, c, shortest=1).output('o.mp4').get_args()
    assert args == [
        '-i',
        'a.mp4',
        '-i',
        'b.mp4',
        '-i',
        'c.mp4',
        '-filter_complex',
        '[0][1][2]vstack=inputs=3:shortest=1[s0]',
        '-map',
        '[s0]',
        'o.mp4',
    ]


def test_stack_inputs_is_overwritten():
    args = (
        ffmpeg.hstack(ffmpeg.input('a.mp4'), ffmpeg.input('b.mp4'), inputs=5)
        .output('o.mp4')
        .get_args()
    )
    assert '[0][1]hstack=inputs=2[s0]' in args


def test_stack_in_all():
    assert 'hstack' in ffmpeg.__all__
    assert 'vstack' in ffmpeg.__all__
