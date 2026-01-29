#!/usr/bin/env python3
"""
Entrypoint to run the FastAPI app (app.main).
Usage:
  python serve.py --model_dir outputs/distilbert-sentiment --port 8080
"""
import argparse
import os
import uvicorn

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_dir", type=str, default=None)
    parser.add_argument("--port", type=int, default=8080)
    parser.add_argument("--host", type=str, default="0.0.0.0")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    if args.model_dir:
        os.environ["MODEL_DIR"] = args.model_dir
    # run uvicorn with app.main:app
    uvicorn.run("app.main:app", host=args.host, port=args.port, reload=False)

if __name__ == "__main__":
    main()