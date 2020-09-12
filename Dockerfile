# Alpine base image that contains python 3.7
FROM python:3.7-alpine

ENV PYTHONUNBUFERED 1

# Install system dependencies
# Install pip dependencies in the same layer
RUN apk add --no-cache  \
    bash build-base gcc && \
    pip3 install --no-cache-dir pip-tools==5.2.1

WORKDIR /src
ADD src/requirements.txt .

RUN pip3 install -r /src/requirements.txt

EXPOSE 5000

ADD src .
