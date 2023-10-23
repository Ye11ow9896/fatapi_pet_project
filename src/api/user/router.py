from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from src.api.user import schemas, service
from messages import UserMessage

user_router = APIRouter(
    prefix='/user',
    tags=['User']
)


@user_router.get('/get/{id}', response_model=schemas.User, status_code=200)
async def get_user(
        id: int,
        user_service: Annotated[service.UserService, Depends(service.UserService)]
):
    if user := await user_service.get_user_by_id(id=id):
        return user
    raise HTTPException(status_code=404, detail=UserMessage.not_found)


@user_router.post('/add', response_model=schemas.User, status_code=200)
async def add_user(
        body: schemas.RequestUser,
        user_service: Annotated[service.UserService, Depends(service.UserService)]
):
    return await user_service.add_user(new_user=body)


@user_router.get('/all', response_model=list[schemas.User])
async def get_all(
    user_service: Annotated[service.UserService, Depends(service.UserService)]
):
    return await user_service.get_all()


@user_router.post('/change/{id}')
async def change(
    id: int,
    body: schemas.RequestUser,
    user_service: Annotated[service.UserService, Depends(service.UserService)]
):
    if not await user_service.get_user_by_id(id=id):
        raise HTTPException(status_code=404, detail=UserMessage.not_found)
    await user_service.update(user_id=id, data=body)
    return JSONResponse(status_code=200, content=UserMessage.updated_success)


@user_router.delete('/delete')
async def delete(
    id: int,
    user_service: Annotated[service.UserService, Depends(service.UserService)]
):
    if not await user_service.get_user_by_id(id=id):
        raise HTTPException(status_code=404, detail=UserMessage.not_found)
    await user_service.delete(user_id=id)
    return JSONResponse(status_code=200, content=UserMessage.deleted_success)
