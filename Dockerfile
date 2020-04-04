FROM python:rc-buster

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt \
        && chmod +x main.py

ENTRYPOINT [ "python", "main.py"]