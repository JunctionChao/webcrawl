import scrapy
from scrapy.http import Request
import time, datetime, random, string
import json


class CareersSpider(scrapy.Spider):
    name = 'careers'
    allowed_domains = ['tencent.com']
    start_urls = [
        'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1606914458513&countryId=&cityId=2&bgIds=953&productId=&categoryId=40001001&parentCategoryId=&attrId=1&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn',
    ]

    headers = {
        "authority": "careers.tencent.com",
        "referer": "https://careers.tencent.com/search.html",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }
    # params = {
    #     "timestamp": "",
    #     "countryId": "",
    #     "cityId": 2,
    #     "bgIds": 953,
    #     "productId": "",
    #     "categoryId": 40001001,
    #     "parentCategoryId": "",
    #     "attrId": 1,
    #     "keyword": "",
    #     "pageIndex": 1,
    #     "pageSize": 10,  # 每页10条记录，第4页就无数据了
    #     "language": "zh-cn",
    #     "area": "cn"
    # }
    
    # 获取今天随机的时间戳
    def today_random_timestamp(self):
        
        def random_num(random_len=3): # 生成3位随机数
            digit = list(string.digits)
            random.shuffle(digit)
            return ''.join(digit[:random_len])

        today = datetime.date.today()
        today_start_timestamp = int(time.mktime(time.strptime(str(today), '%Y-%m-%d')))
        tomorrow = today + datetime.timedelta(days=1)
        today_end_timestamp = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1
        random_timestamp = random.randint(today_start_timestamp, today_end_timestamp)
        return str(random_timestamp) + random_num()

    def parse(self, response):
        data = response.json()

        if data["Code"] == 200 and data["Data"]["Posts"]:
            for item in data["Data"]["Posts"]:
                # print(item)
                yield item
            
            urlbase, get_params = response.url.split("?")
            params = dict()
            for kv in get_params.split("&"):
                key, val = kv.split("=")
                params[key] = val

            params["timestamp"] = self.today_random_timestamp()
            params["pageIndex"] = str(int(params["pageIndex"]) + 1)

            next_get_params = ["=".join((k, v)) for k, v in params.items()]
            next_url = "?".join((urlbase, "&".join(next_get_params)))

            yield Request(next_url, callback=self.parse, headers=self.headers)
        else:
            return
