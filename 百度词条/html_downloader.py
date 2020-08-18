# -*- coding: utf-8 -*-

import requests


class HTMLDownloader():

    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/84.0.4147.125 Safari/537.36 '
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:  # 如果获取成功的话
            r.encoding = 'utf-8'  # 设置编码方式，能够中文显示正常
            return r.text  # 返回该网页的源代码
        return None
