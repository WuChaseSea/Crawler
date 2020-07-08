# -*- coding: utf-8 -*-

from multiprocessing.managers import BaseManager
from  multiprocessing import freeze_support, Queue

task_number = 5
# 服务进程创建任务队列，作为传递任务给任务进程的通道
task_queue = Queue(task_number)
# 服务进程创建结果队列，作为任务进程完成任务后回复服务进程的通道
result_queue = Queue(task_number)

# win7 64 貌似不支持callable下调用匿名函数lambda，这里封装一下
def get_task():
    return task_queue

def get_result():
    return result_queue


class QueueManager(BaseManager):
    pass

def run_task():
    # QueueManager.register('get_task_queue', callable=lambda:task_queue)
    # QueueManager.register('get_task_queue', callable=lambda:result_queue)
    # 将两个队列注册到网上，callable参数关联Queue对象
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)
    # 绑定端口，设置验证码
    manager = QueueManager(address=('127.0.0.1', 8001), authkey='520'.encode())
    # 启动
    manager.start()
    try:
        # 获得通过网络访问的Queue对象
        task = manager.get_task_queue()
        result = manager.get_result_queue()

        # 放任务进去
        for num in ["num " + str(i) for i in range(task_number)]:
            print("放入数据 %s" % num)
            task.put(num)

        # 从结果队列result中读取结果
        print("正在尝试读取结果")
        for i in range(task_number):
            print("结果是 %s" % result.get(timeout=5))
    except:
        print("服务进程错误")
    finally:
        # 关闭
        manager.shutdown()
        print("服务进程关闭...")


if __name__ == '__main__':
    # window下多进程可能有问题
    freeze_support()
    run_task()
