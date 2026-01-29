from fastapi import FastAPI, Request, HTTPException
from app.model import load_model
from app.predict import IrisFeatures, predict_class
from app.utils import is_authorized

app = FastAPI(title="Iris Classifier API", version="1.1")

model = load_model()

@app.get("/")
def read_root():
    return {"message": "Iris Classifier API is up and running!"}

@app.post("/predict")
async def predict(request: Request, iris: IrisFeatures):
    if not is_authorized(request.headers):
        raise HTTPException(status_code=401, detail="Unauthorized")

    prediction = predict_class(model, iris)
    return {"predicted_class": prediction, "model_version": "v1"}
