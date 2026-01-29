#!/usr/bin/env python3
"""
Fine-tune a transformer model (text classification) using Hugging Face Trainer and log artifacts/metrics to MLflow.

Usage example:
python train.py \
  --model_name_or_path distilbert-base-uncased \
  --data_file data/dataset.csv \
  --text_col text \
  --label_col label \
  --output_dir outputs/distilbert-sentiment \
  --num_train_epochs 3 \
  --per_device_train_batch_size 16 \
  --mlflow_uri http://localhost:5000
"""
import argparse
import os
import random
import json
from pathlib import Path
import pandas as pd
import numpy as np
import yaml
import mlflow
from mlflow_utils import set_tracking, ensure_experiment

from datasets import load_dataset, Dataset, DatasetDict
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    TrainingArguments,
    Trainer,
)
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="configs/train_config.yaml")
    parser.add_argument("--model_name_or_path", type=str, default=None)
    parser.add_argument("--data_file", type=str, default=None, help="CSV file with text/label columns")
    parser.add_argument("--text_col", type=str, default=None)
    parser.add_argument("--label_col", type=str, default=None)
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--num_train_epochs", type=int, default=None)
    parser.add_argument("--per_device_train_batch_size", type=int, default=None)
    parser.add_argument("--mlflow_uri", type=str, default=None)
    args = parser.parse_args()
    return args

def load_csv_dataset(path, text_col, label_col):
    df = pd.read_csv(path)
    # Keep only the specified columns
    df = df[[text_col, label_col]].dropna()
    return Dataset.from_pandas(df.reset_index(drop=True))

def prepare_datasets(args, cfg):
    # load or split dataset
    text_col = args.text_col or cfg["data"]["text_col"]
    label_col = args.label_col or cfg["data"]["label_col"]

    if args.data_file:
        ds = load_csv_dataset(args.data_file, text_col, label_col)
        # split into train/validation
        ds = ds.train_test_split(test_size=0.1, seed=cfg["training"]["seed"])
        return DatasetDict({"train": ds["train"], "validation": ds["test"]})
    else:
        # try loading train/validation files from config
        train_file = cfg["data"].get("train_file")
        val_file = cfg["data"].get("validation_file")
        if Path(train_file).exists() and Path(val_file).exists():
            train_ds = load_csv_dataset(train_file, text_col, label_col)
            val_ds = load_csv_dataset(val_file, text_col, label_col)
            return DatasetDict({"train": train_ds, "validation": val_ds})
        else:
            raise ValueError("No dataset provided. Provide --data_file or update configs/train_config.yaml")

def tokenize_function(examples, tokenizer, text_col, max_length):
    return tokenizer(examples[text_col], truncation=True, max_length=max_length)

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    acc = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds, average="weighted")
    precision = precision_score(labels, preds, average="weighted", zero_division=0)
    recall = recall_score(labels, preds, average="weighted", zero_division=0)
    return {"accuracy": acc, "f1": f1, "precision": precision, "recall": recall}

def main():
    args = parse_args()
    cfg = yaml.safe_load(open(args.config, "r"))

    # Override config with CLI args
    model_name = args.model_name_or_path or cfg["model"]["model_name_or_path"]
    output_dir = args.output_dir or Path(cfg["output"]["output_dir"]) / Path(model_name).name
    output_dir = str(output_dir)
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    num_train_epochs = args.num_train_epochs or cfg["training"]["num_train_epochs"]
    per_device_train_batch_size = args.per_device_train_batch_size or cfg["training"]["per_device_train_batch_size"]
    max_seq_length = cfg["training"].get("max_seq_length", 128)
    learning_rate = cfg["training"].get("learning_rate", 5e-5)
    weight_decay = cfg["training"].get("weight_decay", 0.01)
    seed = cfg["training"].get("seed", 42)

    # MLflow
    tracking = args.mlflow_uri or cfg["mlflow"].get("tracking_uri")
    set_tracking(tracking)
    exp_name = cfg["mlflow"].get("experiment_name", "nlp-finetune")
    ensure_experiment(exp_name)
    mlflow.set_experiment(exp_name)

    # Load data
    ds_dict = prepare_datasets(args, cfg)

    # Label mapping (if labels are not ints)
    labels = list({l for l in ds_dict["train"][cfg["data"]["label_col"]]})
    # If labels are scalar ints already, skip mapping
    if all(isinstance(x, (int, np.integer)) for x in labels):
        label2id = None
        num_labels = len(set(labels))
    else:
        labels_sorted = sorted(list(set(labels)))
        label2id = {l: i for i, l in enumerate(labels_sorted)}
        num_labels = len(labels_sorted)
        # map labels in datasets
        def map_label(example):
            example[cfg["data"]["label_col"]] = label2id[example[cfg["data"]["label_col"]]]
            return example
        ds_dict = ds_dict.map(map_label)

    # Tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

    # Tokenize
    text_col = args.text_col or cfg["data"]["text_col"]
    ds_tokenized = ds_dict.map(lambda examples: tokenize_function(examples, tokenizer, text_col, max_seq_length), batched=True)

    # Set format for PyTorch
    label_col = args.label_col or cfg["data"]["label_col"]
    ds_tokenized = ds_tokenized.remove_columns([c for c in ds_tokenized["train"].column_names if c not in (text_col, label_col, "input_ids", "attention_mask", "token_type_ids")])
    ds_tokenized.set_format(type="torch", columns=["input_ids", "attention_mask", label_col])

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        logging_strategy="steps",
        logging_steps=50,
        per_device_train_batch_size=per_device_train_batch_size,
        per_device_eval_batch_size=cfg["training"]["per_device_eval_batch_size"],
        num_train_epochs=num_train_epochs,
        learning_rate=learning_rate,
        weight_decay=weight_decay,
        seed=seed,
        load_best_model_at_end=True,
        metric_for_best_model="eval_f1",
        greater_is_better=True,
        save_total_limit=3,
        report_to="none",  # disable HF hub logging
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=ds_tokenized["train"],
        eval_dataset=ds_tokenized["validation"],
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )

    # Start MLflow run and log params
    with mlflow.start_run():
        # Log params
        mlflow.log_param("model_name_or_path", model_name)
        mlflow.log_param("num_train_epochs", num_train_epochs)
        mlflow.log_param("per_device_train_batch_size", per_device_train_batch_size)
        mlflow.log_param("max_seq_length", max_seq_length)
        mlflow.log_param("learning_rate", learning_rate)

        # Train
        trainer.train()

        # Evaluate
        metrics = trainer.evaluate()
        # clean metrics for mlflow
        for k, v in metrics.items():
            try:
                mlflow.log_metric(k.replace("/", "_"), float(v))
            except Exception:
                pass

        # Save model & tokenizer
        trainer.save_model(output_dir)
        tokenizer.save_pretrained(output_dir)

        # Log artifacts
        mlflow.log_artifacts(output_dir)
        # Save training args as json
        with open(Path(output_dir) / "train_args.json", "w") as f:
            json.dump(training_args.to_dict(), f, indent=2)
        mlflow.log_artifact(str(Path(output_dir) / "train_args.json"))

    print(f"Training finished. Model saved to {output_dir}")

if __name__ == "__main__":
    main()