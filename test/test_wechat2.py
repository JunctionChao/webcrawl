#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from pprint import pprint


def get_comments(url, headers):
    response = requests.get(url=url, headers=headers)
    data = response.json()
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

        return c_list


if __name__ == '__main__':
    headers = {
        # 'Referer': 'https://mp.weixin.qq.com/s?__biz=MjM5OTc2ODUxMw==&mid=2649791825&idx=1&sn=bf69fdec60331247654e130ecb057b66&chksm=bf3245ff8845cce9b4379ddc58ee9e7e7577eae8db8a616d6212167da7ee19cd732c52005d09&scene=21&ascene=0&devicetype=android-25&version=27001134&nettype=WIFI&lang=zh_CN&exportkey=Ax9kKmxrmJPoH9ek2ECln8w%3D&pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC%2BvgSlleHeYmJWT%2BVxDUUap3IDGnGjz0jcY6O&wx_header=1',
        'Cookie': 'rewardsn=; wxtokenkey=777; wxuin=3791121548; devicetype=android-25; version=27001134; lang=zh_CN; pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC+vgSlleHeYmJWT+VxDUUap3IDGnGjz0jcY6O; wap_sid2=CIzZ348OEooBeV9IR2ZHWmQtVFlQWmNYbGxJcUd1V2FkNmtDbVUzUnplS0cwd0Y4RDFZNkwwZjVOOUFoeWVoOHphN0xEVDVKNTdhY1RMcjFVOGJHNmVaNlNjQzhDSTNSck96Y0VkRWVHZUVXeXlPVHpSY3V5MnhFR3N5bExVMHlxcHc3ckQwSDVta2RpTVNBQUF+MO+9u/8FOA1AAQ=='
    }
    url = 'https://mp.weixin.qq.com/mp/appmsg_comment?action=getcomment&scene=0&appmsgid=2649794034&idx=1&comment_id=1658896135152844802&offset=0&limit=100&send_time=&uin=777&key=777&pass_ticket=UpoqmJIxh4MVUaWJHFf5SZUL00dC%2BvgSlleHeYmJWT%2BVxDUUap3IDGnGjz0jcY6O&wxtoken=777&devicetype=android-25&clientversion=27001134&__biz=MjM5OTc2ODUxMw%3D%3D&enterid=1609495630&appmsg_token=1094_ZcSMSwQtZCe9dksPF7xP-rNR-dJwvAEAdUge6QFL35iVfdB_19AQFEvsiZ3CSUskMOTUXqKqAkM61Jom&x5=0&f=json'
    comments = get_comments(url, headers)
    pprint(comments)