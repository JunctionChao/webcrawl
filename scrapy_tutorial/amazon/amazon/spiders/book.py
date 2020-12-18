#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

# 基于redis的CrawlSpider爬虫
class BookSpider(RedisCrawlSpider):
    name = 'book'
    allowed_domains = ['amazon.cn']
    # start_urls = ['https://www.amazon.cn/Kindle%E7%94%B5%E5%AD%90%E4%B9%A6/b?ie=UTF8&node=116169071&ref_=nav_topnav_giftcert']
    redis_key = "amazon"
    # 根据xpath来定位提取url
    rules = (
        # 匹配大分类以及小分类的url地址
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='a-unordered-list a-nostyle a-vertical s-ref-indent-two']/div/li",)), follow=True),
        # 匹配图书的url地址  h2/.. 表示h2的父标签
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul/li//h2/..",)), callback='parse_book_detail'),
        # 列表页翻页的url地址
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='pagn']/span",)), follow=True),
    )

    def parse_book_detail(self, response):
        item = {}
        item["book_title"] = response.xpath("//span[@id='productTitle']/text()").extract_first().strip()
        item['book_author'] = response.xpath("//div[@id='bylineInfo']/span/a/text()").extract_first()
        item["book_img"] = response.xpath("//div[@id='ebooks-img-canvas']/img/@src").extract_first()
        item["book_price"] = response.xpath("//span[@class='a-color-base']/span/text()").extract_first().strip()
        cate_list = response.xpath("//div[@id='wayfinding-breadcrumbs_feature_div']/ul/li[not(@class)]/span/a/text()").extract()
        item["book_cate"] = [cate.strip() for cate in cate_list]
        item["book_url"] = response.url
        # /following-sibling::span[1] 获取当前节点的下一个span标签节点
        item["publisher"] = response.xpath("//span[contains(text(), '出版社')]/following-sibling::span[1]/text()").extract_first()
        yield item