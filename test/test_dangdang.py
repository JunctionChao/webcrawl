#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests, time, json

url = "http://book.dangdang.com/"

response = requests.get(url)

print(response.url)
result = response.text
print(result)