# -*- coding: utf-8 -*-

from gevent import monkey, spawn, joinall, pool
monkey.patch_all()  # 遇到阻塞时自动切换协程

def run_task(num):
    print("得到数字%s, 平方为%s" %(num, pow(num, 2)))


if __name__=='__main__':
    pool = pool.Pool(2)
    nums = [i for i in range(5)]
    # 进程池的map()函数将第二个参数中的值一个个传入第一个参数表示函数所需要的参数中
    pool.map(run_task, nums)
