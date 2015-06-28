from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.contrib.linkextractors import LinkExtractor
from LocName.items import LocNameItem

class LocNameSpider(CrawlSpider):
    name = 'InternalLinkExtractor'
    def __init__(self, *args, **kwargs):
      super(LocNameSpider, self).__init__(*args, **kwargs)
      self.start_urls = [kwargs.get('start_url')]
    rules = (Rule(LinkExtractor(allow=()), callback='parse_obj', follow=True),)

    def parse_obj(self,response):
        for link in LinkExtractor(allow=self.start_urls).extract_links(response):
            item = LocNameItem()
            item['url'] = link.url
            yield item

