import time
from logging import getLogger, basicConfig

import requests
from requests import Response as Resp

from clients.config import SLEEP
from clients.models import Response

logger = getLogger(__name__)
basicConfig(filename="", filemode='w', level="INFO")


class Request:

    @staticmethod
    def get_body(response: Resp) -> dict | str:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return response.text

    def inf_request(self, method="GET", url="", **kwargs) -> None:
        try:
            while True:
                self.send_request(method=method, url=url, kwargs=kwargs)
                time.sleep(SLEEP)
        except Exception as e:
            logger.error(f"Exception is raised {e.__repr__()}")

    def send_request(self, method="GET", url="", **kwargs) -> Response:
        try:
            return self.request(method=method, url=url, kwargs=kwargs)
        except (requests.exceptions.HTTPError, requests.exceptions.TooManyRedirects, requests.ConnectionError,
                requests.Timeout) as e:
            logger.info(f"Client response error url:{url} exception:{e.__repr__()} error:{e}")

    def request(self, method="GET", url="", **kwargs) -> Response:
        response = requests.request(method=method, url=url)
        body = self.get_body(response)
        status = response.status_code
        logger.info(f"Send sync request method: {method}, url: {url}, received body: {body} status: {status}")
        response.raise_for_status()
        return Response(body, status)
