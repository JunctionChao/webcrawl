import scrapy
import re

class Github2Spider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        # 自动从response中寻找form表单，找到 action 的登陆地址
        # 自动预填充登陆页面与会话相关的数据或身份验证token, 通常是这些 <input type="hidden"> 元素
        # 多个表单参数可以控制定位指定表单
        yield scrapy.http.FormRequest.from_response(
            response,
            formdata={
                "login": "123456@qq.com",
                "password": "123456"
            },
            callback=self.after_login
        )

    def after_login(self, response):
        print(re.findall("JunctionChao", response.body.decode()))
