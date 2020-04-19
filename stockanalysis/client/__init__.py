import aiohttp
import asyncio
import logging


logger = logging.getLogger(__name__)


async def get_response_content(response: aiohttp.ClientResponse):
        content_type = response.content_type
        if content_type == "application/json":
            return await response.json()
        else:
            return await response.text()


class Client:
    async def get(url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    return await get_response_content(response)
            except aiohttp.ClientError as e:
                logger.error(e)

    async def post(url, data):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url, data) as response:
                    return await get_response_content(response)
            except aiohttp.ClientError as e:
                logger.error(e)

    async def patch(url):
        pass

    async def put(url):
        pass

    async def delete(url):
        pass

    async def head(url):
        pass

    async def options(url):
        pass
