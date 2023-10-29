from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.repository import GenericSqlRepository
from src.api.api_source.models import ApiSource


class ApiSourceRepository(GenericSqlRepository[ApiSource]):
    def __init__(self, a_session: AsyncSession) -> None:
        super().__init__(a_session, ApiSource)
        self._session = a_session

    async def get_by_name(self, name: str):
        stmt = select(ApiSource).where(ApiSource.name == name)
        res = await self._session.execute(stmt)
        if data := res.scalar_one_or_none():
            return data.read_table()
        return None

    async def __other_crud_methods(self):
        ...
