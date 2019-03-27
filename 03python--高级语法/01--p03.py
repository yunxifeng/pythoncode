#包的导入
import pkg01
pkg01.inInit()
print("*" * 20)

#导入包的某个模块
import pkg01.p01
stu = pkg01.p01.Student()
stu.say()
print("*" * 20)

#from package import *
from pkg01 import *
inInit()
#说明只导入了__init__模块
#stu = Student()
print("*" * 20)

#__all__的用法
from pkg02 import *
stu = p01.Student()
stu.say()
#下面这句报错,只导入__all__,下面的内容不会导入
#inInit()
