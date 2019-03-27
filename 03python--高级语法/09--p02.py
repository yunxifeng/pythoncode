# 协程的实现案例
'''
def simple1():
    print("-> start")
    # yield后面为空,表示返回None
    x = yield
    print("->received", x)
# 主线程
# 第一步,实例化一个协程
s = simple1()
print(11111)
# 可以使用s.send(None),效果一样
next(s) #第二步,预激,此时simple1函数执行到yield,然后返回主线程
print(2222)
# 第三步, 返回simple1函数预激的位置继续执行,并把字符串haha传给x
s.send("haha")

# 协程的状态
def simple2(a):
    print("->start")

    b = yield a
    print("->received", a, b)

    c = yield a+b
    print("->received", a, b, c)
# 主进程
ss = simple2(1)
print(next(ss))
print(ss.send(2))
print(ss.send(3))
'''
# yield from--01
# 生成器1
def simple3():
    for c in 'AB':
        # 这里调用方和生成器之间没有双向通道
        yield c
# list直接用生成器作为参数
l = list(simple3())
print(l)
# 生成器2
def simple4():
    # 这里调用方和生成器之间有一个双向通道
    yield from 'AB'
ll = list(simple4())
print(ll)

# yield from--02
# 委派生成器
from collections import namedtuple
'''
解释：
1. 外层 for 循环每次迭代会新建一个 grouper 实例，赋值给 coroutine 变量； grouper 是委派生成器。
2. 调用 next(coroutine)，预激委派生成器 grouper，此时进入 while True 循环，调用子生成器 averager 后，在 yield from 表达式处暂停。
3. 内层 for 循环调用 coroutine.send(value)，直接把值传给子生成器 averager。同时，当前的 grouper 实例（coroutine）在 yield from 表达式处暂停。
4. 内层循环结束后， grouper 实例依旧在 yield from 表达式处暂停，因此， grouper函数定义体中为 results[key] 赋值的语句还没有执行。
5. coroutine.send(None) 终止 averager 子生成器，子生成器抛出 StopIteration 异常并将返回的数据包含在异常对象的value中，
   yield from 可以直接抓取 StopItration 异常并将异常对象的 value 赋值给 results[key]
'''
ResClass = namedtuple('Res', 'count average')


# 子生成器
def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        term = yield
        # None是哨兵值
        if term is None:
            break
        total += term
        count += 1
        average = total / count

    return ResClass(count, average)


# 委派生成器
def grouper(storages, key):
    while True:
        # 获取averager()返回的值
        storages[key] = yield from averager()


# 客户端代码
def client():
    process_data = {
        'boys_2': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
        'boys_1': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]
    }

    storages = {}
    for k, v in process_data.items():
        # 获得协程
        coroutine = grouper(storages, k)

        # 预激协程
        next(coroutine)

        # 发送数据到协程
        for dt in v:
            coroutine.send(dt)

        # 终止协程
        coroutine.send(None)
    print(storages)

# run
client()
