FROM python:3.7.7-alpine3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    # psycopg2 dependencies
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    # CFFI dependencies: i have no idea what these do but allauth apparently depends on them
    && apk add libffi-dev py-cffi

RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip

# Requirements are installed here to ensure they will be cached.
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
COPY /requirements /code/
RUN pip install -r requirements/production.txt
COPY . /code/

# EXPOSE 8000

# CMD ["python", "manage.py", "collectstatic"]
