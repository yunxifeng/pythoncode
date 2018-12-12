# 线程常用属性案例
#导入包
import time
import threading
#定义三个子线程
def loop1():
    print("Start loop1 at:", time.ctime())
    time.sleep(6)
    print("End loop1 at:", time.ctime())
def loop2():
    print("Start loop2 at:", time.ctime())
    time.sleep(1)
    print("End loop2 at:", time.ctime())
def loop3():
    print("Start loop3 at:", time.ctime())
    time.sleep(5)
    print("End loop3 at:", time.ctime())
#定义主线程
def main():
    print("All start at:", time.ctime())
    #实例化第一个子线程并启动
    t1 = threading.Thread(target=loop1, args=())
    t1.setName("THR_1")
    t1.start()
    #实例化第二个子线程并启动
    t2 = threading.Thread(target=loop2, args=())
    t2.setName("THR_2")
    t2.start()
    #实例化第三个子线程并启动
    t3 = threading.Thread(target=loop3, args=())
    t3.setName("THR_3")
    t3.start()

    time.sleep(3)
    #此时THR_2子线程已结束,而THR_1和THR_3还在运行状态
    #下面代码是查看当前正在运行的子线程名称和个数
    #enumerate函数:查看当前正在运行的子线程
    for i in threading.enumerate():
        #getName函数:获取当前正在运行的子线程名称
        print("当前正在运行的子线程名称是{0}".format(i.getName()))
    #activeCount函数:获取当前正在运行的子线程的数量
    print("当前正在运行的子线程数量为{0}".format(threading.activeCount()))


# 考虑使用两个for循环同时操作start和join,实现并发
    print("All done at:", time.ctime())

if __name__ == "__main__":
    main()
    while True:
        time.sleep(1)
