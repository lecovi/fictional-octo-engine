import os

from dotenv import load_dotenv
from flask import Flask

from .extensions import redis_client, db, login
from .redis.views import redis_bp
from .home.views import home as home_bp
from .db.cli import db_cli
from .db.models import User
from .constants import GOOGLE_DISCOVERY_URL


load_dotenv()

ACTIVE_ENDPOINTS = (
    (home_bp, "/"),
    (redis_bp, "/redis"),
)


def create_app():
    app = Flask(__name__)
    app.config["REDIS_URL"] =  "redis://redis:6379/0"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.secret_key = os.getenv("SECRET_KEY")

    redis_client.init_app(app)
    db.init_app(app)
    login.init_app(app)
    
    for blueprint, url_prefix in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url_prefix)

    app.cli.add_command(db_cli)

    return app


@login.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()