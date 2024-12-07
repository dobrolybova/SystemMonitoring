import asyncio
from clients.requesters.async_requester import RequesterOneSession


monitoring_requester = RequesterOneSession(rps_storage_file='', port='8080')
requester = RequesterOneSession(rps_storage_file='', port='8080')


# TODO: metrics with answer time
async def tasks():
    task1 = asyncio.create_task(monitoring_requester.inf_request(
        name="ping_monitoring_server", method='GET', url='/health'))
    task2 = asyncio.create_task(requester.inf_request(
        name="ping_server", method='GET', url='/health'))
    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    asyncio.run(tasks())
