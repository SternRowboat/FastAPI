FROM python:3.11-slim as base

# required for psycopg2
RUN apt update \
    && apt install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip poetry

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /code

COPY requirements/pyproject.toml .

RUN poetry install

COPY . .

FROM base AS test
RUN pip install pytest
CMD ["pytest"]