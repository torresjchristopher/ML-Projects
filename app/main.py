"""
FastAPI app that serves a fine-tuned Hugging Face text-classification model.
Expect MODEL_DIR env var or pass model_dir to load from local directory or HF model hub path.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import os
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

MODEL_DIR = os.getenv("MODEL_DIR", None)  # e.g., outputs/distilbert-sentiment or model name on HF hub
MODEL_NAME = os.getenv("MODEL_NAME", None)  # alternative

app = FastAPI(title="NLP Model Serving")

classifier = None
label_mapping = None

class PredictRequest(BaseModel):
    text: Optional[str] = None
    texts: Optional[List[str]] = None

class PredictResponse(BaseModel):
    labels: List[str]
    scores: List[float]
    details: Optional[List[Dict[str, Any]]] = None

def get_pipeline():
    global classifier
    if classifier is None:
        model_ref = MODEL_DIR or MODEL_NAME
        if model_ref is None:
            raise RuntimeError("No MODEL_DIR or MODEL_NAME configured.")
        # load tokenizer/model then pipeline
        tokenizer = AutoTokenizer.from_pretrained(model_ref)
        model = AutoModelForSequenceClassification.from_pretrained(model_ref)
        classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, return_all_scores=False)
    return classifier

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    texts = []
    if req.text:
        texts = [req.text]
    elif req.texts:
        texts = req.texts
    else:
        raise HTTPException(status_code=400, detail="Provide `text` or `texts` in the request body.")

    pipe = get_pipeline()
    try:
        outputs = pipe(texts, truncation=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Normalize output to list of dicts
    if isinstance(outputs, dict):
        outputs = [outputs]

    labels = [o["label"] for o in outputs]
    scores = [o["score"] for o in outputs]
    details = outputs
    return PredictResponse(labels=labels, scores=scores, details=details)

@app.get("/health")
def health():
    return {"status": "ok"}