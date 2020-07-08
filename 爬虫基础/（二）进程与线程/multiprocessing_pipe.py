from multiprocessing import Process, Pipe
import time, os, random

def run_send(pipe, nums):
    print("发送进程正在运行 ID: %s" %os.getpid())
    for num in nums:
        pipe.send(num)
        time.sleep(random.random())

def run_recv(pipe):
    print("接收进程正在运行 ID: %s" %os.getpid())
    while True:
        print("接收到：%s" % pipe.recv())
        time.sleep(random.random())

if __name__ == '__main__':
    print("主进程ID %s正在运行..." % os.getpid())
    pipe = Pipe()
    proc_send = Process(target=run_send, args=(pipe[0], [i for i in range(4)]))
    proc_recv = Process(target=run_recv, args=(pipe[1], ))
    proc_send.start()
    proc_recv.start()
    proc_send.join()
    proc_recv.join()
    print("主进程ID %s结束..." % os.getpid())
