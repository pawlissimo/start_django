FROM python:3

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    mc \
    mcedit

WORKDIR /build

ADD requirements.txt /build/

RUN pip3 install -U pip \
  && pip3 install -r requirements.txt


WORKDIR /code

#ADD . /code/
