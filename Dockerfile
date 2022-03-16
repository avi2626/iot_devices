FROM python:3.10-alpine

ENV PYTHONUNBUFFERD 1
RUN apk update && apk add tk

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app/


RUN adduser -D user
USER user