# 将cookie打印出来
from urllib import request, parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 创建cookie的管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handle = request.HTTPHandler()
# 创建http管理器
https_handle = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(cookie_handle, http_handle, https_handle)

def login():
    '''
    负责初次登录
    需要输入用户密码来获取登陆的cookie凭证
    :return:
    '''
    url = "http://www.renren.com/PLogin.do"
    data = {
        "email":"17513238682",
        "password":"gao150398."
    }
    # 对数据进行编码
    data = parse.urlencode(data).encode("utf-8")
    # 创建请求对象
    req = request.Request(url, data=data)
    # 使用opener发起请求
    rsp = opener.open(req)


if __name__ == "__main__":
    '''
    执行完login()之后会得到授权之后的cookie
    尝试打印cookie
    '''
    login()
    # 此时的cookie是cookiejar的实例
    print(cookie)
    for item in cookie:
        # Cookie的实例类型
        print(type(item))
        print(item)
        # dir(): 获取cookie实例的属性列表
        # 二刷时记得查阅一下所有内置函数
        for i in dir(item):
            print(i)