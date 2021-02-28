import scrapy


class WeimobcasesSpider(scrapy.Spider):
    name = 'weimobcases'
    allowed_domains = ['weimob.com']
    start_urls = ['https://www.weimob.com/website/cases.html']

    def parse(self, response):
        pass
