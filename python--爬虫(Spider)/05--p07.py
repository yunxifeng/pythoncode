'''
beautifulsoup4
'''
from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()

# 创建bs实例
soup = BeautifulSoup(content, "lxml")

# bs自动转码
content = soup.prettify()
print(content)
