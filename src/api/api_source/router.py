from fastapi import APIRouter, HTTPException

from src.utils.dependencies import d_ApiSourceService
from src.api.api_source import schemas
from messages import ApiSourceMessages

api_source_router = APIRouter(
    prefix='/api_source',
    tags=['Api Source']
)


@api_source_router.post('/add', response_model=schemas.ResponseCreateApiSource, status_code=200)
async def add_api_source(
    body: schemas.RequestCreateApiSource,
    api_source_service: d_ApiSourceService
) -> schemas.ApiSource:
    if await api_source_service.get_by_name(name=body.name):
        raise HTTPException(404, detail=ApiSourceMessages.not_found)
    return await api_source_service.add(data=body)
