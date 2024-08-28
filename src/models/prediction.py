from typing import Any

import numpy as np
from pydantic import BaseModel, Json


class PredictionResult(BaseModel):
    img_seg: np.ndarray
    results: str

    class Config:
        arbitrary_types_allowed = True
