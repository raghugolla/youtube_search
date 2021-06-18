from abc import ABC, abstractmethod
from http import HTTPStatus
from typing import Dict, Union

from flask import Flask, Response, json


class APIResponse(ABC):
    def __init__(self, status: HTTPStatus):
        self.status = status

    @property
    @abstractmethod
    def payload(self) -> Dict:
        pass

    def to_json(self) -> Response:
        return Response(
            json.dumps(self.payload), status=self.status, mimetype="application/json"
        )


class APISuccess(APIResponse):
    def __init__(
        self, value: Dict = None, status: HTTPStatus = HTTPStatus.OK, meta: Dict = None
    ):
        if meta is None:
            self._payload = {"data": value}
        else:
            self._payload = {"data": value, "meta": meta}
        super().__init__(status)

    @property
    def payload(self) -> Dict:
        return self._payload


class APIError(APIResponse):
    def __init__(
        self,
        error_type: str = None,
        error_message: str = None,
        status: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR,
    ):
        self._error = {"error": {"type": error_type, "message": error_message}}
        self.status = status

    @property
    def payload(self) -> Dict:
        return self._error


class APIFlask(Flask):
    def make_response(self, rv: Union[Response, APISuccess, APIError]) -> Response:
        if isinstance(rv, APIResponse):
            return rv.to_json()
        return super(APIFlask, self).make_response(rv)
