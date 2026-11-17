# ffmpeg-python: Python bindings for FFmpeg

**Continuation of [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) by Karl Kroening.** The original has had no release since 0.2.0 in 2019. This fork keeps its API and its `import ffmpeg`, runs on every Python release from 3.10 on and is removing the `future` dependency.

[![CI][ci-badge]][ci]

[ci-badge]: https://github.com/marco8154/ffmpeg-python/actions/workflows/ci.yml/badge.svg
[ci]: https://github.com/marco8154/ffmpeg-python/actions/workflows/ci.yml

<img src="https://raw.githubusercontent.com/marco8154/ffmpeg-python/master/doc/formula.png" alt="ffmpeg-python logo" width="60%" />

## About this continuation

- **Same API.** Existing code keeps working: the same function names, parameters and generated command lines, and the same `import ffmpeg`.
- **Current Python.** Tested on Python 3.10 to 3.15 on Linux and on the newest release on Windows and macOS. Every future Python release is supported once it is out.
- **No `future` dependency.** The package has no runtime dependencies (in progress for 0.3.0).
- **Fixes with tests.** Pending fixes from the original's pull requests are carried over with tests, and their authors stay credited.
- **Same licence.** Apache-2.0, like the original. The full Git history and all authors are kept ([CREDITS.md](CREDITS.md)).

