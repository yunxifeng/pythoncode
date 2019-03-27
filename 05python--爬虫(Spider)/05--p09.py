'''
beautifulsoup4---Navigable String对象和BeautifulSoup对象
'''
from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()

# 创建bs实例
soup = BeautifulSoup(content, "lxml")

# Navigable String对象
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
# title的内容
print(soup.title.string)


# BeautifulSoup对象
print(soup.name)
print(soup.attrs)


