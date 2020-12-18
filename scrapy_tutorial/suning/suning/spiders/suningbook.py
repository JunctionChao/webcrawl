import scrapy
import re, json

# 'https://pas.suning.com/nspcsale_0_'+ passPartNumber+'_'+ partNumber +'_'+ vendorCode +'_20_021_0210199_502282_1000267_9264_12113_Z001___R9011207_1.0________0___1.0_2__502320_502689_.html?callback=pcData'
# 'https://pas.suning.com/nspcsale_0_000000011516769347_000000011516769347_0071014399_20_021_0210199_502282_1000267_9264_12113_Z001___R9011207_1.0________0___1.0_2__502320_502689_.html?callback=pcData'

class SuningbookSpider(scrapy.Spider):
    name = 'suningbook'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        menu_item_list = response.xpath("//div[@class='menu-list']/div[@class='menu-item']")[:-2]
        menu_sub_list = response.xpath("//div[@class='menu-list']/div[@class='menu-sub']")
            
        for menu_item, menu_sub_item in zip(menu_item_list, menu_sub_list):
            item = {}
            # 一级分类
            item['level1_cate'] = menu_item.xpath(".//h3/a/text()").extract_first()
            p_list = menu_sub_item.xpath("./div[@class='submenu-left']/p")
            ul_list = menu_sub_item.xpath("./div[@class='submenu-left']/ul")
            for p, ul in zip(p_list, ul_list):
                # 二级分类
                item['level2_cate'] = p.xpath("./a/text()").extract_first()
                li_list = ul.xpath("./li")
                for li in li_list:
                    # 三级分类
                    item['level3_cate'] = li.xpath("./a/text()").extract_first()
                    item['level3_href'] = li.xpath("./a/@href").extract_first()
                    if item['level3_href']:
                        yield scrapy.Request(
                            item['level3_href'],
                            callback=self.parse_book_list,
                            meta={"item": item.copy()} # 这里都是一层字典，而且字典值都是不可变类型，浅拷贝足矣
                        )

    def parse_book_list(self, response):
        item = response.meta['item'].copy()
        # 图书列表分组
        li_list = response.xpath("//div[@id='filter-results']/ul/li")
        for li in li_list:
            item['book_href'] = "https:" + li.xpath(".//div[@class='res-img']/div/a/@href").extract_first()
            item['book_img'] = "https:" + li.xpath(".//div[@class='res-img']/div/a/img/@src2").extract_first()
            item['book_store'] = li.xpath(".//div[@class='res-info']/p[last()]/@salesname").extract_first()

            yield scrapy.Request(
                item['book_href'],
                callback=self.parse_book_detail,
                meta={"item": item.copy()}
            )

        # 翻页
        """
        这里分为两类URL
        https://list.suning.com/1-502629-0.html
        https://list.suning.com/1-502629-1-0-0-0-0-14-0-4.html  # 第二页
        https://list.suning.com/1-502629-2-0-0-0-0-14-0-4.html  # 第三页

        https://search.suning.com/emall/bookSearch.do?keyword=%E9%9B%85%E6%80%9DIELTS
        https://search.suning.com/%E9%9B%85%E6%80%9DIELTS/&iy=0&ch=4&cp=1
        https://search.suning.com/%E9%9B%85%E6%80%9DIELTS/&iy=0&ch=4&cp=2
        """
        # current_page = int(re.findall("param\.currentPage = \"(.*?)\";", response.body.decode())[0])
        # count_pages = int(re.findall("param\.pageNumbers = \"(.*?)\";", response.body.decode())[0])
        # if current_page < count_pages - 1: # 页号是从0计数
        #     match_flag = re.search(r'keyword=(.*)', item['level3_href'])
        #     if match_flag:
        #         keyword = match_flag.group(1)
        #         next_url = "https://search.suning.com/" + keyword + "/&iy=0&ch=4&cp={}".format(current_page + 1)
        #     else:
        #         url_pre = re.search(r'(.*)0\.html', item['level3_href']).group(1)
        #         next_url = url_pre + "{}-0-0-0-0-14-0-4.html".format(current_page + 1)
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse_book_list,
        #         meta={"item": response.meta['item']}
        #     )


    def parse_book_detail(self, response):
        item = response.meta['item']
        html = response.text
        publisher = re.findall(r"\"brandName\":\"(.*?)\",", html)
        item["publisher"] = publisher[0] if publisher else None
        title = response.xpath("//title/text()").extract_first()
        if re.search(r'《(.*?)》', title):
            item["display_name"] = re.search(r'《(.*?)》', title).group(1)
        # print(item)

        passPartNumber = re.findall(r"\"passPartNumber\":\"(.*?)\"", html)
        partNumber = re.findall(r"\"partNumber\":\"(.*?)\"", html)
        vendorCode = re.findall(r"\"vendorCode\":\"(.*?)\"",html)
        if not passPartNumber or not partNumber or not vendorCode: # 过滤掉失效book
            print('失效的book: ', item['book_href'])
            return

        passPartNumber = passPartNumber[0]
        partNumber = partNumber[0]
        vendorCode = vendorCode[0]

        price_url = 'https://pas.suning.com/nspcsale_0_'+ passPartNumber + '_'+ partNumber + '_' + vendorCode + '_20_021_0210199_502282_1000267_9264_12113_Z001___R9011207_1.0________0___1.0_2__502320_502689_.html?callback=pcData'
        yield scrapy.Request(
            price_url,
            callback=self.parse_book_price,
            meta={"item": item.copy()}
        )

    def parse_book_price(self, response):
        item = response.meta['item']
        pc_data = response.text

        json_str = re.findall("pcData\((.*)\)", pc_data, re.S)[0] #匹配包括换行符
        data = json.loads(json_str)
        if int(data["code"]) == 1:
            price = data["data"]["price"]["saleInfo"][0]["netPrice"]
            freight = data["data"]["freightObj"]["fare"]
            item["price"] = price
            item["freight"] = freight
            print(item)
            yield item




# 价格及运费api
# https://pas.suning.com/nspcsale_0_000000011516769347_000000011516769347_0071014399_20_021_0210199_502282_1000267_9264_12113_Z001___R9011207_1.0________0___1.0_2__502320_502689_.html?callback=pcData