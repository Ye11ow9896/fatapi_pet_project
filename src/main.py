import uvicorn
from fastapi import FastAPI

from fastapi.requests import Request

from logger.logger import logger_api
from api.weather.router import weather_router
from api.user.router import user_router


app = FastAPI()


#@app.middleware('http')
#async def logging(request: Request, call_next):
#    try:
#        return await call_next(request)
#    except Exception as e:
#        logger_api.error(f"================================================================================================================"    # noqa
#                         f" \n{request.client} - \"{request.method} {request.url}\" {e} ")


app.include_router(user_router)
app.include_router(weather_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1488, reload=True)
    