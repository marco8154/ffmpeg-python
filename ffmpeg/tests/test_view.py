import os
import sys
import tempfile
import types
from unittest import mock

import pytest

import ffmpeg


def _install_fake_graphviz(monkeypatch):
    fake = types.ModuleType('graphviz')
    fake.Digraph = mock.Mock()
    monkeypatch.setitem(sys.modules, 'graphviz', fake)
    return fake


def test_view_uses_existing_temp_file_not_mktemp(monkeypatch):
    fake = _install_fake_graphviz(monkeypatch)

    def fail_mktemp(*args, **kwargs):
        raise AssertionError('tempfile.mktemp must not be used')

    monkeypatch.setattr(tempfile, 'mktemp', fail_mktemp)

    ffmpeg.input('in.mp4').output('out.mp4').view()

    view_mock = fake.Digraph.return_value.view
    view_mock.assert_called_once()
    args, kwargs = view_mock.call_args
    assert kwargs.get('cleanup') is True
    filename = args[0]
    try:
        assert os.path.isfile(filename)
    finally:
        if os.path.exists(filename):
            os.remove(filename)


def test_view_filename_and_pipe_raises_value_error(monkeypatch):
    _install_fake_graphviz(monkeypatch)
    with pytest.raises(ValueError):
        ffmpeg.input('in.mp4').output('out.mp4').view(filename='x.png', pipe=True)
