import asyncio
from clients.requesters.async_requester import Requester
from clients.requesters.sync_requester import Request as SyncRequester
from clients.utils import handle_key_interrupt

URLS = ['/core', '/load']

requester = Requester(port='8000')
sync_requester = SyncRequester()


async def tasks():
    t_list = [asyncio.create_task(requester.inf_request(url=url)) for url in URLS]
    await asyncio.gather(*t_list)


@handle_key_interrupt
def async_main():
    asyncio.run(tasks())


@handle_key_interrupt
def sync_main():
    while True:
        sync_requester.send_request(url='http://localhost:8000/core')
        sync_requester.send_request(url='http://localhost:8000/load')


if __name__ == "__main__":
    # async_main()
    sync_main()



