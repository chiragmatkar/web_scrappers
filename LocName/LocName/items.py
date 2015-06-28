# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LocNameItem(scrapy.Item):
    internal_url=scrapy.Field()
    external_url=scrapy.Field()
    url=scrapy.Field()
    address=scrapy.Field()
    name=scrapy.Field()
    lat=scrapy.Field()
    long=scrapy.Field()

    
