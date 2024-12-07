import loguru     # pylint: disable=E0401
from aiohttp import web
from aiohttp.web_app import Application

from servers.middlewares import middleware_logger
from servers.system_monitoring_server.views import CpuView, LoadView, HealthCheck


def add_routes(application: Application):
    loguru.logger.info("Monitoring, add routers")
    application.router.add_view("/health", HealthCheck)
    application.router.add_view("/core", CpuView)
    application.router.add_view("/load", LoadView)


app = web.Application(middlewares=[middleware_logger])
# TODO: put in docker
# TODO: increase number of workers
if __name__ == "__main__":
    add_routes(app)
    web.run_app(app, port=8000)
