'''
match的使用案例
'''
import re

# 以下正则分成了两个组, 以小括号为单位
s = r'([a-z]+) ([a-z]+)'
# re.I表示忽略大小写
pattern = re.compile(s, re.I)
m = pattern.match("Hello world wide web")

# group(0)表示返回匹配成功的整个字串
s = m.group(0)
print(s)
# group(1)表示返回第一个正则分组([a-z]+)匹配到的字串
s = m.group(1)
print(s)
# 等价于m.group(1),m.group(2),...,以Tuple类型打印出所有正则分组
s = m.groups()
print(s)


# 返回匹配成功的整个字串的跨度
s = m.span(0)
print(s)
# 返回第一个正则分组([a-z]+)匹配成功的字串跨度
s = m.span(1)
print(s)