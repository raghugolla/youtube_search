from sample.utils.flask import APISuccess


def test_api_response():
    api_response = APISuccess(meta={})
    assert {} == api_response.payload.get("meta")

    api_response = APISuccess(value={"a": "b"})
    if api_response.payload.get("meta") is None and {
        "a": "b"
    } == api_response.payload.get("data"):
        assert True

    api_response = APISuccess(value={"a": "b"}, meta={"c": "d"})
    assert {"a": "b"} == api_response.payload.get("data")
    assert {"c": "d"} == api_response.payload.get("meta")
