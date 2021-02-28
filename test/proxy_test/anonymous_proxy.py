import requests

url = "https://httpbin.org/get"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
}

rsp = requests.get(url, headers=headers)
print(rsp.status_code)
print(rsp.headers)
res = rsp.json()
print(res)
print("orgin_ip: ", res["origin"])


proxy = {
    "http": "http://49.87.117.28",
    # "https": "https://67.205.169.251:3128"
}
rsp = requests.get(url, headers=headers, proxies=proxy)
print(rsp.status_code)
print(rsp.headers)
res = rsp.json()
print(res)
print("orgin_ip: ", res["origin"])
    