from fastapi import APIRouter, Depends
from fastapi_skeleton.core import security
from fastapi_skeleton.models.payload import HousePredictionPayload
from fastapi_skeleton.models.prediction import HousePredictionResult
from fastapi_skeleton.services.models import HousePriceModel
from starlette.requests import Request

router = APIRouter()


# TODO: figure out response_model?
# @router.post("/predict", response_model=HousePredictionResult, name="predict")
@router.post("/predict", name="predict")
# TODO: add return type
def post_predict(
    img: HousePredictionPayload,
    _: bool = Depends(security.validate_request),
):
    pass
    # model: HousePriceModel = request.app.state.model
    # prediction: HousePredictionResult = model.predict(block_data)
    #
    # return prediction
