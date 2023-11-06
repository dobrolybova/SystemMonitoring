import asyncio
from functools import wraps

import loguru
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
        except (asyncio.exceptions.TimeoutError, ClientConnectorError, ClientResponseError) as e:
            loguru.logger.info(f"Client response error url:{url} exception:{e.__repr__()} error:{e}")
    return func
