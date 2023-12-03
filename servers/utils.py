from functools import wraps
from json import JSONDecodeError

from aiohttp import web
from aiohttp.web_response import json_response


def response_wrapper(payload: bool):
    def payload_wrapper(resp_func):
        @wraps(resp_func)
        async def foo(*args, **kwargs):
            r, status = await resp_func(*args, **kwargs)
            return json_response(r.json(), status=status)
        return foo

    def wrapper(resp_func):
        @wraps(resp_func)
        async def foo(*args, **kwargs):
            status = await resp_func(*args, **kwargs)
            return json_response(status=status)
        return foo

    if payload:
        return payload_wrapper
    return wrapper


async def get_body_from_request(request: web.Request) -> dict | str:
    try:
        return await request.json()
    except JSONDecodeError:
        return await request.text()
