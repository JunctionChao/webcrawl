#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-22
# Author  : Yuanbo Zhao (chaojunction@gmail.com)


import requests
from bs4 import BeautifulSoup


# target = 'http://www.biqukan.com/1_1094/5403177.html'
# response = requests.get(url=target)
# html_doc = response.text
# bf = BeautifulSoup(html_doc, 'html.parser')
# texts = bf.find_all('div', class_='showtxt')
# print(texts[0].text.replace('\xa0'*8,'\n\n'))

server = 'http://www.biqukan.com'
target_p = 'https://www.biqukan.com/38_38836/'
response = requests.get(url=target_p)
response.encoding = 'GBK'
html_doc = response.text
bf = BeautifulSoup(html_doc, 'lxml')
print(bf.title)

div = bf.find_all('div', class_ = 'listmain')
a_bf = BeautifulSoup(str(div[0]), 'html.parser')
a = a_bf.find_all('a')
print(a[0])
for each in a:
    print(each.string, server + each.get('href'))
