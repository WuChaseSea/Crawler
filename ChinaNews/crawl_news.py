# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


def crawl_directly():
    response = urlopen('http://www.chinanews.com/rss/scroll-news.xml')
    rss = BeautifulSoup(response.read(), "html.parser")
    items = []

    for item in rss.find_all('item'):
        feed_item = {
            'title': item.title.text,
            'link': item.link.text,
            'desc': item.description.text,
            'pub_date': item.pubdate.text
        }
        items.append(feed_item)

    with open('result.json', 'wt') as file:
        file.write(json.dumps(items))


def crawl_feed(url):
    response = urlopen(url)
    rss = BeautifulSoup(response.read(), "lxml")
    items = []
    print("Crawling %s" % url)

    for item in rss.find_all('item'):
        try:
            feed_item = {
                'title': item.title.text,
                'link': item.contents[2],
                'desc': item.description.text,
                'pub_date': u'' if item.pubdate.text is None else item.pubdate.text
            }
            items.append(feed_item)
        except Exception as e:
            print("Crawling %s error." % url)
            print(e.args)

    return items


def crawl_indirectly():
    res = urlopen('http://www.chinanews.com/rss/rss_2.html')
    rss_page = BeautifulSoup(res.read(), "html.parser")
    rss_links = set([item['href'] for item in rss_page.find_all('a')])
    feed_items = []
    for link in rss_links:
        feed_items += crawl_feed(link)
        # feed_items.append(crawl_feed(link))
    with open('result.json', 'w', encoding="utf-8") as file:
        file.write(json.dumps(feed_items, ensure_ascii=False, indent=2))

    print("Total crawl %s items" % len(feed_items))


if __name__ == '__main__':
    crawl_indirectly()
    print('end')
