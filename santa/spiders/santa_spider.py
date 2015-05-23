from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors import LinkExtractor
from santa.items import SantaItem
import string
import urllib2
from scrapy.http.request import Request
import os
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class MySpider(CrawlSpider):
    name = 'santa4'
    allowed_domains = ['santabanta.com']
    actress='kelly-brook'  #check the naming convention as mentioned in santabanta pages
    last_page_no=8          #last page no of pictures in santabanta
    start_urls = ['http://www.santabanta.com/wallpapers/'+actress+'/?page='+str(x) for x in range(1,last_page_no)]

    def parse(self, response):
          hxs = response
          urls2=hxs.xpath('//a[contains(@href,"htm")]//@href').extract()
          for i in urls2:
            yield Request(urllib2.urlparse.urljoin('http://www.santabanta.com/', i[1:]+"?high=5"),callback=self.parse_url2)


    def parse_url2(self, response):
          hxs = response
          item = SantaItem()
          item['image_urls']=hxs.xpath('//a[contains(@href, "full")]/img/@src').extract()
          yield item

