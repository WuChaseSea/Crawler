# -*- coding: utf-8 -*-

def run_func():
    print("函数开始执行")
    num = 0
    for i in range(5):
        recv = yield num
        print("我收到了数据 %s" % recv)
        print("方法中num=%s" % num)
        num += 10


if __name__ == '__main__':
    run_func = run_func()
    print(type(run_func))

    # __next()__等同于 send()方法，返回目前yield后面表达式的值
    num_tmp = run_func.__next__()
    print("目前num_tmp=%s" %num_tmp)
    num_tmp = run_func.send(520)
    print("目前num_tmp=%s" %num_tmp)
