from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.utils.dependencies import d_WeatherService, d_ApiSourceService
from src.api.weather import schemas
from src.api.api_source import schemas as api_source_schemas
from messages import RegionMessages, ApiSourceMessages

weather_router = APIRouter(
    prefix='/weather',
    tags=['Weather']
)


@weather_router.post('/addRegion', status_code=200)
async def add_region(
    body: schemas.RequestAddRegion,
    weather_service: d_WeatherService
):
    if await weather_service.get_region_by_name(name=body.name):
        raise HTTPException(status_code=409, detail=RegionMessages.already_exist)
    await weather_service.add_region(new_region=body)
    return JSONResponse(status_code=200, content=RegionMessages.adding_success)


@weather_router.get('/getRegion/{id}', response_model=schemas.ResponseGetRegion, status_code=200)
async def get_region(
    id: int,
    weather_service: d_WeatherService
):
    if region := await weather_service.get_region_by_id(id=id):
        return region
    raise HTTPException(status_code=404, detail=RegionMessages.not_found)


@weather_router.get('/getRegions', response_model=list[schemas.ResponseGetRegion], status_code=200)
async def get_regions(weather_service: d_WeatherService):
    return await weather_service.get_regions()


@weather_router.get('/current/{region}/{api_source}', status_code=200)
async def get_current_weather(
    region: schemas.RegionName,
    api_source: api_source_schemas.ApiSourceName,
    weather_service: d_WeatherService,
    api_source_service: d_ApiSourceService
):
    if not await weather_service.get_region_by_name(name=region):
        raise HTTPException(status_code=404, detail=RegionMessages.not_found)
    if not await api_source_service.get_by_name(name=api_source):
        raise HTTPException(status_code=404, detail=ApiSourceMessages.not_found)
    return await weather_service.get_current_weather(region=region, api_source=api_source)
