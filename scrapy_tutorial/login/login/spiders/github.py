import scrapy
import re
from pprint import pprint
"""
commit: Sign in
authenticity_token: SDhgq3VmtAnlOchcyi/iXKx7n++nMFoqQiAOYxtDUt+ZUN6auqJ10tGdtujl053H33jDs1JAp22kchpwwaW0gA==
ga_id: 
login: 123456@qq.com
password: 123123
webauthn-support: supported
webauthn-iuvpaa-support: unsupported
return_to: 
allow_signup: 
client_id: 
integration: 
required_field_1b51: 
timestamp: 1607317841187
timestamp_secret: 81a7b74b2aa78a315a97b3d35de1d46a8650eb2ba2bd164af838322e19095c7b
"""

# 模拟登陆发送post请求
class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        print("authenticity_token: ", authenticity_token)
        webauthn_support = response.xpath("//input[@name='webauthn-support']/@value").extract_first()
        webauthn_iuvpaa_support = response.xpath("//input[@name='webauthn-iuvpaa-support']/@value").extract_first()
        timestamp = response.xpath("//input[@name='timestamp']/@value").extract_first()
        timestamp_secret = response.xpath("//input[@name='timestamp_secret']/@value").extract_first()
        commit = response.xpath("//input[@name='commit']/@value").extract_first()

        return_to = response.xpath("//input[@name='return_to']/@value").extract_first()
        if not return_to:
            return_to = ""
        allow_signup = response.xpath("//input[@name='allow_signup']/@value").extract_first()
        if not allow_signup:
            allow_signup = ""
        client_id = response.xpath("//input[@name='client_id']/@value").extract_first()
        if not client_id:
            client_id = ""
        integration = response.xpath("//input[@name='integration']/@value").extract_first()
        if not integration:
            integration = ""
        ga_id = response.xpath("//input[@name='ga_id']/@value").extract_first()
        if not ga_id:
            ga_id = ""
        # xpath中使用正则
        required_field_str = response.xpath("//input[starts-with(@name, 'required_field_')]/@name").extract_first()
        print(required_field_str)
        required_field_value = response.xpath("//input[@name={}]/@value".format(required_field_str)).extract_first()
        if not required_field_value:
            required_field_value = ""
        
        post_data = dict(
            login="111111@qq.com",
            password="123456",
            authenticity_token=authenticity_token,
            ga_id=ga_id,
            webauthn_support=webauthn_support,
            webauthn_iuvpaa_support=webauthn_iuvpaa_support,
            return_to=return_to,
            allow_signup=allow_signup,
            client_id=client_id,
            integration=integration,
            timestamp=timestamp,
            timestamp_secret=timestamp_secret,
            commit=commit,
        )
        post_data[required_field_str] = required_field_value
        # pprint(post_data)
        yield scrapy.http.FormRequest(
            "http://github.com/session",
            formdata=post_data,
            callback=self.after_login
        )

    def after_login(self, response):
        print(re.findall("JunctionChao", response.body.decode()))


