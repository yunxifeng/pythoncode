# 创建list案例
# 1.创建空列表
l1=[]
# type是内置函数，负责打印出变量的类型
print(type(l1))
print(l1)

#2.创建带值的列表
l2=[100]
print(type(l2))
print(l2)

#3.创建列表,带多个值
l3=[1,2,3,4,5]
print(type(l3))
print(l3)

#4.使用list（）
l4=list()
print(type(l4))
print(l4)

# 列表常用操作--访问
# 下标访问列表
l=[3,2,1,4,5,6]

print(l[3])
print(l[0])

# 列表常用操作--分片
# 分片操作,截取2,1,4
# 包含左下标对应值，不包含右下标对应值
l=[3,2,1,4,5,6]
print(l[1:4])

# 下标值可以为空，
# 如果不写，左下标值默认为零，右下标值为最大值加一，即表示截取到最后一个数值
print(l[:])
print(l[:4])
print(l[2:])

# 分片可以控制增长幅度，默认增长幅度为1
print(l[1:6:1])
#增长幅度为2
print(l[1:6:2])

#下标可以超出范围，超出后不再考虑多余下标内容
print(l[2:10])
print(l[-7:3])

#下标值，增长幅度可以为负数
#为负数，表明顺序是从右往左
# 此时，列表最后一个数字的下标是-1
# 分片之负数下标
print(l)
# 下面显示为空，因为默认分片总是从左向右截取
# 即正常情况下，分片左边的值一定小于右边的值
print(l[-2:-4])

print(l[-4:-2])

#如果分片一定要左边下标值比右边大，则步长参数（增长幅度）需要使用负数
# 结果是截取的原列表内容正反颠倒
#此案例为一个list直接正反颠倒提供了一种思路
print(l[-2:-4:-1])

# id()函数举例
a=100
b=200
print(id(a))
print(id(b))
# 证明a和c指向的是同一份数据
c=a
print(id(c))
# 如果a跟c指向同一份数据，则更改a的值同样也会更改c的值
# 但是，显示结果并非如此，为什么？--->已解决
a=101
print(id(a))
print(c)

# 可变数据类型
# 即使l1和l2的值相同,但是地址不同
print("*")
l1 = [1,2]
l2 = [1,2]
print(id(l1))
print(id(l2))

# 不可变数据类型
# a1和a2不仅值相同,而且地址也相同
a1 = 1
a2 = 1
print(id(a1))
print(id(a2))

# 通过id可以判断分片是重新生成了一份数据还是使用的同一份数据
l=[3,4,5,3,2,4,5,3,2]
ll=l[:]
lll=ll
#如果两个id值一样，则表明分片产生的列表是使用的同一份地址同一份数据
#否则，则表明分片是重新生成了一份数据，即一个新的列表，然后把数值拷贝到新列表中
print(id(l))
print(id(ll))
print(id(lll))
# 通过id知道，ll和lll是同一份数据，验证代码如下
l[1]=100
print(l)
print(ll)

ll[1]=100
print(ll)
print(lll)
print(id(ll))
print(id(lll))

# del 删除操作
# 如果使用del之后，id的值和删除前不一样，则说明删除生成了一个新的list
# 案例证明是在原list上执行删除操作, 并没有生成新list
a=[1,2,3,4,5,6]
print(id(a))
del a[2]
print(id(a))
print(a)

# list相加案例
a=[1,2,3]
b=[4,5,6]
d=['a','b','c']
c=a+b+d
print(c)

# list乘法案例
#列表直接跟一个整数相乘
#相当于吧n个列表接在一起
a=[1,2,3]
b=a*10
print(b)

# 成员资格运算
a=[1,2,3,4,5]
b=6
#c的值一定是一个布尔值
c=b in a
print(c)

b=5
print(b in a)

#not in
a=[1,2,3,4,5]
b=6
print(b not in a)


# list的遍历
# for in list
a = [1, 2, 3, 4, 5]
# 挨个打印a里面的元素
for i in a:
    print(i)

b = ["I love Python"]
for i in b:
    print(i)

#java，c++程序员写Python代码
indx=0
for i in range(0,len(a)):
    print(a[i])
    i+=1

#range
#in后面的变量要求是可迭代的内容
for  i in range(1,10):
    print(i)
print(type(range(1,10)))


# while遍历list
#一般情况下不用while遍历list
a=[1,2,3,4,5,6]
length=len(a)
#index表示list的下标
index=0
while index<length:
    print(a[index])
    index+=1

#双层列表循环
#a为嵌套列表，或者叫双层列表
a=[["one",1],["two",2],["three",3]]
for k,v in a:
    print(k,"----",v)

