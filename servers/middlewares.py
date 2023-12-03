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
    query = request.query_string
    method = request.method
    url = request.url
    headers_host = request.headers.get('Host')
    headers_accept = request.headers.get('Accept')
    headers_accept_encoding = request.headers.get('Accept-Encoding')
    headers_user_agent = request.headers.get('User-Agent')
    keep_alive = request.keep_alive
    content_type = request.content_type

    loguru.logger.info(f"New incoming request with "
                       f"body: {body}, "
                       f"query: {query}, "
                       f"method: {method}, "
                       f"url: {url}, "
                       f"headers host: {headers_host}, "
                       f"headers accept: {headers_accept}, "
                       f"headers accept encoding: {headers_accept_encoding}, "
                       f"headers user agent: {headers_user_agent}, "
                       f"keep_alive: {keep_alive}, "
                       f"content_type: {content_type}")
    return await handler(request)
