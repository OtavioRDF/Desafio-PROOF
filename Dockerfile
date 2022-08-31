FROM python:3

ENV PYTHONBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/