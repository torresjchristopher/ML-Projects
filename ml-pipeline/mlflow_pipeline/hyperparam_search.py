"""
Hyperparameter search module that:
- Loads config from configs/train.yaml
- Runs RandomizedSearchCV (or optionally Hyperopt) for each enabled model
- Logs parameters, CV metrics, and best model to MLflow
- Compares runs under a single MLflow experiment

Usage:
    python mlflow_pipeline/hyperparam_search.py --config configs/train.yaml --data data/dataset.csv --target <target_column>
"""

import argparse
import yaml
import os
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, RandomizedSearchCV
from sklearn.metrics import roc_auc_score, make_scorer
import mlflow
import mlflow.sklearn
import joblib
import importlib
from mlflow_pipeline.preprocess import pandas_preprocess
from mlflow_pipeline.mlflow_utils import set_tracking, get_client

RANDOM_STATE = 42

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def import_estimator(path):
    # path is like 'xgboost.XGBClassifier' or 'lightgbm.LGBMClassifier'
    module_name, class_name = path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

def run_search(X_train, y_train, model_cfg, cv, scorer, n_jobs=1):
    EstClass = import_estimator(model_cfg["estimator"])
    param_dist = model_cfg.get("search", {}).get("param_distributions", {})
    n_iter = model_cfg.get("search", {}).get("n_iter", 25)

    base_params = model_cfg.get("fit_params", {}) or {}
    estimator = EstClass(**base_params)

    search = RandomizedSearchCV(
        estimator=estimator,
        param_distributions=param_dist,
        n_iter=n_iter,
        scoring=scorer,
        cv=cv,
        n_jobs=n_jobs,
        random_state=RANDOM_STATE,
        verbose=1,
        return_train_score=False
    )
    search.fit(X_train, y_train)
    return search

def log_search_to_mlflow(search, model_name):
    best = search.best_estimator_
    best_params = search.best_params_
    best_score = search.best_score_

    with mlflow.start_run(run_name=f"search-{model_name}") as run:
        mlflow.set_tag("search", "randomized")
        mlflow.log_param("model_name", model_name)
        mlflow.log_params(best_params)
        mlflow.log_metric("cv_score", float(best_score))

        # log the sklearn-compatible model as artifact
        mlflow.sklearn.log_model(best, artifact_path="model")
        print(f"Logged best {model_name} model to MLflow. Run id: {run.info.run_id}")
        return run.info.run_id

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/train.yaml")
    parser.add_argument("--data", default=None)
    parser.add_argument("--target", default=None)
    parser.add_argument("--tracking-uri", default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    set_tracking(args.tracking_uri or cfg.get("mlflow", {}).get("tracking_uri"))
    mlflow.set_experiment(cfg.get("mlflow", {}).get("experiment_name", "default"))

    # Load data
    data_path = args.data or cfg["data"]["path"]
    target = args.target or cfg["data"]["target"]
    if not target or target == "target":
        raise ValueError("Please provide a valid target column name in args or configs/train.yaml")

    df = pd.read_csv(data_path)
    X_train, X_test, y_train, y_test = pandas_preprocess(df, target_col=target,
                                                        test_size=cfg["data"].get("test_size", 0.2),
                                                        random_state=cfg["data"].get("random_state", 42))

    # CV and scoring
    cv = StratifiedKFold(n_splits=cfg["training"].get("cv_folds", 5), shuffle=True, random_state=RANDOM_STATE)
    scorer = make_scorer(roc_auc_score, needs_proba=True, greater_is_better=True)

    results = {}
    for model_cfg in cfg["models"]:
        if not model_cfg.get("enabled", False):
            continue
        name = model_cfg["name"]
        print(f"Starting search for {name}...")
        search = run_search(X_train, y_train, model_cfg, cv=cv, scorer=scorer, n_jobs=cfg["training"].get("n_jobs", 1))
        run_id = log_search_to_mlflow(search, name)
        # Evaluate on holdout
        preds_proba = search.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, preds_proba)
        results[name] = {"run_id": run_id, "cv_auc": float(search.best_score_), "test_auc": float(auc)}
        print(f"{name} - CV AUC: {search.best_score_:.4f}, Test AUC: {auc:.4f}")

    print("Search results summary:", results)

if __name__ == "__main__":
    main()