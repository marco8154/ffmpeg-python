import inspect
import os

import ffmpeg

TEST_INPUT_FILE1 = os.path.join(os.path.dirname(__file__), 'sample_data', 'in1.mp4')


def test_probe_capture_stderr():
    info, err = ffmpeg.probe(TEST_INPUT_FILE1, capture_stderr=True)
    assert info['format']['nb_streams'] == 2
    assert isinstance(err, bytes)


def test_probe_without_capture_stderr_returns_dict():
    assert isinstance(ffmpeg.probe(TEST_INPUT_FILE1), dict)


def test_probe_signature_with_capture_stderr():
    assert list(inspect.signature(ffmpeg.probe).parameters) == [
        'filename',
        'cmd',
        'timeout',
        'input',
        'capture_stderr',
        'kwargs',
    ]
