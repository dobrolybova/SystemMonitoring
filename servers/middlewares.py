from json import JSONDecodeError
from typing import Callable

import loguru
from aiohttp import web

from servers.utils import get_body_from_request


@web.middleware
async def middleware_logger(request: web.Request, handler: Callable) -> web.Response:
    body = None
    if request.body_exists:
        body = await get_body_from_request(request)
    loguru.logger.info(f"New incoming request with "
                       f"body: {body}, "
                       f"query: {request.query_string}, "
                       f"method: {request.method}, "
                       f"url: {request.url}, "
                       f"headers host: {request.headers.get('Host')}, "
                       f"headers accept: {request.headers.get('Accept')}, "
                       f"headers accept encoding: {request.headers.get('Accept-Encoding')}, "
                       f"headers user agent: {request.headers.get('User-Agent')}, "
                       f"keep_alive: {request.keep_alive}, "
                       f"content_type: {request.content_type}")
    return await handler(request)
