import logging
from typing import Callable

from fastapi import FastAPI

from src.core.config import MODEL_PATH
from src.services.models import YoloFoodModel

logger = logging.getLogger(__name__)


def _startup_model(app: FastAPI) -> None:
    app.state.model = YoloFoodModel(MODEL_PATH)


def _shutdown_model(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        _startup_model(app)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)

    return shutdown
