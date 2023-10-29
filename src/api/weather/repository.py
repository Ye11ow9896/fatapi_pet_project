from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.utils.repository import GenericSqlRepository
from src.api.weather import models, schemas


class WeatherRepository(GenericSqlRepository[models.Region]):
    def __init__(self, a_session: AsyncSession) -> None:
        super().__init__(a_session, models.Region)
        self._session = a_session

    async def get_by_id(self, id: int) -> schemas.CustomRegion:
        stmt = select(models.Region).where(models.Region.id == id).options(selectinload(models.Region.weather))
        res = await self._session.execute(stmt)
        region = res.scalar_one_or_none()
        return region.read_custom()

    async def get_all(self) -> list[schemas.CustomRegion]:
        stmt = select(models.Region).options(selectinload(models.Region.weather))
        res = await self._session.execute(stmt)
        return [row[0].read_custom() for row in res.all()]

    async def get_region_by_name(self, name: str) -> schemas.CustomRegion:
        stmt = select(models.Region).where(models.Region.name == name).options(selectinload(models.Region.weather))
        res = await self._session.execute(stmt)
        region = res.scalar_one_or_none()
        return region.read_custom()

    async def __other_crud_methods(self):
        ...
