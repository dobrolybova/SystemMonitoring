import loguru
from aiohttp import web
from aiohttp.web_app import Application

from servers.system_monitoring_server.views import CpuView, LoadView, HealthCheck


def add_routes(application: Application):
    loguru.logger.info(f"Monitoring, add routers")
    application.router.add_view("/health", HealthCheck)
    application.router.add_view("/cpu", CpuView)
    application.router.add_view("/load", LoadView)


app = web.Application()
# TODO: increase number of workers
if __name__ == "__main__":
    add_routes(app)
    web.run_app(app, port=8000)
