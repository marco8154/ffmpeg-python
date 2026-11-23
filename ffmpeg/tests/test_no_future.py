import os
import subprocess
import sys

import pytest

import ffmpeg


REPO_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


def test__import_without_future():
    code = (
        'import sys\n'
        "sys.modules['past'] = None\n"
        "sys.modules['future'] = None\n"
        'import ffmpeg\n'
    )
    result = subprocess.run(
        [sys.executable, '-c', code],
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert result.returncode == 0, result.stderr.decode(errors='replace')


def test__stream_selector_with_string():
    stream = ffmpeg.input('in.mp4')['a']
    assert isinstance(stream, ffmpeg.Stream)
    assert stream.selector == 'a'


def test__stream_selector_with_int_raises():
    with pytest.raises(TypeError):
        ffmpeg.input('in.mp4')[1]
