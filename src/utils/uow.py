from abc import ABC, abstractmethod

from src.api.weather.repository import WeatherRepository
from src.database import async_session_maker
from src.api.user.repository import UserRepository


class UnitOfWorkBase(ABC):
    user: UserRepository
    weather: WeatherRepository

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.rollback()

    @abstractmethod
    async def commit(self):
        raise NotImplementedError()

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError()


class UnitOfWork(UnitOfWorkBase):
    def __init__(self):
        self._session_factory = async_session_maker

    async def __aenter__(self):
        self._session = self._session_factory()
        self.user = UserRepository(self._session)
        self.weather = WeatherRepository(self._session)
        return await super().__aenter__()

    async def commit(self):
        await self._session.commit()

    async def rollback(self):
        await self._session.rollback()
