# import socket
# import socks
import requests
import re

# socks.set_default_proxy(socks.SOCKS5, "219.245.186.176", 1080)
# socket.socket = socks.socksocket

proxies = {
    "http": "socks5://222.37.106.225:45601",
    # "https": "socks5://222.37.106.225:45601"
}

rsp = requests.get('https://www.baidu.com', proxies=proxies)
print(rsp.status_code)
print(rsp.headers)
html = rsp.content.decode('utf-8')
print(html)
print(len(html))
ser = re.search('百度一下', html)
if ser:
    print(ser.span())