from logging import getLogger, basicConfig
from time import monotonic


logger = getLogger(__name__)
basicConfig(filename="", filemode='w', level="INFO")


# TODO: store to file and make diagram.
# TODO: count ok and nok responses
class RPS:
    def __init__(self):
        self.st = monotonic()
        self.req_n = 0

    def show(self) -> None:
        time_diff = monotonic() - self.st
        if time_diff > 60:
            logger.info(f"Requests number: {self.req_n}, time period: {time_diff}")
            logger.info(f"RPS: {self.req_n / time_diff}")
            self.st = monotonic()
            self.req_n = 0

    def increase(self) -> None:
        self.req_n += 1
