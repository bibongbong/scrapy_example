# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import codecs


class ScrapyExamplePipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir+'/news.txt'

        with open(filename, 'a') as f:
            f.write(item['novelname']+'\n')
            f.write(item['author'] + '\n')
            f.write(item['novelurl'] + '\n\n')
        return item
