import inspect

import ffmpeg
import ffmpeg._run
import pytest


class _FakeProcess:
    def communicate(self, input=None):
        return None, None

    def poll(self):
        return 0


@pytest.fixture
def popen_calls(monkeypatch):
    calls = []

    def fake_popen(*args, **kwargs):
        calls.append((args, kwargs))
        return _FakeProcess()

    monkeypatch.setattr(ffmpeg._run.subprocess, 'Popen', fake_popen)
    return calls


def _stream():
    return ffmpeg.input('in.mp4').output('out.mp4')


def test_run_popen_args_passed_to_popen(popen_calls):
    ffmpeg.run(_stream(), popen_args={'env': {'X': '1'}})
    assert len(popen_calls) == 1
    args, kwargs = popen_calls[0]
    assert args == (['ffmpeg', '-i', 'in.mp4', 'out.mp4'],)
    assert kwargs['env'] == {'X': '1'}


def test_run_without_popen_args_keeps_kwargs(popen_calls):
    ffmpeg.run(_stream())
    assert len(popen_calls) == 1
    args, kwargs = popen_calls[0]
    assert args == (['ffmpeg', '-i', 'in.mp4', 'out.mp4'],)
    assert set(kwargs) == {'stdin', 'stdout', 'stderr', 'cwd'}


def test_run_popen_args_is_last_parameter_with_default_none():
    params = inspect.signature(ffmpeg.run).parameters
    assert list(params)[-1] == 'popen_args'
    assert params['popen_args'].default is None


def test_stream_run_method_passes_popen_args(popen_calls):
    _stream().run(popen_args={'env': {'X': '1'}})
    assert len(popen_calls) == 1
    args, kwargs = popen_calls[0]
    assert args == (['ffmpeg', '-i', 'in.mp4', 'out.mp4'],)
    assert kwargs['env'] == {'X': '1'}
