import subprocess

import ffmpeg
import ffmpeg._run
import pytest


@pytest.fixture
def popen_calls(monkeypatch):
    calls = []

    def fake_popen(*args, **kwargs):
        calls.append((args, kwargs))
        return object()

    monkeypatch.setattr(ffmpeg._run.subprocess, 'Popen', fake_popen)
    return calls


def _stream():
    return ffmpeg.input('in.mp4').output('out.mp4')


@pytest.mark.parametrize(
    'pipe_stdout,pipe_stderr,expected_stdout,expected_stderr',
    [
        (False, False, subprocess.DEVNULL, subprocess.STDOUT),
        (True, False, subprocess.PIPE, subprocess.DEVNULL),
        (False, True, subprocess.DEVNULL, subprocess.PIPE),
        (True, True, subprocess.PIPE, subprocess.PIPE),
    ],
)
def test_quiet_keeps_requested_pipes(
    popen_calls, pipe_stdout, pipe_stderr, expected_stdout, expected_stderr
):
    ffmpeg.run_async(
        _stream(), quiet=True, pipe_stdout=pipe_stdout, pipe_stderr=pipe_stderr
    )
    assert len(popen_calls) == 1
    _, kwargs = popen_calls[0]
    assert kwargs['stdout'] == expected_stdout
    assert kwargs['stderr'] == expected_stderr


def test_not_quiet_with_pipe_stdout(popen_calls):
    ffmpeg.run_async(_stream(), quiet=False, pipe_stdout=True)
    assert len(popen_calls) == 1
    _, kwargs = popen_calls[0]
    assert kwargs['stdout'] == subprocess.PIPE
    assert kwargs['stderr'] is None
