from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors import LinkExtractor
from santa.items import SantaItem
import string
import urllib2
from scrapy.http.request import Request

class MySpider(CrawlSpider):
    name = 'santa3'
    allowed_domains = ['santabanta.com']
    #start_urls =['http://www.santabanta.com/wallpapers/list/indian-celebrities(f)/2/?q=a']
    start_urls = ['http://www.santabanta.com/wallpapers/list/indian-celebrities(f)/2/?q='+ str(x) + '&pagesize=100' for x in list(string.ascii_lowercase)]

    def parse(self, response):
        hxs = response
        urls=hxs.xpath('//*[@class="wallpapers-category-div-3"]//@href').extract()
        for i in urls:
            yield Request(urllib2.urlparse.urljoin('http://www.santabanta.com/', i[1:]),callback=self.parse_url)

    def parse_url(self, response):
          hxs = response
          urls2=hxs.xpath('//a[contains(@href,"htm")]//@href').extract()
          for i in urls2:
            yield Request(urllib2.urlparse.urljoin('http://www.santabanta.com/', i[1:]+"?high=5",),callback=self.parse_url2)

    def parse_url2(self, response):
          hxs = response
          item = SantaItem()
          item['image_urls']=hxs.xpath('//a[contains(@href, "full")]/img/@src').extract()
          yield item