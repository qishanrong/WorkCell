# -*- coding: utf-8 -*-

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
    # _id = scrapy.Field()