# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 8088

data = 'wocao'
s.sendto(data.encode('utf-8'), (host, port))

s.close()
