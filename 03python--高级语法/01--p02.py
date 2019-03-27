#直接导入模块
import p01
stu = p01.Student("yunxifeng" , 21)
stu.say()
p01.sayHello()
print("*" * 20)
#如果模块名称是以数字开头的,可借助importlib包
import importlib
#相当于导入了一个p01(假定p01是数字开头的)的模块并把模块赋值给了death
death = importlib.import_module("p01")
stu = death.Student("云汐风")
stu.say()
death.sayHello()
print("*" * 20)
#给模块起别名
import p01 as p
stu =p.Student("yunxifeng" , 21)
stu.say()
print("*" * 20)
#导入需要使用的模块功能,有选择性导入
from p01 import Student , sayHello
stu = Student("hah")
stu.say()
sayHello()
print("*" * 20)
#导入所有内容
from p01 import *
sayHello()
stu = Student("yunxifeng" , 21)
stu.say()
print("*" * 20)
#系统默认搜索路径
#模块放在以下路径可以被系统找到,放在其他地方可能找不到
import sys
print(type(sys.path))
for p in sys.path:
    print(p)