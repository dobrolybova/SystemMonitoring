import os
import pathlib

CLIENT_TIMEOUT = os.getenv('CLIENT_TIMEOUT', 5)
SLEEP = os.getenv('SLEEP', 0.1)
HOST = os.getenv('HOST', '0.0.0.0')
SCHEME = os.getenv('SCHEME', 'http')
RPS_COUNT_PERIOD = os.getenv('RPS_COUNT_PERIOD', 3)
