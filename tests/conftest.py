import pytest
from app.core import create_app


@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app


@pytest.fixture
def runner(app):
    return app.test_cli_runner()