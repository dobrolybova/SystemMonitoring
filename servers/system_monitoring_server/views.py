import asyncio
import time
from http import HTTPStatus

import loguru
from aiohttp.web import View

from api_schema import CpuAverageCoreResponse, CpuAverageLoadResponse, CpuAverageLoadModel
from servers.system_monitoring_server.ps_utils import get_cpu_load_average, get_cpu_percent, CpuAverageLoad, \
    CpuAverageCoreLoad
from servers.utils import response_wrapper


class HealthCheck(View):
    @response_wrapper(payload=False)
    async def get(self) -> int:
        loguru.logger.info(f"Monitoring heathcheck return status OK")
        return HTTPStatus.OK


class CpuView(View):
    @response_wrapper(payload=True)
    async def get(self) -> (CpuAverageCoreResponse, int):
        # TODO: to take body (for example for post requests)
        # try:
        #     body = await self.request.json()
        # except Exception:
        #     body = await self.request.text()
        value: CpuAverageCoreLoad = get_cpu_percent()
        await asyncio.sleep(3)
        loguru.logger.info(f"return CPU: {value}")
        return CpuAverageCoreResponse.from_dto(value), HTTPStatus.OK


class LoadView(View):
    @response_wrapper(payload=True)
    async def get(self) -> (CpuAverageLoadResponse, int):
        cpu_load: CpuAverageLoad = get_cpu_load_average()
        time.sleep(2)
        loguru.logger.info(f"return load value {cpu_load.last_1_min} {cpu_load.last_5_min} {cpu_load.last_15_min}")
        return CpuAverageLoadResponse(cpu=CpuAverageLoadModel.from_dto(cpu_load)), HTTPStatus.OK

