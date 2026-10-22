from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC


def build_models() -> dict:
    vectorizer_settings = {
        "lowercase": True,
        "strip_accents": "unicode",
        "ngram_range": (1, 2),
        "min_df": 2,
        "max_df": 0.95,
        "sublinear_tf": True,
    }

    return {
        "logistic_regression": Pipeline(
            [
                ("tfidf", TfidfVectorizer(**vectorizer_settings)),
                (
                    "classifier",
                    LogisticRegression(max_iter=1000, random_state=42),
                ),
            ]
        ),
        "linear_svm": Pipeline(
            [
                ("tfidf", TfidfVectorizer(**vectorizer_settings)),
                ("classifier", LinearSVC()),
            ]
        ),
    }
