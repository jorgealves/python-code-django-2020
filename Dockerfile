# Alpine base image that contains python 3.7
FROM python:3.7-alpine

ENV PYTHONUNBUFERED 1

# Install system dependencies
# Install pip dependencies in the same layer
RUN apk add --no-cache  \
    bash build-base gcc postgresql-dev gcc python3-dev musl-dev && \
    pip3 install --no-cache-dir pip-tools==5.2.1

WORKDIR /src
ADD requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ADD . .
