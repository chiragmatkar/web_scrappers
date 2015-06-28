from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.contrib.linkextractors import LinkExtractor
from LocName.items import LocNameItem

class LocNameSpider(CrawlSpider):
  name = 'ExternalLinkExtractor'
  def __init__(self, *args, **kwargs):
      super(LocNameSpider, self).__init__(*args, **kwargs)
      self.start_urls = [kwargs.get('start_url')]
      self.allowed_domains=[kwargs.get('domain')]
  rules = (Rule(LinkExtractor(allow=()), callback='parse_obj', follow=True),)

  def parse_obj(self,response):
    for link in LinkExtractor(allow=(),deny = self.allowed_domains).extract_links(response):
        item = LocNameItem()
        item['url'] = link.url
        yield item
