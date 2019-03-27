# _thread--多线程
# 练习带参数的多线程启动方法
import time
# 导入多线程包并更名为thread
import _thread as thread

def loop1(in1):
    print('Start loop 1 at :', time.ctime())
    print("我是参数 ",in1)
    time.sleep(4)
    print('End loop 1 at:', time.ctime())

def loop2(in1, in2):
    print('Start loop 2 at :', time.ctime())
    print("我是参数 " ,in1 , "和参数  ", in2)
    time.sleep(2)
    print('End loop 2 at:', time.ctime())

def main():
    print("Starting at:", time.ctime())
    #元组,注意要有" ,"
    thread.start_new_thread(loop1,("王老大", ))
    thread.start_new_thread(loop2,("王大鹏", "王晓鹏"))

    print("All done at:", time.ctime())

if __name__ == "__main__":
    main()
    # 一定要有while语句
    # 因为启动多线程后本程序就作为主线程存在
    # 如果主线程执行完毕，则子线程可能也需要终止
    while True:
        time.sleep(10)
