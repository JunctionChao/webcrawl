# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging

logger = logging.getLogger(__name__)


class TutorialPipeline1:
    def process_item(self, item, spider):
        if spider.name == "itcast":
            item["subordinate"] = "传智播客"
        # print(item)
        return item

class TutorialPipeline2:
    def process_item(self, item, spider):
        logger.warning("-"*10)
        logger.warning(item)
        return item