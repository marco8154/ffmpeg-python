import hashlib

import ffmpeg
from ffmpeg import _utils


def test_get_hash_stable_value():
    assert _utils.get_hash('x') == '9dd4e461268c8034f5c8564e155c67a6'
    assert _utils.get_hash('x') == '9dd4e461268c8034f5c8564e155c67a6'


def test_get_hash_works_in_fips_mode(monkeypatch):
    real_md5 = hashlib.md5

    def fake_md5(data=b'', usedforsecurity=True, **kwargs):
        if usedforsecurity is not False:
            raise ValueError('md5 is forbidden in FIPS mode')
        return real_md5(data, usedforsecurity=False)

    monkeypatch.setattr(_utils.hashlib, 'md5', fake_md5)

    assert ffmpeg.input('in.mp4').output('out.mp4').get_args() == [
        '-i',
        'in.mp4',
        'out.mp4',
    ]
