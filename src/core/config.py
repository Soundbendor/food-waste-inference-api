from starlette.config import Config
from starlette.datastructures import Secret

APP_VERSION = "0.2.0"
APP_NAME = "Binsight CV"
API_PREFIX = "/api"

config = Config(".env")

API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)

MODEL_PATH: str = ""
