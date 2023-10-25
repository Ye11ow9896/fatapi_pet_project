from pydantic import BaseModel


class ApiSource(BaseModel):
    id: int
    name: str
    type: str
    url: str
    header_key: str
