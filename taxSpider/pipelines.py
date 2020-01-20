# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TaxspiderPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
         self.connect = pymysql.connect(host='localhost', user='root', password='root', db='taxspider', port=3306)
         self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 往数据库里面写入数据
        self.cursor.execute(
           # 'insert into movieTable(name,href)VALUES ("{}","{}")'.format(item['mov_name'], item['mov_href']))
            'insert into chinatax(Title,Url,Source,Content,PostTime)VALUES ("{}","{}","{}","{}","{'
            '}")'.format(item['title'], item['url'],item['source'], item['content'],item['postTime']))
        self.connect.commit()
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

#
# class TaxspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
