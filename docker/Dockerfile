FROM python:3.10-slim

WORKDIR /app
COPY app/ app/
COPY docker/VERSION .

CMD ["python", "app/main.py"]
