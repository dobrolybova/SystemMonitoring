import loguru   # pylint: disable=E0401
from aiohttp import web
from aiohttp.web_app import Application

from servers.middlewares import middleware_logger
from servers.server.views import HealthCheck

app = web.Application(middlewares=[middleware_logger])


def add_routers(application: Application):
    loguru.logger.info("Add routers")
    application.router.add_view('/health', HealthCheck)


if __name__ == "__main__":
    add_routers(app)
    web.run_app(app, port=8080)
