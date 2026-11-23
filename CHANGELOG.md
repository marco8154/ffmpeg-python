# Changelog

All notable changes to this project are documented in this file.
The format follows Keep a Changelog, and the project uses Semantic Versioning.

## [Unreleased]

## [0.3.0] - unreleased

First release of the continuation ffmpeg-python-ng. It keeps the `import ffmpeg` API of the original `ffmpeg-python` 0.2.0 and works on Python 3.10 and newer. See [CREDITS.md](CREDITS.md) for the authors of the original ffmpeg-python.

### Changed
- Package name on PyPI is `ffmpeg-python-ng`; `import ffmpeg` and the public API stay unchanged.
- Requires Python 3.10 or newer; every released Python version from 3.10 on is supported (tested 3.10 to 3.15).
- Build uses `pyproject.toml` (setuptools); `setup.py`, `setup.cfg`, `tox.ini`, `MANIFEST` and `requirements.txt` are gone.

### Removed
- The runtime dependency `future`; the package has no runtime dependencies.
- Python 2 compatibility code (`__future__` imports, `builtins` imports, version branches).

### Fixed
- Tests no longer depend on the ffmpeg version (`test_pipe`, `test__probe`).

### Security
- `view()` creates its temporary file with `tempfile.mkstemp` instead of the insecure `mktemp`; patch by Sarthak Munshi.

## [0.2.0] - 2019-07-06

Last release of the original ffmpeg-python by Karl Kroening; see its repository.

[Unreleased]: https://github.com/marco8154/ffmpeg-python/compare/...
[0.3.0]: https://github.com/marco8154/ffmpeg-python
[0.2.0]: https://github.com/kkroening/ffmpeg-python/releases/tag/0.2.0
