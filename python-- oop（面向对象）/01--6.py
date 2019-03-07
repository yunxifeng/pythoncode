print("!!!这是第一段代码!!!")
#类的成员描述符(属性/变量)
#变量的三种用法案例
class A():
    def __init__(self):
        self.name = "haha"
        self.sge = 21

a = A()
#属性的三种用法
#1.赋值
#2.读取
#3.删除
a.name = "刘大拿"
print(a.name)
del a.name
#print(a.name)

print("!!!这是第二段代码!!!")
#类属性 property
#应用场景:对变量除了普通的三种操作,还想增加一些附加的操作
class A():
    def __init__(self):
        self.name = "haha"
        self.sge = 21
    #此功能是对变量进行读取操作的时候,执行函数功能
    def fget(self):
        print("我被读取了")
        return self.name
    #此功能是对变量进行写操作的时候,执行函数功能
    def fset(self,name):
        print("我被写入了")
        self.name= "图灵学院:" + name
    # 此功能是对变量进行删除操作的时候,执行函数功能
    def fdel(self):
        del self.name
        print("我被删除了")
    #property的四个参数顺序是固定的,读取调用函数,写入调用函数,删除调用函数
    name2 = property(fget, fset, fdel, "这是一个文档")

a = A()
print(a.name)
print(a.name2)

print("!!!这是第三段代码!!!")
#抽象类的引入
class Animal():
    #在此定义一个功能,这里可以不实现,但是子类必须实现,不实现就报错
    def sayHello(self):
        #print("闻下对方的味道")
        pass
class Dog(Animal):
    def sayHello(self):
        print("闻一下对方")
class Person(Animal):
    def sayHello(self):
        print("Kiss me")

d = Dog()
d.sayHello()

p = Person()
p.sayHello()

print("!!!这是第四段代码!!!")
#抽象类的实现
import abc
#声明一个类并且指定当前类的元类为抽象类的元类
class Human(metaclass=abc.ABCMeta):
    #定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass
    #定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass
    #定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass
    def sleep(self):
        print("Sleeping")

print("!!!这是第五段代码!!!")
#函数名可以当变量使用
def sayHello(name):
    print("{0}你好,要来一发吗?".format(name))
sayHello("yunxifeng")
#这里吧sayHello赋值给death,此时death既是一个变量,也是一个函数,且具备其功能
death = sayHello
death("madao")

print("!!!这是第六段代码!!!")
#自定义类案例,自己组装一个类-01
class A():
    pass
def say(self):
    print("Saying")
class B():
    def say(self):
        print("Saying")
#正常调用
say(1)
#此处,把函数say赋值给类A的一个变量say,那么类A的这个变量就具有了函数的功能
A.say = say
a = A()
a.say()
#正常调用
b = B()
b.say()

print("!!!这是第七段代码!!!")
#自定义类案例,自己组装一个类-02
# method(function, instance)
#Create a bound instance method object.
from types import MethodType
class A():
    pass
def say(self):
    print("Saying")

# 此处去掉say函数的参数self(或者a.say(随便给个参数)),是可以正常运行的,即将say函数绑定在了对象实例a上,与老师所讲(函数不能绑定在对象实例上)有出入
'''
a = A()
a.say = say
a.say()
'''
#需要借助工具from types import MethodType
#通过Methodtype将类和方法绑在了一起,method是一个类,返回一个实例
a = A()
a.say = MethodType(say, A)
a.say()
help(MethodType)

print("!!!这是第八段代码!!!")
#自定义类案例,自己组装一个类-03
#type是一个类
#用type来造一个类
help(type)
#先定义类应该具有的成员函数
def say(self):
    print("Saying")
def talk(self):
    print("Talking")
#用type来创建一个类
#type(name, bases(父类), dict(字典,键值对,成员变量:函数)) -> a new type
#tuple哪怕只有一个也要有逗号
A = type("AName",(object,),{"class_say":say,"class_talk":talk})
#然后可以像正常访问一样实用类
a = A()
a.class_say()
a.class_talk()

print("!!!这是第九段代码!!!")
#元类演示
#元类写法是固定的,必须继承自type
#元类一般命名以MetaClass结尾
class DeathMetaClass(type):
    #注意以下写法
    def __new__(cls,name,bases,attrs):
    #自己的业务处理
        print("haha,我是元类")
        attrs['id'] = 000000
        attrs['addr'] = "北京"
        return type.__new__(cls,name,bases,attrs)
#元类定义完就可以使用,注意写法
class Teacher(object,metaclass=DeathMetaClass):
    pass
t = Teacher()
print(t.addr)


