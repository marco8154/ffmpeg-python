import time

import ffmpeg


def fan(n):
    base = ffmpeg.input('base.mp4')
    for i in range(n):
        ov = ffmpeg.input('in%d.mp4' % i).filter('scale', 64, 64)
        base = base.overlay(ov, x=i, y=i)
    return base.output('out.mp4')


def test_fan_args_unchanged():
    assert fan(3).get_args() == [
        '-i',
        'base.mp4',
        '-i',
        'in0.mp4',
        '-i',
        'in1.mp4',
        '-i',
        'in2.mp4',
        '-filter_complex',
        '[1]scale=64:64[s0];[0][s0]overlay=eof_action=repeat:x=0:y=0[s1];'
        '[2]scale=64:64[s2];[s1][s2]overlay=eof_action=repeat:x=1:y=1[s3];'
        '[3]scale=64:64[s4];[s3][s4]overlay=eof_action=repeat:x=2:y=2[s5]',
        '-map',
        '[s5]',
        'out.mp4',
    ]


def test_fan_800_is_fast():
    graph = fan(800)
    start = time.perf_counter()
    graph.get_args()
    elapsed = time.perf_counter() - start
    assert elapsed < 0.4, 'get_args() took {:.3f} s'.format(elapsed)
