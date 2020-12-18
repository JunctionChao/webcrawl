# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # 给redis中存储的Request对象进行去重
SCHEDULER = "scrapy_redis.scheduler.Scheduler" # 指定scheduler队列
SCHEDULER_PERSIST = True  # 是否持久化队列中的内容，为False时在关闭redis会清空redis，True可实现断点爬取
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 400,  #scrapy_redis 实现的item保存到redis的pipeline
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

# REDIS_URL = "redis://127.0.0.1:6379"
REDIS_URL = "redis://:{psw}@{host}:{port}".format(host="127.0.0.1",port=6379,psw='developer')

# REDIS_HOST = "127.0.0.1"
# REDIS_PORT = 6379