# 生产者消费者模型(多进程)

import multiprocessing
from time import ctime

def producer(sequence, input_queue):
    print ("生产者正在生产:", ctime())
    for product in sequence:
        input_queue.put(product)
        print("生产者正在将{0}号产品放入queue仓库".format(product))
    print("生产者结束生产:", ctime())

def consumer(output_queue):
    print("消费者正在消费:", ctime())
    #下面是一个死循环,实现消费者不停消费
    while True:
        # 从仓库中取出商品
        product = output_queue.get()
        print("消费者正在消费{0}号产品".format(product))
        #发出信号,消费完成
        output_queue.task_done()
    # 下面这句话不会被输出
    # 此句未执行，因为q.join()收集到四个task_done()信号后，
    # 主进程启动，未等到print此句完成，程序就结束了
    print("消费者已经消耗了全部产品:", ctime())

# 建立主进程
def main():
    #实例化一个存放产品的仓库
    #JoinableQueue是一种进程安全的数据结构,不必考虑死锁和互斥问题
    q = multiprocessing.JoinableQueue()
    #生产多个项(产品), sequence代表将要发送给消费者的项序列
    #在实践中,这可能是生成器的输出或者是通过其他方式生产出来
    sequence = [1,2,3,4]
    #生产者将产品队列sequence放入q中,供消费者使用
    producer(sequence, q)

    #实例化一个消费者进程
    c = multiprocessing.Process(target=consumer, args=(q,))
    #将此进程设置为一个守护进程:主进程结束,此进程随之结束
    c.daemon = True
    #启动消费者进程
    c.start()

    # q.join()方法会查询q中的数据是否已读完(取完)——这里指的就是任务是否执行完，
    # 如果没有，程序会阻塞住等待q中数据读完(取完)才开始继续执行（可以用Ctrl+C强制停止）。
    # 这里与queue相比,就体现出了优势,joinableQueue有join()方法,可以等待任务完成再结束主进程
    q.join()
if __name__ == "__main__":
    main()

