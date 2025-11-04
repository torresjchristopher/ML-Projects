.PHONY: help mlflow train lint build run

help:
	@echo "make mlflow   - start a local MLflow server (background)"
	@echo "make train    - run training script"
	@echo "make build    - build docker image"
	@echo "make run      - run API locally (uvicorn)"

mlflow:
	@echo "Starting MLflow server..."
	nohup mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000 > mlflow.log 2>&1 &

train:
	python mlflow_pipeline/train.py

build:
	docker build -t e2e-ml-pipeline:latest .

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8080