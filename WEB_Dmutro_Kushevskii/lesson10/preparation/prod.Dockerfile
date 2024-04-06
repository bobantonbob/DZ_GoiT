FROM python:3.10.12-slim-bullseye as requirements-stage

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

WORKDIR /tmp

RUN poetry export -f requirements.txt \
                  --output requirements.txt \
                  --without-hashes


FROM python:3.10.12-slim-bullseye

RUN apt update && apt install -y libpq-dev gcc
RUN pip install gunicorn

COPY --from=requirements-stage /tmp/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY notes /notes

WORKDIR /notes

CMD ["gunicorn", "--workers", "3",  "--bind", "0.0.0.0:8000", "notes.wsgi:application"]
