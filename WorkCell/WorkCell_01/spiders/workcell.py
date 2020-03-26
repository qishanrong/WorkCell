# -*- coding: utf-8 -*-
import scrapy
import json
from WorkCell_01.items import Workcell01Item


class WorkcellSpider(scrapy.Spider):
    BASE_URL = 'https://api.bilibili.com/pgc/review/short/list?media_id=102392&ps=20&sort=0&cursor={}'
    name = 'workcell'
    allowed_domains = ['api.bilibili.com']
    # start_urls = [BASE_URL.format('78782601543127')]
    start_urls = ['https://api.bilibili.com/pgc/review/short/list?media_id=102392&ps=20&sort=0']
    def parse(self, response):
        print(response.url)
        resdata = json.loads(response.body_as_unicode())
        # print(resdata)
        if resdata['code'] == 0:
            if len(resdata['data']['list']) > 0:
                datas = resdata['data']['list']
                cursor =resdata['data']['next']
                for one in datas:
                    item = Workcell01Item()
                    item['author'] = one['author']['uname']
                    item['content'] = one['content']
                    item['ctime'] = one['ctime']
                    item['disliked'] = one['stat']['disliked']
                    item['liked'] = one['stat']['liked']
                    item['likes'] = one['stat']['likes']
                    item['score'] = one['score'] if 'score' in one else ""
                    yield item
                yield scrapy.Request(self.BASE_URL.format(cursor),callback=self.parse)