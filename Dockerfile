FROM python:3.9-slim

WORKDIR /app

# Install system deps for lightgbm/xgboost if needed (simplified)
RUN apt-get update && apt-get install -y build-essential ca-certificates git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY mlflow_pipeline ./mlflow_pipeline

ENV PYTHONUNBUFFERED=1

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]