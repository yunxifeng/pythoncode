print("！！！下面是第一段代码！！！")
class Student():
    name = "yunxifeng"
    age = 21
Student.__dict__
# 实例化
Death = Student()
Death.__dict__
# 不打印，则输出结果为空
print(Death.name)

print("！！！下面是第二段代码！！！")
class A():
    name = "yunxifeng"
    age = 18
# 注意say的写法，参数有一个self
    def say(self):
        self.name = "aaaa"
        self.age = 200
# 此案例说明
# 类实例的属性和其对象实例的属性在不对对象实例赋值的前提下，指向同一个变量
print(A.name)
print(A.age)
print(id(A.name))
print(id(A.age))

print("*" * 10)

a=A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print("！！！下面是第三段代码！！！")
class A():
    name = "yunxifeng"
    age = 18
    def say(self):
        self.name = "aaaa"
        self.age = 200
print(A.name)
print(A.age)
print(id(A.name))
print(id(A.age))

print("*" * 10)

a=A()
print(A.__dict__)
print(a.__dict__ )

a.name = "Death"
a.age = 21

print(a.__dict__)

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print("！！！下面是第四段代码！！！")
class Student():
    name = "yunxifeng"
    age = 18
# 注意say的写法，参数有一个self
    def say(self):
        self.name = "aaaa"
        self.age = 200
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

    def sayAgain(s):
        print("My name is {0}".format(s.name))
        print("My age is {0}".format(s.age))

yunxifeng = Student()
yunxifeng.say()

yunxifeng.sayAgain()

print("！！！下面是第五段代码！！！")
class Teacher():
    name = "yunxifeng"
    age = "21"
#非绑定类函数,
    def say(self):
        self.name = "Death"
        self.age = 18
        print("My name is {0}".format(self.name))
# (__class__.成员名)访问当前类的成员变量
        print("My age is {0}".format(__class__.age))
#绑定类函数
    def sayAgain():
#(__class__.成员名)访问当前类的成员变量
        print(__class__.name)
        print(__class__.age)
        print("Hello,nice to see you again")
t = Teacher()
#通过对象访问
t.say()
#错误示例,类型错误,不能使用对象访问
#t.sayAgain()
#修正,调用绑定类函数,使用类名访问
Teacher.sayAgain()

print("！！！下面是第六段代码！！！")
#关于self的案例
class A():
    name = "yunxifeng"
    age = 21

    def __init__(self):
        self.name = "Death"
        self.age = 18
    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "Madao"
    age = 15

a = A()

#此时,系统会默认把a作为第一个参数传入函数
a.say()

#错误示例.类型错误
#A.say()
#此时,self被a替换
A.say(a)
#同样可以把A作为参数传入
A.say(A)

#此时,传入的是类示例B,因为B具有name和age属性,所以不会报错
A.say(B)

#以上代码,利用了鸭子模型

print("！！！下面是第七段代码！！！")
#私有变量案例

class Person():
# name是共有的成员
    name = "yunxifeng"
# __age就是私有成员
    __age = 21

p = Person()
# name是公有变量
print(p.name)
# __age是私有变量,不能访问
#print(p.__age)

# name mangling技术,'_Person__age:21'
print(Person.__dict__)

p._Person__age = 19
print(p._Person__age)


