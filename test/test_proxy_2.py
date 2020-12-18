#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://zhuanlan.zhihu.com/p/79466893
import requests
from bs4 import BeautifulSoup


def validate(proxies=None):
    https_url = "https://jsonip.com/"
    # https_url = 'https://ip.cn/api/index?ip=&type=0'
    http_url = 'http://ip111.cn/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }
    try:
        https_r = requests.get(https_url, headers=headers, proxies=proxies, timeout=10)
        print(https_r.json())
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)
        
        
    



    http_r = requests.get(http_url, headers=headers, proxies=proxies, timeout=10)
    print(http_r.status_code)
    # with open("http_r.html", "w", encoding='utf-8') as f:
    #     f.write(http_r.content.decode('utf-8'))
    bs = BeautifulSoup(http_r.content.decode('utf-8'), 'lxml')
    divs = bs.find_all('div', class_="card-body")
    for div in divs:
        print(div.get_text().strip())

    # soup = BeautifulSoup(http_r.content, 'html.parser')
    # result = soup.find(class_='card-body').get_text().strip().split('''\n''')[0]

    # print(f"当前使用代理：{proxies.values()}")
    # print(f"访问https网站使用代理：{https_r.json()}")
    # print(f"访问http网站使用代理：{result}")


if __name__ == '__main__':
    # https://www.fanqieip.com
    proxies = {
        "http": "http://218.72.185.39:28193",
        "https": "https://218.72.185.39:28193"
    }
    validate(proxies)