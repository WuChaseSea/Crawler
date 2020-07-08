# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue
import os, time, random

def run_writer(queue, nums):
    print("写进程正在运行 ID：%s" % os.getpid())
    for num in nums:
        queue.put(num)
        print("将 %s 放入 queue中..." % num)
        time.sleep(random.random())
    print("写进程结束 ID：%s" % os.getpid())

def run_reader(queue):
    print("读进程正在运行 ID：%s" % os.getpid())
    while not queue.empty():
        num = queue.get(True)
        print("从中取出数据 %s " % num)
        time.sleep(random.random())
    print("读进程结束 ID：%s" % os.getpid())
    # while True:
    #     if not queue.empty():
    #         num = queue.get(True)
    #         print("从中取出数据 %s " % num)
    #         time.sleep(random.random())
    #     else:
    #         break

if __name__ == "__main__":
    print("当前进程ID：%s" % os.getpid())
    queue = Queue()
    proc_writer1 = Process(target=run_writer, args=(queue, [1, 2, 3]))
    proc_writer2 = Process(target=run_writer, args=(queue, [4, 5, 6]))
    proc_reader = Process(target=run_reader, args=(queue, ))

    proc_writer1.start()
    proc_writer2.start()

    proc_reader.start()

    proc_writer1.join()
    proc_writer2.join()
    proc_reader.join()
    print("主进程结束 ID：%s" % os.getpid())
