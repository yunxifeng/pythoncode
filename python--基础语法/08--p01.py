# 集合的创建
s=set()
print(type(s))
print(s)
#此时，大括号内一定要有值，否则定义出的是一个dict
s={1,2,3,4,5,6}
print(type(s))
print(s)
# 如果只是用大括号定义，则定义的是一个dict类型
d={}
print(type(d))
print(d)

# 集合常用操作
#成员检测
#in, not in
s={4,5,"i","love","python"}
print(s)
if "love" in s:
    print("爱呀")
if "haha" not in s:
    print("爱个锤子")

# 集合的遍历
# for循环
s={4,5,"i","love","python"}
for i in s:
    print(i,end="  ")

# 带有Tuple的集合遍历
# set本身不可哈希,list不可哈希，tuple可哈希
# s={(1,2,3),{4,5,6},{"i","love","python"}}集合本身不可哈希
s = {(1, 2, 3), (4, 5, 6), ("i", "love", "python")}
for k, m, n in s:
    print(k, "--", m, "--", n)

for k in s:
    print(k)

# 普通集合内涵
# 以下集合在初始化之后自动过滤重复元素
s={12,3,4,5,5,5,6,54,1,4,3,6}
print(s)

ss={i for i in s}
print(ss)

#带条件的集合内涵
sss={i for i in s if i%2 ==0}
print(sss)

#多循环的集合内涵
s1={1,2,3,4}
s2={"I","love","Python"}

s={m*n for m in s1 for n in s2}
print(s)
print("*" * 20)
s={m*n for m in s2 for n in s1 if n==2}
print(s)

# 关于集合的函数
#len,max,min:跟其他基本函数一致
s={1,1,1,2,3,4,6,6,4,3}
print(len(s))
print(max(s))
print(min(s))

# set():生成一个集合
l=[1,2,4,5,3,2,45]
s=set(l)
print(s)

# add:向集合内添加元素
s={1}
print(id(s))
s.add(334)
print(s)
print(id(s))

#clear: 清空Set
s={1,2,3,4}
print(id(s))
s.clear()
print(id(s))
#表明clear是原地清空数据

# copy: 拷贝
#remove：移除指定值,直接改变原有值，如果要删除的值不存在，报错（脾气不好）
#discard：移除集合中指定的值，跟remove一样，但如果要删除不存在的值，不报错（脾气好）
s={23,3,4,5,1,2,3}
s.remove(4)
print(s)
s.discard(1)
print(s)

print("*" * 20)
s.discard(100)
print(s)

s.remove(100)
print(s)
#思考：为什么remove不存在的值会报keyerror？提示：哈希

# s.pop(): 弹出第一个元素
s={1,2,3,4,5,6,7}
print(id(s))
print(s.pop())
print(id(s))

# 集合函数
# intersection:交集
# difference：差集
# union：并集
# issubset：检查一个集合是否为另一个集合的子集
# issuperset：检查一个集合是否为另一个集合的超集
s1={1,2,3,4,5,6}
s2={5,6,7,8,9}

s_1=s1.intersection(s2)
print(s_1)

s_2=s1.difference(s2)
print(s_2)

s_3=s1.union(s2)
print(s_3)

s_4=s1.issubset(s2)
print(s_4)

s_5=s1.issuperset(s2)
print(s_4)


# 集合的数学操作
s1={1,2,3,4,5,6}
s2={5,6,7,8,9}
#"+"好像不支持
s_1=s1-s2
print(s_1)


#创建冰冻集合
s=frozenset()
print(type(s))
print(s)
