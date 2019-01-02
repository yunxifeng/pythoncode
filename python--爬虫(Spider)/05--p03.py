'''
search练习
'''
import re
s = r'\d+'
partten = re.compile(s)
m = partten.search("one12two34three56")
print(m.group())

# 参数表示起始范围
m = partten.search("one12two34three56", 10, 40)
print(m.group())


'''
findall练习
'''
partten = re.compile(r'\d+')
m = partten.findall("one12two34three56")
print(m)


'''
finditer练习
'''
partten = re.compile(r'\d+')
m = partten.finditer("one12two34three56")
# 可迭代类型
print(type(m))
for i in m:
    # 发现i是Match类型的实例
    print(i.group())