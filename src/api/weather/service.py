from typing import Annotated

from fastapi import Depends

from src.config import YANDEX_WEATHER_API_TOKEN
from src.utils.uow import UnitOfWork
from src.api.weather import schemas
from src.utils.requests import Request
from src.api.api_source.service import ApiSourceService


class WeatherService:
    def __init__(self, api_source_service: Annotated[ApiSourceService, Depends(ApiSourceService)]):
        self.api_source_service = api_source_service

    @staticmethod
    async def add_region(new_region: schemas.AddRegion):
        async with UnitOfWork() as uow:
            return await uow.weather.add(new_region.model_dump())

    @staticmethod
    async def get_region_by_name(name: str) -> schemas.Region:
        async with UnitOfWork() as uow:
            return await uow.weather.get_region_by_name(name=name)

    async def get_current_weather(self, name: str) -> schemas.Region:
        async with UnitOfWork() as uow:
            region = await uow.weather.get_region_by_name(name=name)
        services = await self.api_source_service.get_all_api_source()

        url = f'https://api.weather.yandex.ru/v2/informers'
        params = {'lat': region.lat, 'lon': region.lon}
        headers = {'X-Yandex-API-Key': YANDEX_WEATHER_API_TOKEN}
        result = await Request.get(url=url, params=params, headers=headers)
        return region
