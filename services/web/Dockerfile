FROM python:3.8-alpine

WORKDIR /usr/src/app

ENV SECRET_KEY dev
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/
RUN pip install --upgrade pip \
        && cd /usr/src/app \
        && pip install -e ".[DEV]"
