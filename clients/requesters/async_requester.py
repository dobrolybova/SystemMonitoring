import asyncio

import loguru
from aiohttp import (
    ContentTypeError,
    ClientTimeout,
    ClientSession,
    ClientResponse,
)

from clients.config import CLIENT_TIMEOUT, SLEEP, SCHEME, HOST
from clients.models import Response
from clients.rps.rps_counter import RPS
from clients.utils import handle_request


class Requester:
    def __init__(self,  rps_storage_file, scheme=SCHEME, host=HOST, port='8080'):
        self.base_url = scheme + "://" + host + ":" + port
        self.session = None
        self.rps_counter = RPS(rps_storage_file)

    def get_new_session(self) -> ClientSession:
        timeout = ClientTimeout(total=CLIENT_TIMEOUT)
        return ClientSession(
            timeout=timeout,
            raise_for_status=True,
            base_url=self.base_url,
        )

    def rps_handle(self):
        self.rps_counter.increase()
        self.rps_counter.count_last_period()

    @staticmethod
    async def get_body(response: ClientResponse) -> dict | str:
        try:
            return await response.json()
        except ContentTypeError:
            return await response.text()

    @handle_request
    async def request(self, name='', method="GET", url="", **kwargs) -> Response | None:
        async with self.get_new_session() as session:
            async with session.request(method, url, **kwargs) as response:
                body = await self.get_body(response)
                self.rps_handle()
                return Response(body, response.status)

    async def inf_request(self, name="", method='GET', url=''):
        try:
            while True:
                await self.request(name=name, method=method, url=url)
                await asyncio.sleep(SLEEP)
        except Exception as e:
            loguru.logger.error(f"Exception is raised from {name} {e.__repr__()}")


class RequesterOneSession(Requester):
    def __init__(self, rps_storage_file, scheme=SCHEME, host=HOST, port='8080'):
        super().__init__(rps_storage_file, scheme=scheme, host=host, port=port)
        self.session = None

    def get_session(self) -> ClientSession:
        if self.session is None or self.session.closed:
            self.session = self.get_new_session()
        return self.session

    @handle_request
    async def request(self, name='', method="GET", url="", **kwargs) -> Response | None:
        async with self.get_session().request(method, url, **kwargs) as response:
            body = await self.get_body(response)
            self.rps_handle()
            return Response(body, response.status)
