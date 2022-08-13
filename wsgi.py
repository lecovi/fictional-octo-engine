import os

from app.core import create_app

APP_VERSION = os.environ["APP_VERSION"]
APP_NAME = os.environ["APP_NAME"]

app = create_app()

app.logger.debug(f"Running {APP_NAME} v{APP_VERSION}")