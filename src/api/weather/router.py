from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.api.weather import schemas, service
from src.api.api_source import schemas as api_source_schemas
from messages import RegionMessages, ApiSourceMessages

weather_router = APIRouter(
    prefix='/weather',
    tags=['Weather']
)


@weather_router.post('/addRegion', status_code=200)
async def add_region(
    body: schemas.AddRegion,
    weather_service: Annotated[service.WeatherService, Depends(service.WeatherService)]
):
    if await weather_service.get_region_by_name(name=body.name):
        raise HTTPException(status_code=409, detail=RegionMessages.already_exist)
    await weather_service.add_region(new_region=body)
    return JSONResponse(status_code=200, content=RegionMessages.adding_success)


@weather_router.get('/current/{region}/{api_source}', status_code=200)
async def get_current_weather(
        region: schemas.RegionName,
        api_source: api_source_schemas.ApiSourceName,
        weather_service: Annotated[service.WeatherService, Depends(service.WeatherService)],
        api_source_service: Annotated[service.ApiSourceService, Depends(service.ApiSourceService)]
):
    if not await weather_service.get_region_by_name(name=region):
        raise HTTPException(status_code=404, detail=RegionMessages.not_found)
    if not await api_source_service.get_by_name(name=api_source):
        raise HTTPException(status_code=404, detail=ApiSourceMessages.not_found)
    await weather_service.get_current_weather(region=region, api_source=api_source)
