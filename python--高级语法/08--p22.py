# 哨兵改进
# 多个消费者的处理办法

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
    #设置哨兵,使之在消费完全部产品后跳出循环,继续执行后续代码
    while True:
        product = output_queue.get()
        if product is None:
            break
        print("消费者正在消费{0}号产品".format(product))
    print("消费者已经消耗了全部产品:", ctime())

# 建立主进程
def main():
    q = multiprocessing.Queue()

    sequence = [1,2,3,4]
    producer(sequence, q)
    # 在q中放入两个个None,表示产品已经被消费完了
    q.put(None)
    q.put(None)

   # 实例化两个消费者子进程
    c1 = multiprocessing.Process(target=consumer, args=(q,))
    c2 = multiprocessing.Process(target=consumer, args=(q,))

    c1.start()
    c2.start()

    c1.join()
    c2.join()

if __name__ == "__main__":
    main()

