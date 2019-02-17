# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class FaraScraperPipeline(object):
    # def process_item(self, item, spider):
        # return item

import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.json', 'w', encoding='utf-8')
        self.json_array = []

    def process_item(self, item, spider):
        self.json_array.append(dict(item))
        return item

    def close_spider(self, spider):
        self.file.write(json.dumps(self.json_array, indent=4))
        self.file.close()