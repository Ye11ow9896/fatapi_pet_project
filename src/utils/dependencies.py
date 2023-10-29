from typing import Annotated

from fastapi import Depends

from src.api.user.service import UserService
from src.api.api_source.service import ApiSourceService
from src.api.weather.service import WeatherService

d_UserService = Annotated[UserService, Depends(UserService)]
d_ApiSourceService = Annotated[ApiSourceService, Depends(ApiSourceService)]
d_WeatherService = Annotated[WeatherService, Depends(WeatherService)]
