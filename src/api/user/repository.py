from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.utils.repository import GenericSqlRepository
from src.api.user.models import User


class UserRepository(GenericSqlRepository[User]):
    def __init__(self, a_session: AsyncSession) -> None:
        super().__init__(a_session, User)
        self._session = a_session

    async def get_by_login(self, login: str) -> Optional[User]:
        stmt = select(User).where(User.login == login)
        res = await self._session.execute(stmt)
        if data := res.scalar_one_or_none():
            return data.read_table()
        return None

    async def get_hash_password_by_id(self, id: int) -> Optional[str]:
        stmt = select(User.password).where(User.id == id)  # noqa
        res = await self._session.execute(stmt)
        return res.scalar()

    async def __other_crud_methods(self):
        ...
