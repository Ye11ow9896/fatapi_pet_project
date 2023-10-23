from logger.logger import logger_api
from src.utils.uow import UnitOfWork
from src.api.user import schemas


class UserService:
    @staticmethod
    async def get_user_by_id(id: int) -> schemas.User:
        """
        Get user by id. If user not found this method raise http exception.
        """
        async with UnitOfWork() as uow:
            return await uow.user.get_by_id(id=id)

    @staticmethod
    async def add_user(new_user: schemas.RequestUser):
        """
        Adding new user by body params
        """
        async with UnitOfWork() as uow:
            return await uow.user.add(data=new_user.model_dump())

    @staticmethod
    async def get_all() -> list[schemas.User]:
        async with UnitOfWork() as uow:
            return await uow.user.get_all()

    async def update(self, user_id: int, data: schemas.RequestUser):
        if await self.get_user_by_id(id=user_id):
            async with UnitOfWork() as uow:
                return await uow.user.update(id=user_id, data=data.model_dump())

    async def delete(self,user_id: int):
        if await self.get_user_by_id(id=user_id):
            async with UnitOfWork() as uow:
                return await uow.user.delete(id=user_id)
