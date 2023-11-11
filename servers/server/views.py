from http import HTTPStatus

import loguru
from aiohttp.web import View

from servers.utils import response_wrapper


# TODO: logging to middleware
class HealthCheck(View):
    @response_wrapper(payload=False)
    async def get(self) -> int:
        loguru.logger.info(f"HealthCheck return status OK")
        return HTTPStatus.OK
