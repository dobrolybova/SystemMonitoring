import asyncio
from clients.requesters.async_requester import RequesterOneSession


monitoring_requester = RequesterOneSession(port='8000')
requester = RequesterOneSession(port='8080')


# TODO: metrics with answer time
async def tasks():
    t1 = asyncio.create_task(monitoring_requester.inf_request(name="ping_monitoring_server", method='GET', url='/health'))
    t2 = asyncio.create_task(requester.inf_request(name="ping_server", method='GET', url='/health'))
    await asyncio.gather(t1, t2)


if __name__ == "__main__":
    asyncio.run(tasks())
