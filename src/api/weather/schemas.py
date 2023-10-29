import enum
from datetime import datetime

from pydantic import BaseModel


class RegionName(str, enum.Enum):
    murino = 'Мурино'
    other = 'Другой'


class Weather(BaseModel):
    id: int
    id_region: int
    date: datetime
    temp: int
    feel_like: int
    condition: str
    wind_speed: int
    wind_dir: str
    pressure_mm: int
    pressure_pa: int
    humidity: int
    sunrise: str
    sunset: str


class Region(BaseModel):
    id: int
    name: str
    lat: float
    lon: float


class CustomRegion(Region):
    weather: list[Weather]


class RequestAddRegion(BaseModel):
    name: str
    lat: float
    lon: float


class ResponseGetRegion(BaseModel):
    name: str
    lat: float
    lon: float
    weather: list[Weather]
