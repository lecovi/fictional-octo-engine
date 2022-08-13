import os
from dotenv import load_dotenv
from flask import Flask

from .extensions import redis_client
from .redis.views import redis as redis_bp
from .home.views import home as home_bp


load_dotenv()
APP_VERSION = os.environ["APP_VERSION"]
APP_NAME = os.environ["APP_NAME"]

ACTIVE_ENDPOINTS = (
    (home_bp, "/"),
    (redis_bp, "/redis"),
)

def create_app():
    app = Flask(__name__)
    app.config["REDIS_URL"] =  "redis://redis:6379/0"

    redis_client.init_app(app)
    
    for blueprint, url_prefix in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
    return app

