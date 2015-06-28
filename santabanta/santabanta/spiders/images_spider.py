from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.selector import HtmlXPathSelector
from santabanta.items import SantaBantaItem
from scrapy.http.request import Request
import urllib2
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


# This spider scraps images gallery from www.santabanta.com
class MySpider(CrawlSpider):
    name = 'santabanta2'
    
    def __init__(self, *args, **kwargs):
      super(MySpider, self).__init__(*args, **kwargs)
      self.allowed_domains = ['santabanta.com']
      self.images = str(kwargs.get('images'))
      self.start_urls = ['http://www.santabanta.com/images/' + str(self.images)]

    rules = (Rule(SgmlLinkExtractor(allow=r'/?page=.*',),callback='parsePage', follow=True),)
    
    def parsePage(self,response):
        hxs=response
        urls2=hxs.xpath('//*[@class="imgdiv1"]//@href').extract()
        for i in urls2:
            print i
            yield Request(urllib2.urlparse.urljoin('http://www.santabanta.com/', i[1:]),callback=self.parse_url2)

    def parse_url2(self, response):
          hxs = response
          item = SantaBantaItem()
          item['image_urls']=hxs.xpath('//a[contains(@href, "gal")]/img/@src').extract()
          yield item
