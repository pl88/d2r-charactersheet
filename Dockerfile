FROM python:3.12

ENV PYTHONFAULTHANDLER=1 \
PYTHONUNBUFFERED=1 \
PYTHONHASHSEED=random \
PIP_NO_CACHE_DIR=off \
PIP_DISABLE_PIP_VERSION_CHECK=on \
PIP_DEFAULT_TIMEOUT=100 \
POETRY_NO_INTERACTION=1 \
POETRY_VIRTUALENVS_CREATE=false \
POETRY_CACHE_DIR='/var/cache/pypoetry' \
POETRY_HOME='/usr/local' \
POETRY_VERSION=2.1.2

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /d2r-charactersheet

COPY poetry.lock pyproject.toml /d2r-charactersheet/

RUN poetry install --no-interaction --no-ansi --no-root

COPY ./d2r-charactersheet/src /d2r-charactersheet

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]