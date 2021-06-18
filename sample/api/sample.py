from uuid import uuid4
from http import HTTPStatus

import requests
from flask import Blueprint
from shuttlis.serialization import serialize
from voluptuous import Schema

from sample.domain.models import User
from sample.store.repos import UserRepo
from sample.utils.flask import APISuccess, APIResponse, APIError
from sample.utils.schema import dataschema
from sample.utils.log import LOG
from sample.worker import add_task


blueprint = Blueprint("sample", __name__)


@blueprint.route("/")
def hello() -> APISuccess:
    # this adds all the fields specified inside the extra dict as attributes to the
    # logRecord object __dict__ for this log line
    LOG.info("api.hello", extra={"param1": "hey"})
    res = requests.get("http://www.google.com")
    LOG.debug("Response is: %s", res.headers)
    return APISuccess({"hello": "world"})


@blueprint.route("/health")
def health() -> APISuccess:
    return APISuccess({"data": "healthy"})


# Testing uncaught exceptions in flask app
@blueprint.route("/testexception")
def test_exception():
    LOG.debug("Inside test exception")
    raise ValueError("test error")


@blueprint.route("/testmaskpassword")
def test_mask_password() -> APISuccess:
    LOG.info(
        "test password",
        extra={"password": "This is a test pass which should be masked"},
    )
    return APISuccess({"message": "check logs for masked password"})


@blueprint.route("/users", methods=["POST"])
@dataschema(Schema({"name": str}))
def create_user(name: str) -> APISuccess:
    user = User(id=uuid4(), name=name)
    user = UserRepo().create(user)

    return APISuccess(serialize(user))


@blueprint.route("/users", methods=["GET"])
def fetch_users() -> APISuccess:
    users = UserRepo().get_all()

    return APISuccess({"users": serialize(users)})


@blueprint.route("/users/<id>")
def get_user(id: str) -> APIResponse:
    user = UserRepo().get(id)
    if not user:
        return APIError(
            error_type="NOT_FOUND",
            error_message="User not found",
            status=HTTPStatus.NOT_FOUND,
        )

    return APISuccess(serialize(user))


@blueprint.route("/create_random_users/<int:n_users>", methods=["GET"])
def create_random_users(n_users: int) -> APISuccess:
    print("here")
    add_task("create_random_users", n_users=n_users)
    return APISuccess({"task": "queued"})
