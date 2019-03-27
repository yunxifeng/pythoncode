print("!!!下面是第一段代码!!!")
# 属性案例
# 创建Student类,描述学生类
# 学生具有Student.name属性
# 但name格式并不统一
# 下面的做法很麻烦
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

        #如果不想修改代码
        self.setName(name)
        #介绍下自己
    def intro(self):
        print("Hi, my name is {0}".format(self.name))
    def setName(self,name):
        self.name = name.upper()
s1 = Student("YUN Xifeng", 21)
s2 = Student("death madao", 18)

s1.intro()
s2.intro()

print("!!!下面是第二段代码!!!")
#property案例
#定义一个Person类,具有name,age属性
#对于任意输入的姓名,用大写方式保存
#对于任意输入的年龄,用整数保存
class Person():
    '''
    这是一个说明文档doc
    '''
    #函数名称任意
    def fget(self):
        return self._name * 2
    #所有输入的姓名以大写形式保存
    def fset(self,name):
        self._name = name.upper()
    def fdel(self):
        self._name = "NoName"
    name = property(fget, fset, fdel, "对name进行了操作")

p1 = Person()
#执行fset
p1.name = "TuLing"
#执行fget
print(p1.name)

# 作业:
# 在用户输入年龄的时候,可以输入整数,小数(浮点数)
# 但为了数据清洁,我们统一保存整数,去除小数

print("!!!下面是第三段代码!!!")
#类的内置属性案例
print(Person.__dict__)
print(Person.__doc__)
print(Person.__bases__)
print(Person.__name__)

print("!!!下面是第四段代码!!!")
#__init__案例
class A():
    def __init__(self, name = "yunxifeng"):
        print("haha,我被调用了")
a = A()
#__call__案例
class A():
    def __init__(self, name = "yunxifeng"):
        print("haha,我被调用了")
    def __call__(self):
        print("haha,我又被调用了")
a = A()
#将实例化对象当做函数使用,需要调用call函数功能,在call函数里写什么功能调用什么功能
a()
#__str案例
class A():
    def __init__(self, name = "yunxifeng"):
        print("haha,我被调用了")
    def __str__(self):
        return "这是一个例子"
a = A()
#打印这个对象时需要调用str函数
print(a)

print("!!!下面是第四段代码!!!")
class A():
    name = "NoName"
    age = 21
    def __getattr__(self,name):
        print("没找到")
        print(name)
a = A()
print(a.name)
#没有addr这个属性,调用getattr函数,不报错,并且将这个属性打印出来
#这里是两个参数a和addr,所以getattr函数定义时也需要两个参数
print(a.addr)
#这里会打印出None,为什么?

print("!!!这是第五段代码!!!")
class Person():
    def __init__(self):
        pass
    def __setattr__(self, key, value):
        print("设置属性: {0}".format(key))
        #下面是我们想要给key这个属性赋值value,然后会触发setattr函数,然后又重复第一句话的内容,导致死循环
        #self.key = value
        #此种情况,为了避免死循环,规定统一调用父类魔法函数
        #super().__setattr__(key,value)
p = Person()
print(p.__dict__)
#设置属性,触发setattr函数
p.age = 21

print("!!!这是第六段代码!!!")
# __gt__案例
class Student():
    def __init__(self,name):
        self._name = name
    def __gt__(self, obj):
        print("haha,{0}会比{1}大吗?".format(self,obj))
        return self._name > obj._name
#作业:字符串的比较是按什么规则
#下面的显示结果不美观,能否显示"haha,yunxifeng会比deathmadao大吗?"
stu1 = Student("yunxifeng")
stu2 = Student("deathmadao")
print(stu1 > stu2)

print("!!!这是第七段代码!!!")
#类和对象的方法案例
class Person():
    #实例方法
    def eat(self):
        print(self)
        print("Eatting")
    #类方法
    #类方法的第一个参数,一般命名为cls,区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing")
    #静态方法,没有参数,不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print("Saying")
yunxifeng = Person()
#实例方法
yunxifeng.eat()
#类方法
Person.play()
yunxifeng.play()#实例调用类方法
#静态方法
Person.say()
yunxifeng.say()#实例调用静态方法
#作业:自行查找三种方法内存使用方面的区别