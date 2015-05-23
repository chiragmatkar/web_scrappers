from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors import LinkExtractor
from santa.items import SantaItem
import string
import urllib2
from scrapy.http.request import Request

class MySpider(CrawlSpider):
    name = 'santa2'
    allowed_domains = ['santabanta.com']
    start_urls = ['http://www.santabanta.com/wallpapers/aishwarya-rai/?page='+str(page)  for page in xrange(1,16)
                  ]


    def parse(self, response):
          hxs = response
          urls2=hxs.xpath('//a[contains(@href,"htm")]//@href').extract()
          for i in urls2:
            yield Request(urllib2.urlparse.urljoin('http://www.santabanta.com/', i[1:]+"?high=5"),callback=self.parse_url2)

    def parse_url2(self, response):
          hxs = response
          item = SantaItem()
          item['image']=hxs.xpath('//a[contains(@href, "full")]/img/@src').extract()
          return item




