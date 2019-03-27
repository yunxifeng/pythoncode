# 可迭代
l = [i for i in range(10)]
# l是可迭代对象,但不是迭代器
for idx in l:
    print(idx)
# range是迭代器
for i in range(5):
    print(i)
print("-" * 30)
# isinstance
# from collections 将在Python3.8中停止工作
from collections.abc import Iterable
from collections.abc import Iterator
ll = [i for i in range(10)]
# 判断ll是否是可迭代对象
print(isinstance(ll, Iterable))
# 判断ll是否是迭代器
print(isinstance(ll, Iterator))
print("-" * 30)
# iter函数
str = "I love Python"
print(isinstance(str, Iterable))
print(isinstance(str, Iterator))
str0 = iter(str)
print(isinstance(str0, Iterable))
print(isinstance(str0, Iterator))
print("-" * 30)
# 1.直接使用生成器
# 放在中括号里是列表生成器
l = [x*x for x in range(10)]
# 放在小括号里是生成器
g = (x*x for x in range(10))
print(type(l))
print(type(g))
# 2.函数创建生成器案例
# yieId负责返回
# 需要使用next函数调用生成器
def odd():
    print("Step 1")
    yield 1
    print("Step 2")
    yield 2
    print("Step 3")
    yield 3
g = odd()
one = next(g)
print(one)
two = next(g)
print(two)
three = next(g)
print(three)
# 通过for循环调用生成器
# 斐波那契数列(fib)一般写法
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n += 1
    return 'Done'
fib(5)
# 斐波那契数列生成器写法
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    # 下面如果为range(6),则会执行到return语句,会爆出异常,异常的返回值是return的返回值
    return 'Done'

g = fib(5)
# for循环调用
for i in range(5):
    rst = next(g)
    print(rst)

print("-" * 30)
# 生成器的典型用法是在for循环中使用
# 比较典型的生成器就是range
# 与上述写法相比, 比较正常的写法如下
gg = fib(10)
for i in gg:
    print(i)