FROM mcr.microsoft.com/playwright/python:v1.49.1-noble

WORKDIR /app

RUN pip install poetry

COPY ./myscreenshot/__init__.py /app/myscreenshot/__init__.py
COPY ./poetry.lock /app/poetry.lock
COPY ./pyproject.toml /app/pyproject.toml
COPY ./README.md /app/README.md

RUN poetry install

COPY . /app

EXPOSE 5000
ENV FLASK_APP=./myscreenshot/app.py

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
