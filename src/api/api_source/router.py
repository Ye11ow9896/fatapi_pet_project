from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.api.api_source import schemas, service
from messages import ApiSourceMessages

api_source_router = APIRouter(
    prefix='/api_source',
    tags=['Api Source']
)


@api_source_router.post('/add', response_model=schemas.ApiSource, status_code=200)
async def add_api_source(
        body: schemas.CreateApiSource,
        api_source_service: Annotated[service.ApiSourceService, Depends(service.ApiSourceService)]
) -> schemas.ApiSource:
    if await api_source_service.get_by_name(name=body.name):
        raise HTTPException(404, detail=ApiSourceMessages.not_found)
    return await api_source_service.add(data=body)
