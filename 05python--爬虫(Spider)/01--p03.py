# urlopen的返回值
from urllib import request

if __name__ == "__main__":
    url = "https://study.163.com/course/courseLearn.htm?courseId=1004987028#/learn/video?lessonId=1052092284&courseId=1004987028"
    rsp = request.urlopen(url)
    # HttpResponse类型
    print(type(rsp))
    # 内容是HttpResponse的一个实例
    print(rsp)

    print("URL: {0}".format(rsp.geturl()))
    print("INFO: {0}".format(rsp.info()))
    print("CODE: {0}".format(rsp.getcode()))

# get方式
'''
掌握对url进行参数编码的方法
需要使用urllib.parse
'''
from urllib import request,parse

if __name__ == "__main__":
    url = "http://www.baidu.com/s?"
    wd = input("Input your keyword:")
    # 要使用data, 需使用dict结构
    qs ={
        "wd":wd
    }
    # 给参数编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()
    print(html)


