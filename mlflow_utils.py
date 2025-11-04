"""
Small MLflow helper for setting tracking URI and creating experiments.
"""
import mlflow
from mlflow.tracking import MlflowClient
import os

def set_tracking(tracking_uri: str = None):
    if tracking_uri:
        mlflow.set_tracking_uri(tracking_uri)
    else:
        mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000"))
    return mlflow.get_tracking_uri()

def ensure_experiment(name: str):
    client = MlflowClient(tracking_uri=mlflow.get_tracking_uri())
    try:
        exp = client.get_experiment_by_name(name)
        if exp is None:
            client.create_experiment(name)
    except Exception:
        # best-effort
        pass