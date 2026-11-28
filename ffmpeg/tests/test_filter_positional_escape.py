import ffmpeg


def test_subtitles_positional_path_escaped_once():
    # Issue #745: a positional path like 'I:/x.srt' must reach ffmpeg with the
    # same single escaping a keyword argument would get, not double escaping.
    args = (
        ffmpeg.input('in.mp4')
        .filter('subtitles', 'I:/x.srt')
        .output('o.mp4')
        .get_args()
    )
    assert args == [
        '-i',
        'in.mp4',
        '-filter_complex',
        r'[0]subtitles=I\\:/x.srt[s0]',
        '-map',
        '[s0]',
        'o.mp4',
    ]


def test_subtitles_positional_apostrophe_escaped_once():
    # Issue #416: an apostrophe in a positional path must end up with exactly
    # three backslashes (the form that works with ffmpeg), not more.
    args = (
        ffmpeg.input('in.mp4')
        .filter('subtitles', "Ted's.srt", si=0)
        .output('o.mp4')
        .get_args()
    )
    assert args[3] == r"[0]subtitles=Ted\\\'s.srt:si=0[s0]"


def test_positional_and_keyword_args_are_escaped_the_same():
    # A positional argument and a keyword argument with the same value must be
    # masked identically (acceptance criterion over the chars : ' \ = , [ ] ;).
    for ch in [':', "'", '\\', '=', ',', '[', ']', ';', 'x']:
        value = 'a' + ch + 'b'
        pos = (
            ffmpeg.input('in.mp4')
            .filter('f', value)
            .output('o.mp4')
            .get_args()[3]
        )
        kw = (
            ffmpeg.input('in.mp4')
            .filter('f', k=value)
            .output('o.mp4')
            .get_args()[3]
        )
        pos_param = pos[len('[0]f='):-len('[s0]')]
        kw_param = kw[len('[0]f=k='):-len('[s0]')]
        assert pos_param == kw_param, (ch, pos, kw)
