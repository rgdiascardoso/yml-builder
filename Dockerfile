FROM python:3.9.0a5-buster
ADD . /app
WORKDIR /app

RUN chmod +x /app/main.py

CMD ["python", "/app/main.py"]