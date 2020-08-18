# -*- coding: utf-8 -*-

from urllib.parse import unquote

from url_manager import UrlManager
from html_downloader import HTMLDownloader
from html_parser import HTMLParser
from data_output import DataOutput

class Spider():
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HTMLDownloader()
        self.parser = HTMLParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while (self.manager.has_new_url() and self.manager.old_urls_size()<50):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print("已经抓取%s个链接" % self.manager.old_urls_size())
            except Exception as e:
                print(e)
        self.output.output_html()


if __name__ == '__main__':
    spider = Spider()
    url = 'https://baike.baidu.com/item/%E7%99%BE%E7%A7%91%E8%AF%8D%E6%9D%A1/1772433?fromtitle=%E7%99%BE%E5%BA%A6%E8%AF%8D%E6%9D%A1&fromid=370660'
    # url = unquote(url)
    # print(url)
    spider.crawl(url)
