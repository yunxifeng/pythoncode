#异常
'''
l = [1,2,3,4,5,6]
#IndexError: list index out of range
print(l[10])
#AttributeError: 'list' object has no attribute 'yunxifeng'
print(l.yunxifeng)
#常犯的除零错误
#ZeroDivisionError: division by zero
num = int(input("输入数字:"))
print(100/num)


print("*" * 20)

#简单异常案例01
try:
    num = int(input("输入数字:"))
    rst = 100/num
    #上述语句出错,则直接跳转到except,不执行下面的print
    print("计算结果是:{0}".format(rst))
except:
    print("你是傻子吗")
    #下面的语句是退出程序
    exit()

print("*" * 20)

#简单异常案例02
#给出提示信息
try:
    num = int(input("输入数字:"))
    rst = 100/num
    #上述语句出错,则直接跳转到except,不执行下面的print
    print("计算结果是:{0}".format(rst))
    #捕获异常后,将异常实例化,出错信息会出现在实例里
    #注意以下写法
    #以下语句是捕获ZeroDivisionError异常并将其实例化为实例e
except ZeroDivisionError as e:
    print("你是傻子吗")
    print(e)
    #下面的语句是退出程序
    exit()
#作业:为什么可以直接打印出实例e,此时实例e应该实现了哪个函数

print("*" * 20)
'''
#简单异常案例03
try:
    num = int(input("输入数字:"))
    rst = 100/num
    print("计算结果是:{0}".format(rst))

#如果是多种错误
#越具体的错误,越往前放
#在异常类继承关系中,越是子类的异常,越要往前放
#在处理异常的时候,一旦捕获到某一个异常,则不再进行下一个except代码
#有finally则执行,没有则执行下一大块代码
except ZeroDivisionError as e:
    print("hentai!除数不能为零")
    print(e)
    exit()
except NameError as e:
    print("hentai!名字错了")
    print(e)
    exit()
except AttributeError as e:
    print("hentai!属性有问题了")
    print(e)
    exit()
#所有异常都是继承自Exception
#建议写上且放在最后,后面的不会执行,此处就会拦截住所有异常
except Exception as e:
    print("hentai!不知道哪里错了")
    print(e)
    exit()

print("*" * 20)

#用户手动引发异常
#rise案例01
try:
    print("我爱Python")
    print(3.1415926)
    #手动引发异常,注意语法:raise ErrorClassName
    raise ValueError
    print("还没完")
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("我是所有异常的father")
finally:
    print("Hentai!你们都要经过我")

print("*" * 20)
#用户手动引发异常
#rise案例02
#自定义异常必须是系统异常的子类
class YunxifengError(ValueError):
    pass
try:
    print("我爱Python")
    print(3.1415926)
    #手动引发异常,注意语法:raise ErrorClassName
    raise YunxifengError
    print("还没完")
except NameError as e:
    print("NameError")
#如果没有下面两行,则抛出ValueError(自定义异常的父类)
except YunxifengError as e:
    print("Heitai自定义的错误")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("我是所有异常的father")
finally:
    print("Hentai!你们都要经过我")

print("*" * 20)
#else案例
try:
    num = int(input("输入数字:"))
    rst = 100/num
    print("计算结果是:{0}".format(rst))
except Exception as e:
    print("Exception")
else:
    print("No Exception")
finally:
    print("嘤嘤嘤,反正我最可耐!")
