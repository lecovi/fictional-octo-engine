import os
import click
import redis
from flask import Blueprint, current_app

from app.extensions import redis_client


redis_bp = Blueprint('redis', __name__, cli_group='redis')


@redis_bp.route('/<key>')
def values(key):
    value = redis_client.get(key)

    if value is not None:
        value = value.decode()
    else:
        return f'Not found value for "{key}" in Redis'

    return (
        f'From Redis {key}={value}'
    )


@redis_bp.cli.command('init')
def init():
    r = redis.Redis(host="redis", port=6379, db=0)
    r.set("app_name", os.getenv("APP_NAME"))
    r.set("app_version", os.getenv("APP_VERSION"))
    r.set("foo", "f00")
    r.set("bar", "b4r")
    r.set("baz", "b4z")
    current_app.logger.debug("Initializing redis")


@redis_bp.cli.command('flush')
def flush():
    r = redis.Redis(host="redis", port=6379, db=0)
    r.flushdb()
    current_app.logger.debug("Redis DB flushed")


@redis_bp.cli.command('add')
@click.argument('key')
@click.argument('value')
def add(key, value):
    r = redis.Redis(host="redis", port=6379, db=0)
    r.set(key, value)
    current_app.logger.debug(f"Added {key}:{value} to redis")


@redis_bp.cli.command('remove')
@click.argument('key')
def remove(key):
    r = redis.Redis(host="redis", port=6379, db=0)
    r.delete(key)
    current_app.logger.debug(f"Removing {key} from redis")


@redis_bp.cli.command('get')
@click.argument('key')
def get(key):
    r = redis.Redis(host="redis", port=6379, db=0)
    value = r.get(key)
    if value is not None:
        current_app.logger.debug(f"{key} = {value} in redis")
    else:
        current_app.logger.debug(f"No value for '{key}' in redis")