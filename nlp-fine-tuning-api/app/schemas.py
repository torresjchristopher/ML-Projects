from pydantic import BaseModel
from typing import Dict, Any

class PredictRequest(BaseModel):
    inputs: Dict[str, Any]

class PredictResponse(BaseModel):
    prediction: float
    probability: float = None