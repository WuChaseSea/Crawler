import threading
import random, time


def run_thread():
    global num
    for i in range(4):
        rlock.acquire()
        print("线程 %s 已锁定，此时 num = %s"
              %(threading.current_thread().name, num))
        num = random.random()
        rlock.release()
        print("线程 %s 已解锁，此时 num = %s"
              %(threading.current_thread().name, num))

if __name__ == '__main__':
    print("当前线程 %s 正在运行..." % threading.current_thread().name)

    rlock = threading.RLock()
    num = random.random()
    thread1 = threading.Thread(target=run_thread)
    thread2 = threading.Thread(target=run_thread)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("线程 %s 结束..." % threading.current_thread().name)
