import uvicorn
from fastapi import FastAPI, Response

from fastapi.requests import Request
from api.word_stat.router import word_stat_router
from api.user.router import user_router
from logger.logger import logger_api


app = FastAPI()


@app.middleware('http')
async def logging(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        logger_api.error(f"================================================================================================================"
                         f" \n{request.client} - \"{request.method} {request.url}\" {e} ")

app.include_router(word_stat_router)
app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1488, reload=True)
    