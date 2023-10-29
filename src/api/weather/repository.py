from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.utils.repository import GenericSqlRepository
from src.api.weather.models import Region


class WeatherRepository(GenericSqlRepository[Region]):
    def __init__(self, a_session: AsyncSession) -> None:
        super().__init__(a_session, Region)
        self._session = a_session

    async def get_region_by_name(self, name: str):
        stmt = select(Region).options(selectinload(Region.weather))
        res = await self._session.execute(stmt)
        if data := res.scalar_one_or_none():
            return data.to_read_model()
        return None

    async def __other_crud_methods(self):
        ...
