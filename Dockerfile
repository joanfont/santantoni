FROM library/python:3.6.4-alpine

RUN pip3 install -U pip

WORKDIR /code/
ADD requirements.txt /code/

RUN pip3 install -r requirements.txt

ADD . /code/
ENTRYPOINT ["python3", "main.py"]