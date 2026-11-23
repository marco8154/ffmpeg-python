from pathlib import Path

import ffmpeg
import pytest


def test_input_pathlike():
    args = ffmpeg.input(Path('in.mp4')).output(Path('out.mp4')).get_args()
    assert args == ['-i', 'in.mp4', 'out.mp4']


def test_output_filename_pathlike():
    args = ffmpeg.input(Path('in.mp4')).output(filename=Path('out.mp4')).get_args()
    assert args == ['-i', 'in.mp4', 'out.mp4']


def test_output_requires_filename():
    with pytest.raises(ValueError):
        ffmpeg.output(ffmpeg.input('in.mp4'))
