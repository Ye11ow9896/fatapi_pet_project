from fastapi import APIRouter

word_stat_router = APIRouter(
    prefix='/word_stat',
    tags=['Word Stat']
)

@word_stat_router.post('/add_stat')
async def add_stat(

):
    ...