import scrapy
import logging
import re

logger = logging.getLogger(__name__)

class JdbookSpider(scrapy.Spider):
    name = 'jdbook'
    allowed_domains = ['jd.com']
    headers = {
        "referer": "https://book.jd.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
    }

    # 主页需要特定的请求头，重写start_requests方法
    def start_requests(self):
        start_url = "https://pjapi.jd.com/book/sort?source=bookSort"
        yield scrapy.http.Request(
            url=start_url,
            callback=self.parse,
            headers=self.headers
        )

    def parse(self, response):
        data = response.json()
        if data["code"] != 0:
            logger.warning(f"url: {response.url} 主页请求数据失败")
            return
        book_data = data["data"]
        for b_cate in book_data:
            item = {}
            item["b_cate"] = b_cate["categoryName"]
            top_cate_id = int(b_cate["fatherCategoryId"])
            father_cate_id = int(b_cate["categoryId"])
            for s_cate in b_cate["sonList"]:
                item["s_cate"] = s_cate["categoryName"]
                cate_id = int(s_cate["categoryId"])
                # https://list.jd.com/list.html?cat=1713,3260,3341
                url = "https://list.jd.com/list.html?cat=" + ",".join((str(id) for id in (top_cate_id, father_cate_id, cate_id)))
                yield scrapy.http.Request(
                    url,
                    callback=self.parse_book_list,
                    headers=self.headers,
                    meta={"item": item.copy()}
                )
                
    def parse_book_list(self, response):
        item = response.meta["item"].copy()
        li_list = response.xpath("//div[@id='J_goodsList']/ul/li")
        for li in li_list:
            url = li.xpath(".//div[@class='p-img']/a/img/@data-lazy-img").extract_first()
            if url:
                item["book_img"] = response.urljoin(url)
            item["book_href"] = response.urljoin(li.xpath(".//div[@class='p-img']/a/@href").extract_first())
            item["book_name"] = li.xpath(".//div[@class='p-name']/a/em/text()").extract_first()
            item["book_author"] = li.xpath(".//div[@class='p-bookdetails']/span[@class='p-bi-name']/a/text()").extract()
            item["book_publisher"] = li.xpath(".//div[@class='p-bookdetails']/span[@class='p-bi-store']/a/text()").extract()
            item["book_publish_date"] = li.xpath(".//div[@class='p-bookdetails']/span[@class='p-bi-date']/text()").extract_first()
            item["book_price"] = li.xpath(".//div[@class='p-price']//i/text()").extract_first()
            print(item)
            yield item
            
        # 翻页，JD页数是按1,3,5,7...
        current_page = int(re.search(r"page:\"(\d+)\"", response.text).group(1))
        count_page = int(re.search(r"page_count:\"(\d+)\"", response.text).group(1))
        if current_page < count_page:
            next_page = current_page + 2
            next_url = re.sub(r"page=\d+", "page={}".format(next_page), response.url)
            yield scrapy.http.Request(
                next_url,
                callback=self.parse_book_list,
                meta={"item": response.meta["item"]}
            )



