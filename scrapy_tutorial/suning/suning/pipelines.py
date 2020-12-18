# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class SuningPipeline:

    # def open_spider(self, spider): # spider启动时调用
    #     # spider.attribute = value # 可以在spider启动时添加属性
    #     self.mongo = pymongo.MongoClient()
    #     # self.collection = mongo["test"]["suning_book"]
    #     self.collection = mongo.test.suning_book

    def process_item(self, item, spider):
        # self.collection.insert(item)
        return item

    # def close_spider(self, spider):
    #     self.mongo.close()
