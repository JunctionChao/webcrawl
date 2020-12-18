#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-24
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

import requests, json, time, os

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
        pages, rest = divmod(self.nums, self.per_page)
        pages = pages + 2 if rest else pages + 1
        for i in range(1, pages):
            payload = {
                'page':i,
                'per_page':self.per_page
            }
            response = requests.get(url=self.target, headers=self.headers, params=payload)
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

    def download(self, photo_id, filename):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        download_link = self.download_link.format(photo_id=photo_id)
        with requests.get(url=download_link, stream=True, timeout=10, headers=self.headers) as r:
            file_path = os.path.join(self.dir, '%03d.jpg' %filename)
            with open(file_path, 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__ == '__main__':
    nums = 25
    uc = UnsplashCrawl(nums)
    print("获取图片连接中")
    uc.get_ids()
    print("%d张图片连接获取成功，开始下载" %nums)
    for i in range(len(uc.photos_id)):
        print("正在下载第%d张图片" %(i+1))
        try:
            uc.download(uc.photos_id[i], i+1)
            print("第%d张图片下载完成" %(i+1))
        except Exception as e:
            print("出现异常:", e)
            continue
        

