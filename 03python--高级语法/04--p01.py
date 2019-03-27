#"小"函数举例
def a():
    print("哈哈哈")
a()
#lambda表达式举例
#计算两个数的乘积
stm = lambda a, b, c: a * b +c
print(stm(1,2,3))
print("*" * 20)
#高阶函数
def A():
    print("哈哈")
B = A
B()
#以上案例说明:
# 1.函数名称是变量
# 2.A和B只是名称不一样
# 3.既然函数名称是变量,则应该可以被当做参数传入另一个函数
#高阶函数案例01
#普通方法
def A(n):
    return n * 100
def B(n):
    return A(n) * 3
print(B(10))
#写一个高阶函数
#f是一个函数,放进去哪个函数,就调用哪个函数
def C(n ,f):
    #假定函数f是把n扩大100倍
    return f(n) * 3
print(C(10,A))
#比较这两种写法,显然高阶函数更加灵活
#例如:
def D(n):
    return n*10
#假定我们现在需要把n扩大30倍,而不是300倍
#此时发现第一种方法是写死的,很难操作
#采用高阶函数如下,很灵活
print(C(10,D))

#map函数案例
#对列表每一个元素乘以10,得到新的列表
#第一种方法
print([i*10 for i in[0,1,2,3,4,5,6,7,8,9]])
#第二种方法
l1 = [i for i in range(10)]
print(l1)
l2=[]
for i in range(10):
    l2.append(i*10)
print(l2)
#第三种方法:map
def mulTen(n):
    return n*10
l3 = map(mulTen, l1)
#调用map函数,变成map类型,map类型可迭代,可迭代的都可以用for循环
print(type(l3))
print([i for i in l3])
#此处大拿运用列表生成式生成新的列表,但是得到的结果为空,为什么?
#或者
#l4 = list(l3)
#print(l4)

#reduce函数案例
from functools import reduce
#定义一个操作函数:相加
def add(x,y):
    return x+y
#对列表执行add的reduce操作
print(reduce(add, [1,2,3,4,5,6]))

#filter函数
#先定义过滤函数,要求有输入,返回布尔值
#案例要求:取一个列表中的偶数,生成新列表
def isEven(a):
    return a%2 == 0
l = [2,4,5,3,23,4,5,3,54,3]
rst = filter(isEven, l)
print(type(rst))
#print(list(rst))
#或者
print([i for i in rst])

#sorted函数
help(sorted)
#排序案例01
a = [2,3,4,5654,234234,64564,23423,654,2,3,5,43,66,8,8]
#默认是从小到大
print(sorted(a))
#下面是从大到小
print(sorted(a,reverse=True))
#排序案例02
a = [-3,-2,-45,-7,-89]
#按绝对值进行排序,abs是求绝对值的意思
print(sorted(a, key=abs, reverse=True))
#排序案例03
astr = ["yunxifeng", "Death", "madao", "deatigg"]
#默认大写在前
str1 = sorted(astr)
print(str1)
#按小写进行排序
str2 = sorted(astr, key=str.lower)
print(str2)

#返回函数案例01
#函数作为返回值返回,被返回的函数在函数体内定义
def myA():
    def myB():
        print("hahah")
        return 3
    return myB
#调用myA,返回一个函数myB,赋值给a
a = myA()
print(type(a))
print(a)
print(a())
#返回函数案例02
#args:参数列表
#myD使用了外部变量,即myC的参数
def myC(*args):
    def myD():
        a = 0
        for i in args:
            a+=i
        return a
    return myD
x = myC(3,4,5,6,7)
print(x())
#上面的myC就是一个标准闭包结构

#闭包常见坑
def count():
    #定义了一个列表,里面放着定义的函数1,函数2,函数3
    fs = []
    #每次循环定义一个函数
    for i in range(1,4):
        def f():
            return i*i
        #每次循环,都将定义的这个函数加入到列表中
        #注意,此时存放进列表中的函数都是"i*i"
        #f函数虽然引用了外部变量,但是这个i并没有被立即执行,而是被存放起来了
        fs.append(f)
        #所以,最终返回的fs列表应该是[i*i,i*i,i*i],此处仅为示意
    return fs
#调用count()函数,返回fs列表(里面是三个函数),将这三个函数分别赋值给f1,f2,f3,此时的i已经变成了3
f1,f2,f3 = count()
#此时,调用这三个函数,却都已经变成了3*3
#而我们的预期是1*1,2*2,3*3
print(f1())
print(f2())
print(f3())
#出现的问题:造成上述状况的原因是,返回函数引用了变量i,i并非立即执行，而是等到三个函数都返回的时候才统一使用，
          #此时i已经变成了3，最终调用的时候，都返回的是 3*3
#此问题描述成：返回闭包时，返回函数不能引用任何循环变量
#解决方案:再创建一个函数，用该函数的参数绑定循环变量的当前值，
         #无论该循环变量以后如何改变，已经绑定的函数参数值不再改变
print("*" * 20)
# 解决方案
# 修改上述函数
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        #此处传进列表里的就是i值,1,2,3,即f的参数就是1,2,3,
        # f(1)返回g函数,g函数返回1*1
        # f(2)返回g函数,g函数返回2*2
        # f(3)返回g函数,g函数返回3*3
        fs.append(f(i))
    return fs

f1,f2,f3 = count1()
print(f1())
print(f2())
print(f3())

#装饰器
def hello():
    print("Hello world")
f = hello
#f和hello是一个函数
print(id(f))
print(id(hello))
print(f.__name__)
print(hello.__name__)
#需求:对hello功能进行扩展,在打印Hello world之前打印系统时间
#不能修改当前现有代码
#可以使用装饰器
import time
#高阶函数,以函数作为参数
#f是想要被装饰的函数,作为参数传进printTime函数
def printTime(f):
    def wrapper(*args, **kwargs):
        print("Time:",time.ctime())
        return f(*args, **kwargs)
    return wrapper
#写法是比较固定的
#上面定义了装饰器,使用的时候需要用到@,此符号是python的语法糖
#建议查阅一下语法糖的原理
@printTime
def hello():
    print("Hello world")
hello()

#下面开始手动执行下装饰器
#先定义函数
def haha():
    print("hahaha")
haha()
#此处要装饰函数haha,就把它当做参数传进printTime函数,并执行printTime函数,
#返回值是wrapper函数,并将其赋值给h
h = printTime(haha)
#调用h函数,就相当于调用wrapper函数,首先打印系统时间,然后返回haha函数并调用
h()
print("*" * 20)
#下面会打印两次系统时间,我的看法:h函数是原haha函数被装饰过一次的函数,此时再度调用装饰器,就相当于对haha函数进行了二次装饰
#故此,会打印两次系统时间
f = printTime(h)
f()

#把字符串转化为十进制数字
#int函数中base代表进制,默认是十进制
print(int("12345"))
help(int)
#把一个八进制的字符串转化为十进制数字
#12345是一个八进制的数值,"12345"就是一个八进制数值的字符串,要把它转化为一个十进制的数字
print(int("12345", base=8))
#新建一个函数,此函数是默认输入的字符串是16进制数字,返回十进制数字
def int16(x, base=16):
    return int(x, base)
#在调用这个函数时,没有输入base参数,则使用默认
int16("12345")
#->引出偏函数
#偏函数
import functools
#此处固定了int函数的base参数
int16 = functools.partial(int, base=16)
print(int16("12345"))