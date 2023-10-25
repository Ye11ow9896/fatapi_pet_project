import httpx
from typing import Optional

from logger.logger import logger_api


class Request:
    @staticmethod
    async def get(
            url: str,
            timeout: Optional[int] = None,
            params: Optional[dict] = None,
            headers: Optional[dict] = None
    ) -> httpx.Response:
        async with httpx.AsyncClient() as request:
            try:
                response = await request.get(url, timeout=timeout, params=params, headers=headers)
                response.raise_for_status()
            except httpx.TimeoutException as e:
                logger_api.error(e)
                print(e)
            except httpx.HTTPStatusError as e:
                logger_api.error(e)
                print(e)

        return response

    @staticmethod
    async def post(
            url: str,
            timeout: Optional[int] = None,
            params: Optional[dict] = None,
            headers: Optional[dict] = None
    ) -> httpx.Response:
        async with httpx.AsyncClient() as request:
            try:
                response = await request.post(url, timeout=timeout, params=params, headers=headers)
                response.raise_for_status()
            except httpx.TimeoutException as e:
                logger_api.error(e)
                print(e)
            except httpx.HTTPStatusError as e:
                logger_api.error(e)
                print(e)

        return response

    @staticmethod
    async def put(
            url: str,
            timeout: Optional[int] = None,
            params: Optional[dict] = None,
            headers: Optional[dict] = None
    ) -> httpx.Response:
        async with httpx.AsyncClient() as request:
            try:
                response = await request.put(url, timeout=timeout, params=params, headers=headers)
                response.raise_for_status()
            except httpx.TimeoutException as e:
                logger_api.error(e)
                print(e)
            except httpx.HTTPStatusError as e:
                logger_api.error(e)
                print(e)

        return response

    @staticmethod
    async def patch(
            url: str,
            timeout: Optional[int] = None,
            params: Optional[dict] = None,
            headers: Optional[dict] = None
    ) -> httpx.Response:
        async with httpx.AsyncClient() as request:
            try:
                response = await request.patch(url, timeout=timeout, params=params, headers=headers)
                response.raise_for_status()
            except httpx.TimeoutException as e:
                logger_api.error(e)
                print(e)
            except httpx.HTTPStatusError as e:
                logger_api.error(e)
                print(e)

        return response
