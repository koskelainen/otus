from scrappers.spiders.HabrSpider import HabrSpider

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_inline_scrapper():
    configure_logging(install_root_handler=True)
    # logger = logging.getLogger(__name__)
    # logger.setLevel(level=logging.DEBUG)
    # logger.setLevel(level=logging.INFO)
    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(HabrSpider)
        # yield runner.crawl(HabrSpider2)
        reactor.stop()

    crawl()
    reactor.run()