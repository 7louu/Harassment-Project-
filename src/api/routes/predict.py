from fastapi import APIRouter

from ..schemas import PredictionRequest, PredictionResponse
from ..services.predictor import predict_text


router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    label = predict_text(request.text)
    label_name = "bullying" if label == 1 else "not_bullying"
    return PredictionResponse(label=label, label_name=label_name)
