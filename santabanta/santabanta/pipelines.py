# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images  import ImagesPipeline
from scrapy.exceptions import DropItem
import os


class MyImagesPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return 'full/%s' % (image_guid)


    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # iterate over the local file paths of all downloaded images
        for result in [x for ok, x in results if ok]:
            path = result['path']

             #here we create the session-path where the files should be in the end
            # you'll have to change this path creation depending on your needs
            #target_path = 'eva-green/'+ os.path.basename(path)

            # try to move the file and raise exception if not possible
            #if not os.rename(path, target_path):
            #    raise ImageException("Could not move image to target folder")

            # here we'll write out the result with the new path,
            # if there is a result field on the item (just like the original code does)
            #if self.IMAGES_RESULT_FIELD in item.fields:
            #    result['path'] = target_path
             #   item[self.IMAGES_RESULT_FIELD].append(result)

        return item
