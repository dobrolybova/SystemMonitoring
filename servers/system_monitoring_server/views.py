import asyncio
import time

import psutil
from aiohttp.web import View, json_response
import loguru


class HealthCheck(View):
    async def get(self):
        loguru.logger.info(f"Monitoring heathcheck return status OK")
        return json_response({'status': 'OK'})


class CpuView(View):
    async def get(self):
        # TODO: to take body (for example for post requests)
        # try:
        #     body = await self.request.json()
        # except Exception:
        #     body = await self.request.text()
        value = psutil.cpu_percent(percpu=True)
        await asyncio.sleep(3)
        loguru.logger.info(f"return CPU: {value}")
        return json_response({'CPU': value})


class LoadView(View):
    async def get(self):
        # TODO: to take body (for example for post requests)
        # try:
        #     body = await self.request.json()
        # except Exception:
        #     body = await self.request.text()
        value = psutil.getloadavg()
        time.sleep(2)
        loguru.logger.info(f"return load value {value}")
        return json_response({1: value[0], 5: value[1], 15: value[2]})

