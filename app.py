import os
import redis
from dotenv import load_dotenv
from flask import Flask
from flask_redis import FlaskRedis


load_dotenv()
APP_VERSION = os.environ["APP_VERSION"]
APP_NAME = os.environ["APP_NAME"]


r = redis.Redis(host="redis", port=6379, db=0)
r.set("app_name", APP_NAME)
r.set("app_version", APP_VERSION)
r.set("foo", "f00")
r.set("bar", "b4r")
r.set("baz", "b4z")


app = Flask(__name__)
app.config["REDIS_URL"] =  "redis://redis:6379/0"

redis_client = FlaskRedis(app)

app.logger.debug(f"Running {APP_NAME} v{APP_VERSION}")


@app.route('/')
def hello_world():
    name = redis_client.get("app_name").decode()
    version = redis_client.get("app_version").decode()

    return (
        f'Hello, World! from {name} v{version}'
    )
