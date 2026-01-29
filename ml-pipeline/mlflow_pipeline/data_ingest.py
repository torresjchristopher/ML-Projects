"""
Utilities to download / ingest Kaggle or public tabular datasets.
Replace `DATA_URL` or integrate Kaggle API as needed.
"""
import os
import argparse
import pandas as pd
from pathlib import Path

DEFAULT_DIR = Path("data")
DEFAULT_DIR.mkdir(exist_ok=True)

def download_csv(url: str, out_path: str):
    out = Path(out_path)
    if out.exists():
        print(f"{out} already exists.")
        return out
    print(f"Downloading {url} -> {out}")
    df = pd.read_csv(url)
    df.to_csv(out, index=False)
    return out

def load_local(path: str):
    return pd.read_csv(path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, help="CSV URL to download", required=True)
    parser.add_argument("--out", type=str, default=str(DEFAULT_DIR/"dataset.csv"))
    args = parser.parse_args()
    download_csv(args.url, args.out)

if __name__ == "__main__":
    main()