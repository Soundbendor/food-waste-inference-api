import io

import cv2
import numpy as np
from fastapi import APIRouter, Depends, HTTPException, Response, UploadFile
from fastapi.responses import FileResponse
from starlette.requests import Request

from src.core import security
from src.models.prediction import PredictionResult
from src.services.models import YoloFoodModel

router = APIRouter()


@router.post("/predict", name="predict")
async def post_predict(
    request: Request,
    img: UploadFile,
    _: bool = Depends(security.validate_request),
):
    # use cv2 to read image in
    im_bin = await img.read()
    im_np = np.fromstring(im_bin, np.uint8)
    img_cv = cv2.imdecode(im_np, cv2.IMREAD_COLOR)
    # Make call to prediction API, return cv2 img with predictions
    # TODO: how to get state from request?
    model: YoloFoodModel = request.app.state.model
    preds: PredictionResult = model.predict(img_cv)
    _, im_png = cv2.imencode(".png", preds.img_seg)
    # TODO: try-except for this logic, catch HTTPException
    # return {"img": io.BytesIO(im_png.tobytes()).getvalue(), "results": preds.results}
    return Response(
        content=io.BytesIO(im_png.tobytes()).getvalue(),
        headers={x.name: x for x in preds.results},
        media_type="image/png",
    )
