#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2021-01-06
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

import requests
from pprint import pprint


url = 'https://aweme.snssdk.com/aweme/v1/aweme/post/?source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&publish_video_strategy_type=2&max_cursor=0&sec_user_id=MS4wLjABAAAAI-lEgbXAy9AcrRR_ujh1DfyWRuh1ZjxLdzmjMD948KY&count=20&is_order_flow=0&longitude=114.56962337758173&latitude=40.00226648118827&location_permission=true&os_api=22&device_type=SM-G973N&ssmix=a&manifest_version_code=130901&dpi=320&uuid=351564422117622&app_name=aweme&version_name=13.9.0&ts=1609867110&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=13909900&channel=tengxun_new&_rticket=1609867110662&device_platform=android&iid=1600542259283175&version_code=130900&cdid=5c48cb70-2eb7-4709-82a3-75929677122c&openudid=f795f21196fb5adf&device_id=1020000118778600&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=samsung&aid=1128&mcc_mnc=46007'
XTtToken1 = '00a27781509ab61b477346e7f767bb296702bd23a6df845d5071031288397d234ca68403361d7cda0b797189ef14684543a93a6dad8cd887b19affac39294d038e9d7ea581666d81fa2d33d62b9274c4ce9ac-1.0.0'
XTtToken2 = '00a27781509ab61b477346e7f767bb296702bd23a6df845d5071031288397d234ca68403361d7cda0b797189ef14684543a93a6dad8cd887b19affac39294d038e9d7ea581666d81fa2d33d62b9274c4ce9ac-1.0.0'
print(XTtToken1 == XTtToken2)

# headers = {
#     'User-Agent': 'okhttp/3.10.0.1',
#     'Host': 'aweme.snssdk.com',
#     'Cookie': 'install_id=1600542259283175; ttreq=1$a7f704df58dca38069b5233aa3a0b655e1e4c322; passport_csrf_token=db847db33b9801101795918fb1b8e4fe; passport_csrf_token_default=db847db33b9801101795918fb1b8e4fe; MONITOR_WEB_ID=3ab9381e-4929-46c5-9aad-8f11d9256ec2; d_ticket=9d9c8fbcf98e4516f40582977a2db3e918ac2; multi_sids=4292146724602957%3Aa27781509ab61b477346e7f767bb2967; odin_tt=c646dcca3e6fc6f4cc11ba30d981296b4043b32a9d08de155662cee4ddff326413e7a3da45444cc94563caecf38cca81b9bcd121d6dc44d3aefb3eca3e03b315; n_mh=4Tm58DHuZyu6eu3sZZQlPoNTYvHGFXur4UnCsexlg-U; sid_guard=a27781509ab61b477346e7f767bb2967%7C1609866842%7C5184000%7CSat%2C+06-Mar-2021+17%3A14%3A02+GMT; uid_tt=91d02867df48fc0d742fb6c2c378674d; uid_tt_ss=91d02867df48fc0d742fb6c2c378674d; sid_tt=a27781509ab61b477346e7f767bb2967; sessionid=a27781509ab61b477346e7f767bb2967; sessionid_ss=a27781509ab61b477346e7f767bb2967',
#     'tc_2021_now_client': '1609862844786',
#     'passport-sdk-version': '18',
#     'X-Tt-Token': '00a27781509ab61b477346e7f767bb296702bd23a6df845d5071031288397d234ca68403361d7cda0b797189ef14684543a93a6dad8cd887b19affac39294d038e9d7ea581666d81fa2d33d62b9274c4ce9ac-1.0.0',
#     'sdk-version': '2',
#     'X-SS-REQ-TICKET': '1609867109173',
#     'X-Tyhon': 'oBnULET+x1wkp/ZjdprgVSWq9Cprn/ljVqrwUz4=',
#     'X-Khronos': '1609918571',
#     'X-Gorgon': '0404c05200016f84f3f34669a3d7c6e9858d730695e69a94ad00'
# }

