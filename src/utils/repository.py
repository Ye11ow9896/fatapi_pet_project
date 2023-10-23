from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type, Optional

from sqlalchemy import select, update, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import Base


T = TypeVar("T", bound=Base)


class IGenericRepository(Generic[T], ABC):
    @abstractmethod
    async def add(self, record: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[T]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, id: int, data: dict) -> int:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, id: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> list[T]:
        raise NotImplementedError()


class GenericSqlRepository(IGenericRepository[T]):
    def __init__(self, session: AsyncSession, model: Type[T]) -> None:
        self._session = session
        self._model = model

    async def add(self, data: dict) -> T:
        stmt = insert(self._model).values(**data).returning(self._model)
        res = await self._session.execute(stmt)
        await self._session.commit()
        return res.scalar().to_read_model()

    async def get_by_id(self, id: int) -> Optional[T]:
        stmt = select(self._model).where(self._model.id == id)
        cour = await self._session.execute(stmt)
        if res := cour.scalar_one_or_none():
            return res.to_read_model()
        return None

    async def update(self, id: int, data: dict) -> Optional[int]:
        stmt = update(self._model).values(**data).filter_by(id=id).returning(self._model.id)
        res = await self._session.execute(stmt)
        await self._session.commit()
        return res.scalar_one()

    async def delete(self, id: int) -> int:
        stmt = delete(self._model).filter_by(id=id).returning(self._model.id)
        res = await self._session.execute(stmt)
        await self._session.commit()
        return res.scalar_one_or_none()

    async def get_all(self) -> list[T]:
        stmt = select(self._model)
        result = await self._session.execute(stmt)
        return [row[0].to_read_model() for row in result.all()]
