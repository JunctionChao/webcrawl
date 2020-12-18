import scrapy
import urllib
import re
from scrapy.selector import Selector


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E5%91%A8%E6%9D%B0%E4%BC%A6&ie=utf-8&tab=good']

    def parse(self, response):
        # with open("parse.html", 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        
        # print(type(response))
        # print(type(response).__mro__) # 查看类的继承关系

        # 贴吧是注释形式的html,不能直接使用xpath
        html_parse_list = re.findall(r'<!--(.*?)-->', response.body.decode(), re.S)
        html_parse = ''.join(html_parse_list)

        # response._set_body(html_parse.encode(encoding=response.encoding)) # 修改response的body属性
        # response._cached_ubody = html_parse # 修改response的text属性
        selector = Selector(text=html_parse)
        # with open("parse2.html", 'w', encoding='utf-8') as f:
        #     f.write(response.text)

        # 根据帖子进行分组
        li_list = selector.xpath("//li[@class=' j_thread_list clearfix']")
        for li in li_list:
            div = li.xpath("//div[@class='threadlist_lz clearfix']/div[@class='threadlist_title pull_left j_th_tit ']")
            item = {}
            item["title"] = div.xpath("./a/@title").extract_first()
            item["href"] = div.xpath("./a/@href").extract_first()
            item["img_list"] = []
            if item["href"]:
                # item["href"] = response.urljoin(item["href"]) # scrapy自带的urljoin,其实也是调用下面的方法，只是进行了包装
                item["href"] = urllib.parse.urljoin(response.url, item["href"])
                yield scrapy.http.Request(
                    item["href"],
                    callback=self.parse_detail,
                    meta={"item": item}
                )

        # 列表页翻页
        next_url = selector.xpath("//a[text()='下一页>']/@href").extract_first()
        if next_url:
            next_url = urllib.parse.urljoin(response.url, next_url)
            yield scrapy.http.Request(
                next_url,
                callback=self.parse
            )

    def parse_detail(self, response):
        # with open("parse_detail.html", 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        
        item = response.meta["item"]
        item["img_list"].extend(response.xpath("//img[@class='BDE_Image']/@src").extract())
        # 帖子内部翻页
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_url:
            next_url = urllib.parse.urljoin(response.url, next_url)
            yield scrapy.http.Request(
                next_url,
                callback=self.parse_detail,
                meta={"item": item}
            )
        else:
            print(item)
            yield item

