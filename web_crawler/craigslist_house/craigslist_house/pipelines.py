# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json
import urllib

localPath="results/"
class CraigslistHousePipeline(object):
    def process_item(self, item, spider):
        return item

class HtmlWriterPipeline(object):
    
    def process_item(self, item, spider):
        fileName=item['url'].split("/")[-1]
        urllib.urlretrieve (item['url'],localPath+fileName)
        return item

class PriceValidationPipeline(object):
    
    def process_item(self, item, spider):
        try:
            price =int(item['price'][0][1:])
        except:
            raise DropItem("Invaild item found: %s" % item)
        if price<=2000:
            return item
        else:
            raise DropItem("I cannot afford that: %s" % item)
        
class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['url'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['url'])
            return item
