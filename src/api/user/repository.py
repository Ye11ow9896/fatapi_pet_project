from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.utils.repository import GenericSqlRepository
from src.api.user.models import User


class UserRepository(GenericSqlRepository[User]):
    def __init__(self, a_session: AsyncSession) -> None:
        super().__init__(a_session, User)

    def other_crud_methods(self):
        ...
