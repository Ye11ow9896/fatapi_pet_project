from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Region(BaseModel):
    id: int
    name: str
    lat: float
    lon: float


class AddRegion(BaseModel):
    name: str
    lat: float
    lon: float
