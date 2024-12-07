from logging import getLogger, basicConfig
from time import monotonic

from clients.config import RPS_COUNT_PERIOD

logger = getLogger(__name__)
basicConfig(filename="", filemode='w', level="INFO")


class RPS:
    def __init__(self, file):
        self.timestamp = monotonic()
        self.req_n = 0
        self.file = file

    def _store(self, rps: float) -> None:
        try:
            with open(self.file, 'a+', encoding='utf8') as file:
                file.write(str(rps) + '\n')
                logger.info(f"Store rps:{rps} to file: {self.file}")
        except FileNotFoundError:
            logger.error(f"Wrong file name to store rps: {self.file}")

    def _reset_count(self):
        self.timestamp = monotonic()
        self.req_n = 0

    def _count_rps(self, period: float) -> float:
        rps = self.req_n / period
        logger.info(f"Number of requests: {self.req_n}, time period: {period}")
        logger.info(f"RPS: {rps}")
        return rps

    def count_last_period(self) -> None:
        period = monotonic() - self.timestamp
        if period > RPS_COUNT_PERIOD:
            rps = self._count_rps(period)
            self._store(rps)
            self._reset_count()

    def increase(self) -> None:
        self.req_n += 1
