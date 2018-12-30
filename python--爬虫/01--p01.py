'''
使用urllib.request请求一个网页内容,并把内容打印出来
'''
from urllib import request



# 1.请求打开url
# 2.读取页面
# 3.解码

if __name__ == "__main__":
    url = "https://study.163.com/course/courseLearn.htm?courseId=1004987028#/learn/video?lessonId=1052092284&courseId=1004987028"
    # request.urlopen(url):请求打开url, 返回相应页面(HttpResponse)
    rsp = request.urlopen(url)
    # 读取相应页面, 内容类型是bytes
    # 转换为字符串, 需要解码
    html = rsp.read()
    print(type(html))
    # html.decode()负责解码
    html = html.decode("utf-8")
    print(html)