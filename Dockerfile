# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
RUN apk add zlib-dev jpeg-dev gcc musl-dev
# install psycopg2
RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2

# install dependencies
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# copy project
COPY . .

# collect static files
#RUN python3 manage.py collectstatic --noinput
#RUN python3 manage.py makemigrations
#RUN python3 manage.py migrate

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD gunicorn puppy_pics_project.wsgi:application --bind 0.0.0.0:8000
