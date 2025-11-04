"""
Preprocessing utilities. This module contains both Pandas-based
and a template for PySpark-based transforms for scale.
"""
from typing import Tuple, List
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
from pathlib import Path

ARTIFACTS_DIR = Path("artifacts")
ARTIFACTS_DIR.mkdir(exist_ok=True)

def pandas_preprocess(df: pd.DataFrame, target_col: str, test_size=0.2, random_state=42):
    # Basic example preprocessing:
    # - Fill missing values
    # - One-hot encode categorical (placeholder)
    df = df.copy()
    # Simple imputation
    for c in df.select_dtypes(include=["number"]).columns:
        df[c] = df[c].fillna(df[c].median())
    for c in df.select_dtypes(include=["object","category"]).columns:
        df[c] = df[c].fillna("MISSING")

    # TODO: proper encoding pipeline; for now use pandas.get_dummies
    X = df.drop(columns=[target_col])
    y = df[target_col].astype(int)

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
    # Standard scale numeric columns
    scaler = StandardScaler()
    X_train[X_train.select_dtypes(include=["number"]).columns] = scaler.fit_transform(X_train.select_dtypes(include=["number"]))
    X_test[X_test.select_dtypes(include=["number"]).columns] = scaler.transform(X_test.select_dtypes(include=["number"]))

    joblib.dump(scaler, ARTIFACTS_DIR/"scaler.joblib")
    print("Saved scaler to artifacts/scaler.joblib")
    return X_train, X_test, y_train, y_test

# Placeholder for PySpark pipeline
def pyspark_preprocess(spark, input_path: str, output_path: str):
    """
    Load parquet / CSV via spark, perform distributed feature engineering,
    and write out processed data for training.
    """
    df = spark.read.option("header", True).csv(input_path)
    # Implement transformations using Spark DataFrame APIs
    df = df.na.fill({"some_numeric_col": 0})
    df.write.mode("overwrite").parquet(output_path)
    print(f"Wrote processed data to {output_path}")