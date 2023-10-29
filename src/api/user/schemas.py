from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    surname: str
    create_date: datetime
    stat_id: Optional[int]


class RequestUserCreateUpdate(BaseModel):
    name: str
    surname: str
    login: str
    password: str
    stat_id: Optional[int] = None


class ResponseUserCreateUpdate(BaseModel):
    name: str
    login: str
    stat_id: Optional[int] = None


class RequestUserLogin(BaseModel):
    login: str
    password: str
