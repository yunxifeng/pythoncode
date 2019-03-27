# 解决死锁问题
import time
import threading

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def func_1():
    print("func_1 start")
    #如果在4秒之内没有申请到lock_1,则不再申请,代码继续向下执行
    lock_1.acquire(timeout=4)
    #这段代码是存在问题的,因为我们在实际情况中需要判断func_1是否申请到了lock_1
    #如果没申请到,那么后续释放lock_1是肯定要出问题的
    #此处仅为了演示作用,所以假设func_1申请到了lock_1
    print("func_1 申请到了 lock_1")

    time.sleep(2)
    print("func1 等待申请 lock_2")

    #返回一个布尔值
    rst = lock_2.acquire(timeout=2)
    if rst:
        print("func_1 申请到了 lock_2")
        lock_2.release()
        print("func_1 释放了 lock_2")
    else:
        print("func_1 无法申请到 lock_2")

    lock_1.release()
    print("func_1 释放了 lock_1")
    print("func_1 end")

def func_2():
        print("func_2 start")
        lock_2.acquire(timeout=4)
        print("func_2 申请了 lock_2")

        time.sleep(4)
        print("func_2 等待申请 lock_1")

        lock_1.acquire(timeout=2)
        print("func_2 申请到了 lock_1")

        lock_1.release()
        print("func_2 释放了 lock_1")
        lock_2.release()
        print("func_2 释放了 lock_2")
        print("func_2 end")

def main():
    print("主程序启动")
    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主程序结束")

if __name__ == "__main__":
    main()