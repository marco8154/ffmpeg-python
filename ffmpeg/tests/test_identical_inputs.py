import ffmpeg


def test_concat_of_identical_inputs_has_two_inputs():
    args = (
        ffmpeg.concat(ffmpeg.input('a.mp4'), ffmpeg.input('a.mp4'))
        .output('o.mp4')
        .get_args()
    )
    assert args == [
        '-i',
        'a.mp4',
        '-i',
        'a.mp4',
        '-filter_complex',
        '[0][1]concat=n=2[s0]',
        '-map',
        '[s0]',
        'o.mp4',
    ]


def test_issue_880_identical_inputs_with_same_filter():
    a = ffmpeg.input('a.mov')
    b = ffmpeg.input('a.mov')
    args = ffmpeg.merge_outputs(
        a.trim(start_frame=1, end_frame=2).output('o1.mp4'),
        b.trim(start_frame=1, end_frame=2).output('o2.mp4'),
    ).get_args()
    assert args == [
        '-i',
        'a.mov',
        '-i',
        'a.mov',
        '-filter_complex',
        '[0]trim=end_frame=2:start_frame=1[s0];[1]trim=end_frame=2:start_frame=1[s1]',
        '-map',
        '[s0]',
        'o1.mp4',
        '-map',
        '[s1]',
        'o2.mp4',
    ]


def test_same_stream_object_is_one_input():
    s = ffmpeg.input('a.mp4')
    args = (
        ffmpeg.concat(
            s.trim(start_frame=0, end_frame=1), s.trim(start_frame=2, end_frame=3)
        )
        .output('o.mp4')
        .get_args()
    )
    assert args.count('-i') == 1


def test_input_identity():
    assert ffmpeg.input('x.mp4') != ffmpeg.input('x.mp4')
    s = ffmpeg.input('x.mp4')
    assert s == s
    assert hash(s) == hash(s)
