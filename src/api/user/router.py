from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from logger import logger
from src.utils.dependencies import d_UserService
from src.api.user import schemas
from messages import UserMessages

user_router = APIRouter(
    prefix='/user',
    tags=['User']
)


@user_router.get('/get/{id}', response_model=schemas.ResponseUserCreateUpdate, status_code=200)
async def get_user(
        id: int,
        user_service: d_UserService
):
    if user := await user_service.get_user_by_id(id=id):
        return user
    raise HTTPException(status_code=404, detail=UserMessages.not_found)


@user_router.post('/add', response_model=schemas.ResponseUserCreateUpdate, status_code=200)
async def add_user(
        body: schemas.RequestUserCreateUpdate,
        user_service: d_UserService
):
    return await user_service.add_user(new_user=body)


@user_router.get('/all', response_model=list[schemas.ResponseUserCreateUpdate], status_code=200)
async def get_all(
        user_service: d_UserService
):
    return await user_service.get_all()


@user_router.post('/change/{id}', status_code=200)
async def change(
        id: int,
        body: schemas.RequestUserCreateUpdate,
        user_service: d_UserService
):
    if not await user_service.get_user_by_id(id=id):
        raise HTTPException(status_code=404, detail=UserMessages.not_found)
    await user_service.update(user_id=id, data=body)
    return JSONResponse(status_code=200, content=UserMessages.updated_success)


@user_router.delete('/delete', status_code=200)
async def delete(
        id: int,
        user_service: d_UserService
):
    if not await user_service.get_user_by_id(id=id):
        raise HTTPException(status_code=404, detail=UserMessages.not_found)
    await user_service.delete(user_id=id)
    return JSONResponse(status_code=200, content=UserMessages.deleted_success)


@user_router.post('/login', status_code=200)
async def login(
        body: schemas.RequestUserLogin,
        user_service: d_UserService
):
    user = await user_service.get_user_by_login(login=body.login)
    if not user:
        raise HTTPException(status_code=404, detail=UserMessages.not_found)
    await user_service.check_password(id=user.id, data=body)
    return JSONResponse(status_code=200, content=UserMessages.login_success)
