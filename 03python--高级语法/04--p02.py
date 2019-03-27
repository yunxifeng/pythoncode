#补充几个高级函数
#zip案例01
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]
z = zip(l1,l2)
print(type(z))
print(tuple(z))
#zip案例02
l1 = ["yunxifeng", "deayh", "madao"]
l2 = [80, 90, 100]
print(tuple(zip(l1,l2)))
#enumerate案例01
l1 = [11,22,3,4,5,66]
en = enumerate(l1)
l2 = [i for i in en]
print(l2)
#enumerate案例02
#指定索引从100开始
en = enumerate(l1, start=100)
print(tuple(en))

print("- " * 20)

#collections模块
#namedtuple-01
import collections
help(collections.namedtuple)
Point = collections.namedtuple("Point", ['x', 'y'])
p = Point(11,22)
print(p.x)
print(p[0])
#namedtuple-02
Circle = collections.namedtuple("Circle",["x","y","r"])
c = Circle(100,100,20)
print(c)
print(type(c))
#检测一下namedtuple是不是tuple的子类
print(isinstance(c,tuple))
#deque
q = collections.deque(["a","b","c"])
print(q)
q.append("d")
print(q)
q.appendleft("x")
print(q)

#defaultdict
d = {"one","two","three"}
#定义一个函数,简单的lambda表达式,输出字符串"yunxifeng"
func = lambda: "yunxifeng"
#当调用字典里存在的值时,正常输出,当调用字典里不存在的值时,调用func函数,不报错
d = collections.defaultdict(func)
d["one"]=1
print(d["one"])
print(d["four"])
# Counter
#为什么不把"***"当做一个字符串
#因为括号里的内容是可迭代的
c = collections.Counter("aaakjdksaflkjdsddd")
print(c)
s = ["love","love","haha","haha","yunxifeng"]
print(collections.Counter(s))


