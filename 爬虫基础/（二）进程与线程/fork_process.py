import os

if __name__ == '__main__':
    print("当前进程的ID：%s" % os.getpid())
    pid = os.fork()
    if pid < 0:
        print("创建进程失败！！！")
    elif (pid == 0):
        # 子进程中
        print("子进程的ID：%s，其父进程的ID：%s" %(os.getpid(), os.getppid()))
    else:
        # 父进程中
        print("父进程的ID：%s，其子进程的ID：%s" %(os.getpid(), pid))
