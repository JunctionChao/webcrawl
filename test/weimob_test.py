#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2021-02-27
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

import requests, time
from lxml import etree


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
}
rsp = requests.get("http://www.weimob.com/website/cases.html", headers=headers)

html = rsp.text
with open("cases.html", "w", encoding="utf-8") as f:
    f.write(html)

# print(html)
# etree_html = etree.HTML(html)
# li_list = etree_html.xpath("//ul[@id='wp1']/li")
# print(li_list)
# for li in li_list:
#     p2 = li.xpath("./div[@class='f2-item-show f-oh']/p")
#     title = p2[0].xpath("text()")
#     desc = p2[1].xpath("text()")
#     print(title, desc)

etree_html = etree.HTML(html)
li_list = etree_html.xpath("//ul[@id='actBan2']/li")
print(li_list)
print(li_list[0])
for li in li_list[1:]:
    category = li.xpath("./p/text()")
    print(category, type(category))
