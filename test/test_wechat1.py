#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from datetime import datetime
from pprint import pprint

"""
GET https://mp.weixin.qq.com/mp/appmsg_comment?action=getcomment&scene=0&appmsgid=2649791825&idx=1&comment_id=1619804738252816388&offset=0&limit=100&send_time=&uin=777&key=777&pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC%2BvgSlleHeYmJWT%2BVxDUUap3IDGnGjz0jcY6O&wxtoken=777&devicetype=android-25&clientversion=27001134&__biz=MjM5OTc2ODUxMw%3D%3D&appmsg_token=1094_qYvpQv3rrIWRjfKuSRRqMNKpY2XGbhEGbHpUFNDn3diC25KlBk8TirWxffbbkn7ZMOmteE4roI8zJjJB&x5=0&f=json HTTP/1.1
Host: mp.weixin.qq.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Linux; Android 7.1.2; TAS-AN00 Build/TAS-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 MMWEBID/573 MicroMessenger/7.0.17.1720(0x27001134) Process/toolsmp WeChat/arm32 NetType/WIFI Language/zh_CN ABI/arm32
X-Requested-With: XMLHttpRequest
Accept: */*
Referer: https://mp.weixin.qq.com/s?__biz=MjM5OTc2ODUxMw==&mid=2649791825&idx=1&sn=bf69fdec60331247654e130ecb057b66&chksm=bf3245ff8845cce9b4379ddc58ee9e7e7577eae8db8a616d6212167da7ee19cd732c52005d09&scene=21&ascene=0&devicetype=android-25&version=27001134&nettype=WIFI&lang=zh_CN&exportkey=Ax9kKmxrmJPoH9ek2ECln8w%3D&pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC%2BvgSlleHeYmJWT%2BVxDUUap3IDGnGjz0jcY6O&wx_header=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: rewardsn=; wxtokenkey=777; wxuin=3791121548; devicetype=android-25; version=27001134; lang=zh_CN; pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC+vgSlleHeYmJWT+VxDUUap3IDGnGjz0jcY6O; wap_sid2=CIzZ348OEooBeV9IR2ZHWmQtVFlQWmNYbGxJcUd1V2FkNmtDbVUzUnplS0cwd0Y4RDFZNkwwZjVOOUFoeWVoOHphN0xEVDVKNTdhY1RMcjFVOGJHNmVaNlNjQzhDSTNSck96Y0VkRWVHZUVXeXlPVHpSY3V5MnhFR3N5bExVMHlxcHc3ckQwSDVta2RpTVNBQUF+MO+9u/8FOA1AAQ==


GET https://mp.weixin.qq.com/mp/appmsg_comment?action=getcomment&scene=0&appmsgid=2649788541&idx=1&comment_id=1572083934367170561&offset=0&limit=100&send_time=&uin=777&key=777&pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC%2BvgSlleHeYmJWT%2BVxDUUap3IDGnGjz0jcY6O&wxtoken=777&devicetype=android-25&clientversion=27001134&__biz=MjM5OTc2ODUxMw%3D%3D&appmsg_token=1094_SrYgVCGKTs5ElhmniFXuq2cpDtSHb05xmpOOtxTUkdwjGBKVcZIGqKFd6RvaLtqH4KSyoJrvyppMkiYZ&x5=0&f=json HTTP/1.1
Host: mp.weixin.qq.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Linux; Android 7.1.2; TAS-AN00 Build/TAS-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 MMWEBID/573 MicroMessenger/7.0.17.1720(0x27001134) Process/toolsmp WeChat/arm32 NetType/WIFI Language/zh_CN ABI/arm32
X-Requested-With: XMLHttpRequest
Accept: */*
Referer: https://mp.weixin.qq.com/s?__biz=MjM5OTc2ODUxMw==&mid=2649788541&idx=1&sn=738a33f5d4eb36058360981e6d90ada4&chksm=bf3248d38845c1c590398e567482f64bab41136484bef2ba57bcb0829259e77aee61b8b5a7cf&scene=21&ascene=0&devicetype=android-25&version=27001134&nettype=WIFI&lang=zh_CN&exportkey=A9VTenELCy57TrIwgEdN6lo%3D&pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC%2BvgSlleHeYmJWT%2BVxDUUap3IDGnGjz0jcY6O&wx_header=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: rewardsn=; wxtokenkey=777; wxuin=3791121548; devicetype=android-25; version=27001134; lang=zh_CN; pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC+vgSlleHeYmJWT+VxDUUap3IDGnGjz0jcY6O; wap_sid2=CIzZ348OEooBeV9IRHFGWmI2U08zOERhVWRDXzBNNlhBT1ROU0tSQndLQXpuYmhMOXpwTHBHd3U3eHRLMWZwUy1wWUpoNEJ0WnIteTZzSXBGU3NKVVd6NWVRUnlTbkwtY0NOQXVWYkJIbFRuMThYRzB2ZFZIV0VYQy1JZUNjUktHejdQNXZUWW95c05TTVNBQUF+MJLku/8FOA1AAQ==


"""

