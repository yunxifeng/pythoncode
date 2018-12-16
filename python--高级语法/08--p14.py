# Semaphore信号灯
import time
import threading

# 参数定义最多可以有多少个线程同时使用资源s
s = threading.Semaphore(3)

def func():
    if s.acquire():
        print(threading.currentThread().getName() + "get Semaphore")
        time.sleep(5)
        s.release()
        print(threading.currentThread().getName() + "release Semaphore")

for i in range(8):
    t1 = threading.Thread(target=func, args=())
    t1.start()
