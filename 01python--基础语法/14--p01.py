# 案例1
#a1是全局变量,a2是局部变量
a1=100
def fun():
    print(a1)
    print("I am fun")
    a2=99
    print(a2)

print(a1)
fun()
# a2是函数内定义的变量, 不能被外部调用
# print(a2)


# global--提升局部变量为全局变量
def fun():
    global b1
    b1=100
    print(b1)
    print("I am fun")
    #b2作用域是fun
    b2=99
    print(b2)

#print(b2)
fun()
#print(b1)如果在fun()上面，则报错，为什么？
# 因为只有运行fun()函数后,b1才被提升为全局变量
print(b1)


# globals和locals是内建函数（builtin）
a=1
b=2

def fun(c,d):
    e=111
    print("Locals{0}".format(locals()))
    print("Globals{0}".format(globals()))

fun(100,200)