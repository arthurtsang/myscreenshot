FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install poetry
RUN poetry install
RUN poetry run playwright install

EXPOSE 5000
ENV FLASK_APP=wayback.py

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
