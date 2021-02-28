# -*- encoding: utf-8 -*-

import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
}

# url = "http://httpbin.org/get"
# url = "http://example.org/"
url = "https://www.baidu.com"
# url = "http://httpbin.org/ip"

rsp = requests.get(url, headers=headers)

print(rsp.status_code)
print(rsp.headers)
html = rsp.content.decode('utf-8')
print(len(html))
ser = re.search('百度一下', html)
if ser:
    print(ser.span())


# https://www.fanqieip.com
proxy = {
    # "http": "http://150.138.253.71:808",
    "https": "https://150.138.253.71:808"
}
try:
    rsp = requests.get(url, headers=headers, proxies=proxy)
    print(rsp.status_code)
    print(rsp.headers)
    html = rsp.content.decode('utf-8')
    print(len(html))
    ser = re.search('百度一下', html)
    if ser:
        print(ser.span())
    
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)