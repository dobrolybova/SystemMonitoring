import asyncio
from clients.async_requester import Requester

URLS = ['/core', '/load']

requester = Requester(port='8000')


async def tasks():
    t_list = [asyncio.create_task(requester.inf_request(url=url)) for url in URLS]
    await asyncio.gather(*t_list)


if __name__ == "__main__":
    asyncio.run(tasks())
