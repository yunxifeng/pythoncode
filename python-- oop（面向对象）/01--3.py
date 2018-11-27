print("!!!下面是第一段代码!!!")
# 继承的语法
# 在Python中,任何类都有一个共同的父类--object
class Person():
    name = "Noname"
    __score = 0
    _petname = "sec"
    def sleep(self):
        print("Sleeping...")

# 父类写在括号内
class Teacher(Person):
    teacher_id = "9527"
    def make_test(self):
        print("attention")

t = Teacher()
print(t.name)
print(Teacher.name)
# 受保护的
print(t._petname)
# 私有的,公开访问报错
#print(t.__score)

t.sleep()
print(t.teacher_id)
t.make_test()

print("!!!下面是第二段代码!!!")
# 子类和父类定义同一个变量名称,则优先使用子类本身
class Person():
    name = "Noname"
    __score = 0
    _petname = "sec"
    def sleep(self):
        print("Sleeping...")
class Teacher(Person):
    teacher_id = "9527"
    name = "yunxifeng"
    def make_test(self):
        print("attention")
t = Teacher()
print(t.name)

print("!!!下面是第三段代码!!!")
#子类扩充父类功能的案例
class Person():
    name = "Noname"
    __score = 0
    _petname = "sec"
    def sleep(self):
        print("Sleeping...")
    def work(self):
        print("make some money")
class Teacher(Person):
    teacher_id = "9527"
    name = "yunxifeng"
    def make_test(self):
        print("attention")
    def work(self):
        #扩充父类功能方法一:只需要调用父类相应的函数
        Person.work(self)
        #扩充父类功能方法二:super代表调用父类
        super().work()
        self.make_test()
t = Teacher()
t.work()

print("!!!下面是第四段代码!!!")
#构造函数的概念
class Dog():
    #__init__就是构造函数
    #每次实例化的时候,第一个被自动调用
    #因为主要工作是进行初始化,所以得名
    #对类进行实例化的时候,通常需要确定一些属性,对实例化对象进行初始化
    def __init__(self):
        self.name = "Noname"
        self.age = 10
        self.address = "None"
        print("I am init in dog")
# 实例化的时候,括号内的参数需要跟构造函数参数匹配
kaka = Dog()

print("!!!下面是第五段代码!!!")
#继承中的构造函数-01
class Animal():
    def __init__(self):
        print("Animal")
class BuruAni(Animal):
    def __init__(self):
        print("Buru Animal")
class Dog(BuruAni):
    def __init__(self):
        print("I am init in dog")
# 实例化的时候,自动调用了Dog的构造函数
kaka = Dog()
# 猫没有写构造函数
class Cat(BuruAni):
    pass
# 此时应该自动调用构造函数,因为Cat没有构造函数,所以向上按照MRO顺序查找父类构造函数
# 在BuruAni中查找到了构造函数,则停止向上查找
c = Cat()

print("!!!下面是第六段代码!!!")
#继承中的构造函数-02
class Animal():
    def __init__(self):
        print("Animal")
class BuruAni(Animal):
    def __init__(self,name):
        print("Buru Animal {0}".format(name))
class Dog(BuruAni):
    def __init__(self):
        print("I am init in dog")
# 实例化Dog时,查找到Dog的构造函数,参数匹配,不报错
d = Dog()

class Cat(BuruAni):
    pass
# 此时,由于Cat没有构造函数,则向上查找
# 因为BuruAni的构造函数需要两个参数,实例化的时候给了一个,所以会报错
#c = Cat()
c = Cat(name)

print("!!!下面是第七段代码!!!")
#继承中的构造函数-03
class Animal():
    def __init__(self):
        print("Animal")
class BuruAni(Animal):
    pass
class Dog(BuruAni):
    def __init__(self):
        print("I am init in dog")

kaka = Dog()

class Cat(BuruAni):
    pass
#此时调用Animal的构造函数
c = Cat()

print("!!!下面是第八段代码!!!")
# 证明super不是关键字,而是一个类
print(type(super))
help(super)
