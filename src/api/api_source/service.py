from src.utils.uow import UnitOfWork
from src.api.api_source import schemas


class ApiSourceService:
    @staticmethod
    async def add(data: schemas.RequestCreateApiSource) -> schemas.ApiSource:
        async with UnitOfWork() as uow:
            return await uow.api_source.add(data=data.model_dump())

    @staticmethod
    async def get_by_id(id: int) -> schemas.ApiSource:
        async with UnitOfWork() as uow:
            return await uow.api_source.get_by_id(id=id)

    @staticmethod
    async def get_all() -> list[schemas.ApiSource]:
        async with UnitOfWork() as uow:
            return await uow.api_source.get_all()

    @staticmethod
    async def get_by_name(name: str) -> schemas.ApiSource:
        async with UnitOfWork() as uow:
            return await uow.api_source.get_by_name(name=name)
