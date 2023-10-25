from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.api.api_source import schemas, service
from messages import UserMessages

api_source_router = APIRouter(
    prefix='/api_source',
    tags=['Api Source']
)


@api_source_router.post('/add', response_model=schemas.ApiSource)
async def add_api_source(
        body: schemas.CreateApiSource,
        api_source_service: Annotated[service.ApiSourceService, Depends(service.ApiSourceService)]
) -> schemas.ApiSource:
    return await api_source_service.add_api_source(data=body)
