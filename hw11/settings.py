# -*- coding: utf-8 -*-
# scrapy settings

BOT_NAME = 'scrappers'

SPIDER_MODULES = ['scrappers.spiders']
NEWSPIDER_MODULE = 'scrappers.spiders'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/56.0'

CONCURRENT_REQUESTS = 100
REACTOR_THREADPOOL_MAXSIZE = 2

LOG_LEVEL = 'DEBUG'
DOWNLOAD_DELAY = 2.5
DOWNLOAD_TIMEOUT = 15

ITEM_PIPELINES = {
    # 'scrappers.pipelines.pipelines.CsvPipeline': 300,
    # 'scrappers.pipelines.pipelines.XmlPipeline': 400,
    'scrappers.pipelines.pipelines.JsonPipeline': 500,
}
