import asyncio
from functools import wraps

import loguru  # pylint: disable=E0401
from aiohttp import ClientConnectorError, ClientResponseError


def handle_request(request_func):
    @wraps(request_func)
    async def func(*args, **kwargs):
        name = kwargs.get('name')
        url = kwargs.get('url')
        method = kwargs.get('method')
        loguru.logger.info(f"Send request name: {name} url: {url} method: {method}")
        try:
            response_obj = await request_func(*args, **kwargs)
            loguru.logger.info(f"Receive response for "
                               f"name: {name} "
                               f"method: {method} "
                               f"url: {url} "
                               f"body: {response_obj.body} "
                               f"status: {response_obj.status}")
            return response_obj
        except (asyncio.exceptions.TimeoutError, ClientConnectorError, ClientResponseError) as exc:
            loguru.logger.info(f"Client response error url:{url} "
                               f"exception:{exc.__repr__()} error:{exc}")
    return func


def handle_key_interrupt(main_func):
    @wraps(main_func)
    def func(*args, **kwargs):
        try:
            main_func(*args, **kwargs)
        except KeyboardInterrupt:
            pass
    return func
