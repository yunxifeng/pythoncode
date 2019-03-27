#字典的创建
#1.创建空字典
d={}
print(type(d))
print(d)
#或者
d=dict()
print(d)

#2.创建有值字典
d={"one":1,"two":2,"three":3}
print(d)
#或者
d=dict({"one":1,"two":2,"three":3})
print(d)
#利用关键字参数
d=dict(one=1,two=2,three=3)
print(d)

#利用元组
d=dict([("one",1),("two",2),("three",3)])
print(d)

# Dict常见操作
# 访问数据
d={"one":1,"two":2,"three":3}
#注意访问格式
#中括号里是键值
print(d["one"])

d["one"]="eins"
print(d)

#删除操作
#del 删除
del d["one"]
print(d)

# 成员检测
#下例说明成员检测检测的是key内容
d={"one":1,"two":2,"three":3}

if 2 in d:
    print("value")
if "two" in d:
    print("key")
if ("two",2) in d:
    print("kv")

# 遍历在python2和python3中区别较大，代码不通用
# 按key值来使用for循环
d = {"one": 1, "two": 2, "three": 3}
# 1.使用for循环，直接按key值访问
for k in d:
    print(k, d[k])

# 上述代码可以改写如下
d = {"one": 1, "two": 2, "three": 3}
for k in d.keys():
    print(k, d[k])
# 只访问字典的值
for v in d.values():
    print(v)

# 注意以下特殊用法
for k, v in d.items():
    print(k, "--", v)

# Dict生成式
d={"one":1,"two":2,"three":3}
#常规字典生成式
dd={k:v for k,v in d.items()}
print(dd)
#加限制条件的字典生成式
dd={k:v for k,v in d.items() if v%2==0}
print(dd)

d = {k:v for k in range(1,3) for v in range(4,6)}
print(type(d))

# 通用函数
a = {"one":1, "two":2, "three":3}
print(len(a))
print(max(a, key=a.get))
print(min(a, key=a.get))

# str(d)：返回字典的字符串格式
d={"one":1,"two":2,"three":3}
print(str(d))

# clear():清空
d.clear()
print(d)

#items：返回字典的键值对组成的元组格式
d={"one":1,"two":2,"three":3}
i=d.items()
print(type(i))
print(i)

# keys：返回字典的键组成的一个结构
k=d.keys()
print(type(k))
print(k)

# values:同理，一个可迭代的结构
v=d.values()
print(type(v))
print(v)

# get :根据指定键返回相应的值，好处，可以设置默认值
d={"one":1,"two":2,"three":3}
print(d.get("two"))

#返回None
print(d.get("hskah"))
#下面的代码会报错
#print(d["撒发生"])

#get默认值是None，可以设置
#能找到，返回对应值；找不到，返回默认值,这里设置默认值是100
print(d.get("one",100))
print(d.get("jkashf",100))

#fromkeys:使用指定的序列作为键，使用一个值作为字典的所有键的值
l=["enis","zwei","dree"]
#注意fromkeys两个参数的类型
#注意fromkeys的调用主体-->dict
d=dict.fromkeys(l,"hahahah")
print(d)