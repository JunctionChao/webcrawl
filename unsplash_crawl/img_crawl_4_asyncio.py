#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-25
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# 使用协程异步的方式

import requests, json, time, os
import aiohttp
import asyncio
import async_timeout

class UnsplashCrawl():
    def __init__(self, nums): # nums：要下载的数量
        self.nums = nums
        self.per_page = 10 # 每页10张
        self.dir = os.path.split(__file__)[-1].split(".")[0]
        self.photos_id = []
        self.download_link = 'https://unsplash.com/photos/{photo_id}/download?force=true'
        self.target = 'https://unsplash.com/napi/photos/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Referer': 'https://unsplash.com/'
        }

    def get_ids(self):
        session = requests.Session()
        session.headers.update(self.headers) # 后面使用session都会默认带着headers

        pages, rest = divmod(self.nums, self.per_page)
        pages = pages + 2 if rest else pages + 1
        for i in range(1, pages):
            payload = {
                'page':i,
                'per_page':self.per_page
            }
            response = session.get(url=self.target, params=payload)
            result = json.loads(response.text)
            if i == pages - 1 and rest: # 当有余数时，以后一次取到余数就行
                for j, each in enumerate(result, start=1):
                    if j == rest:
                        self.photos_id.append(each['id'])
                        break
                    self.photos_id.append(each['id'])
            else:
                for each in result:
                    self.photos_id.append(each['id'])
            time.sleep(1) # 延迟一秒获取，防止被检测到
        session.close() # 关闭连接

    async def download(self, session, filename, photo_id):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        download_link = self.download_link.format(photo_id=photo_id)
        file_path = os.path.join(self.dir, '%03d.jpg' %filename)
        with async_timeout.timeout(10):
            async with session.get(download_link) as response:
                with open(file_path, 'wb') as f:
                    while True:
                        chunk = await response.content.read(1024)
                        if not chunk:
                            break
                        f.write(chunk)
            print("第%d张图片下载完成" %filename)

    async def main(self):
        iter_ = enumerate(self.photos_id, 1)
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.ensure_future(self.download(session, i, id_)) for i, id_ in iter_]
            await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    nums = 25
    uc = UnsplashCrawl(nums)
    print("获取图片连接中")
    uc.get_ids()
    print("%d张图片连接获取成功，开始下载" %nums)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(uc.main())
    
    