# -*- coding: utf-8 -*-

import socket
import threading
import time


# 接收传来的数据并发送数据
def run_server(sock, addr):
    print('接收来自 %s:%s 的连接...' % addr)
    while True:
        # 接收最大数据量大小为1024字节的数据
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            print('收到结束信息，即将关闭连接...')
            break
        print('接收到数据 %s' % data.decode('utf-8'))
        # 服务端在收到数据之后发送确认信息
        sock.send(('确认收到数据 %s' % data.decode('utf-8')).encode('utf-8'))
    # 关闭socket
    sock.close()
    print('来自 %s:%s 的连接已经关闭...' % addr)


if __name__ == '__main__':
    # 创建TCP Socket 并绑定IP与端口
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8088))
    # 监听, 设置最大连接数量
    s.listen(5)
    print('正在准备连接...')
    # 接收连接
    sock, addr = s.accept()
    # 创建线程处理连接
    t = threading.Thread(target=run_server, args=(sock, addr))
    t.start()
    t.join()
    print('线程结束...')
