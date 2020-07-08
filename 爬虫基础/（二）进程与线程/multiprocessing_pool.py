# -*- coding: utf-8 -*-
from multiprocessing import Pool
import os, time, random

def run_mytask(num):
    print("进程%s正在运行...ID%s" %(num, os.getpid()))
    time.sleep(random.random()*2)
    print("进程%s结束" %num)

if __name__ == '__main__':
    print("当前进程 %s " %os.getpid())
    pool = Pool(processes=3)
    for i in range(4):
        pool.apply_async(run_mytask, args=(i, ))
    print("等待所有进程结束")
    pool.close()
    pool.join()
    print("所有进程结束")
