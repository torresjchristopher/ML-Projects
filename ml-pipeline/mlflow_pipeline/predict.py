"""
Local prediction helper that loads an MLflow model and runs inference on a DataFrame.
"""
import pandas as pd
from mlflow.tracking import MlflowClient
import mlflow
import argparse

def load_model_from_run(run_id: str, model_path: str = "model"):
    model_uri = f"runs:/{run_id}/{model_path}"
    model = mlflow.pyfunc.load_model(model_uri)
    return model

def predict(run_id: str, X: pd.DataFrame):
    model = load_model_from_run(run_id)
    preds = model.predict(X)
    return preds

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--input-csv", required=True)
    args = parser.parse_args()
    X = pd.read_csv(args.input_csv)
    preds = predict(args.run_id, X)
    print(preds[:10])