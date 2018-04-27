FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements/local.txt /code/
RUN pip install -r local.txt
ADD . /code/