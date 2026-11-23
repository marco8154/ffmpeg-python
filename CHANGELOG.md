# Changelog

All notable changes to this project are documented in this file.
The format follows Keep a Changelog, and the project uses Semantic Versioning.

## [Unreleased]

### Added
- `get_args()` and `compile()` accept `explicit_maps=True` to write a `-map` before every output; patch by Artem Eltyshev.
- `run_async()` accepts `popen_args`, a dict of extra keyword arguments for `subprocess.Popen`; patch by Michael Litvin.
- `probe()` accepts `input=` to read the media from a pipe; patch by Rocky Cai.
- `probe()` accepts `capture_stderr=True` and then returns `(info, stderr)`; patch by Ezequiel Ramos.
- `input()` and `output()` accept path-like objects such as `pathlib.Path`; patch by Brian Hou.
- New filter `atrim`; patch by Jason Cordial.

### Changed
- `output(..., filename=None)` raises `TypeError` when the graph is built instead of failing later in `run()`.

### Fixed
- A stream selector with index 0 (for example `stream[0]`) is no longer dropped; patch by Artem Eltyshev.
- `get_args()` works on FIPS systems (`md5` is called with `usedforsecurity=False`); patch by Zachary Berry.
- `ffmpeg/_view.py` imports the package relatively, so a vendored copy under another name works; patch by Shimpei Yamaguchi.
- `get_args()` handles large graphs: visited nodes are kept in sets, and long filter chains (2000 filters) no longer raise `RecursionError`.
- `repr()` of a node no longer raises `TypeError`.

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

[Unreleased]: https://github.com/marco8154/ffmpeg-python
[0.3.0]: https://github.com/marco8154/ffmpeg-python
[0.2.0]: https://github.com/kkroening/ffmpeg-python/releases/tag/0.2.0
