from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.selector import HtmlXPathSelector
from santabanta.items import SantaBantaItem
import urllib2
from scrapy.http.request import Request
import os
# This spider scraps images gallery from www.santabanta.com
class MySpider(CrawlSpider):
    name = 'santa'
    allowed_domains = ['santabanta.com']

def __init__(self, *args, **kwargs):
      super(MySpider, self).__init__(*args, **kwargs)
      self.images = [kwargs.get('images')]
      self.start_urls = ['http://www.santabanta.com/images/' + str(self.images)]



def parse(self,response):
        hxs=response
        urls2=hxs.xpath('//*[@class="imgdiv1"]//@href').extract()
        for i in urls2:
            yield Request(urllib2.urlparse.urljoin('http://www.santabanta.com/', i[1:]),callback=self.parse_url2)

def parse_url2(self, response):
          hxs = response
          item = SantaBantaItem()
          item['image_urls']=hxs.xpath('//a[contains(@href, "gal")]/img/@src').extract()
          yield item

