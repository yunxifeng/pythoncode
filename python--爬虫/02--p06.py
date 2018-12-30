# cookie的读取
from urllib import request, parse
from http import cookiejar

# 创建filecookiejar的实例
cookie = cookiejar.MozillaCookieJar()
# 读取cookie
cookie.load("cookie.txt", ignore_discard=True, ignore_expires=True)

# 创建cookie的管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handle = request.HTTPHandler()
# 创建http管理器
https_handle = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(cookie_handle, http_handle, https_handle)

def getHomePage():
    url = "http://www.renren.com/969284558/profile"
    # 如果已经执行了login函数,则opener已经自动包含了相应的cookie值
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("rsp4.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    getHomePage()