url = "https://mp.weixin.qq.com/mp/appmsg_comment?action=getcomment&scene=0&appmsgid=2649791825&idx=1&comment_id=1619804738252816388&offset=0&limit=100&send_time=&uin=777&key=777&pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC%2BvgSlleHeYmJWT%2BVxDUUap3IDGnGjz0jcY6O&wxtoken=777&devicetype=android-25&clientversion=27001134&__biz=MjM5OTc2ODUxMw%3D%3D&appmsg_token=1094_qYvpQv3rrIWRjfKuSRRqMNKpY2XGbhEGbHpUFNDn3diC25KlBk8TirWxffbbkn7ZMOmteE4roI8zJjJB&x5=0&f=json"
headers = {
    'Referer': 'https://mp.weixin.qq.com/s?__biz=MjM5OTc2ODUxMw==&mid=2649791825&idx=1&sn=bf69fdec60331247654e130ecb057b66&chksm=bf3245ff8845cce9b4379ddc58ee9e7e7577eae8db8a616d6212167da7ee19cd732c52005d09&scene=21&ascene=0&devicetype=android-25&version=27001134&nettype=WIFI&lang=zh_CN&exportkey=Ax9kKmxrmJPoH9ek2ECln8w%3D&pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC%2BvgSlleHeYmJWT%2BVxDUUap3IDGnGjz0jcY6O&wx_header=1',
    'Cookie': 'rewardsn=; wxtokenkey=777; wxuin=3791121548; devicetype=android-25; version=27001134; lang=zh_CN; pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC+vgSlleHeYmJWT+VxDUUap3IDGnGjz0jcY6O; wap_sid2=CIzZ348OEooBeV9IR2ZHWmQtVFlQWmNYbGxJcUd1V2FkNmtDbVUzUnplS0cwd0Y4RDFZNkwwZjVOOUFoeWVoOHphN0xEVDVKNTdhY1RMcjFVOGJHNmVaNlNjQzhDSTNSck96Y0VkRWVHZUVXeXlPVHpSY3V5MnhFR3N5bExVMHlxcHc3ckQwSDVta2RpTVNBQUF+MO+9u/8FOA1AAQ=='
}
response = requests.get(url, headers=headers)
data = response.json()
# print(data)
if data['base_resp']['ret'] == 0 and data['base_resp']['errmsg'] == 'ok':
    total = data['elected_comment_total_cnt']
    print(f'成功获取 {total} 条评论')
    elected_comment = data['elected_comment']
    print(len(elected_comment))
    c_list = []

    for comment in elected_comment:
        timestamp = comment['create_time']
        create_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        d = {
            '昵称': comment['nick_name'],
            '评论内容': comment['content'],
            '评论点赞数': comment['like_num'],
            '评论时间': create_time,
        }
        # 评论回复
        reply_list = comment['reply']['reply_list']
        if reply_list:
            replys = [reply['content'] for reply in reply_list]
            d['评论回复'] = replys
        c_list.append(d)

    pprint(c_list)
