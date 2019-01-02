'''
beautifulsoup4---Tag对象
'''
from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()

# 创建bs实例
soup = BeautifulSoup(content, "lxml")

print("*********" * 20)
print(soup.head)

print("*********" * 20)
print(soup.meta)

print("*********" * 20)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs) # dict格式
print(soup.link.attrs["type"])

# 更改link的属性attrs
soup.link.attrs["type"] = "hahahaha"
print(soup.link)