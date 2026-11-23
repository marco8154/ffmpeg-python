# Umgebung fuer Sandbox und Testpipeline von ffmpeg-python-ng.
# ffmpeg und ffprobe kommen aus Debian 13 (trixie) und sind damit auf eine Version festgelegt.
FROM docker.io/library/python:3.13-slim-trixie
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir pytest==9.2.0 pytest-mock==3.17.0
