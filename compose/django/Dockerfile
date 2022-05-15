FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

# depencies
RUN apt-get update \
    && apt-get install postgresql-client -y

# Requirements installing.
COPY ./requirements /requirements
RUN pip install -r /requirements/base.txt


COPY ./compose/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY ./compose/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r//' /start-celerybeat
RUN chmod +x /start-celerybeat

WORKDIR /app
