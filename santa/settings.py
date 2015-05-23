# -*- coding: utf-8 -*-

# Scrapy settings for santa project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'santa'

SPIDER_MODULES = ['santa.spiders']
NEWSPIDER_MODULE = 'santa.spiders'
#Below is default pipeline for downloading images and renaming them according to hashes
#ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}

#Below is customized pipeline defined by us for renaming images,moving to folders etc
ITEM_PIPELINES = {'santa.pipelines.MyImagesPipeline':1}

#Images store path
IMAGES_STORE = 'E:\PICS'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'santa (+http://www.yourdomain.com)'
#IMAGES_MIN_HEIGHT = 1024
#IMAGES_MIN_WIDTH = 1280