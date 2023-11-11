from dataclasses import dataclass

import psutil


@dataclass
class CpuAverageLoad:
    last_1_min: float
    last_5_min: float
    last_15_min: float


@dataclass
class CpuAverageCoreLoad:
    cpu: list[float]


def get_cpu_percent() -> CpuAverageCoreLoad:
    return CpuAverageCoreLoad(cpu=psutil.cpu_percent(percpu=True))


def get_cpu_load_average() -> CpuAverageLoad:
    last_1_min, last_5_min, last_15_min = psutil.getloadavg()
    return CpuAverageLoad(last_1_min=last_1_min, last_5_min=last_5_min, last_15_min=last_15_min)
