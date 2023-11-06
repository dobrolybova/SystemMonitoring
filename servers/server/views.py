import loguru
from aiohttp.web import View, json_response


# TODO: logging to middleware
class HealthCheck(View):
    async def get(self):
        loguru.logger.info(f"HealthCheck return status OK")
        return json_response({'status': 'ok'})
