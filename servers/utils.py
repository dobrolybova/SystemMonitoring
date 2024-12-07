from functools import wraps
from json import JSONDecodeError

from aiohttp import web
from aiohttp.web_response import json_response


def response_wrapper(payload: bool):
    def payload_wrapper(resp_func):
        @wraps(resp_func)
        async def resp(*args, **kwargs):
            response, status = await resp_func(*args, **kwargs)
            return json_response(response.json(), status=status)
        return resp

    def wrapper(resp_func):
        @wraps(resp_func)
        async def resp(*args, **kwargs):
            status = await resp_func(*args, **kwargs)
            return json_response(status=status)
        return resp

    if payload:
        return payload_wrapper
    return wrapper


async def get_body_from_request(request: web.Request) -> dict | str:
    try:
        return await request.json()
    except JSONDecodeError:
        return await request.text()
