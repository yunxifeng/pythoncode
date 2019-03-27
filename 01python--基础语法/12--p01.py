# 函数--01
# 定义一个函数
# 只是定义的话不会执行
# 1.def(define)关键字，后跟一个空格
# 2.函数名，自己定义，需要遵循变量名命名规则，约定俗成，大驼峰命名只给类用
# 3.后面的括号和冒号不能省，括号内可以有参数也可以没有
# 4.函数内所有代码缩进
# 5.判断一个语句是否是函数内的语句，看缩进
def func():
    print("我是一个函数")
    print("我要完成一定功能")
print("我要结束了")

# 函数的调用
# 直接函数名后面跟括号，如果函数带参数，则调用时也要带参数
func()


# 参数的定义和使用
# 参数person只是一个符号，代表的是调用的时候的某一个数据
# 调用的时候，会用p的值代替函数中所有person
def hello(person):
    print("{0},你怎么了".format(person))
    print("sir,你不理我我就走了")
p="明月"
hello(p)

# return语句的基本使用
# 函数打完招呼后返回一句话
def hello(person):
    print("{0},你怎么了".format(person))
    print("sir,你不理我我就走了")
    return "我已经跟{0}打招呼了，{0}不理我".format(person)
p="明月"
rst=hello(p)

print(rst)


# return案例2
# 函数一旦执行return语句，则无条件返回，即结束函数的执行
def hello(person):
    print("{0},你怎么了".format(person))
    return "哈哈，我提前结束了"
    print("sir,你不理我我就走了")
    return "我已经跟{0}打招呼了，{0}不理我".format(person)
p="明月"
rst=hello(p)
print(rst)

# return: 返回值示例3
def func_1():
    print("有返回值呀")
    return 1


def func_2():
    print("没有返回值")


f1 = func_1()
print(f1)

f2 = func_2()
print(f2)


# 九九乘法表 version1.0
# 该用for循环就用for循环，该用while循环就用while循环，另外，相比而言，推荐for循环
for row in range(1,10):
    #打印一行
    #print("{0}--a line".format(row))
    for col in range(1,row+1):
        #print函数默认任务打印完毕后换行
        # print(value, sep="", end="\n",...)参数
        # value: 打印内容
        # sep(separator): 分隔符
        # end: 以...结束
        print(row * col, end="")
    print("-------------------")
# 没有对齐，是因为没用占位符，格式化

# 九九乘法表 version2.0
# 定义一个函数，打印一行九九乘法表
def printLine(row):
    for col in range(1,row+1):
        #print函数默认任务打印完毕后换行
        print(row * col,end="")
# 这里借用print的换行功能
    print("")

# 九九乘法表 version2.0
for row in range(1,10):
    printLine(row)

# eval案例
x=100
y=200
#执行x+y
#z=x+y
z1=x+y
z2=eval("x+y")
print(z1)
print(z2)

# exec案例
x=100
y=200
#执行x+y
#z=x+y
z1=x+y
#1.注意字符串中引号的写法
#2.对比exec执行结果和代码执行结果
z2=exec("print('x+y:',x+y)")
print(z1)
print(z2)


# 递归调用深度限制代码
x=0
def fun():
    global x
    x+=1
    print(x)
    #函数自己调用自己
    fun()
# 调用函数
fun()

# 斐波那契数列
# 一列数字，第一个值是1，第二个也是1，从第三个开始，每一个数字的值等于前两个数字的值之和
# 数学公式为：f（1）=1，f（2）=1，f（n）=f（n-1）+f（n-2）
# 例 1,1,2,3,5,8,13，......

#下面求斐波那契数列函数有一定问题，比如n一开始就是负数，如何修正
# n表示第n个数字的斐波那契数列的值
def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    #思考：为什么后面return能够正确执行，而不用else语句
    # 缩进
    return fib(n-1)+fib(n-2)

print(fib(10))


# 汉诺塔问题
# 规则：1.每次只能移动一个盘子
# 2.任何一次移动，三个塔的状态必须是小盘子在上，大盘子在下
# 移动
# 1.n=1，A->C
# 2.n=2,(小)A->B,（大）A->C,B（小）->C
# 3.n=3,（小）A->C,(中)A->B,(小)C->B,调用递归实现
# （大）A->C
#  (小)B->A,（中）B->C,A（小）->C，调用递归实现
# 4.n=n
#   （1）把A上的n-1个盘子，借助于C移动到B上去，调用递归实现
#   （2）把A上最大的盘子，也是唯一一个，移动到C上，A->C
#   （3）把B上n-1个盘子，借助于A，移动到C上，调用递归
# 代码如下
def hano(n, a, b, c):
    '''
    n:代表几个盘子
    a：代表第一个塔,开始塔
    b：代表第二个塔,中间塔
    c：代表第三个塔,目标塔

    '''
    if n == 1:
        print(a, "-->", c)
        return None
    if n == 2:
        print(a, "-->", b)
        print(a, "-->", c)
        print(b, "-->", c)
        return None
    # 把n-1个盘子，从a塔借助于c塔，挪到b塔上去
    hano(n - 1, a, c, b)
    print(a, "-->", c)
    # 把n-1个盘子，从b塔借助于a塔，挪到c塔上去
    hano(n - 1, b, a, c)


a = "A"
b = "B"
c = "C"

n = 1
hano(n, a, b, c)

# 查找函数帮助文档
# 1.用help函数
help(print)
#  sep=''(分隔符，以’‘作为分隔) end=’\n‘(结束后换行)
# （）里面就是默认参数

# 函数文档案例
# 函数stu模拟一个学生的自我介绍内容
def stu(name,age,*args):
# 单引号定义单行，严格来说不能定义多行，推荐三单引号
#    '这是文档'
# 这样写也不是特别好
    '''
    这是第一行
    这是第二行
    这是第三行
    '''
    print("This is hanshu stu")
# 查看函数文档
help(stu)
# 或者
stu.__doc__

# 函数文档标准格式示例
def stu(name,age):
    '''
    这是文档的文字内容
    :param name: 表示学生的姓名
    :param age: 表示学生的年龄
    :return: 此函数没有返回值
    '''
    pass
# 注: param(英文释义: 参数)
print(help(stu))
print("*" * 20)
print(stu.__doc__)