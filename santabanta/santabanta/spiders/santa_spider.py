from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.selector import HtmlXPathSelector
from santabanta.items import SantaBantaItem
import urllib2
from scrapy.http.request import Request
import os

class MySpider(CrawlSpider):
    name = 'santabanta'
    allowed_domains = ['santabanta.com']

    def __init__(self, wallpapers='kelly-brook'):
        self.start_urls = ['http://www.santabanta.com/wallpapers/' + str(wallpapers)]

    def parse(self, response):
          hxs = response
          pages= hxs.xpath('//*[@class=\'paging-div-new\']//@href').extract()
          if  pages:
            for j in pages:
                yield Request(urllib2.urlparse.urljoin('http://www.santabanta.com/', j[1:]),callback=self.parse_url1)
          else:
                yield Request(response.url,callback=self.parse_url1)

    def parse_url1(self,response):
        hxs=response
        urls2=hxs.xpath('//a[contains(@href,"htm")]//@href').extract()
        for i in urls2:
            yield Request(urllib2.urlparse.urljoin('http://www.santabanta.com/', i[1:]+"?high=5"),callback=self.parse_url2)

    def parse_url2(self, response):
          hxs = response
          item = SantaBantaItem()
          item['image_urls']=hxs.xpath('//a[contains(@href, "full")]/img/@src').extract()
          yield item
