"""
FastAPI app to serve an MLflow model.
- Config via environment variables:
  - MODEL_URI or MODEL_NAME
  - MLFLOW_TRACKING_URI
"""
from fastapi import FastAPI, HTTPException
from app.schemas import PredictRequest, PredictResponse
from app.model_loader import load_model
import os
import pandas as pd

app = FastAPI(title="E2E ML Pipeline - Model Serving")

MODEL_URI = os.getenv("MODEL_URI")  # runs:/<run_id>/model or models:/<name>/Production
MODEL_NAME = os.getenv("MODEL_NAME")

# Lazy load
_model = None

def get_model():
    global _model
    if _model is None:
        if MODEL_URI:
            _model = load_model(model_uri=MODEL_URI)
        elif MODEL_NAME:
            _model = load_model(registered_name=MODEL_NAME)
        else:
            raise RuntimeError("No model configured. Set MODEL_URI or MODEL_NAME env variable.")
    return _model

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    model = get_model()
    try:
        # Expect inputs as single row dict; convert to DataFrame
        df = pd.DataFrame([req.inputs])
        preds = model.predict(df)
        # For pyfunc models, predict may return probabilities or labels
        pred = float(preds[0])
        return PredictResponse(prediction=pred)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}