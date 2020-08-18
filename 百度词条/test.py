# -*- coding: utf-8 -*-

import requests
from urllib.request import urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://baike.baidu.com/item/%E7%99%BE%E7%A7%91%E8%AF%8D%E6%9D%A1/1772433?fromtitle=%E7%99%BE%E5%BA%A6%E8' \
          '%AF%8D%E6%9D%A1&fromid=370660 '
    url = unquote(url)
    # print(url)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/84.0.4147.125 Safari/537.36 '
    cookie = 'AIDUID=E53C92B09135498D3F57BAF8DE2429D0:FG=1; ab_jid=425616a7447b057179d8bbdcaf1b77adab41; ' \
             'ab_jid_BFESS=425616a7447b057179d8bbdcaf1b77adab41 '
    headers = {'User-Agent': user_agent,
               'Cookie': cookie}
    r = requests.get(url, headers=headers)
    # print(r.text)
    r.encoding = 'utf-8'
    # text = r.text.encode('utf-8')
    print(r.text.encode('utf8', 'ignore'))
    # rs = urlopen(url)
    # x = rs.read()
    # print(x.decode('utf-8'))
