from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator

class Statistic(BaseModel):
    id: int
    date: datetime
    request: str
    result: str
    