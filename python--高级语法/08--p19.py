# 查看进程id
import os
from multiprocessing import Process

def info(title):
    print(title)
    print("module name:", __name__)
    #得到父进程的id
    print("Parent process id:", os.getppid())
    #得到子进程的id
    print("Now process id:", os.getpid())

def mainLine():
    # 当前主进程mainLine先执行info函数
    # 此时主进程的父进程是指启动08--p19.py的进程
    info("First")
    # 这里实例化了一个子进程并启动
    # 这个子进程是当前运行的进程
    # 它的父进程是mainLine这个进程
    p = Process(target=info, args=("Second",))
    p.start()
    p.join()
if __name__ == "__main__":
    mainLine()