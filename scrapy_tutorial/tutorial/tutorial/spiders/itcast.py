import scrapy
import logging


logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # ret = response.xpath("//div[@class='maincon']//h2/text()").extract()
        # print(ret)

        # 分组
        li_list = response.xpath("//div[@class='maincon']//li")
        for li in li_list:
            item = {}
            # item["name"] = li.xpath(".//h2/text()").extract()[0]
            item["name"] = li.xpath(".//h2/text()").extract_first() # extract_first取不到值就会返回None
            # item["title"] = li.xpath(".//h2/span/text()").extract()[0]
            item["title"] = li.xpath(".//h2/span/text()").extract_first()
            item["tags"] = li.xpath(".//h3/span/text()").extract()
            # print(item)
            # 该方法返回的对象只能是以下类型：Request, BaseItem, dict or None
            
            yield item