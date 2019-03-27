# 多进程--multiprocessing
import multiprocessing
from time import sleep, ctime

def clock(interval):
     while True:
         print("The time is %s" % ctime())
         sleep(interval)
def main():
    # 此处实例化一个进程,与实例化一个线程很相似
    p = multiprocessing.Process(target=clock, args=(5,))
    p.start()

if __name__ == "__main__":
    main()