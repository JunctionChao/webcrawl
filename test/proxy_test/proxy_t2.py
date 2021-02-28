import aiohttp
import asyncio
import re


url = "https://www.baidu.com"
keyword = "百度一下"
# url = "https://www.sogou.com"
# keyword = "搜狗搜索"


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get(url, proxy="http://61.160.210.223:808") as response: # 218.60.8.83:3129

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print(html)
            ser = re.search(keyword, html)
            if ser:
                print(ser.span())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())