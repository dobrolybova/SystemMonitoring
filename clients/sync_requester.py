from dataclasses import dataclass

import loguru

from clients.config import SCHEME, HOST
import requests


# TODO: move to utils
@dataclass
class Response:
    body: dict
    status: int

# TODO: check request and exceptions, move to decorator


class Request:
    def __init__(self, scheme=SCHEME, host=HOST, port='8080'):
        self.base_url = scheme + "://" + host + ":" + port

    def request(self, method="GET", url="", **kwargs):
        try:
            response = requests.request(method=method, url=url)
            try:
                body = response.json()
            except Exception as ex:
                body = response.text()
            response.raise_for_status()
            return Response(body, response.status_code)
        except (requests.exceptions.HTTPError, requests.exceptions.TooManyRedirects, requests.ConnectionError,
                requests.Timeout) as e:
            loguru.logger.info(f"Client response error url:{url} exception:{e.__repr__()} error:{e}")
