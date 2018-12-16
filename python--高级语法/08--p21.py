# 设置哨兵

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
    # 在q中放入一个None,表示产品已经被消费完了
    q.put(None)

    c = multiprocessing.Process(target=consumer, args=(q,))
    c.daemon = True
    c.start()
    c.join()

if __name__ == "__main__":
    main()

