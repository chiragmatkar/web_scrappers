from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.contrib.linkextractors import LinkExtractor
from LocName.items import LocNameItem

class LocNameSpider(CrawlSpider):
  name = 'LinkExtractor'

  def __init__(self, *args, **kwargs):
      super(LocNameSpider, self).__init__(*args, **kwargs)
      self.start_urls = [kwargs.get('start_url')]

  rules = (Rule(LinkExtractor(allow=()), callback='parse_obj', follow=True),)

  def parse_obj(self,response):
    item = LocNameItem()
    for link in LinkExtractor(allow=self.start_url).extract_links(response):
            item['internal_url'] = link.url
    yield item   
