# Tuple创建
# 创建空元组
t=()
print(type(t))

# 创建只有一个值的元组
# 注意逗号不能少，否则类型为int
t=(1,)
print(type(t))
print(t)
#或者
t=1,
print(type(t))
print(t)

# 创建多个值的元组
t=(1,2,3,4,5)
print(type(t))
print(t)
#或者
t=1,2,3,4,5
print(type(t))
print(t)
#或者，使用其他结构创建
l=[1,2,3,4,5]
t=tuple(l)
print(type(t))
print(t)

# 常见操作--索引
# 索引操作
t=(1,2,3,4,5)
print(t[4])
# 超标错误
# print(t[12])

# 常见操作--分片操作
t=(1,2,3,4,5)
t1=t[1::2]
print(id(t))
print(id(t1))
print(t1)
#分片可以超标
t2=t[2:100]
print(t2)

# 序列相加
t1=(1,2,3)
t2=(4,5,6)
#传址操作
print(t1)
print(id(t1))
t1+=t2
print(t1)
print(id(t1))
#以上操作，类似于
t1=(1,2,3)
t1=(4,5,6)
#元组的不可修改，指的是内容的不可更改
# t1[1]=300

# Tuple乘法
t=(1,2,3)
t=t*3
print(t)

# 成员检测
t=(1,2,3)
if 2 in t:
    print("yes")
else:
    print("no")

# 元组遍历，一般用for
# 1.单层元组遍历
t = (1, 2, 3, "I love python", "I", "hate")
for i in t:
    print(i, end=" ")

# 2.双层元组的遍历
t = ((1, 2, 3), (3, 4, 5), ("I love python", "I", "hate"))
for i in t:
    print(i)
# 或者
for k, v, w in t:
    print(k, "--", v, "--", w)

# 关于Tuple的函数
# len:获取元祖的长度
t=(1,2,3,4,5)
len(t)

#max,min:最大最小值
#思考：如果，列表或元组中有多个最大值最小值，则实际打印出哪个-->第一个
t = (1,2,3,4,4,4)
print(id(t[3]))
print(id(max(t)))
print(min(t))

# tuple:转化或创建元组
l=[1,2,3,4,5]
t=tuple(l)
print(t)

t=tuple()
print(t)

# count: 指定数据显示次数
t=(1,1,1,2,3,4,4,5,5,)
print(t.count(1))

# index:指定元素在元组中的索引值
print(t.index(4))
#如果需要查找的数字是多个，则返回第一个

#两个变量交换值
a=1
b=3
print(a)
print(b)
print("*" * 20)
#java程序员会这么写
c=a
a=b
b=c
print(a)
print(b)
print("*" * 20)
#python程序员的写法
a,b=b,a
print(a)
print(b)