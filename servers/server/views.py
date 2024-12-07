from http import HTTPStatus

import loguru     # pylint: disable=E0401
from aiohttp.web import View

from servers.utils import response_wrapper


class HealthCheck(View):
    @response_wrapper(payload=False)
    async def get(self) -> int:
        loguru.logger.info("HealthCheck return status OK")
        return HTTPStatus.OK
