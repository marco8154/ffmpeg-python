import pytest

import ffmpeg


def test_get_args_without_output_raises_type_error():
    with pytest.raises(TypeError, match='has no output'):
        ffmpeg.get_args(ffmpeg.input('in.mp4'))


def test_compile_without_output_raises_type_error():
    with pytest.raises(TypeError, match='has no output'):
        ffmpeg.compile(ffmpeg.input('in.mp4'))


def test_get_args_with_filter_without_output_raises_type_error():
    with pytest.raises(TypeError, match='has no output'):
        ffmpeg.get_args(ffmpeg.input('in.mp4').hflip())


def test_get_args_with_output_is_unchanged():
    assert ffmpeg.input('in.mp4').output('out.mp4').get_args() == [
        '-i',
        'in.mp4',
        'out.mp4',
    ]
