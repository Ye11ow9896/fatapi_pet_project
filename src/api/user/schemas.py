from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    surname: str
    create_date: datetime
    stat_id: Optional[int]


class RequestUser(BaseModel):
    name: str
    surname: str
    stat_id: Optional[int] = None


    