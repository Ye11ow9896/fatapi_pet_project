from pydantic import BaseModel


class ApiSource(BaseModel):
    id: int
    name: str
    type: str
    url: str
    header_key: str


class CreateApiSource(BaseModel):
    name: str
    type: str
    url: str
    header_key: str
