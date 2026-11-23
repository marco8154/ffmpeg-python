import ffmpeg


def test_selector_zero_slice():
    assert (
        ffmpeg.input('in.mp4').node[:0].output('out.mp4').get_args()
        == ['-i', 'in.mp4', '-map', '0:0', 'out.mp4']
    )


def test_selector_zero_stream():
    assert (
        ffmpeg.input('in.mp4').node.stream(selector=0).output('out.mp4').get_args()
        == ['-i', 'in.mp4', '-map', '0:0', 'out.mp4']
    )


def test_selector_none_unchanged():
    assert (
        ffmpeg.input('in.mp4').output('out.mp4').get_args()
        == ['-i', 'in.mp4', 'out.mp4']
    )
