from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.api.weather import schemas, service
from messages import RegionMessages

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

@weather_router.get('/current/{name}', status_code=200)
async def get_current_weather(
        name: str,
        weather_service: Annotated[service.WeatherService, Depends(service.WeatherService)]
):
    if not await weather_service.get_region_by_name(name=name):
        raise HTTPException(status_code=409, detail=RegionMessages.not_found)
    await weather_service.get_current_weather(name=name)
