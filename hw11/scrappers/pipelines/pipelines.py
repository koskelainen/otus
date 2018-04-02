from scrapy import signals
from scrapy.exporters import CsvItemExporter, XmlItemExporter, JsonItemExporter
import abc


class BasicPipeline(object):
    def __init__(self):
        self.files = {}
        self.exporter = None

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    @abc.abstractmethod
    def spider_opened(self, spider):
        raise NotImplementedError

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class CsvPipeline(BasicPipeline):

    def spider_opened(self, spider):
        file = open('%s_dump.csv' % spider.name, 'wb')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file, encoding='utf-8')
        self.exporter.start_exporting()


class JsonPipeline(BasicPipeline):

    def spider_opened(self, spider):
        file = open('%s_dump.json' % spider.name, 'wb')
        self.files[spider] = file
        self.exporter = JsonItemExporter(file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()


class XmlPipeline(BasicPipeline):

    def spider_opened(self, spider):
        file = open('%s_dump.xml' % spider.name, 'wb')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file, encoding='utf-8')
        self.exporter.start_exporting()
