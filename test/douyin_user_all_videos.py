#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2021-01-06
# Author  : Yuanbo Zhao (chaojunction@gmail.com)


import requests, time
from pprint import pprint
import urllib


class NoQuoteSession(requests.Session):
    def send(self, prep, **send_kwargs):
        table = {
            urllib.parse.quote('*'): '*', # 添加不进行编码的字符
        }
        for old, new in table.items():
            prep.url = prep.url.replace(old, new)
        return super(NoQuoteSession, self).send(prep, **send_kwargs)

s = NoQuoteSession()
# res = s.get(url)


url1 = 'https://aweme.snssdk.com/aweme/v1/aweme/post/?source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&publish_video_strategy_type=2&max_cursor=0&sec_user_id=MS4wLjABAAAAI-lEgbXAy9AcrRR_ujh1DfyWRuh1ZjxLdzmjMD948KY&count=20&is_order_flow=0&longitude=114.56962337758173&latitude=40.00226648118827&location_permission=true&os_api=22&device_type=SM-G973N&ssmix=a&manifest_version_code=130901&dpi=320&uuid=351564422117622&app_name=aweme&version_name=13.9.0&ts=1609867110&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=13909900&channel=tengxun_new&_rticket=1609867110662&device_platform=android&iid=1600542259283175&version_code=130900&cdid=5c48cb70-2eb7-4709-82a3-75929677122c&openudid=f795f21196fb5adf&device_id=1020000118778600&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=samsung&aid=1128&mcc_mnc=46007'
url2 = 'https://aweme.snssdk.com/aweme/v1/aweme/post/?source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&publish_video_strategy_type=2&max_cursor=0&sec_user_id=MS4wLjABAAAAI-lEgbXAy9AcrRR_ujh1DfyWRuh1ZjxLdzmjMD948KY&count=20&is_order_flow=0&longitude=114.56962337758173&latitude=40.00226648118827&location_permission=true&os_api=22&device_type=SM-G973N&ssmix=a&manifest_version_code=130901&dpi=320&uuid=351564422117622&app_name=aweme&version_name=13.9.0&ts=1609867110&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=13909900&channel=tengxun_new&_rticket=1609867110662&device_platform=android&iid=1600542259283175&version_code=130900&cdid=5c48cb70-2eb7-4709-82a3-75929677122c&openudid=f795f21196fb5adf&device_id=1020000118778600&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=samsung&aid=1128&mcc_mnc=46007'
print(url1 == url2)

# url = 'https://aweme.snssdk.com/aweme/v1/aweme/post/?source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&publish_video_strategy_type=2&max_cursor=1607005096000&sec_user_id=MS4wLjABAAAAI-lEgbXAy9AcrRR_ujh1DfyWRuh1ZjxLdzmjMD948KY&count=10&is_order_flow=0&longitude=114.56962337758173&latitude=40.00226648118827&location_permission=true&os_api=22&device_type=SM-G973N&ssmix=a&manifest_version_code=130901&dpi=320&uuid=351564422117622&app_name=aweme&version_name=13.9.0&ts=1609867119&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=13909900&channel=tengxun_new&_rticket=1609867119355&device_platform=android&iid=1600542259283175&version_code=130900&cdid=5c48cb70-2eb7-4709-82a3-75929677122c&openudid=f795f21196fb5adf&device_id=1020000118778600&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=samsung&aid=1128&mcc_mnc=46007'

params_str = 'source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&publish_video_strategy_type=2&max_cursor=0&sec_user_id=MS4wLjABAAAAI-lEgbXAy9AcrRR_ujh1DfyWRuh1ZjxLdzmjMD948KY&count=20&is_order_flow=0&longitude=114.56962337758173&latitude=40.00226648118827&location_permission=true&os_api=22&device_type=SM-G973N&ssmix=a&manifest_version_code=130901&dpi=320&uuid=351564422117622&app_name=aweme&version_name=13.9.0&ts=1609867110&cpu_support64=false&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=13909900&channel=tengxun_new&_rticket=1609867110662&device_platform=android&iid=1600542259283175&version_code=130900&cdid=5c48cb70-2eb7-4709-82a3-75929677122c&openudid=f795f21196fb5adf&device_id=1020000118778600&resolution=900*1600&os_version=5.1.1&language=zh&device_brand=samsung&aid=1128&mcc_mnc=46007'
params = {kv.split('=')[0]: kv.split('=')[1] for kv in params_str.split('&')}
# pprint(params)
# resolution=900%2A1600


