# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaxspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()  # 文章标题
    url = scrapy.Field()  # 链接
    source = scrapy.Field()  # 发布来源
    postTime = scrapy.Field()  # 发布时间
    content = scrapy.Field()  # 内容
    pass
