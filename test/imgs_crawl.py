#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-24
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# 爬取该网站的图片：https://unsplash.com/
# GET https://unsplash.com/napi/photos/Z4pqYFMKrBM/related HTTP/1.1
import requests
import json
from pprint import pprint

target = 'https://unsplash.com/napi/photos/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Referer': 'https://unsplash.com/'
}
payload = {
    'page':1,
    'per_page':10
}
# response = requests.get(url=target, headers=headers, params=payload)
# # print(response.text)
# result_dict = json.loads(response.text)
# # print(len(result_dict))
# # pprint(result_dict)
# photos = []
# for photo in result_dict:
#     photos.append(photo['id'])
# print(photos)

# payload = {
#     'page':2,
#     'per_page':10
# }
# response = requests.get(url=target, headers=headers, params=payload)
# result_dict = json.loads(response.text)
# photos = []
# for photo in result_dict:
#     photos.append(photo['id'])
# print(photos)

# https://www.dazhuanlan.com/2019/12/12/5df17801d9e93/
download_link = 'https://unsplash.com/photos/mABnjMWNki4/download?force=true'
response = requests.get(url=download_link, stream=True, headers=headers)
# print(response.headers)
# print(response.headers['Content-length'])

with open('%s.jpg' %'mABnjMWNki4', 'ab+') as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            f.flush()

response.close()