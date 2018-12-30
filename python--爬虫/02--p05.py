# cookie的保存
from urllib import request, parse
from http import cookiejar

# 创建filecookiejar的实例
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)
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

    # 保存到cookie文件
    # ignore_discard表示即使cookie将要被丢弃也要被保存下来
    # ignore_expires表示如果cookies已经过期也将它保存并且文件已存在时将覆盖
    cookie.save(ignore_discard=True, ignore_expires=True)

if __name__ == "__main__":
    login()
