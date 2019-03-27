'''
# 打开文件, 写方式
# r表示后面的字符串内容不需要转义
#f = open(r"test01.txt", "w")
# 文件打开后必须关闭
#f.close()
#此案例说明,以写方式打开文件,如果没有此文件,则自动创建
print(" _ " * 20)
# with语句案例
with open(r"test01.txt", "r") as f:
    pass
# 下面语句块开始对文件f进行操作
# 在本模块中不需要再使用close关闭文件f
print(" _ " * 20)
# 按行完整读取文件
with open(r"test01.txt", "r") as f:
    # 按行读取文件
    strline = f.readline()
    # 此结构保证能够完整地读取文件直到结束
    while strline:
        print(strline)
        strline = f.readline()
print(" _ " * 20)
# list能把打开的文件作为参数,把文件内每一行内容作为一个元素
with open(r"test01.txt", "r") as f:
    # 以打开的文件作为参数,创建列表
    l = list(f)
    for i in l:
        print(i)
print(" _ " * 20)
# read是按照字符读取文件内容
# 允许输入参数决定读取几个字符,如果没有指定,则从当前位置读取到结尾
# 否则,从指定位置读取指定个数字符
with open(r"test01.txt", "r" ) as f:
    strChar = f.read(1)
    print(len(strChar))
    print(strChar)
# 作业: 使用read读取文件,每次读取一个,使用循环读完且保证输出格式
print(" _ " * 20)
# seek案例
# 打开文件后,从第五个字节开始读取
# 打开文件,读写指针默认在0处,即文件的开头
with open(r"test01.txt", "r") as f:
    # seek移动单位是字节
    f.seek(4,0)
    strChar = f.read()
    print(strChar)
print(" _ " * 20)
# 关于读取文件的练习
# 打开文件, 三个字符一组读出内容,然后打印
# 每读取一次,休息一秒
import time
with open(r"test01.txt", "r") as f:
    #read参数的单位是字符,一个汉字就是一个字符
    strChar = f.read(3)
    while strChar:
        print(strChar)
        time.sleep(0.1)
        strChar = f.read(3)
#解释一下运行结果,为什么不是每行三个字符

print(" - " * 20)
with open(r"test01.txt", "r") as f:
    strChar = f.read(3)
    pos = f.tell()
    while strChar:
        print(pos)
        print(strChar)
        strChar = f.read(3)
        pos = f.tell()
# 以下结果说明:tell的返回数字是以字符为单位的
# read也是以字符为单位

print(" - " * 30)
# write案例01
#向文件追加一句话
#with open(r"test01.txt", "a") as f:
 #   f.write("\n生活不止眼前的苟且, \n 还有诗和远方")

#writelines表示写入很多行,参数可以是list格式
l = ["I", "love", "Python"]
with open("test01.txt", "a") as f:
    f.writelines(l)
# 此处追加结果:IlovePython

#pickle
#序列化模块
#序列化案例01
import pickle
age = 21
with open(r"test01.txt", "wb") as f:
    pickle.dump(age,f)

#反序列化
import pickle
with open(r"test01.txt", "rb") as  f:
    age = pickle.load(f)
    print(age)

#序列化案例02
a = [21, "yunxifeng", "男", "single", "post-love", [168,64]]
with open(r"test02","wb") as f:
    pickle.dump(a, f)
#反序列化
with open(r"test02", "rb") as f:
    a = pickle.load(f)
    print(a)
'''
#shelve
#使用shelve创建文件并使用
import shelve
#打开文件
#shv相当于一个字典
shv = shelve.open(r"shv.db")
shv["one"] = 1
shv["two"] = 2
shv["three"] = 3
shv.close()
# shelve自动创建的不仅仅是一个shv.db文件,还包括其他其他格式文件,保证正常读取数据库
#shelve的读取
shv = shelve.open(r"shv.db")
try:
    print(shv["one"])
    print(shv["threeeeeee"])
except Exception as e:
    print("让你报错")
finally:
#上面的代码一旦出错,则无法执行关闭操作
#加上错误处理,就可以正常执行关闭操作了
    shv.close()

# shelve 之只读打开
import shelve
shv = shelve.open(r'shv.db', flag='r')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()

# 更改shelve
import shelve
shv = shelve.open(r'shv.db')
try:
    shv['one'] = {"eins": 1, "zwei": 2, "drei": 3}
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    one = shv['one']
    #此时发现已经更改成功
    print(one)
finally:
    shv.close()

print(" - " * 30)

# shelve忘记写回，不使用强制写回
shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    #此处对字典one中的eins的值做了修改,但是并没有写回到shv.db中,而是在缓存中
    k1["eins"] = 100
finally:
    #关闭了连接,更改的数据在缓存中,没有写入
    shv.close()

shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()

# shelve忘记写回，使用强制写回
shv = shelve.open(r'shv.db', writeback=True)
try:
    k1 = shv['one']
    print(k1)
    #使用强制写回,将缓存中修改了的数值直接强制写到数据库
    #实际上是把数据库中所有的键值对都放到了内存缓存中,修改之后,再全部写回数据库
    k1["eins"] = 100
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()

#shelve使用with管理上下文环境
with shelve.open(r'shv.db', writeback=True) as shv:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] = 10000
with shelve.open(r"shv.db", writeback=True) as shv:
    print(shv["one"])