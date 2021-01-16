FROM library/python:3.6.4-alpine

ARG env=prod
RUN apk --no-cache --update add tzdata
RUN pip3 install -U pip

WORKDIR /code/
ADD requirements*.txt /code/

RUN pip3 install -r requirements-${env}.txt

ADD . /code/
ENTRYPOINT ["python3", "main.py"]