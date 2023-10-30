from logger import logger
from src.utils.uow import UnitOfWork
from src.api.api_source import schemas


class ApiSourceService:
    @staticmethod
    async def add(data: schemas.RequestCreateApiSource) -> schemas.ApiSource:
        async with UnitOfWork() as uow:
            try:
                new_api_service = await uow.api_source.add(data=data.model_dump())
                logger.logger.warning(f'Created a new API service with id: {new_api_service.id}')
            except Exception as e:
                logger.logger.error(f'An error occurred while creating a new service. {e}')
        return new_api_service

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
