# 1.默认参数示例
# 报名函数，需要知道学生性别
# 没有特别指定，默认性别设为男生
def reg(name,age,gender="male"):
    if gender=="male":
        print("{0} is {1},and he is a good student".format(name,age))
    else:
        print("{0} is {1},and she is a good student".format(name,age))
# 调用默认函数案例1
reg("mingyue",21)
reg("xiaoming",23,"female")


# 关键字参数案例
def stu_key(name="no name", age=0, addr="no addr"):
    print("I am a student")
    print("我叫{0},我今年{1}岁了，我住{2}".format(name, age, addr))


n = "Python"
a = "18"
addr = "我家"
stu_key(age=a, name=n, addr=addr)

# 错误示例，普通参数只按照位置传递
# stu_key(a,n,addr)


# 收集参数示例1
# 函数模拟一个学生进行自我介绍，但具体内容不清楚
# *args-->创建了一个空Tuple
def stu(*args):
    print("hello,大家好，我自我介绍一下，简单说两句：")
    # type函数作用是检测变量的类型
    print(type(args))
    for item in args:
        print(item)

stu("Death",21,"郑州","Python","sigle")
stu("Madao")
# 收集参数调用示例
# 说明收集参数可以不带任何实参调用，此时收集参数为空tuple
stu()
# 如果使用关键字参数格式调用，会出现问题
# stu(name = "Python")


# 收集参数案例2
# 自我介绍
# 调用的时候需要使用关键字参数调用
def stu(**kwargs):
    print("hello,大家好,我先自我介绍一下：")
    print(type(kwargs))
    # 对于字典的访问，Python2和Python3有区别
    for k, v in kwargs.items():
        print(k, "---", v)


stu(name="Death", age=21, addr="郑州", lover="Python", work="student")
print("*" * 20)
stu(name="Madao")




# 收集参数混合调用案例
# stu模拟一个学生的自我介绍
# *args收集的是位置参数,同样要放在关键字参数前面
def stu(name, age, *args, hobby="没有", **kwargs):
    print("我叫{0}，我今年{1}岁了".format(name, age))
    if hobby == "没有":
        print("我没有爱好，很遗憾")
    else:
        print("我的爱好是{0}".format(hobby))

    print("*" * 20)
    for i in args:
        print(i)
    print("#" * 20)

    for k, v in kwargs.items():
        print(k, "---", v)

# 开始调用函数
name = "Death"
age = 21
# 调用的不同格式
stu(name, age)

stu(name, age, hobby="编程")
# 普通参数前置，关键字参数后置
stu(name, age, "Python", "java", hobby="哈哈哈", job="程序员", home="nanyang")


# 收集参数的解包问题01
def stu(*args):
    print("哈哈哈")
    # 标示循环次数，主要用来调试
    n = 0
    for i in args:
        print(type(i))
        print(n)
        n += 1
        print(i)


stu("Python", "郑大", "21", "happy")

# 下面代码将整个list当做一个参数放进了Tuple
# 这里，args的表示形式是Tuple内一个list类型的元素，即args=（【"Python","郑大","21","happy"】）
# 很显然与我们最初的想法相违背
l = ["Python", "郑大", "21", "happy"]
stu(l)
# 此时的调用，我们就需要解包符号，即调用的时候在前面加一个星号
stu(*l)

# 收集参数的解包问题02
def stu(**kwargs):
    print("哈哈哈")
    # 标示循环次数，主要用来调试
    n = 0
    for i in kwargs:
        print(type(i))
        print(n)
        n += 1
        print(i)

d = {"name": "云汐风", "age": 18, "sex": "男"}
stu(**d)