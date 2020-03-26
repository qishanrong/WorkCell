# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv
import pymongo
from WorkCell_01.db_mysql import insertdata

class Workcell01Pipeline(object):
    def __init__(self):
        store_file = os.path.dirname(__file__)+'/spiders/cell.csv'
        self.file = open(store_file,'a+',newline='',encoding='utf-8')
        self.writer = csv.writer(self.file)
    def process_item(self, item, spider):
        try:
            self.writer.writerow((
                item['author'],
                item['content'],
                item['ctime'],
                item['disliked'],
                item['liked'],
                item['likes'],
                item['score'],
            ))
        except Exception as e:
            print(e)
        def close_spider(self,spider):
            self.file.close()

DATABASE_IP = '127.0.0.1'
DATABASE_PORT=27017
DATABASE_NAME = 'sun'
client = pymongo.MongoClient(DATABASE_IP,DATABASE_PORT)
db = client.sun
collection = db.workcell01
class MongodbPipeline(object):
    def process_item(self,item,spider):
        try:
            collection.insert(item)
        except Exception as e:
            print(e)


class MySQLPipeline(object):
    def process_item(self,item,spider):
        try:
            db = 'workcell'
            sql = "insert into workcell_01(author,content,ctime,disliked,liked,likes,score) values('%s','%s','%d','%s','%s','%s','%s');"
            parms = (item['author'],item['content'],item['ctime'],item['disliked'],item['liked'],item['likes'],item['score'])
            insertdata(db, sql, parms)
        except Exception as e:
            print(e)