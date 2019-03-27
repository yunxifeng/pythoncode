# concurrent案例
from concurrent.futures import ThreadPoolExecutor
import time

def return_future(msg):
    time.sleep(3)
    return msg

# 创建一个线程池,最多两个核心"干活"
pool = ThreadPoolExecutor(max_workers=2)

# 往线程池加入/提交2个task,准备执行
f1 = pool.submit(return_future, 'hello')#执行函数和参数
f2 = pool.submit(return_future, 'world')

# done:等待执行完毕
print(f1.done())
time.sleep(3)
print(f2.done())

#执行结果
print(f1.result())
print(f2.result())

# map案例
# re是正则
import time,re
import os,datetime
from concurrent import futures

data = ['1','2']

def wait_on(argument):
   print(argument)
   time.sleep(2)
   return "ok"
# map和submit都具有提交作用,使用一个就可以
ex = futures.ThreadPoolExecutor(max_workers=2)
for i in ex.map(wait_on,data):
   print(i)