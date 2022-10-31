from oauthlib.oauth2 import WebApplicationClient
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .helpers import get_credentials


redis_client = FlaskRedis()
db = SQLAlchemy()
login = LoginManager()

credentials = get_credentials()
client = WebApplicationClient(credentials["web"]["client_id"])
