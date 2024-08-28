import numpy as np
from ultralytics import YOLO

from src.models.prediction import PredictionResult


class YoloFoodModel:
    def __init__(self, model_path: str) -> None:
        self.yolo = YOLO(model_path)

    def predict(self, payload: np.ndarray) -> PredictionResult:
        result = self.yolo.predict(payload)[0]
        # Plot segmentations on image
        im_seg = result.plot()
        return PredictionResult(im_seg, result.to_json())
