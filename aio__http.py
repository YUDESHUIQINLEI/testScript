import aiohttp
import asyncio
import time


async def task(n):
    url = 'https://www.baidu.com'
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "cookie": "xxxxx"
    body = {
        "orderId": "xxx"
    }
    async with aiohttp.ClientSession() as session:
        print('协程{}开始执行……'.format(n))
        await asyncio.sleep(2)
        async with session.post(
                url=url, json=body, headers=headers) as resp:
            res = await resp.json()
            print(res)
            print('协程{}执行结束……'.format(n))


async def task_1(n):
    url = 'https://www.baiduwangpan.com'
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "cookie": "xxxxx"
    body = {
        "orderId": "xxx"
    }
    async with aiohttp.ClientSession() as session:
        print('协程{}开始执行……'.format(n))
        await asyncio.sleep(2)
        async with session.post(
                url=url, json=body, headers=headers) as resp:
            res = await resp.json()
            print(res)
            print('协程{}执行结束……'.format(n))




if __name__=='__main__':
    loop = asyncio.get_event_loop()
    task_list = [
        asyncio.ensure_future(task(1)),
        asyncio.ensure_future(task_1(2)),
        asyncio.ensure_future(task(3)),
        asyncio.ensure_future(task_1(4))
    ]
    loop.run_until_complete(asyncio.wait(task_list))
    loop.close()
