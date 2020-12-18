import scrapy
from scrapy_redis.spiders import RedisSpider

# 基于redis的分布式爬虫
# 程序启动后会从redis中读取列表名为redis_key的start_urls
# 如果redis列表中没数据则程序会阻塞，直到push进去一个start_url，爬虫解阻塞，开始爬取数据
class DdbookSpider(RedisSpider):
    name = 'ddbook'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://book.dangdang.com/']
    redis_key = "ddbookspider:start_urls"

    def parse(self, response):
        # 大分类
        div_list = response.xpath("//div[@class='con flq_body']/div")
        for div in div_list:
            item = {}
            b_cate_list = div.xpath("./dl/dt//text()").extract()
            item["b_cate"] = [l.strip() for l in b_cate_list if len(l.strip())>0]
            # 中间分类
            dl_list = div.xpath("./div//dl[@class='inner_dl']")
            for dl in dl_list:
                item["m_cate"] = dl.xpath("./dt/a/text()").extract_first()
                # 小分类
                a_list = dl.xpath("./dd/a")
                for a in a_list:
                    item["s_href"] = a.xpath("./@href").extract_first()
                    item["s_cate"] = a.xpath("./text()").extract_first()

                    if item["s_href"] and "category.dangdang.com" in item["s_href"]: # 这里过滤掉电子书和一些不规则url
                        yield scrapy.Request(
                            item["s_href"],
                            callback=self.parse_book_list,
                            meta={"item": item.copy()}
                        )

    def parse_book_list(self, response):
        item = response.meta["item"].copy()
        li_list = response.xpath("//ul[@class='bigimg']/li")
        for li in li_list:
            item["book_img"] = li.xpath("./a/img/@src").extract_first()
            if item["book_img"] == "images/model/guan/url_none.png":
                item["book_img"] = li.xpath("./a/img/@data-original").extract_first()
            item["book_href"] = li.xpath("./a/@href").extract_first()
            item["book_name"] = li.xpath("./p[@class='name']/a/@title").extract_first().strip()
            item["book_desc"] = li.xpath("./p[@class='detail']/text()").extract_first()
            if not item["book_desc"]:
                item["book_desc"] = ""
            item["book_price"] = li.xpath(".//span[@class='search_now_price']/text()").extract_first()
            item["book_author"] = li.xpath("./p[@class='search_book_author']/span[1]/a/text()").extract()
            item["book_publish_date"] = li.xpath("./p[@class='search_book_author']/span[2]/text()").extract_first()
            item["book_publisher"] = li.xpath("./p[@class='search_book_author']/span[3]/a/text()").extract_first()
            item["book_comments_count"] = li.xpath("./p[class='search_star_line']/a/text()").extract_first()
            if not item["book_comments_count"]:
                item["book_comments_count"] = "0条评论"
            # print(item)
            yield item

        next_page_url = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(
                next_page_url,
                callback=self.parse_book_list,
                meta={"item": response.meta["item"]}
            )
