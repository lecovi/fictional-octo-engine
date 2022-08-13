from flask import Blueprint

from app.extensions import redis_client


home = Blueprint('home', __name__)


@home.route('/')
def hello_world():
    name = redis_client.get("app_name").decode()
    version = redis_client.get("app_version").decode()

    return (
        f'Hello, World! from {name} v{version}'
    )