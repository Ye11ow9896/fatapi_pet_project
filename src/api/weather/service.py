import hashlib

from fastapi.exceptions import HTTPException

from messages import UserMessages
from src.utils.uow import UnitOfWork
from src.api.weather import schemas
from src.config import SALT


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
    async def get_current_weather(name: str) -> schemas.Region:
        async with UnitOfWork() as uow:
            region = await uow.weather.get_region_by_name(name=name)
        return region
        # TODO: делаем запрос на апи яндекса по широте и долготе региона
    #    curl -H "X-Yandex-API-Key:87b152bb-1820-435b-9612-1953690bdb3a" https://api.weather.yandex.ru/v2/informers?lat=60.056521&lon=30.430426

