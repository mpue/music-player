# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry && poetry install --no-root

COPY . /app

CMD ["poetry", "run", "python", "app.py"]
