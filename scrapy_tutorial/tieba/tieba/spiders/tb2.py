import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# 用下载中间件处理response，并且结合CrawlSpider的方式

class Tb2Spider(CrawlSpider):
    name = 'tb2'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E5%91%A8%E6%9D%B0%E4%BC%A6&ie=utf-8&tab=good']

    rules = (
        Rule(LinkExtractor(allow=r'/p/\d+'), callback='post_bar_detail'), # 帖子链接
        Rule(LinkExtractor(allow=r'/f\?kw=%E5%91%A8%E6%9D%B0%E4%BC%A6&ie=utf-8&tab=good&cid=&pn=\d+'), follow=True), # 帖子翻页链接
    )

    def post_bar_detail(self, response):
        # print("meta: ", response.meta)
        if "item" not in response.meta:
            item = {}
            # with open("post_parse.html", 'w', encoding='utf-8') as f:
            #     f.write(response.text)
            item["title"] = response.xpath("//h1[@class='core_title_txt  ']/@title").extract_first()
            if item["title"] is None:
                item["title"] = ""
        else:
            item = response.meta['item']

        if "img_list" not in item:
            item["img_list"] = response.xpath("//img[@class='BDE_Image']/@src").extract()
        else:
            item["img_list"].extend(response.xpath("//img[@class='BDE_Image']/@src").extract())
        
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.http.Request(
                next_url,
                callback=self.post_bar_detail,
                meta={"item": item}
            )
        else:
            print(item)
            yield item
