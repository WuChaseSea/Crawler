# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

if __name__ == '__main__':
    x11 = []
    x1 = {'1': '1', '11': '11'}
    x2 = {'2': '2'}
    x22 = []
    x3 = {'3': '3'}
    x11.append(x1)
    x11.append(x2)
    x22.append(x3)
    print(x11)
    print(x22)
    x = []
    x += x11
    x += x22
    print(len(x))
    print(x)
    print('end')
