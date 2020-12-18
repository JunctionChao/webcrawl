#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://pjapi.jd.com/book/sort?source=bookSort&callback=jsonp_1607664510914_55104

import requests, time, json
from pprint import pprint

url = "https://pjapi.jd.com/book/sort?source=bookSort"

headers = {
    "authority": "pjapi.jd.com",
    "referer": "https://book.jd.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
}

response = requests.get(url, headers=headers)

print(response.url)
result = response.json()
pprint(result)