import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/975499361/profile']

    # 重写start_requests方法，指定start_urls的处理方式，这里携带cookies
    def start_requests(self):
        cookies = 'anonymid=khyvrhx6-80yu6s; _r01_=1; JSESSIONID=abcR9eeVJ4qve98NoXeyx; ick_login=e0b2c46b-0066-4e59-934b-9319f57aa74f; taihe_bi_sdk_session=69d5d17b433c4c283ca2c705a633d3c2; taihe_bi_sdk_uid=69a5213039176a4317d99b7d6658c100; depovince=BJ; t=94a36386e713921666a996a559ddb30d1; societyguester=94a36386e713921666a996a559ddb30d1; id=975499361; xnsid=c4a49c44; ver=7.0; loginfrom=null; jebecookies=007353c2-6c26-4298-a479-ccac77ef4dc9|||||; wp_fold=0'
        cookies = {kv.split("=")[0]: kv.split("=")[1] for kv in cookies.split("; ")}
        yield scrapy.http.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    # 后续请求会自动带上cookies，scrapy默认开启cookies
    def parse(self, response):
        print(re.findall("曳游", response.body.decode()))
        yield scrapy.http.Request(
            "http://www.renren.com/975499361/profile?v=info_timeline",
            callback=self.parse_detail
        )

    def parse_detail(self, response):
        print(re.findall("曳游", response.body.decode()))