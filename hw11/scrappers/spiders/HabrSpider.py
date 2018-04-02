from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field
from scrapy.linkextractors import LinkExtractor
from constants.consts import ALLOWED_DOMAINS, START_URLS, ALLOWED_PATTERNS
import logging

logger = logging.getLogger(__name__)


class HabrItem(Item):

    post_id = Field()
    datetime = Field()
    hubs = Field()
    tags = Field()
    counter_positive = Field()
    counter_favs = Field()
    counter_views = Field()
    counter_comments = Field()

    user = Field()
    karma = Field()
    ratio = Field()
    followers = Field()


class HabrSpider(CrawlSpider):
    name = 'Habr'
    allowed_domains = ALLOWED_DOMAINS

    start_urls = START_URLS

    rules = (
        Rule(LinkExtractor(allow=ALLOWED_PATTERNS),
             callback='parse_post'),
    )

    def parse_post(self, response):
        # post information
        item = HabrItem()
        item['post_id'] = response.url.split('/')[-2]
        item['datetime'] = response.css('.post__time::text').extract()
        item['hubs'] = response.css('.hub-link::text').extract()
        item['tags'] = response.css('.post__tag::text').extract()
        item['counter_positive'] = response.css('.voting-wjt__counter_positive::text').extract_first()
        item['counter_favs'] = response.css('.bookmark__counter::text').extract_first()
        item['counter_views'] = response.css('.post-stats__views-count::text').extract_first()
        item['counter_comments'] = response.css('.post-stats__comments-count::text').extract_first()
        # user data:
        item['user'] = response.css('.user-info__nickname_doggy::text').extract_first()
        item['karma'] = response.css('.stacked-counter__value_green::text').extract_first()
        item['ratio'] = response.css('.stacked-counter__value_magenta::text').extract_first()
        item['followers'] = response.css('.stacked-counter__value_blue::text').extract_first()
        yield item
