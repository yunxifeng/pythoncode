'''
遍历document和搜索document对象
'''
from urllib import request
from bs4 import BeautifulSoup
import re

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()

# 创建bs实例
soup = BeautifulSoup(content, "lxml")
print(soup.name)
print("********" * 20)

# 遍历
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node.string)

print("********" * 20)

# 搜索
tags = soup.find_all(name="meta")
for tag in tags:
    print(tag)

print("********" * 20)

tags = soup.find_all(re.compile(r'^me'), content="always")
for tag in tags:
    print(tag)