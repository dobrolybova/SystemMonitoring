from pydantic import BaseModel, Field

from servers.system_monitoring_server.ps_utils import CpuAverageLoad, CpuAverageCoreLoad


class CpuAverageCoreResponse(BaseModel):
    cpu: list[float] = Field(description="List of average CPU load per core")

    @classmethod
    def from_dto(cls, dto: CpuAverageCoreLoad) -> 'CpuAverageCoreResponse':
        return CpuAverageCoreResponse(
            cpu=dto.cpu,
        )


class CpuAverageLoadModel(BaseModel):
    last_1_min: float = Field(description="1 minute average load")
    last_5_min: float = Field(description="5 minute average load")
    last_15_min: float = Field(description="15 minute average load")

    @classmethod
    def from_dto(cls, dto: CpuAverageLoad) -> 'CpuAverageLoadModel':
        return CpuAverageLoadModel(
            last_1_min=dto.last_1_min,
            last_5_min=dto.last_5_min,
            last_15_min=dto.last_15_min,
        )


class CpuAverageLoadResponse(BaseModel):
    cpu: CpuAverageLoadModel

