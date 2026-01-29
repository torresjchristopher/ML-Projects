# Dockerfile for serving the FastAPI model
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential git ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app
COPY serve.py ./serve.py
COPY mlflow_utils.py ./mlflow_utils.py

EXPOSE 8080

# Default: expects MODEL_DIR env var to be set when running container
CMD ["python", "serve.py", "--port", "8080"]