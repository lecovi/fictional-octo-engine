from flask_redis import FlaskRedis
from authlib.integrations.flask_client import OAuth


redis_client = FlaskRedis()
oauth = OAuth()