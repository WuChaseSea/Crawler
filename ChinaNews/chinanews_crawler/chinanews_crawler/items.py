# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

'''
@function: 用于承载爬取回来的数据内容
'''


class NewsFeedItem(Item):
    title = Field()  # 标题
    link = Field()  # 新闻链接详情
    desc = Field()  # 新闻综述
    pub_date = Field()  # 发布日期


class ChinanewsCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
