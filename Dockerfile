FROM python:3.10 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install pipenv
RUN apt-get update

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv requirements --dev > dev-requirements.txt

RUN pip install -r dev-requirements.txt

WORKDIR /home/parser

COPY . .

RUN chmod +x src/scripts/fastapi.sh
RUN chmod +x src/scripts/consumer.sh
