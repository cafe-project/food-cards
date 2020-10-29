import json

from django.core.handlers.wsgi import WSGIRequest


def parse_json_from_request_data(request: WSGIRequest) -> dict:
    if not request.data:
        raise AssertionError('Empty HTTP body')

    try:
        parameters = request.data  # type: dict
    except Exception as ex:
        raise Exception(ex)

    return parameters


def parse_json_from_request(request: WSGIRequest) -> dict:
    if not request.body:
        return {}

    try:
        parameters = json.loads(request.body.decode('UTF-8'))  # type: dict
    except Exception as ex:
        raise Exception(str(ex))

    return parameters
