# 包含一个学生类,一个sayhello函数,一个打印函数
class Student():
    def __init__(self, name = "NoName" , age = 18):
        self.name = name
        self.age = age
    def say(self):
        print("My name is {0}".format(self.name))
def sayHello():
    print("Hi , 你好")

# 此判断语句建议作为程序入口
# 此语句的理解,如果该段代码作为主进程/主线程被执行的时候,那么这段代码的名称就是main
# 当这个模块文件被单独执行时,正常执行下面的代码
# 当这个文件作为模块被导入的时候,此时name将不再是main,而是模块的名称,此时不再执行下面这段代码
if __name__ == '__main__':
    print("我是模块p01.")