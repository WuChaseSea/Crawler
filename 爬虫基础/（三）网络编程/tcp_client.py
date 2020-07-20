# -*- coding: utf-8 -*-

import socket


# 创建Socket并连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8088))
print('客户端已连接')
# 发送消息
s.send('wocao'.encode('utf-8'))
print('%s' % s.recv(1024).decode('utf-8'))
s.send('exit'.encode('utf-8'))
# 关闭socket
s.close()
