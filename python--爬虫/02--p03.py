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

def getHomePage():
    url = "http://www.renren.com/969284558/profile"
    # 如果已经执行了login函数,则opener已经自动包含了相应的cookie值
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("rsp3.html", "w", encoding="utf-8") as f:
        f.write(html)
if __name__ == "__main__":
    login()
    getHomePage()