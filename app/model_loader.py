"""
Load an MLflow model given a model uri or registered model.
"""
import mlflow
import os

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000")

def load_model(model_uri: str = None, registered_name: str = None, stage: str = "Production"):
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    if model_uri:
        model = mlflow.pyfunc.load_model(model_uri)
    elif registered_name:
        model_uri = f"models:/{registered_name}/{stage}"
        model = mlflow.pyfunc.load_model(model_uri)
    else:
        raise ValueError("Either model_uri or registered_name must be provided.")
    return model