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