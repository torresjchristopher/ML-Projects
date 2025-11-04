"""
Auto-register best model from an MLflow experiment into the Model Registry.

Usage:
    python mlflow_pipeline/auto_register.py --experiment-name e2e-ml-experiments --metric test_auc --model-name MyModel --stage Staging --ascending false --top-k 1

Notes:
- Requires MLflow tracking server reachable via MLFLOW_TRACKING_URI env var or provide --tracking-uri
- Will attempt to create the registered model if it does not exist
- Will register the best run's artifact path 'model' by default; adjust --model-path if needed
"""
import argparse
import os
from mlflow.tracking import MlflowClient
import mlflow

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment-name", required=True)
    parser.add_argument("--metric", default="test_auc")
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--stage", default="Staging", choices=["None","NoneStage","Staging","Production","Archived","None"])
    parser.add_argument("--tracking-uri", default=None)
    parser.add_argument("--model-path", default="model")
    parser.add_argument("--ascending", action="store_true", help="Lower metric is better")
    parser.add_argument("--top-k", type=int, default=1)
    return parser.parse_args()

def main():
    args = parse_args()

    if args.tracking_uri:
        mlflow.set_tracking_uri(args.tracking_uri)
    # else rely on env var MLFLOW_TRACKING_URI or default

    client = MlflowClient(tracking_uri=mlflow.get_tracking_uri())
    exp = client.get_experiment_by_name(args.experiment_name)
    if exp is None:
        raise RuntimeError(f"Experiment {args.experiment_name} not found in MLflow at {mlflow.get_tracking_uri()}")

    experiment_id = exp.experiment_id

    # Fetch runs - summary: use search_runs; specify metric filter if desired
    runs = client.search_runs(
        experiment_ids=[experiment_id],
        filter_string="",
        run_view_type=1,  # ACTIVE_ONLY
        max_results=1000,
    )

    # Filter runs that have the metric
    runs_with_metric = [r for r in runs if args.metric in r.data.metrics]

    if not runs_with_metric:
        raise RuntimeError(f"No runs found with metric {args.metric} in experiment {args.experiment_name}")

    # Sort by metric
    runs_sorted = sorted(runs_with_metric, key=lambda r: r.data.metrics.get(args.metric, float("-inf")), reverse=not args.ascending)

    registered_versions = []
    for r in runs_sorted[: args.top_k]:
        run_id = r.info.run_id
        model_uri = f"runs:/{run_id}/{args.model_path}"
        # Create registered model if needed
        try:
            client.create_registered_model(args.model_name)
        except Exception:
            # if already exists, ignore
            pass
        # Create model version
        mv = client.create_model_version(name=args.model_name, source=model_uri, run_id=run_id)
        registered_versions.append({"run_id": run_id, "version": mv.version, "model_uri": model_uri})
        # Transition to stage if requested and supported
        try:
            if args.stage and args.stage != "None":
                client.transition_model_version_stage(
                    name=args.model_name,
                    version=mv.version,
                    stage=args.stage,
                    archive_existing_versions=False
                )
        except Exception as e:
            print(f"Warning: could not transition model version {mv.version} to stage {args.stage}: {e}")

    print("Registered versions:", registered_versions)

if __name__ == "__main__":
    main()