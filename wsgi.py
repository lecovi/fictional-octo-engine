from app.core import create_app, APP_NAME, APP_VERSION

app = create_app()

app.logger.debug(f"Running {APP_NAME} v{APP_VERSION}")