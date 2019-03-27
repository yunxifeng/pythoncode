#_thread--多线程
import time
import _thread as thread
#线程1
def loop1():
    #ctime得到当前时间
    print("Start loop1 at :", time.ctime())
    #睡眠多少时间,单位是秒
    time.sleep(4)
    print("End loop1 at :", time.ctime())
#线程2
def loop2():
    print("Start loop2 at :", time.ctime())
    time.sleep(2)
    print("End loop2 at :", time.ctime())
#主线程
def main():
    print("Starting at:", time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 参数两个，一个是需要运行的函数名，第二是函数的参数作为元祖使用，为空则使用空元祖
    # 注意：如果函数只有一个参数，需要参数后由一个逗号
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())

    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
#死循环
while True:
     time.sleep(1)