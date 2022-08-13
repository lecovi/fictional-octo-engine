from http import HTTPStatus

from flask import url_for
from app.extensions import redis_client


def test_values(client):
    redis_client.set("boston", "Bost0n")
    response = client.get(url_for("redis.values", key="boston"))

    assert response.status_code == HTTPStatus.OK
    assert "Bost0n" in response.text
    redis_client.delete("boston")
