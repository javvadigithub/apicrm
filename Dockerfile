FROM python:3.8-alpine
LABEL maintainer="Srikanth Javvadi"

ENV PYTHONUNBUFFFERED 1

COPY ./requirments.txt /requirments.txt
RUN pip install -r /requirments.txt

RUN mkdir /crm
WORKDIR /crm
COPY ./crm /crm

RUN adduser -D user
USER user
