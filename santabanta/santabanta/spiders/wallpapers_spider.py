from scrapy.spiders import CrawlSpider , Rule
from scrapy.selector import Selector
from santabanta.items import SantaBantaItem
from urllib.parse import urljoin
from scrapy.http.request import Request
import os


class MySpider(CrawlSpider):
    name = 'santabanta'

    def __init__(self, *args, **kwargs):
      super(MySpider, self).__init__(*args, **kwargs)
      self.allowed_domains = ['santabanta.com']
      self.wallpapers = str(kwargs.get('wallpapers'))
      self.start_urls = ['http://www.santabanta.com/wallpapers/' + str(self.wallpapers)]

    def parse(self, response):
          sel = Selector(response)
          pages = sel.xpath('//*[@class=\'paging-div-new\']//@href').extract()
          if  pages:
            yield Request(response.url,callback=self.parse_url1)
            for j in pages:
                yield Request(urljoin('http://www.santabanta.com/', j[1:]),callback=self.parse_url1)
          else:
                yield Request(response.url,callback=self.parse_url1)

    def parse_url1(self,response):
        sel = Selector(response)
        urls2 = sel.xpath('//a[contains(@href,"htm")]//@href').extract()
        for i in urls2:
            yield Request(urljoin('http://www.santabanta.com/', i[1:]+"?high=5"),callback=self.parse_url2)

    def parse_url2(self, response):
          sel = Selector(response)
          item = SantaBantaItem()
          item['image_urls']= sel.xpath('//a[contains(@href, "full")]/img/@src').extract()
          yield item