headers = {
    # 'User-Agent': 'okhttp/3.10.0.1',
    # 'Host': 'aweme.snssdk.com',
    # 'Cookie': 'install_id=1600542259283175; ttreq=1$a7f704df58dca38069b5233aa3a0b655e1e4c322; passport_csrf_token=db847db33b9801101795918fb1b8e4fe; passport_csrf_token_default=db847db33b9801101795918fb1b8e4fe; MONITOR_WEB_ID=3ab9381e-4929-46c5-9aad-8f11d9256ec2; d_ticket=9d9c8fbcf98e4516f40582977a2db3e918ac2; multi_sids=4292146724602957%3Aa27781509ab61b477346e7f767bb2967; odin_tt=c646dcca3e6fc6f4cc11ba30d981296b4043b32a9d08de155662cee4ddff326413e7a3da45444cc94563caecf38cca81b9bcd121d6dc44d3aefb3eca3e03b315; n_mh=4Tm58DHuZyu6eu3sZZQlPoNTYvHGFXur4UnCsexlg-U; sid_guard=a27781509ab61b477346e7f767bb2967%7C1609866842%7C5184000%7CSat%2C+06-Mar-2021+17%3A14%3A02+GMT; uid_tt=91d02867df48fc0d742fb6c2c378674d; uid_tt_ss=91d02867df48fc0d742fb6c2c378674d; sid_tt=a27781509ab61b477346e7f767bb2967; sessionid=a27781509ab61b477346e7f767bb2967; sessionid_ss=a27781509ab61b477346e7f767bb2967',
    # 'tc_2021_now_client': '1609862844786',
    # 'passport-sdk-version': '18',
    # 'X-Tt-Token': '00a27781509ab61b477346e7f767bb296702bd23a6df845d5071031288397d234ca68403361d7cda0b797189ef14684543a93a6dad8cd887b19affac39294d038e9d7ea581666d81fa2d33d62b9274c4ce9ac-1.0.0',
    # 'sdk-version': '2',
    # 'X-SS-REQ-TICKET': '1609867109173',
    # 'X-Tyhon': 'oBnULET+x1wkp/ZjdprgVSWq9Cprn/ljVqrwUz4=',
    # 'X-Khronos': '1609918571',
    # 'X-Gorgon': '0404c05200016f84f3f34669a3d7c6e9858d730695e69a94ad00'

    'tc_2021_now_client': '1609933776435',
    'passport-sdk-version': '18',
    'X-Tt-Token': '00ea31aaa58947a6f0f53705f700c6751c047e5891d1bce5d53113509b3d7972f09d3dd60f5f2fa9c8a25d30f5f3c401e5c0df281e8372bdeb2700e32f9bc43e7a031d6dd136bd59ed15bcb528e8f0d8c4670-1.0.0',
    'sdk-version': '2',
    'X-SS-REQ-TICKET': '1609933776328',
    'Cookie': 'odin_tt=200374b5ee2a98022ae9d48c8bb83d1b57ee88ca3fe497de05535a2ab4dfedbb01c433d9347d47a27d1d2a862014100c33bb8d2030d1a3b57c08bd6667c079d8',
    'X-Tyhon': 'SRYKPOFWOAPqXzoPzU05POxQHW/AdSV012QijiI=',
    'X-Khronos': '1609933776',
    'X-Gorgon': '0404609f0001e73fcaec74f823022a80532ad130d4acd68dad06',
    'Host': 'aweme.snssdk.com'
}


response = requests.get(url, headers=headers)
# pprint(response.json())
data = response.json()
print(data)

if data['aweme_list']:
    extract_data = []
    aweme_list = data['aweme_list']
    for aweme in aweme_list:
        d = {}
        d['aweme_id'] = aweme['aweme_id']
        d['desc'] = aweme['desc']
        d['create_time'] = aweme['create_time']
        d['download_url_list'] = aweme['video']['download_addr']['url_list']
        extract_data.append(d)
    print(len(extract_data))
    pprint(extract_data)


else:
    print('个人作品获取失败')