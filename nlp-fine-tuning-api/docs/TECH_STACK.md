```markdown
# Technology Stack — End-to-End MLOps Template

This repository uses the following primary technologies and responsibilities:

- Python 3.9 — primary runtime
- Data: pandas, numpy, PySpark (for scale)
- Modeling: scikit-learn, XGBoost, LightGBM, CatBoost, Hugging Face Transformers (PyTorch)
- Experiment tracking & model registry: MLflow
- Hyperparameter optimization: Optuna (optional)
- Serving: FastAPI (uvicorn), Docker containers, Kubernetes manifests
- CI/CD: GitHub Actions (lint/tests/build/publish/deploy)
- Testing: pytest, nbval (for notebooks)
- Dev tooling: pre-commit hooks (Black, isort, flake8, nbstripout)
- Monitoring suggestions: Prometheus, Grafana; logging to a centralized store (ELK, Cloud Logging)