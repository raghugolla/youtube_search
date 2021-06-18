from http import HTTPStatus

import pytest

from sample.utils.flask import APIFlask


@pytest.mark.integration
def test_hello_world_is_returned(app: APIFlask):
    with app.test_client() as client:
        response = client.get("/")
        data = response.get_json()["data"]
        assert HTTPStatus.OK == response.status_code
        assert "world" == data["hello"]


@pytest.mark.integration
def test_create_and_fetch_user(app: APIFlask):
    with app.test_client() as client:
        response = client.post("/users", json={"name": "hey"})
        assert HTTPStatus.OK == response.status_code

    user_id = response.get_json()["data"]["id"]

    with app.test_client() as client:
        response = client.get("/users/%s" % user_id)
        assert HTTPStatus.OK == response.status_code

    name = response.get_json()["data"]["name"]
    assert name == "hey"
