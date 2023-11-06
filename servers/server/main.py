import loguru
from aiohttp import web
from aiohttp.web_app import Application

from servers.server.views import HealthCheck

app = web.Application()


def add_routers(application: Application):
    loguru.logger.info(f"Add routers")
    application.router.add_view('/health', HealthCheck)


if __name__ == "__main__":
    add_routers(app)
    web.run_app(app, port=8080)
