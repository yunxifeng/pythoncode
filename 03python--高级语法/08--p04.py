# threading--多线程
import time
import threading
def loop1(in1):
    print('Start loop 1 at :', time.ctime())
    print("我是",in1)
    time.sleep(4)
    print('End loop 1 at:', time.ctime())

def loop2(in1, in2):
    print('Start loop 2 at :', time.ctime())
    print("我是" ,in1 , "和", in2)
    time.sleep(2)
    print('End loop 2 at:', time.ctime())

def main():
    print("Starting at:", time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("yunxifeng",))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("death", "madao"))
    t2.start()

    #等待多线程执行完毕
    t1.join()
    t2.join()

    print("All done at :", time.ctime())

if __name__ == "__main__":
    main()