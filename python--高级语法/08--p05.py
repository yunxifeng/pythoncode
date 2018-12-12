# 守护线程--daemon
#01--不设置守护线程
'''
import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("End fun")
#模拟主线程启动
print("Main thread")

t1 = threading.Thread(target=fun, args=())
t1.start()

#主线程1s之后结束
time.sleep(1)
print("Main thread end")
'''
#02--设置守护线程
import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("End fun")
#模拟主线程启动
print("Main thread")

t1 = threading.Thread(target=fun, args=())
#必须在start之前设置守护线程
t1.setDaemon(True)
t1.start()

#主线程1s之后结束
time.sleep(1)
print("Main thread end")
#结果表明,主程序结束后,子线程也结束了