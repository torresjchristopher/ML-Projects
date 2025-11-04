import os
import shutil
from pathlib import Path
import pandas as pd
import joblib
import tempfile

from mlflow_pipeline.preprocess import pandas_preprocess, ARTIFACTS_DIR

def test_pandas_preprocess_creates_scaler_and_splits():
    # Create a tiny synthetic dataframe
    df = pd.DataFrame({
        "num1": [1.0, 2.0, 3.0, None],
        "num2": [4.0, None, 6.0, 8.0],
        "cat": ["a", "b", "a", None],
        "target": [0, 1, 0, 1]
    })

    # Ensure artifacts directory is isolated
    tmpdir = tempfile.mkdtemp()
    orig_artifacts = ARTIFACTS_DIR
    try:
        # Monkey-patch artifacts dir if needed
        # (The code uses ARTIFACTS_DIR from preprocess; ensure it's writable)
        Path(tmpdir).mkdir(exist_ok=True)
        X_train, X_test, y_train, y_test = pandas_preprocess(df, target_col="target", test_size=0.25, random_state=1)
        # Check shapes
        assert len(X_train) > 0
        assert len(X_test) > 0
        assert len(y_train) > 0
        assert len(y_test) > 0
        # Check scaler exists in artifacts
        scaler_path = Path("artifacts") / "scaler.joblib"
        assert scaler_path.exists(), f"Expected scaler at {scaler_path}"
        # Load scaler
        scaler = joblib.load(scaler_path)
        assert scaler is not None
    finally:
        # cleanup artifacts
        if Path("artifacts").exists():
            try:
                shutil.rmtree("artifacts")
            except Exception:
                pass