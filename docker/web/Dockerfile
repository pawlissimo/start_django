FROM python:3

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    mc \
    mcedit

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip3 install -U pip \
  && pip3 install -r requirements.txt

ADD . /code/
