import numpy as np
from pydantic import BaseModel


class PredictionResult(BaseModel):
    img_seg: np.ndarray
    results: dict

    class Config:
        arbitrary_types_allowed = True
