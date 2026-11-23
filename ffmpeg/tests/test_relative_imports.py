"""Ensure every module inside the ffmpeg package uses relative imports.

Absolute imports like ``from ffmpeg.nodes import ...`` break the package when it
is vendored under another name. Each module must import from ``.nodes`` etc.
instead.
"""

import ast
import glob
import os


def _package_files():
    package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = []
    for path in sorted(glob.glob(os.path.join(package_dir, "*.py"))):
        if path.endswith(os.path.join("tests", "*.py")):
            continue
        files.append(path)
    return files


def _absolute_ffmpeg_imports(tree):
    violations = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module is not None:
                module = node.module
                if module == "ffmpeg" or module.startswith("ffmpeg."):
                    violations.append(
                        f"{node.lineno}: from {module} import ... (absolute import)"
                    )
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "ffmpeg" or alias.name.startswith("ffmpeg."):
                    violations.append(
                        f"{node.lineno}: import {alias.name} (absolute import)"
                    )
    return violations


def test_no_absolute_ffmpeg_imports():
    failures = []
    for path in _package_files():
        with open(path, "r", encoding="utf-8") as handle:
            source = handle.read()
        tree = ast.parse(source, filename=path)
        for violation in _absolute_ffmpeg_imports(tree):
            failures.append(f"{path}:{violation}")
    assert not failures, "\n".join(sorted(failures))
