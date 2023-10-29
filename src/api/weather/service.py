from src.config import YANDEX_WEATHER_API_TOKEN
from src.utils.uow import UnitOfWork
from src.api.weather import schemas
from src.utils.requests import Request


class WeatherService:
    @staticmethod
    async def add_region(new_region: schemas.AddRegion):
        async with UnitOfWork() as uow:
            return await uow.weather.add(new_region.model_dump())

    @staticmethod
    async def get_region_by_name(name: str) -> schemas.Region:
        async with UnitOfWork() as uow:
            return await uow.weather.get_region_by_name(name=name)

    @staticmethod
    async def get_current_weather(region: str, api_source: str) -> schemas.Region:
        async with UnitOfWork() as uow:
            region = await uow.weather.get_region_by_name(name=region)
            api_service = await uow.api_source.get_by_name(name=api_source)

        params = {'lat': region.lat, 'lon': region.lon}
        headers = {api_service.header_key: YANDEX_WEATHER_API_TOKEN}
        result = await Request.get(url=api_service.url, params=params, headers=headers)

        return result.json()
