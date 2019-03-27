# cookie和session
- 由于http协议的无记忆性(无状态性),人们为了弥补这个缺陷,所采取的的一个补充协议
- cookie发放给用户(即http浏览器)的一段信息,session是保存在服务器上的对应的另一半信息,用来记录用户信息
- session的存放位置:
    - 存放在服务器端
    - 一般情况,session是放在内存中或者数据库中
- 两者的区别
    - 存放位置不同
    - cookie不安全
    - session会保存在服务器上一定时间,会过期
    - 单个cookie保存数据不超过4k,很多浏览器限制一个站点最多保存20个
## cookie登陆
- 没有cookie登陆,反馈网页是未登录状态
    - 案例: 02--p01.py
- 使用cookie登陆
    - 直接复制登陆状态下的cookie,然后放入请求头
    - 案例: 02--p02.py
- http模块包含一些关于cookie的模块,可以实现自动使用cookie
    - CookieJar
        - 管理存储Cookie,向传出的http请求添加cookie
        - cookie存储在内存中,CookieJar实例回收之后,cookie消失
    - FileCookieJar(filename, delayload=None, policy=None)
        - 使用文件管理cookie
        - filename是保存cookie的文件名
    - MozillaCookieJar(filename, delayload=None, policy=None)
        - 创建与Mozilla浏览器的cookie.txt兼容的FileCookieJar实例
    - LwpCookieJar
        - 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookie实例
- 关系: CookieJar(父)-->FileCookieJar(子)-->MozillaCookieJar(孙子)-->LwpCookieJar(曾孙子)
## 利用CookieJar实现cookie登陆:
- 利用CookieJar访问人人网
    - 大致流程:
        - 打开登录页面后自动通过用户名密码登陆
        - 自动提取反馈回来的cookie
        - 利用反馈回来的cookie登陆隐私页面
        - 案例: 02--p03.py     
    - handler是Handler的实例
    - 用来处理复杂请求
        - e.g.
            
                # 创建cookie的管理器
                cookie_handle = request.HTTPCookieProcessor(cookie)
                # 创建http请求管理器
                http_handle = request.HTTPHandler()
                # 创建http管理器
                https_handle = request.HTTPSHandler()
            
    - 创建handler之后,使用opener打开,打开后相应的业务由相应的handler处理
### cookie的属性
 - 将cookie作为一个变量打印出来
 - 案例: 02--p04.py
 - cookie的常见属性: 
    - name: 名称
    - value: 值
    - domain: 可以访问此cookie的域名
    - path: 可以访问此cookie的页面路径
    - expires: 过期时间
    - size: 大小
    - Http字段
## cookie的保存-FileCookieJar
    - 案例: 02--p05.py
- cookie的读取
    - 案例: 02--p06.py