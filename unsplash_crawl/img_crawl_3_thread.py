#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-24
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# 线程池方式
import threading
import concurrent.futures
import requests, json, time, os

thread_local = threading.local() # 给每个线程开辟一个空间，互不干扰

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
        self.session = requests.Session()
        self.session.headers.update(self.headers) # 后面使用session都会默认带着headers

        pages, rest = divmod(self.nums, self.per_page)
        pages = pages + 2 if rest else pages + 1
        for i in range(1, pages):
            payload = {
                'page':i,
                'per_page':self.per_page
            }
            response = self.session.get(url=self.target, params=payload)
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
        self.session.close()

    def get_local_session(self):
        if not hasattr(thread_local, 'session'):
            thread_local.session = requests.Session() # 不是线程安全的,所以每个线程重新建立会话
            thread_local.session.headers.update(self.headers)
        return thread_local.session

    def download(self, filename, photo_id):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        download_link = self.download_link.format(photo_id=photo_id)
        file_path = os.path.join(self.dir, '%03d.jpg' %filename)
        session = self.get_local_session()
        try:
            r = session.get(url=download_link, stream=True, timeout=10)
            print("正在下载第%d张图片" %filename)
            with open(file_path, 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
        except Exception as e:
            print("出现异常:", e)
        else:
            print("第%d张图片下载完成" %filename)
            
    def download_all_imgs(self):
        iter_ = enumerate(self.photos_id, 1)
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(lambda p: self.download(*p), iter_)


if __name__ == '__main__':
    nums = 25
    uc = UnsplashCrawl(nums)
    print("获取图片连接中")
    uc.get_ids()
    print("%d张图片连接获取成功，开始下载" %nums)
    uc.download_all_imgs()

    # iter_ = enumerate(uc.photos_id, 1)
    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    #     executor.map(uc.download, iter_)
    