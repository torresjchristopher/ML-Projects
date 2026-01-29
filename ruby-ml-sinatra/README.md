# Sentiment Analysis Blog Post Filter

This is a lightweight blog app where users submit posts, and the sentiment (positive, neutral, or negative) is automatically analyzed using a Python ML model.

## Components

- **Ruby Sinatra App** — Handles the frontend and blog post submission
- **Python FastAPI App** — Analyzes sentiment using TextBlob

## Getting Started

### 1. Python API (ML)

"```bash
cd ml_api
pip install -r requirements.txt
uvicorn main:app --reload --port 8000"
