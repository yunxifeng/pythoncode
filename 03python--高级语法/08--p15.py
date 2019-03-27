# threading.Timer()
import threading
import time
i = 0
def func():
    print("Start")
    time.sleep(4)
    print("End")
def main():
    #6秒之后执行func函数
    t = threading.Timer(6, func)
    t.start()
if __name__ == "__main__":
    main()
    while True:
        print("**********{0}**********".format(i))
        time.sleep(3)
        i += 1