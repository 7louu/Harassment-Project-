import time
import pandas as pd
from typing import Dict
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

from sklearn.model_selection import train_test_split
from src.data.preprocessing import df
from src.modeling.models import build_models

def load_data(dataframe: pd.DataFrame):
    required_columns = {"Text", "Label"}
    missing_columns = required_columns.difference(dataframe.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    dataset = dataframe[["Text", "Label"]].dropna()
    texts = dataset["Text"].astype(str)
    labels = dataset["Label"].astype(int)

    if not labels.isin({0, 1}).all():
        raise ValueError("The Label column must contain only 0 and 1")

    return texts, labels


def evaluate_model(model, x_test, y_test) -> Dict:
    predictions = model.predict(x_test)

    if hasattr(model, "predict_proba"):
        scores = model.predict_proba(x_test)[:, 1]
    else:
        scores = model.decision_function(x_test)

    print(classification_report(y_test, predictions, zero_division=0))
    print("Confusion matrix:")
    print(confusion_matrix(y_test, predictions))

    return {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, zero_division=0),
        "recall": recall_score(y_test, predictions, zero_division=0),
        "f1_score": f1_score(y_test, predictions, zero_division=0),
        "roc_auc": roc_auc_score(y_test, scores),
    }


def main():
    texts, labels = load_data(df)
    x_train, x_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42, stratify=labels)

    results = []
    for model_name, model in build_models().items():
        start_time = time.perf_counter()
        model.fit(x_train, y_train)
        training_time = time.perf_counter() - start_time

        metrics = evaluate_model(model, x_test, y_test)
        results.append(
            {
                "model": model_name,
                **metrics,
                "training_time_seconds": training_time,
            }
        )

    comparison = (pd.DataFrame(results).sort_values("f1_score", ascending=False).reset_index(drop=True))
    print(comparison.to_string(index=False))
    return comparison


if __name__ == "__main__":
    main()
