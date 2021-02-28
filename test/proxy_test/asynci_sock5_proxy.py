import asyncio
import aiohttp
from aiosocksy.connector import ProxyConnector, ProxyClientRequest
import re

async def fetch(url):
    connector = ProxyConnector()
    socks = 'socks5://222.37.106.225:45601'
    async with aiohttp.ClientSession(connector=connector, request_class=ProxyClientRequest) as session:
        async with session.get(url, proxy=socks) as response:
            # html = await response.text()
            uhtml = await response.read()
            html = uhtml.decode('utf-8')
            print(html)
            ser = re.search('搜狗搜索', html)
            if ser:
                print(ser.span())


loop = asyncio.get_event_loop()
loop.run_until_complete(fetch('https://www.sogou.com/'))