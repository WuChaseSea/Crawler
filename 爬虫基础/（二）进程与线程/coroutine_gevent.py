# -*- coding: utf-8 -*-

from gevent import monkey, spawn, joinall

def run_task(num):
    print("得到数字%s, 平方为%s" %(num, pow(num, 2)))


if __name__=='__main__':
    monkey.patch_all()  # 遇到阻塞时自动切换协程
    nums = [i for i in range(5)]
    # 定义协程方法
    greenlets = [spawn(run_task, num) for num in nums]
    # 添加协程任务并且启动运行
    joinall(greenlets)
