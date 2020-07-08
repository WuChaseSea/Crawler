# -*- coding: utf-8 -*-

from greenlet import greenlet

def run_task1():
    print("方法1...520")
    gtask2.switch()  # 手动切换去执行run_task2
    print("方法1，我回来了")
    gtask2.switch()  # 手动切换回run_task2之前执行的位置


def run_task2():
    print("方法2...520")
    gtask1.switch()  # 手动切换回run_task1之前执行的位置
    print("方法2，我回来了")


if __name__ == '__main__':
    gtask1 = greenlet(run=run_task1)  # 创建协程task1
    gtask2 = greenlet(run=run_task2)  # 创建协程task2
    gtask1.switch()  # 跳转至协程gtask1
