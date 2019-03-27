'''
访问一个网址
更改自己的UA进行伪装
'''
from urllib import request,error
if __name__ == "__main__":
    url = "http://www.baidu.com"
    try:
        # 1.使用Headers方法伪装
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3"
        rep = request.Request(url=url, headers=headers)
        # 正常访问
        rsp = request.urlopen(rep)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
    print("Done...........")


# 第二种方式
from urllib import request,error
if __name__ == "__main__":
    url = "http://www.baidu.com"
    try:
        # 2.使用add_header方法伪装
        rep = request.Request(url)
        rep.add_header("User-Agent", "Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3")

        # 正常访问
        rsp = request.urlopen(rep)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
    print("Done.....")