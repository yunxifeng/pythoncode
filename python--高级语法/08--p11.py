# 生产者消费者模型/queue
#encoding=utf-8
import threading
import time

# Python2
# from Queue import Queue

# Python3
import queue

# 实例化一个queue队列
# 这里一开始犯了一个低级错误,把queue的实例化放在了主线程里面
q = queue.Queue()

class Producer(threading.Thread):
    def run(self):
        global q
        count = 0
        while True:
            # qsize返回queue内容长度
            if q.qsize() < 1000:
                for i in range(100):
                    #一个生产者每次生产一个产品
                    count = count +1
                    msg = '生成产品'+str(count)
                    # put是向queue中放入一个值
                    q.put(msg)
                    print(msg)
            time.sleep(0.5)
class Consumer(threading.Thread):
    def run(self):
        global q
        while True:
            if q.qsize() > 100:
                for i in range(3):
                    #一个消费者每次消费三个产品
                    # get是从queue中取出一个值
                    msg = self.name + '消费了 '+q.get()
                    print(msg)
            time.sleep(1)
def main():
    # 先放入500个初始产品
    for i in range(500):
        q.put('初始产品'+str(i))
    #生成两个生产者
    for i in range(2):
        p = Producer()
        p.start()
    #生成五个消费者
    for i in range(5):
        c = Consumer()
        c.start()

if __name__ == "__main__":
    main()