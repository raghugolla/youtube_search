from http import HTTPStatus

from flask import json, Response, Flask


class APIFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, APIResponse):
            return rv.to_json()
        if isinstance(rv, APIError):
            return rv.to_json()
        return super(APIFlask, self).make_response(rv)


class APIResponse:
    def __init__(self, value=None, status=HTTPStatus.OK, meta=None):
        if meta is None:
            self.payload = {"data": value}
        else:
            self.payload = {"data": value, "meta": meta}
        self.status = status

    def to_json(self):
        return Response(
            json.dumps(self.payload), status=self.status, mimetype="application/json"
        )


class APIError:
    def __init__(self, error=None, status=HTTPStatus.INTERNAL_SERVER_ERROR):
        self.payload = {"error": error}
        self.status = status

    def to_json(self):
        return Response(
            json.dumps(self.payload), status=self.status, mimetype="application/json"
        )


class ValidationException(Exception):
    def __init__(self, message, status=HTTPStatus.BAD_REQUEST):
        self.message = message
        self.status = status

    def to_json(self):
        payload = {"message": self.message, "type": "VALIDATION_EXCEPTION"}
        return APIError(payload, status=self.status)
