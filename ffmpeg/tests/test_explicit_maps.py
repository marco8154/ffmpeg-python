import inspect

import ffmpeg


def _inputs():
    in_ = ffmpeg.input('in.mp4')
    out1 = in_.output('out1.mp4')
    out2 = in_.output('out2.mp4')
    return out1, out2


def test_merge_outputs_with_explicit_maps():
    out1, out2 = _inputs()
    assert ffmpeg.merge_outputs(out1, out2).get_args(explicit_maps=True) == [
        '-i',
        'in.mp4',
        '-map',
        '0',
        'out1.mp4',
        '-map',
        '0',
        'out2.mp4',
    ]


def test_get_args_list_with_explicit_maps():
    out1, out2 = _inputs()
    assert ffmpeg.get_args([out1, out2], explicit_maps=True) == [
        '-i',
        'in.mp4',
        '-map',
        '0',
        'out2.mp4',
        '-map',
        '0',
        'out1.mp4',
    ]


def test_merge_outputs_without_explicit_maps():
    out1, out2 = _inputs()
    assert ffmpeg.merge_outputs(out1, out2).get_args() == [
        '-i',
        'in.mp4',
        'out1.mp4',
        'out2.mp4',
    ]


def test_compile_with_explicit_maps():
    out1, _ = _inputs()
    assert ffmpeg.compile(out1, explicit_maps=True) == [
        'ffmpeg',
        '-i',
        'in.mp4',
        '-map',
        '0',
        'out1.mp4',
    ]


def test_get_args_parameter_order():
    params = list(inspect.signature(ffmpeg.get_args).parameters)
    assert params[-2:] == ['overwrite_output', 'explicit_maps']


def test_compile_parameter_order():
    params = list(inspect.signature(ffmpeg.compile).parameters)
    assert params[-3:] == ['cmd', 'overwrite_output', 'explicit_maps']
