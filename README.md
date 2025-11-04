```markdown
# End-to-End Machine Learning Pipeline with MLOps (Tabular Data)

Overview
--------
This repository demonstrates a full ML lifecycle for tabular data:
data ingestion → preprocessing (Pandas / PySpark) → training & experiment tracking (MLflow) → model registry → containerized serving (FastAPI + Docker) → orchestration (Kubernetes) → cloud deployment (SageMaker / Vertex AI optional).

Goal
- Predict a binary outcome on tabular data (e.g., loan default, churn, credit risk)
- Compare XGBoost, LightGBM, CatBoost models
- Track experiments and models with MLflow
- Serve best model via a FastAPI endpoint in Docker + Kubernetes

What's new
- configs/train.yaml — concrete training/hyperparameter search config (models, search spaces, MLflow settings)
- mlflow_pipeline/hyperparam_search.py — orchestrates RandomizedSearchCV for each candidate model and logs best models to MLflow
- .github/workflows/ci.yml — GitHub Actions workflow to lint, build & push Docker image and deploy to Kubernetes (requires secrets for registry/KUBECONFIG)
- notebooks/04-give-me-some-credit.ipynb — sample notebook wired to the "Give Me Some Credit" Kaggle dataset

Repository structure
- notebooks/                # Jupyter notebooks for EDA and experiments
- mlflow_pipeline/
  - data_ingest.py          # dataset download & ingestion utilities
  - preprocess.py           # preprocessing pipelines (Pandas + PySpark hooks)
  - train.py                # train models & log experiments to MLflow
  - predict.py              # local inference utilities
  - mlflow_utils.py         # mlflow helpers: tracking URI, registry operations
  - hyperparam_search.py    # hyperparameter search & MLflow logging
- app/
  - main.py                 # FastAPI app for serving model
  - model_loader.py         # MLflow model loader
  - schemas.py              # request/response Pydantic schemas
- Dockerfile                # Build container for the FastAPI server
- k8s.yaml                  # Kubernetes deployment & service skeleton
- requirements.txt          # Python dependencies
- configs/train.yaml        # Training and search configuration
- .github/workflows/ci.yml  # CI workflow for build/push/deploy
- Makefile                  # helper commands

Quickstart (local)
1. Install Python 3.9+
2. Create a virtualenv and install deps:
   pip install -r requirements.txt
3. Start an MLflow server (local):
   mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 0.0.0.0 --port 5000
4. Download the Kaggle "Give Me Some Credit" dataset and place as data/dataset.csv (or use Kaggle API)
5. Run hyperparameter search:
   python mlflow_pipeline/hyperparam_search.py --config configs/train.yaml --data data/dataset.csv --target SeriousDlqin2yrs
6. Check MLflow UI at http://localhost:5000 to compare experiments and register the best model
7. Build & run Docker:
   docker build -t e2e-ml-pipeline:latest .
   docker run -p 8080:8080 -e MODEL_URI="runs:/<run_id>/model" e2e-ml-pipeline:latest

CI/CD (GitHub Actions)
- The provided workflow builds and pushes an image to GitHub Container Registry and will apply k8s.yaml if KUBECONFIG is provided as a secret.
- Update k8s.yaml to use the correct image path or allow the workflow to substitute it.

Next steps
- Add more robust feature pipelines, categorical encoding, and column types.
- Implement Hyperopt / Optuna for larger hyperparameter search.
- Add unit tests and end-to-end integration tests for the pipeline.
- Add monitoring (Prometheus/Grafana) and structured logs.
```