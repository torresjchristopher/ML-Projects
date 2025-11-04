"""
Helpers to interact with MLflow: set tracking URI, register models, and helper logging.
"""
import mlflow
from mlflow.tracking import MlflowClient
import os

def set_tracking(tracking_uri: str = None):
    if tracking_uri:
        mlflow.set_tracking_uri(tracking_uri)
    else:
        mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000"))
    print("MLflow tracking URI:", mlflow.get_tracking_uri())

def get_client():
    return MlflowClient()

def register_model(run_id: str, model_path: str, name: str):
    client = get_client()
    # Create registered model if not exists (MlflowClient will raise if exists)
    try:
        client.create_registered_model(name)
    except Exception:
        pass
    model_uri = f"runs:/{run_id}/{model_path}"
    mv = client.create_model_version(name, model_uri, run_id)
    return mv