#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2021-01-05
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# 13632088
# max_cursor=1607005096000
# min_cursor=1609860151000
"""
aweme.snssdk.com;
log.snssdk.com;
p5-dy-ipv6.byteimg.com;
p3-dy-ipv6.byteimg.com;p26-dy.byteimg.com;

webcast.amemv.com;
"""

import requests


url = 'https://aweme.snssdk.com/aweme/v1/aweme/post/?source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&publish_video_strategy_type=2&max_cursor=0&sec_user_id=MS4wLjABAAAAqiS54tMmRXp4znZU7OQJS2exmfLoXB0oiHo1SFajTBg&count=20&is_order_flow=0&longitude=114.56962337758173&latitude=40.00226648118827&location_permission=true&os_api=22&device_type=SM-G973N&ssmix=a&manifest_version_code=130901&dpi=320&uuid=351564422117622&app_name=aweme&version_name=13.9.0&ts=1609864586&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=13909900&channel=tengxun_new&_rticket=1609864587395&device_platform=android&iid=1600542259283175&version_code=130900&cdid=5c48cb70-2eb7-4709-82a3-75929677122c&openudid=f795f21196fb5adf&device_id=1020000118778600&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=samsung&aid=1128&mcc_mnc=46007'
url = 'https://aweme.snssdk.com/aweme/v1/aweme/post/?source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&publish_video_strategy_type=2&max_cursor=0&sec_user_id=MS4wLjABAAAA78Qx0bOctRk8tLsatEPfcs8JjqqUvqleUIIKpHXSGQIlJxW25Ory2_Lf2pTmbXdo&count=20&is_order_flow=0&longitude=114.56962337758173&latitude=40.00226648118827&location_permission=true&os_api=22&device_type=SM-G973N&ssmix=a&manifest_version_code=130901&dpi=320&uuid=351564422117622&app_name=aweme&version_name=13.9.0&'+ \
      'ts=1609865760' + \
      '&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=13909900&channel=tengxun_new&_rticket=1609865194079&device_platform=android&iid=1600542259283175&version_code=130900&cdid=5c48cb70-2eb7-4709-82a3-75929677122c&openudid=f795f21196fb5adf&device_id=1020000118778600&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=samsung&aid=1128&mcc_mnc=46007'

headers = {
    'User-Agent': 'okhttp/3.10.0.1',
    'Host': 'aweme.snssdk.com',
    'Cookie': 'install_id=1600542259283175; ttreq=1$a7f704df58dca38069b5233aa3a0b655e1e4c322; odin_tt=5446c8081935b5531f52b2ff85b3796df7b293cd08df7b39ff8e94c76b471b619197df31d5b4cf4323b50db0d653ea242a21af0efe1f83132f6042b55a7541b5; MONITOR_WEB_ID=1aa37a36-91f9-418e-8969-8ab5c3695286'
}

response = requests.get(url, headers=headers)

print(response.content.decode('utf-8'))
# print(response.url)
print(response.json())


# print(html)
# with open('dy_video.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)
