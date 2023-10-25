from src.utils.uow import UnitOfWork
from src.api.api_source import schemas


class ApiSourceService:
    @staticmethod
    async def add_api_source(data: schemas.CreateApiSource) -> schemas.ApiSource:
        async with UnitOfWork() as uow:
            return await uow.api_source.add(data=data.model_dump())

    @staticmethod
    async def get_api_source_by_id(id: int) -> schemas.ApiSource:
        async with UnitOfWork() as uow:
            return await uow.api_source.get_by_id(id=id)

    @staticmethod
    async def get_all_api_source() -> list[schemas.ApiSource]:
        async with UnitOfWork() as uow:
            return uow.api_source.get_all()
