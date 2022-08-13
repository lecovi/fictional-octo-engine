from flask import Blueprint

from app.extensions import redis_client


redis = Blueprint('redis', __name__)


@redis.route('/<key>')
def values(key):
    value = redis_client.get(key)

    if value is not None:
        value = value.decode()
    else:
        return f'Not found value for "{key}" in Redis'

    return (
        f'From Redis {key}={value}'
    )
