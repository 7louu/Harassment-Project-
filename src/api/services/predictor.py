from functools import lru_cache


@lru_cache(maxsize=1)
def get_model():
    # I made some mistakes at the start of the implementation so the preprocessing file is going to display
    # all the comments i made when the request is sent so i googled how to make it at least appear one time and then never appear again
    # and the answer was to just cache it
    from data.preprocessing import df
    from modeling.models import build_models

    dataset = df[["Text", "Label"]].dropna()
    model = build_models()["linear_svm"]
    model.fit(dataset["Text"].astype(str), dataset["Label"].astype(int))
    return model


def predict_text(text: str) -> int:
    return int(get_model().predict([text])[0])
