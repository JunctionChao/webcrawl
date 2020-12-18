#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, time, json

url = "https://www.amazon.cn/Kindle%E7%94%B5%E5%AD%90%E4%B9%A6/b?ie=UTF8&node=116169071&ref_=nav_topnav_giftcert"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
}
response = requests.get(url, headers=headers)

print(response.url)
result = response.content.decode('utf-8')
print(result)