import os
from multiprocessing import Process

def run_proc(num):
    print("%s 号进程准备开始" %num)
    print("%s 号进程正在运行...ID为：%s" %(num, os.getpid()))
    print("%s 号进程已结束" %num)

class MyProcess(Process):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        print("%s 号进程准备开始" %self.num)
        print("%s 号进程正在运行...ID为：%s" %(self.num, os.getpid()))
        print("%s 号进程已结束" %self.num)

if __name__ == '__main__':
    print("进程正在运行...ID为：%s" %os.getpid())

    for i in range(3):
        p = Process(target=run_proc, args=(str(i), ))
        print("进程即将开始：")
        p.start()
        p.join()

    for i in range(3):
        my_process = MyProcess(i)
        print("进程即将开始：")
        my_process.start()
        my_process.join()

    print("进程结束")
