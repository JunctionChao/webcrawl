#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-12-02
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://careers.tencent.com/search.html

# https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1606914458513&countryId=&cityId=2&bgIds=953&productId=&categoryId=40001001&parentCategoryId=&attrId=1&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn
import requests, time, json
from pprint import pprint

# response = requests.get(url="https://careers.tencent.com/search.html")
# html_doc = response.text
# print(html_doc)


url = "https://careers.tencent.com/tencentcareer/api/post/Query"

headers = {
    "authority": "careers.tencent.com",
    "referer": "https://careers.tencent.com/search.html",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
}

int_part, fract_part = str(time.time()).split('.')
timestamp = int_part + fract_part[0:3]
params = {
    "timestamp": timestamp,
    "countryId": None,
    "cityId": 2,
    "bgIds": 953,
    "productId": None,
    "categoryId": 40001001,
    "parentCategoryId": None,
    "attrId": 1,
    "keyword": None,
    "pageIndex": 2,
    "pageSize": 10,  # 每页10条记录，第4页就无数据了
    "language": "zh-cn",
    "area": "cn"
}

# https://www.89ip.cn/
# 设置代理
proxy = {
    # "http": "http://127.0.0.1:8888",
    "http": "120.79.184.148:8118",
}
# response = requests.get(url, headers=headers, params=params)
response = requests.get(url, headers=headers, params=params, proxies=proxy) #设置代理
print(response.status_code)
print(dir(response))
print(response.cookies)
print(response.headers)
print(response.request)
print(response.raw.__dict__)
print('-'*50)
print(dir(response.raw))
# print(response.url)
# print(response.text)
# result = response.json()

# if result["Code"] == 200:
#     data = result["Data"]["Posts"]
#     if data:
#         print(len(data))
#         pprint(data)
#     else:
#         print("无数据")