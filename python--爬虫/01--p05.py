'''
URLError的使用
'''
from urllib import request, error

if __name__ == "__main__":
    url = "http://www.baiiiiiiiiiiiiiiiiidu.com"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))
    except Exception as e:
        print(e)

'''
URLError的子类HttpError的使用
'''
from urllib import request, error

if __name__ == "__main__":
    url = "http://blog.csdn.net/cqcrehhh"
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    # 先子类
    except error.HTTPError as e:
        print("HttpError: {0}".format(e.reason))
        print("HttpError: {0}".format(e))
    # 后父类
    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)