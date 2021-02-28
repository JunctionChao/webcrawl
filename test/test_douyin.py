#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2021-01-05
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

import requests

def user_page():
    
    # random_field = 'RVb7WBAZG.rGG9zDDDoezEVW-0&dytk=a61cb3ce173fbfa0465051b2a6a9027e'
    # url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAF5ZfVgdRbJ3OPGJPMFHnDp2sdJaemZo3Aw6piEtkdOA&count=21&max_cursor=0&aid=1128&_signature=' + random_field
    
    # url = 'https://www.douyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAI-lEgbXAy9AcrRR_ujh1DfyWRuh1ZjxLdzmjMD948KY&count=21&max_cursor=0&aid=1128&_signature=moJz.QAAxYF99Yv78sPXsJqCc-&dytk='
    url = 'https://www.douyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAI-lEgbXAy9AcrRR_ujh1DfyWRuh1ZjxLdzmjMD948KY&count=21&max_cursor=0&aid=1128&_signature=kW.jSgAAzqd2GBtMN7T5L5Fv41&dytk='
    url = 'https://www.douyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAI-lEgbXAy9AcrRR_ujh1DfyWRuh1ZjxLdzmjMD948KY&count=21&max_cursor=0&aid=1128&_signature=g--LAwAA3ChkmHMFYOGS0oPvix&dytk='
    url = 'https://www.douyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAI-lEgbXAy9AcrRR_ujh1DfyWRuh1ZjxLdzmjMD948KY&count=21&max_cursor=0&aid=1128&_signature=VgVoowAACfGxcpClSOoPU1YFaL&dytk='
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
        'authority': 'www.douyin.com',
        'referer': 'https://www.douyin.com/share/user/60043717321?sec_uid=MS4wLjABAAAAI-lEgbXAy9AcrRR_ujh1DfyWRuh1ZjxLdzmjMD948KY',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'cookie': 'MONITOR_WEB_ID=1884b5dc-32a4-43d8-bf13-d1835b3d7f9e',
        'scheme': 'https'
        # 'Cookie': 'gr_user_id=9559a066-e688-42cc-9acb-c2dea23cb12a; b2901b7fe30fd554_gr_session_id=f5bc8ff5-084c-4f6c-a8ca-a62e1681653f; b2901b7fe30fd554_gr_session_id_f5bc8ff5-084c-4f6c-a8ca-a62e1681653f=true; grwng_uid=d9868b5e-4ce4-4bec-a73a-1930a1523c71; MONITOR_WEB_ID=abd324c5-4721-4d0a-ab45-2de5cfc29451'
    }
    response = requests.get(url, headers=headers)
    print(response.content.decode('utf-8'))
    data = response.json()
    print(data)
    #转换成json数据
    # resp = json.loads(response)
    # #遍历
    # for data in resp["aweme_list"]:
    #     # id值
    #     video_id = data['aweme_id']
    #     # 视频简介
    #     video_title = data['desc']
    #     # 构造视频网址
    #     video_url = 'https://www.iesdouyin.com/share/video/{}/?mid=1'
    #     # 填充内容
    #     video_douyin = video_url.format(video_id)
    #     print(video_id)
    #     print(video_title)
    #     print(video_douyin)


if __name__ == '__main__':
    user_page()