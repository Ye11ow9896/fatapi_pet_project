import enum

from pydantic import BaseModel


class RegionName(str, enum.Enum):
    murino = 'Мурино'
    other = 'Другой'


class Region(BaseModel):
    id: int
    name: str
    lat: float
    lon: float


class AddRegion(BaseModel):
    name: str
    lat: float
    lon: float
