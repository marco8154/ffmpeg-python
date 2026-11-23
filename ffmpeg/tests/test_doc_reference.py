import re
import runpy
from pathlib import Path

import ffmpeg

HERE = Path(__file__).resolve().parent
PROJECT_ROOT = HERE.parent.parent


def test_every_public_name_has_docstring():
    for name in ffmpeg.__all__:
        obj = getattr(ffmpeg, name)
        doc = getattr(obj, '__doc__', None) or ''
        assert doc.strip(), f'{name} has no docstring'


def test_sphinx_conf():
    conf_path = PROJECT_ROOT / 'doc' / 'src' / 'conf.py'
    conf = runpy.run_path(str(conf_path))

    assert conf['project'] == 'ffmpeg-python-ng'
    assert conf['language'] == 'en'

    pyproject = (PROJECT_ROOT / 'pyproject.toml').read_text()
    version = re.search(r"^version = '([^']+)'", pyproject, re.M).group(1)
    assert conf['release'] == version


def test_index_names_fork():
    index = (PROJECT_ROOT / 'doc' / 'src' / 'index.rst').read_text()
    assert 'ffmpeg-python-ng' in index
    assert 'https://github.com/marco8154/ffmpeg-python' in index
    assert '.. automodule:: ffmpeg' in index
