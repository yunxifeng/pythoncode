'''
使用代理访问代理
'''
from urllib import request, error

if __name__ == "__main__":
    url = "https://study.163.com/course/courseLearn.htm?courseId=1004987028#/learn/video?lessonId=1052091395&courseId=1004987028"
    # 1.设置代理
    proxy = {"http":"144.255.14.161"}
    # 2.创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener
    opener = request.build_opener(proxy_handler)
    # 4.安装Opener
    request.install_opener(opener)

    # 使用代理访问url
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
