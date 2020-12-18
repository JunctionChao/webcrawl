#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 用来测试的url地址 http://httpbin.org/

import requests


url = "http://httpbin.org/get"
# url = "http://example.org/"
# url = "https://www.baidu.com"

rsp = requests.get(url)

print(rsp.status_code)
print(rsp.headers)
print(rsp.text)

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
}

# https://www.fanqieip.com
proxy = {
    "http": "http://128.199.130.31:8080",
    # "https": "https://218.72.185.39:28193"
}
try:
    rsp = requests.get(url, headers=headers, proxies=proxy)
    print(rsp.status_code)
    print(rsp.headers)
    print(rsp.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
# with open("r.html", "w", encoding='utf-8') as f:
#     f.write(rsp.text)