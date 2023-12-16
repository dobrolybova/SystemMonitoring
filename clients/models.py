from dataclasses import dataclass


@dataclass
class Response:
    body: dict
    status: int
