# -*- coding: utf-8 -*-

from multiprocessing.managers import BaseManager
import time

class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    # 在任务进程中QueueManager只从网络上获取Queue，所以注册时只提供名字即可
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # 连接服务器，也就是运行服务进程的机器
    server_addr = '127.0.0.1'
    print("正在连接服务器 %s..." % server_addr)
    # 端口和验证码需要正确
    manager = QueueManager(address=(server_addr, 8001), authkey='520'.encode())
    manager.connect()
    # 获取网络中的Queue
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 从task任务队列中获取任务，将结果写入result结果队列
    while (not task.empty()):
        num = task.get(True, timeout=5)
        print("执行任务数据 %s..." % num)
        time.sleep(1)
        result.put('num %s' % pow(int(num[4]), 2))
    print("任务进程结束...")
