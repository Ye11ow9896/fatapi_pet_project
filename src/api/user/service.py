import hashlib

from fastapi.exceptions import HTTPException

from messages import UserMessages
from src.utils.uow import UnitOfWork
from src.api.user import schemas
from src.config import SALT


class UserService:
    @staticmethod
    async def get_user_by_id(id: int) -> schemas.User:
        async with UnitOfWork() as uow:
            return await uow.user.get_by_id(id=id)

    @staticmethod
    async def get_user_by_login(login: str) -> schemas.User:
        async with UnitOfWork() as uow:
            return await uow.user.get_by_login(login=login)

    async def check_password(self, id: int, data: schemas.RequestUserLogin):
        async with UnitOfWork() as uow:
            password_hash_db = await uow.user.get_hash_password_by_id(id=id)
        hashed_password = self._get_hashed_password(password=data.password)
        if password_hash_db == hashed_password:
            return True
        raise HTTPException(status_code=423, detail=UserMessages.invalid_psw)

    async def add_user(self, new_user: schemas.RequestUserCreateUpdate):
        """
        Adding new user by body params
        """
        new_user.password = self._get_hashed_password(password=new_user.password)
        async with UnitOfWork() as uow:
            return await uow.user.add(data=new_user.model_dump())

    @staticmethod
    async def get_all() -> list[schemas.User]:
        async with UnitOfWork() as uow:
            return await uow.user.get_all()

    async def update(self, user_id: int, data: schemas.RequestUserCreateUpdate):
        if await self.get_user_by_id(id=user_id):
            async with UnitOfWork() as uow:
                return await uow.user.update(id=user_id, data=data.model_dump())

    async def delete(self,user_id: int):
        if await self.get_user_by_id(id=user_id):
            async with UnitOfWork() as uow:
                return await uow.user.delete(id=user_id)

    @staticmethod
    def _get_hashed_password(password: str):
        convert_password = str.encode(password + str(SALT), encoding='utf-8')
        return hashlib.md5(convert_password).hexdigest()