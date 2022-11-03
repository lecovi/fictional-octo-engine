import os

from dotenv import load_dotenv
from flask import Flask

from .extensions import redis_client, oauth
from .redis.views import redis_bp
from .home.views import home as home_bp


load_dotenv()

ACTIVE_ENDPOINTS = (
    (home_bp, "/"),
    (redis_bp, "/redis"),
)

def create_app():
    app = Flask(__name__)
    app.config["REDIS_URL"] =  "redis://redis:6379/0"
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    redis_client.init_app(app)

    redis_client.set("app_name", os.getenv("APP_NAME"))
    redis_client.set("app_version", os.getenv("APP_VERSION"))

    oauth.init_app(app)

    oauth.register(
        "auth0",
        client_id=os.getenv("AUTH0_CLIENT_ID"),
        client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
        client_kwargs={
            "scope": "openid profile email",
        },
        server_metadata_url=(
            f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/openid-configuration'
        )
    )
    
    for blueprint, url_prefix in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
    return app

