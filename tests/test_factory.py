import os
from http import HTTPStatus

from flask import url_for


def test_factory_testing(app):
    assert app.testing


def test_home(client):
    response = client.get(url_for("home.hello_world"))
    
    APP_VERSION = os.environ["APP_VERSION"]
    APP_NAME = os.environ["APP_NAME"]
    
    assert response.status_code == HTTPStatus.OK
    assert APP_NAME in response.text
    assert APP_VERSION in response.text