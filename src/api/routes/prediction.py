import io

import cv2
import numpy as np
from fastapi import APIRouter, Depends, HTTPException, Response

from src.core import security
from src.models.prediction import PredictionResult
from src.services.models import YoloFoodModel

router = APIRouter()


@router.post("/predict", name="predict")
async def post_predict(
    img: UploadFile,
    _: bool = Depends(security.validate_request),
):
    # use cv2 to read image in
    im_bin = await img.read()
    im_np = np.fromstring(im_bin, np.uint8)
    img = cv2.imdecode(im_np, cv2.IMREAD_COLOR)
    # Make call to prediction API, return cv2 img with predictions
    model: YoloFoodModel = img.app.state.model
    preds: PredictionResult = model.predict(img)
    _, im_png = cv2.imencode(".png", preds.img_seg)
    return Response(
        content=io.BytesIO(im_png.tobytes()).getvalue(),
        headers=preds.results,
        media_type="image/png",
    )
