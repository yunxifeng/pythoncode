print("!!!这是第一段代码!!!")
# super
class A():
    pass
class B(A):
    pass
#下面的写法不推荐
class C(B,A):
    pass
#mro显示一个类的所有父类,包括这个类自身
print(A.__mro__)
print(B.__mro__)

print("!!!这是第二段代码!!!")
#单继承和多继承的例子
#子类可以直接拥有父类的属性和方法,私有属性和方法除外
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("I am swimming")
class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("I am flying")
class Person():
    def __init__(self, name):
        self.name = name
    def Work(self):
        print("I am working")

#单继承的例子
class Student(Person):
    def __init__(self, name):
        self.name = name
stu = Student("yunxifeng")
stu.Work()

#多继承的例子
#有顺序,不推荐这么用,有其他方法
class Superman(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name
s = Superman("yunxifeng")
s.fly()
s.swim()
s.Work()

print("!!!这是第三段代码!!!")
#菱形继承/钻石继承
class A():
    pass
class B(A):
    pass
class C(A):
    pass

class D(B,C):
    pass

print("!!!这是第四段代码!!!")
# Mixin例子
class Person():
    name = "yunxifeng"
    age = 21
    def eat(self):
        print("EAT")
    def drink(self):
        print("DRINK")
    def sleep(self):
        print("SLEEP")
class Teacher(Person):
    def work(self):
        print("WORK")
class Student(Person):
    def study(self):
        print("STUDY")
class Tutor(Teacher,Student):
    pass

t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

print("*" * 20)

class TeacherMixin():
    def work(self):
        print("work")
class StudentMixin():
    def study(self):
        print("study")
class TutorM(Person,TeacherMixin,StudentMixin):
    pass

tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)

print("!!!这是第五段代码!!!")
# 类相关函数--issubclass
class A():
    pass
class B(A):
    pass
class C():
    pass

print(issubclass (B,A))
print(issubclass(C,A))
print(issubclass(B,object))
print("*" * 20)
#类相关函数--isinstance
class A():
    pass
a = A()
print(isinstance(a,A))
print("*" * 20)
#类相关函数--hasattr
class A():
    name = "NoName"
a = A()
print(hasattr(a,"name"))
print(hasattr(a,"age"))
print("*" * 20)
#类相关函数--dir
class A():
    pass
a = A()
dir(A)
dir(a)












