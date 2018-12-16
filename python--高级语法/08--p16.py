# 可重入锁
import threading
import time

num = 0
#mySource = threading.Lock()
#使用可重入锁
mySource = threading.RLock()
class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if mySource.acquire(timeout=1):
            num += 1
            msg = self.name+"set num to"+str(num)
            print(msg)
            # 这里当前再一次申请使用这个变量,
            # 但是这个变量被当前线程锁着还没有被释放,会导致程序卡死在这里
            # 解决办法,使用可重入锁threading.RLock
            # 这个线程就可以在没有释放这个被锁着的变量时再次申请使用这个共享变量,
            mySource.acquire()
            mySource.release()
            mySource.release()
def main():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == "__main__":
    main()