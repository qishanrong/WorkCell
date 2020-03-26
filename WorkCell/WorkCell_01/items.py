# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# item = Workcell01Item()
#                     item['author'] = one['author']['uname']
#                     item['content'] = one['content']
#                     item['ctime'] = one['ctime']
#                     item['disliked'] = one['stat']['disliked']
#                     item['liked'] = one['stat']['liked']
#                     item['likes'] = one['stat']['likes']
#                     item['score'] = one['score']['uname']
import scrapy


class Workcell01Item(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    content = scrapy.Field()
    ctime = scrapy.Field()
    disliked = scrapy.Field()
    liked = scrapy.Field()
    likes = scrapy.Field()
    score = scrapy.Field()
    _id = scrapy.Field()