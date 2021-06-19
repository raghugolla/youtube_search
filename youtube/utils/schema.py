from functools import wraps
from http import HTTPStatus
from typing import Callable

from flask import request
from stringcase import snakecase
from voluptuous import Invalid, Schema

from youtube.utils.flask import APIError, APIResponse


def _mk_error_payload(e: Invalid) -> APIError:
    path = ".".join(str(k) for k in e.path)
    type = "VALIDATION_EXCEPTION"
    message = f"Invalid data: {e.msg} (path {path})"
    return APIError(
        error_type=type, error_message=message, status=HTTPStatus.BAD_REQUEST
    )


def dataschema(schema: Schema) -> Callable[[Schema], Callable[[Callable], Callable]]:
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def new_func(*args, **kwargs) -> APIResponse:
            try:
                parsed_json = request.get_json()
                valid_dict = schema(parsed_json)
                snaked_kwargs = {snakecase(k): v for k, v in valid_dict.items()}
                kwargs.update(snaked_kwargs)
            except Invalid as e:
                return _mk_error_payload(e)
            return f(*args, **kwargs)

        return new_func

    return decorator


def queryschema(schema: Schema) -> Callable[[Schema], Callable[[Callable], Callable]]:
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def new_func(*args, **kwargs) -> APIResponse:
            try:
                parsed_query_string = request.args.to_dict()
                valid_dict = schema(parsed_query_string)
                snaked_kwargs = {snakecase(k): v for k, v in valid_dict.items()}
                kwargs.update(snaked_kwargs)
            except Invalid as e:
                return _mk_error_payload(e)
            return f(*args, **kwargs)

        return new_func

    return decorator
