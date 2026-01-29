import os
import joblib

MODEL_VERSION = "v1"
MODEL_PATH = f"model/iris_clf_{MODEL_VERSION}.pkl"

def load_model():
    return joblib.load(MODEL_PATH)
