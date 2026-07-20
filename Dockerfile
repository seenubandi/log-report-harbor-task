FROM python:3.11.9-slim@sha256:5f3b3d7d3f6a5d9b1c8d4c3e5c2d4b9e0b7c6f5a4e3d2c1b0a9f8e7d6c5b4a3

WORKDIR /app

RUN pip install --no-cache-dir pytest

COPY tests /app/tests
COPY access.log /app/access.log

ENV PYTHONPATH=/app
