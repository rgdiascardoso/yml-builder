FROM python:3.9.0a5-buster
ADD . /app
WORKDIR /app

ENV PYTHONPATH /app
CMD ["/app/main.py"]