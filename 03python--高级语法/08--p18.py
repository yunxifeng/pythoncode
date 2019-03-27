# 多进程--派生子类
import multiprocessing
from time import sleep, ctime

class myProcess(multiprocessing.Process):
    '''
    两个函数比较重要
    1.__init__
    2.run
    '''
    def __init__(self, interval):
        super().__init__()
        self.interval = interval
    def run(self):
        while True:
            print("The time is %s" % ctime())
            sleep(self.interval)
if __name__ == "__main__":
    p = myProcess(3)
    p.start()