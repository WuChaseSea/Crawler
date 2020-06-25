# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.http import Request
from bs4 import BeautifulSoup

from ..items import NewsFeedItem


class ChinanewsSpider(Spider):
    name = 'chinanews'
    allowed_domains = ['chinanews.com']
    start_urls = ['http://chinanews.com/rss/rss_2.html']

    '''
    @function: 在第一批请求被下载器发向目标地址并得到响应结果时将被调用
    该函数用于分析响应结果
    '''

    def parse(self, response):
        rss_page = BeautifulSoup(response.body, "html.parser")
        rss_links = set([item['href'] for item in rss_page.find_all('a')])
        for link in rss_links:
            yield Request(url=link, callback=self.parse_feed)

    def parse_feed(self, response):
        rss = BeautifulSoup(response.body, "html.parser")
        for item in rss.find_all('item'):
            feed_item = NewsFeedItem()
            feed_item['title'] = item.title.text
            feed_item['link'] = item.link.text
            feed_item['desc'] = item.description.text
            feed_item['pub_date'] = item.pubdate.text

            yield feed_item
