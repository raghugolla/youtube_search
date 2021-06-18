FROM python:3.7.1

RUN pip install -U pip
RUN pip install poetry

WORKDIR /app

RUN poetry config virtualenvs.create false
ADD pyproject.toml poetry.lock /app/
RUN poetry install --no-root --no-interaction --no-ansi

ADD . /app

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