headers = {
    'tc_2021_now_client': '1609867110878',
    'passport-sdk-version': '18',
    'X-Tt-Token': '00a27781509ab61b477346e7f767bb296702bd23a6df845d5071031288397d234ca68403361d7cda0b797189ef14684543a93a6dad8cd887b19affac39294d038e9d7ea581666d81fa2d33d62b9274c4ce9ac-1.0.0',
    'sdk-version': '2',
    'X-SS-REQ-TICKET': '1609867110663',
    'Cookie': 'install_id=1600542259283175; ttreq=1$a7f704df58dca38069b5233aa3a0b655e1e4c322; passport_csrf_token=db847db33b9801101795918fb1b8e4fe; passport_csrf_token_default=db847db33b9801101795918fb1b8e4fe; MONITOR_WEB_ID=3ab9381e-4929-46c5-9aad-8f11d9256ec2; d_ticket=9d9c8fbcf98e4516f40582977a2db3e918ac2; multi_sids=4292146724602957%3Aa27781509ab61b477346e7f767bb2967; odin_tt=c646dcca3e6fc6f4cc11ba30d981296b4043b32a9d08de155662cee4ddff326413e7a3da45444cc94563caecf38cca81b9bcd121d6dc44d3aefb3eca3e03b315; n_mh=4Tm58DHuZyu6eu3sZZQlPoNTYvHGFXur4UnCsexlg-U; sid_guard=a27781509ab61b477346e7f767bb2967%7C1609866842%7C5184000%7CSat%2C+06-Mar-2021+17%3A14%3A02+GMT; uid_tt=91d02867df48fc0d742fb6c2c378674d; uid_tt_ss=91d02867df48fc0d742fb6c2c378674d; sid_tt=a27781509ab61b477346e7f767bb2967; sessionid=a27781509ab61b477346e7f767bb2967; sessionid_ss=a27781509ab61b477346e7f767bb2967',
    'X-Tyhon': '5BO9hPy6hpPMnZSx4YLLoMHzmYHggJe1+4mmK3g=',
    'X-Khronos': '1609867110',
    'X-Gorgon': '0404607e000014f78330838d0b7fa2057fd828d7828758a98695',
    'Host': 'aweme.snssdk.com',
    'User-Agent': 'okhttp/3.10.0.1'
}


def get_info(url, headers, params, extract_data=[]):
    # response = requests.get(url=url, headers=headers, params=params)
    response = s.get(url=url, headers=headers, params=params)
    print(response.url)
    data = response.json()
    if data['aweme_list']:
        print('*'*50)
        print(len(data['aweme_list']))
        aweme_list = data['aweme_list']
        for aweme in aweme_list:
            d = {}
            d['aweme_id'] = aweme['aweme_id']
            d['desc'] = aweme['desc']
            d['create_time'] = aweme['create_time']
            d['download_url_list'] = aweme['video']['download_addr']['url_list']
        extract_data.append(d)
        params['max_cursor'] = data['max_cursor']
        params['count'] = 10
        time.sleep(2)
        if data['has_more']:
            get_info(url, headers, params, extract_data)
        else:
            s.close()
            return extract_data
            
    else:
        print('个人作品获取失败')
        s.close()
        return extract_data


if __name__ == '__main__':
    url = 'https://aweme.snssdk.com/aweme/v1/aweme/post/'
    # user_all_videos = get_info(url, headers, params)
    # print(len(user_all_videos))


# import requests
# url = "https://httpbin.org/get"

# params = {"show_env":'1'}

# r = requests.get(url,params=params)
# print(r.url)
# print(r.status_code)
# print(r.json())