#  共享冲突案例
import threading

sum = 0
loopSum = 1000001

def myAdd():
    global sum, loopSum
    for i in range(1,loopSum):
        sum += 1
def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1
'''
if __name__ == "__main__":
    myAdd()
    print(sum)
    myMinu()
    print(sum)
#输出结果1000000  0
'''
# 下面使用多线程
def main():
    print("Start at {0}".format(sum))

    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    #非原子操作
    #每次执行结果都不一样
    #两个子进程都在对变量sum进行操作
    print("End at {0}".format(sum))

if __name__ == "__main__":
    main()