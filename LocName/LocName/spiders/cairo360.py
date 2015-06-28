from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.contrib.linkextractors import LinkExtractor
from LocName.items import LocNameItem

class Cairo360(CrawlSpider):
    name = 'cairo360'
    allowed_domains = ['cairo360.com']
    start_urls = ['http://www.cairo360.com/category']
    #depth_limit= 0
    rules = (Rule(LinkExtractor(allow=('')), callback='parse_obj', follow=True),)


def parse_obj(self,response):
    item = LocNameItem()
    for link in LinkExtractor(allow=self.allowed_domains).extract_links(response):
        item['url'] = link.url
        item['name']= link.xpath('//*[@class="name row"]//text()').extract()
        item['address']=link.xpath('//*[@class="adress row"]//text()').extract()
        yield item