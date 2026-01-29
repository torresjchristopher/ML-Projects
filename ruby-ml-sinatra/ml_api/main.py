from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from model import predict_sentiment

app = FastAPI()

# Enable CORS (optional if separate ports/hosts)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/sentiment")
async def get_sentiment(request: Request):
    data = await request.json()
    text = data.get("text", "")
    sentiment = predict_sentiment(text)
    return {"sentiment": sentiment}
