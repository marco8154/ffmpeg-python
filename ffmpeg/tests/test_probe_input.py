import inspect

import ffmpeg

TEST_INPUT_FILE1 = 'ffmpeg/tests/sample_data/in1.mp4'


def test_probe_pipe_input():
    with open(TEST_INPUT_FILE1, 'rb') as f:
        data = f.read()
    data = ffmpeg.probe('pipe:', input=data)
    assert data['format']['nb_streams'] == 2


def test_probe_signature():
    assert list(inspect.signature(ffmpeg.probe).parameters) == [
        'filename',
        'cmd',
        'timeout',
        'input',
        'capture_stderr',
        'kwargs',
    ]


def test_probe_positional_timeout():
    ffmpeg.probe(TEST_INPUT_FILE1, 'ffprobe', 30)
