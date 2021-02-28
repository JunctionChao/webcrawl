## Scrapy笔记

#### 基本命令

- 创建项目：`scrapy startproject projectname`

- 生成一个爬虫：`scrapy genspider weimobcases "weimob.com"`

  通过CrawlSpider生成爬虫：`scrapy genspider -t crawl weimobcases "weimob.com"`

  设置 name, allow_domain, start_urls

- 提取输出：完善spider中的parase方法，使用xpth等提取数据

- 保存数据：pipeline中保存数据

- 启动爬虫：`scrapy crawl weimobcases`

#### 日志使用

在需要的输出日志的位置

- ```python
  import logging
  logger = logging.getLogger(__name__)
  logger.warning("this is a warning")
  ```

- 在settings中设置LOG_LEVEL = "WARNING"， 设置log级别
- settings中设置日志保存文件LOG_FILE = "./crawl.log" ，设置后终端不会显示日志内容

[Scrapy爬虫框架之settings文件详解，内置设置](https://www.cnblogs.com/yoyowin/p/12165538.html)

#### scrapy_redis

scrapy_redis在scrapy的基础上实现了request去重，增量式爬虫，爬虫持久化，分布式等特性