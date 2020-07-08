# -*- coding: utf-8 -*-

import threading
import random, time

def run_thread(nums):
    print("当前线程 %s 正在运行..." % threading.current_thread().name)
    for num in nums:
        print("线程 %s 读取数据 %s" % (threading.current_thread().name, num))
        time.sleep(random.random())
    print("线程 %s 结束..." % threading.current_thread().name)

class MyThread(threading.Thread):
    def __init__(self, name, nums):
        threading.Thread.__init__(self, name=name)
        self.nums = nums

    def run(self):
        print("当前线程 %s 正在运行..." % threading.current_thread().name)
        for num in self.nums:
            print("线程 %s 读取数据 %s" % (threading.current_thread().name, num))
            time.sleep(random.random())
        print("线程 %s 结束..." % threading.current_thread().name)

if __name__ == '__main__':
    print("当前线程 %s 正在运行..." % threading.current_thread().name)

    thread1 = threading.Thread(target=run_thread, args=([i for i in range(1, 4)], ))
    thread2 = threading.Thread(target=run_thread, args=([i for i in range(4, 7)], ))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    thread3 = MyThread(name='thread3', nums=[i for i in range(1,4)])
    thread4 = MyThread(name='thread4', nums=[i for i in range(4,7)])
    thread3.start()
    thread4.start()
    thread3.join()
    thread4.join()

    print("线程 %s 结束..." % threading.current_thread().name)
