# 解决共享冲突
import threading

sum = 0
loopSum = 1000000
#实例化一把锁
lock = threading.Lock()

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        #上锁,申请锁
        lock.acquire()
        sum += 1
        #释放锁
        lock.release()
def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        lock.acquire()
        sum -= 1
        lock.release()
def main():
    print("Start at {0}".format(sum))

    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("End at {0}".format(sum))

if __name__ == "__main__":
    main()