#双层列表循环变异
#a为嵌套列表，或者叫双层列表
a=[["one",1,"eins"],["two",2,"zwei"],["three",3,"drei"]]
#这个例子说明，k,v,w的个数应该跟解包出来的变量个数保持一致
for k,v,w in a:
    print(k,"----",v,"----",w)

# list content
#for创建
a=['a','b','c']
#用list a创建一个list b
#对于所有a中的元素，逐个放入新列表b中
b=[i for i in a]
print(b)

#对a中所有元素乘以10，生成一个新的list
a=[1,2,3]
#用list a创建一个list b
#对于所有a中的元素，逐个放入新列表b中
b=[i*10 for i in a]
print(b)

#还可以过滤掉原来list中的内容放入新列表
#例，原有列表a，需要把所有a中的偶数拿出来生成新列表b
a=[x for x in range(1,35)]#生成1到34的一个列表
#把a中所有偶数生成一个新的列表b
b=[m for m in a if m%2==0]
print(b)

#列表生成式可以嵌套
#有两个列表a，b
a=[i for i in range(1,4)]
print(a)
b=[i for i in range(100,400) if i%100==0]
print(b)
#嵌套,等于两个for循环嵌套
c=[m+n for m in a for n in b]
print(c)
#上面代码和下面等价，区别为是否是列表
for m in a:
    for n in b:
        print(m+n,end=" ")
print()

c=[m+n for m in a for n in b if m+n<250]
print(c)

# list常用函数

# len：求列表长度
a=[x for x in range(1,100)]
print(len(a))
# max:求最大值
# min:求最小值
print(max(a))
b=["man","file","python"]
print(max(b))

# list：将其他格式的数据转换成list
# 只要是可迭代的都可以转换
a=[1,2,3]
print(list(a))

s="I love python"
print(list(s))

#把range产生的内容转换成list
print(list(range(1,10)))


# 这是个什么案例
l=['a',"I love python",250,5+4j]
print(l)

# append
a=[i for i in range(1,5)]
print(a)
a.append(100)
print(a)

# 删除操作相关函数
#del 删除
# pop，从队尾拿出一个元素，即把最后一个元素拿出来
print(a)
last_ele=a.pop()
print(last_ele)
print(a)

# remove在列表中删除指定的值的元素
# 如果删除的值不在list中，则报错
# 即，即删除list指定值的操作应该使用try...excepty语句，或者先进行判断
#if x in list:
#   list.remove(x)
a.insert(3,666)
print(a)
print(id(a))
a.remove(666)
print(a)
print(id(a))
#id相同。说明remove操作是在原list上直接操作

#clear清空
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))
#如果不需要保持列表地址不变，则清空列表可以使用以下方式
#a=list()
#a=[]

#reverse:翻转列表内容，原地翻转
a=[1,2,3,4,5]
print(a)
print(id(a))
a.reverse()
print(a)
print(id(a))

# extend：扩展列表，两个列表，把一个直接拼接到后一个上
a=[1,2,3,4,5]
b=[6,7,8,9,10]
print(a)
print(id(a))
a.extend(b)
print(a)
print(id(a))

# count:查找列表中指定值或元素的个数
print(a)
a.append(8)
a.insert(4,8)
print(a)
print(a.count(8))


# 拷贝
# copy:浅拷贝，传值
#列表类型变量赋值示例
a=[1,2,3,4,5,666]
print(a)
#list类型，简单赋值操作，是传地址
b=a
b[3]=777
print(a)
print(id(a))
print(b)
print(id(b))
print("*" * 20)
#为了解决以上问题，list赋值需要采用copy函数
b=a.copy()
print(a)
print(id(a))
print(b)
print(id(b))

print("*" * 20)
b[3]=888
print(a)
print(b)

# 深拷贝--deepcopy
from copy import deepcopy
a = [1,2,3]
print(id(a))
b = deepcopy(a)
print(id(b))

# 同学问题
# 传值与传址问题
# 对于简单的数值，采用传值操作，即在函数内对参数的操作不影响外面的变量
# 对于复杂变量，采用传址操作，此时函数内的参数和外部变量是同一份内容，任何地方对此内容的更改都影响到另外的变量或参数的使用
def a(n):
    n[2] = 300
    print(n)
    return None


def b(n):
    n += 100
    print(n)
    return None


an = [1, 2, 3, 4, 5, 6]
bn = 9

print(an)
# 传址
a(an)
# 全局变量an被函数改变
print(an)

print(bn)
# 传值
b(bn)
# 全局变量bn没有被改变
print(bn)

