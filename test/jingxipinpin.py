#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
GET https://api.m.jd.com/jxpp.category.catePageRpc.cateSkuFetch?appid=jxpp_miniprogram&functionId=jxpp.category.catePageRpc.cateSkuFetch&t=1612200412386&body=%7B%22fcId%22%3A2000674%2C%22pageIndex%22%3A2%2C%22pageSize%22%3A30%2C%22page%22%3A2%2C%22time%22%3A1612200412452%2C%22signStr%22%3A%22d782d5b445905a1ffc2cb42f4b6c9cf3%22%7D&channel=wxappjxpp&cv=1.4.1&clientVersion=1.4.1&client=wxappjxpp HTTP/1.1
Host: api.m.jd.com
Connection: keep-alive
cookie: channel=wxappjxpp;openId=oKP9Q5Sn0guW9FgFNKOTQbl4i0pY;defaultHeadId=12903383;
User-Agent: Mozilla/5.0 (Linux; Android 5.1.1; VOG-AL10 Build/HUAWEIVOG-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.17.1720(0x27001134) Process/appbrand0 WeChat/arm32 NetType/WIFI Language/zh_CN ABI/arm32
charset: utf-8
Accept-Encoding: gzip,compress,br,deflate
content-type: application/json
Referer: https://servicewechat.com/wxf95d0d80e9d5bfc0/21/page-frame.html


"""
import requests

url = "https://api.m.jd.com/jxpp.category.catePageRpc.cateSkuFetch?appid=jxpp_miniprogram&functionId=jxpp.category.catePageRpc.cateSkuFetch&t=1612200412386&body=%7B%22fcId%22%3A2000674%2C%22pageIndex%22%3A2%2C%22pageSize%22%3A30%2C%22page%22%3A2%2C%22time%22%3A1612200412452%2C%22signStr%22%3A%22d782d5b445905a1ffc2cb42f4b6c9cf3%22%7D&channel=wxappjxpp&cv=1.4.1&clientVersion=1.4.1&client=wxappjxpp"
headers = {
    "cookie": "channel=wxappjxpp;openId=oKP9Q5Sn0guW9FgFNKOTQbl4i0pY;defaultHeadId=12903383;",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; VOG-AL10 Build/HUAWEIVOG-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.17.1720(0x27001134) Process/appbrand0 WeChat/arm32 NetType/WIFI Language/zh_CN ABI/arm32",
    "Referer": "https://servicewechat.com/wxf95d0d80e9d5bfc0/21/page-frame.html"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data["code"])
print(len(data["data"]["pageList"]))