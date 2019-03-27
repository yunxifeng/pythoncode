from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()

# 创建bs实例
soup = BeautifulSoup(content, "lxml")
# prettify(): 让<html>页面更友好的显示
print(soup.prettify())

print("====" * 20)
titles = soup.select("title")
print(titles[0])

print("====" * 20)
metas = soup.select("meta[content='always']")
print(metas[0])