**Status:** in development. The first release, 0.3.0, will be published on PyPI as `ffmpeg-python-ng`. Until then, install from GitHub (see [Installation](#installation)).

If the original project becomes active again, fixes from here will be offered back as pull requests. See [kkroening/ffmpeg-python#807](https://github.com/kkroening/ffmpeg-python/issues/807).

## Overview

There are tons of Python FFmpeg wrappers out there but they seem to lack complex filter support.  `ffmpeg-python` works well for simple as well as complex signal graphs.


## Quickstart

Flip a video horizontally:
```python
import ffmpeg
stream = ffmpeg.input('input.mp4')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.mp4')
ffmpeg.run(stream)
```

Or if you prefer a fluent interface:
```python
import ffmpeg
(
    ffmpeg
    .input('input.mp4')
    .hflip()
    .output('output.mp4')
    .run()
)
```

## [API reference](https://kkroening.github.io/ffmpeg-python/)

The API is unchanged, so the original project's reference applies. A reference for this continuation is planned for 0.3.1.

## Complex filter graphs
FFmpeg is extremely powerful, but its command-line interface gets really complicated rather quickly - especially when working with signal graphs and doing anything more than trivial.

Take for example a signal graph that looks like this:

![Signal graph](https://raw.githubusercontent.com/marco8154/ffmpeg-python/master/doc/graph1.png)

The corresponding command-line arguments are pretty gnarly:
```bash
ffmpeg -i input.mp4 -i overlay.png -filter_complex "[0]trim=start_frame=10:end_frame=20[v0];\
    [0]trim=start_frame=30:end_frame=40[v1];[v0][v1]concat=n=2[v2];[1]hflip[v3];\
    [v2][v3]overlay=eof_action=repeat[v4];[v4]drawbox=50:50:120:120:red:t=5[v5]"\
    -map [v5] output.mp4
```

Maybe this looks great to you, but if you're not an FFmpeg command-line expert, it probably looks alien.

If you're like me and find Python to be powerful and readable, it's easier with `ffmpeg-python`:
```python
import ffmpeg

in_file = ffmpeg.input('input.mp4')
overlay_file = ffmpeg.input('overlay.png')
(
    ffmpeg
    .concat(
        in_file.trim(start_frame=10, end_frame=20),
        in_file.trim(start_frame=30, end_frame=40),
    )
    .overlay(overlay_file.hflip())
    .drawbox(50, 50, 120, 120, color='red', thickness=5)
    .output('out.mp4')
    .run()
)
```

`ffmpeg-python` takes care of running `ffmpeg` with the command-line arguments that correspond to the above filter diagram, in familiar Python terms.

<img src="https://raw.githubusercontent.com/marco8154/ffmpeg-python/master/doc/screenshot.png" alt="Screenshot" align="middle" width="60%" />

Real-world signal graphs can get a heck of a lot more complex, but `ffmpeg-python` handles arbitrarily large (directed-acyclic) signal graphs.

## Installation

### Installing `ffmpeg-python`

Python 3.10 or newer is required.

Until the first release is on PyPI, install the continuation straight from GitHub:

```bash
pip install git+https://github.com/marco8154/ffmpeg-python.git
```

Or clone it and install from the local copy:
```bash
git clone https://github.com/marco8154/ffmpeg-python.git
pip install -e ./ffmpeg-python
```

From release 0.3.0 on, it will be available from PyPI:

```bash
pip install ffmpeg-python-ng
```

### Switching from the original `ffmpeg-python`

Both packages install the same module `ffmpeg`, so they must not be installed side by side. Remove the original first; your code does not change:

```bash
pip uninstall ffmpeg-python
pip install git+https://github.com/marco8154/ffmpeg-python.git
```

The only intended difference is that Python 2 and Python versions before 3.10 are no longer supported.

> **Note**: `ffmpeg-python` makes no attempt to download/install FFmpeg, as `ffmpeg-python` is merely a pure-Python wrapper - whereas FFmpeg installation is platform-dependent/environment-specific, and is thus the responsibility of the user, as described below.

### Installing FFmpeg

Before using `ffmpeg-python`, FFmpeg must be installed and accessible via the `$PATH` environment variable.

There are a variety of ways to install FFmpeg, such as the [official download links](https://ffmpeg.org/download.html), or using your package manager of choice (e.g. `sudo apt install ffmpeg` on Debian/Ubuntu, `brew install ffmpeg` on macOS, `winget install Gyan.FFmpeg` on Windows, etc.).

Regardless of how FFmpeg is installed, you can check if your environment path is set correctly by running the `ffmpeg` command from the terminal, in which case the version information should appear, as in the following example (truncated for brevity):

```
$ ffmpeg
ffmpeg version 7.1.5-0+deb13u1 Copyright (c) 2000-2026 the FFmpeg developers
```

> **Note**: The actual version information displayed here may vary from one system to another; but if a message such as `ffmpeg: command not found` appears instead of the version information, FFmpeg is not properly installed.

## [Examples](examples)

When in doubt, take a look at the [examples](examples) to see if there's something that's close to whatever you're trying to do.

Here are a few:
- [Convert video to numpy array](examples/README.md#convert-video-to-numpy-array)
- [Generate thumbnail for video](examples/README.md#generate-thumbnail-for-video)
- [Read raw PCM audio via pipe](examples/README.md#convert-sound-to-raw-pcm-audio)

- [JupyterLab/Notebook stream editor](examples/README.md#jupyter-stream-editor)

<img src="https://raw.githubusercontent.com/marco8154/ffmpeg-python/master/doc/jupyter-demo.gif" alt="jupyter demo" width="75%" />

- [Tensorflow/DeepDream streaming](examples/README.md#tensorflow-streaming)

<img src="https://raw.githubusercontent.com/marco8154/ffmpeg-python/master/examples/graphs/dream.png" alt="deep dream streaming" width="40%" />

See the [Examples README](examples) for additional examples.

## Custom Filters

Don't see the filter you're looking for?  While `ffmpeg-python` includes shorthand notation for some of the most commonly used filters (such as `concat`), all filters can be referenced via the `.filter` operator:
```python
stream = ffmpeg.input('dummy.mp4')
stream = ffmpeg.filter(stream, 'fps', fps=25, round='up')
stream = ffmpeg.output(stream, 'dummy2.mp4')
ffmpeg.run(stream)
```

Or fluently:
```python
(
    ffmpeg
    .input('dummy.mp4')
    .filter('fps', fps=25, round='up')
    .output('dummy2.mp4')
    .run()
)
```

**Special option names:**

Arguments with special names such as `-qscale:v` (variable bitrate), `-b:v` (constant bitrate), etc. can be specified as a keyword-args dictionary as follows:
```python
(
    ffmpeg
    .input('in.mp4')
    .output('out.mp4', **{'qscale:v': 3})
    .run()
)
```

**Multiple inputs:**

Filters that take multiple input streams can be used by passing the input streams as an array to `ffmpeg.filter`:
```python
main = ffmpeg.input('main.mp4')
logo = ffmpeg.input('logo.png')
(
    ffmpeg
    .filter([main, logo], 'overlay', 10, 10)
    .output('out.mp4')
    .run()
)
```

**Multiple outputs:**

Filters that produce multiple outputs can be used with `.filter_multi_output`:
```python
split = (
    ffmpeg
    .input('in.mp4')
    .filter_multi_output('split')  # or `.split()`
)
(
    ffmpeg
    .concat(split[0], split[1].reverse())
    .output('out.mp4')
    .run()
)
```
(In this particular case, `.split()` is the equivalent shorthand, but the general approach works for other multi-output filters)

**String expressions:**

Expressions to be interpreted by ffmpeg can be included as string parameters and reference any special ffmpeg variable names:
```python
(
    ffmpeg
    .input('in.mp4')
    .filter('crop', 'in_w-2*10', 'in_h-2*20')
    .output('out.mp4')
)
```

<br />

When in doubt, refer to the [existing filters](ffmpeg/_filters.py), [examples](examples), and/or the [official ffmpeg documentation](https://ffmpeg.org/ffmpeg-filters.html).

## Frequently asked questions

**Why do I get an import/attribute/etc. error from `import ffmpeg`?**

Make sure only one of `ffmpeg-python` and `ffmpeg-python-ng` is installed, and _**not**_ `ffmpeg` (wrong) or `python-ffmpeg` (also wrong). Those other packages also provide a module named `ffmpeg`. `pip list` shows what is installed.

**Why did my audio stream get dropped?**

Some ffmpeg filters drop audio streams, and care must be taken to preserve the audio in the final output.  The ``.audio`` and ``.video`` operators can be used to reference the audio/video portions of a stream so that they can be processed separately and then re-combined later in the pipeline.

This dilemma is intrinsic to ffmpeg, and ffmpeg-python tries to stay out of the way while users may refer to the official ffmpeg documentation as to why certain filters drop audio.

As usual, take a look at the [examples](examples#audiovideo-pipeline) (*Audio/video pipeline* in particular).

**How can I find out the used command line arguments?**

You can run `stream.get_args()` before `stream.run()` to retrieve the command line arguments that will be passed to `ffmpeg`. You can also run `stream.compile()` that also includes the `ffmpeg` executable as the first argument.

**How do I do XYZ?**

Take a look at each of the links in the [Additional Resources](#additional-resources) section at the end of this README.  If you look everywhere and can't find what you're looking for and have a question that may be relevant to other users, you may open an issue asking how to do it, while providing a thorough explanation of what you're trying to do and what you've tried so far.

Issues not directly related to `ffmpeg-python` or issues asking others to write your code for you or how to do the work of solving a complex signal processing problem for you that's not relevant to other users will be closed.

## Contributing

<img align="right" src="https://raw.githubusercontent.com/marco8154/ffmpeg-python/master/doc/logo.png" alt="ffmpeg-python logo" width="20%" />

Bug reports, questions and feature requests go to the [issue tracker](https://github.com/marco8154/ffmpeg-python/issues). Please include your Python version, your FFmpeg version (`ffmpeg -version`), your operating system and, if possible, the output of `stream.get_args()`.

Security issues are reported privately, as described in [SECURITY.md](SECURITY.md).

Code contributions are coordinated as tasks on [swarvex.ai](https://swarvex.ai/en/projects/ffmpeg-python-ng): each task names the files to change and the tests that must pass. The rules for contributors are in [AGENTS.md](AGENTS.md). Every change comes with tests, and existing behaviour stays compatible.

### Running tests

FFmpeg must be installed (see [Installing FFmpeg](#installing-ffmpeg)).

```bash
git clone https://github.com/marco8154/ffmpeg-python.git
cd ffmpeg-python
python -m venv venv
. venv/bin/activate     # Linux / macOS
venv\Scripts\activate   # Windows
pip install -e . pytest pytest-mock
python -m pytest
```

<br />

### Special thanks

- [Karl Kroening](https://github.com/kkroening), who wrote and maintained `ffmpeg-python`
- Everyone who contributed to the original project, listed in [CREDITS.md](CREDITS.md)
- [Fabrice Bellard](https://bellard.org/)
- [The FFmpeg team](https://ffmpeg.org/donations.html)
- [Arne de Laat](https://github.com/153957)
- [Davide Depau](https://github.com/depau)
- [Dim](https://github.com/lloti)
- [Noah Stier](https://github.com/noahstier)

## Additional Resources

- [API Reference](https://kkroening.github.io/ffmpeg-python/) (original project)
- [Examples](examples)
- [Filters](ffmpeg/_filters.py)
- [FFmpeg Homepage](https://ffmpeg.org/)
- [FFmpeg Documentation](https://ffmpeg.org/ffmpeg.html)
- [FFmpeg Filters Documentation](https://ffmpeg.org/ffmpeg-filters.html)
- [Test cases](ffmpeg/tests/test_ffmpeg.py)
- [Issue tracker](https://github.com/marco8154/ffmpeg-python/issues)
- [Original project](https://github.com/kkroening/ffmpeg-python)
