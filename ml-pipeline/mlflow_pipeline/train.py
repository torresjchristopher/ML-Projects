"""
Train script:
- loads data (CSV)
- preprocesses (pandas_preprocess)
- trains candidate models (XGBoost, LightGBM, CatBoost)
- logs parameters, metrics, and model to MLflow
"""
import argparse
import pandas as pd
from pathlib import Path
import mlflow
import mlflow.sklearn
from mlflow_pipeline.preprocess import pandas_preprocess
from mlflow_pipeline.mlflow_utils import set_tracking
from sklearn.metrics import roc_auc_score
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostClassifier
import joblib

DEFAULT_DATA = "data/dataset.csv"
ARTIFACTS = Path("artifacts")
ARTIFACTS.mkdir(exist_ok=True)

def train_and_log(X_train, X_test, y_train, y_test, model_type="xgboost", params=None):
    if params is None:
        params = {}

    with mlflow.start_run() as run:
        mlflow.set_tag("model_type", model_type)
        # Train model
        if model_type == "xgboost":
            model = xgb.XGBClassifier(**params, use_label_encoder=False, eval_metric="logloss")
        elif model_type == "lightgbm":
            model = lgb.LGBMClassifier(**params)
        elif model_type == "catboost":
            model = CatBoostClassifier(verbose=0, **params)
        else:
            raise ValueError("Unsupported model type")

        model.fit(X_train, y_train)
        preds_proba = model.predict_proba(X_test)[:,1]
        auc = roc_auc_score(y_test, preds_proba)
        mlflow.log_metric("roc_auc", float(auc))
        mlflow.log_param("n_features", X_train.shape[1])

        # Save model artifact
        model_artifact_path = "model"
        mlflow.sklearn.log_model(model, model_artifact_path)
        print(f"Logged {model_type} model with AUC={auc:.4f}")
        return run.info.run_id, auc

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default=DEFAULT_DATA)
    parser.add_argument("--target", type=str, required=True)
    parser.add_argument("--tracking-uri", type=str, default=None)
    args = parser.parse_args()

    set_tracking(args.tracking_uri)

    df = pd.read_csv(args.data)
    X_train, X_test, y_train, y_test = pandas_preprocess(df, target_col=args.target)

    # Candidate models with small default params (tune using MLflow experiments)
    runs = {}
    for model_type in ["xgboost", "lightgbm", "catboost"]:
        run_id, auc = train_and_log(X_train, X_test, y_train, y_test, model_type=model_type, params={"n_estimators":100})
        runs[model_type] = {"run_id": run_id, "auc": auc}
    print("Training runs:", runs)

if __name__ == "__main__":
    main()