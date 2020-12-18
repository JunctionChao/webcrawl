# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

import re, requests, json
import logging


class TiebaSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TiebaDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class ParseHtmlDownloaderMiddleware:
    def process_response(self, request, response, spider):
        if spider.name == 'tb2':
            # 对于帖子页面需要解析出注释形式的html
            # 否则后续的rules无法提取指定url
            if re.match(r"https://tieba\.baidu\.com/f\?kw=%E5%91%A8%E6%9D%B0%E4%BC%A6&ie=utf-8&tab=good", response.url):
                html_parse_list = re.findall(r'<!--(.*?)-->', response.body.decode(), re.S)
                html_parse = ''.join(html_parse_list)
                response._set_body(html_parse.encode(encoding=response.encoding)) # 修改response的body属性
                response._cached_ubody = html_parse # 修改response的text属性
            
        return response


# 以下为一些中间件案例
class CookiesMiddleware:
    def __init__(self, cookies_pool_url):
        self.logger = logging.getLogger(__name__)
        self.cookies_pool_url = cookies_pool_url

    # https://docs.scrapy.org/en/latest/topics/api.html?highlight=from_crawler#crawler-api
    """
    ScrapyAPI的主要入口点是Crawler对象，它通过from_crawler类方法传递给扩展
    Crawler对象提供接入所有的scrapy组件，这是扩展访问它们并将其功能连接到Scrapy的唯一方法
    也就是说通过Crawler对象，才能将我们自己定义的中间件接入到scrapy整个工作流程中，当然还需要在settings中配置好
    """
    # 通过该方法创建一个中间件实例，可以简单的理解为其他语言中的实例化重载机制
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            cookies_pool_url=crawler.settings.get("COOKIES_POOL_URL")
        )
    
    def _get_random_cookies(self):
        try:
            response = requests.get(self.cookies_pool_url)
            if response.status_code == 200:
                return json.loads(response.text)
        except ConnectionError:
            return None
    
    def process_request(self, request, spider):
        cookies = self._get_random_cookies()
        if cookies:
            request.cookies = cookies
            self.logger.debug('Using Cookies' + json.dumps(cookies))
        else:
            self.logger.debug('No Valid Cookies')


class ProxyMiddleware:
    def __init__(self, proxy_pool_url):
        self.logger = logging.getLogger(__name__)
        self.cookies_pool_url = proxy_pool_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            proxy_pool_url=crawler.settings.get("PROXY_POOL_URL")
        )

    def _get_random_proxy(self):
        try:
            response = requests.get(self.proxy_pool_url)
            if response.status_code == 200:
                return response.text
        except ConnectionError:
            return None

    def process_request(self, request, spider):
        proxy = self._get_random_proxy()
        if proxy:
            request.meta['proxy'] = "http://" + proxy
            self.logger.debug('Using Proxy: ' + proxy)
        else:
            self.logger.debug('No Proxy')


