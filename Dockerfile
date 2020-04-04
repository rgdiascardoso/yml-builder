FROM python:rc-buster

ADD . /app

RUN pip install -r /app/requirements.txt \
        && chmod +x /app/main.py

ENTRYPOINT [ "python", "/app/main.py"]