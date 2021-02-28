#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'https://search.bilibili.com/all?keyword=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&from_source=nav_suggest_new'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
}

response = requests.get(url, headers=headers)

print(response.content.decode('utf-8'))