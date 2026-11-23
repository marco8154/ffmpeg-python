"""Guard against Python-2 helpers coming back into the ``ffmpeg`` package."""

import os
import re

import pytest


PACKAGE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PY_FILES = sorted(
    os.path.join(PACKAGE_DIR, name)
    for name in os.listdir(PACKAGE_DIR)
    if name.endswith('.py') and os.path.isfile(os.path.join(PACKAGE_DIR, name))
)

BANNED_IMPORT = re.compile(
    r'^(from __future__ import|from builtins import|from past|from future)',
    re.MULTILINE,
)


@pytest.mark.parametrize('path', PY_FILES)
def test_no_python2_leftovers(path):
    with open(path, encoding='utf-8') as fh:
        content = fh.read()
    banned = BANNED_IMPORT.findall(content)
    assert not banned, '{} contains Python-2 import(s): {}'.format(path, banned)
    assert 'sys.version_info' not in content, '{} uses sys.version_info'.format(path)
