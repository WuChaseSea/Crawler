# -*- coding: utf-8 -*-

import socket

# 创建socket并绑定
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 8088
s.bind((host, port))

data, addr = s.recvfrom(1024)
print('从%s:%s中获取数据...' % addr)
print('接收到数据 %s' % data.decode('utf-8'))
