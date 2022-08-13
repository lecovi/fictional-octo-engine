import click
from flask.cli import AppGroup
import redis

from app.core import create_app, APP_NAME, APP_VERSION


app = create_app()


redis_cli = AppGroup('redis')


@redis_cli.command('init')
def init():
    r = redis.Redis(host="redis", port=6379, db=0)
    r.set("app_name", APP_NAME)
    r.set("app_version", APP_VERSION)
    r.set("foo", "f00")
    r.set("bar", "b4r")
    r.set("baz", "b4z")
    app.logger.debug("Initializing redis")


@redis_cli.command('flush')
def flush():
    r = redis.Redis(host="redis", port=6379, db=0)
    r.flushdb()
    app.logger.debug("Redis DB flushed")


@redis_cli.command('add')
@click.argument('key')
@click.argument('value')
def add(key, value):
    r = redis.Redis(host="redis", port=6379, db=0)
    r.set(key, value)
    app.logger.debug(f"Added {key}:{value} to redis")


@redis_cli.command('remove')
@click.argument('key')
def remove(key):
    r = redis.Redis(host="redis", port=6379, db=0)
    r.delete(key)
    app.logger.debug(f"Removing {key} from redis")


@redis_cli.command('get')
@click.argument('key')
def get(key):
    r = redis.Redis(host="redis", port=6379, db=0)
    value = r.get(key)
    if value is not None:
        app.logger.debug(f"{key} = {value} in redis")
    else:
        app.logger.debug(f"No value for '{key}' in redis")


app.cli.add_command(redis_cli)

app.logger.debug(f"Running {APP_NAME} v{APP_VERSION}")