# Ajax
  - 异步请求
  - 一定会有url,请求方法,可能会有数据
  - 一般使用json格式
  - 案例: 04--p01.py
    - 爬取豆瓣电影数据
    - 排行榜单可以一直下拉,猜测可能使用了Ajax异步请求 
    - 获取url: https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20
        - 大致解读一下: limit=20-->本次下拉加载20个,最好不要改,可能会报错
                        start=40-->本次下拉从第40部影片开始加载
                        interval_id=100%3A90-->被加载影片的限制条件(区间),此处就是好评区间
# Requests模块-献给人类
- HTTP for Humans, 更简洁,更友好
- 继承了urllib的所有特征
- 底层使用的urllib3
- 开源地址： https://github.com/requests/requests
- 中文文档： http://docs.python-requests.org/zh_CN/latest/index.html   
- 安装： conda install requests
## 使用requests模块
- get请求
    - 两种方式:
        - 方式1: requests.get(url)
        - 方式2: requests.request("get", url)
               - request(method, url, **kwargs) # 官方
               - 可以带有headers和params参数
        - 案例: 04--p02.py
    -get请求的返回内容:
        - 案例: 04--p02.py
- post请求
    - rsp = requests.post(url, data=data)    
        - 案例: 04--p03.py  
- proxy代理
    - 基本用法:
        
            proxies = { 
                "http" : "address of proxy",
                "http" : "address of proxy"
            } 
            
            rsp = requests.request("get/post", url = "http:xxxx", proxies = proxies)
            
    - 代理有可能报错,如果使用人多,考虑安全问题,可能会被强行关闭
    
- 用户验证
    - 代理验证
    
            # 可能需要使用HTTP basic Auth
            # 格式: 用户名:密码@代理地址:端口地址
            proxy = {"http": "云汐风:123456@192.168.1.123:4444"}
            rsp = requests.get(url="http://www.baidu.com", proxies=proxy)
            
    - web客户端验证
            
            # 如果遇到web客户端验证,需要添加 auth=("用户名", "密码")
            # 授权信息
            auth = ("云汐风", "123456")
            rsp = requests.get(url="http://www.baidu.com", auth=auth)
- cookie
    - requests可以自动处理cookie信息
        
            rsp = requests.get(url="http://xxxxx")   
            # 返回一个cookiejar实例
            cookiejar = rsp.cookies
            # 将cookiejar转化为字典
            cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
- session 
    - 跟前面讲的服务器端的session是不一样的概念
    - 模拟一个会话,从客户端浏览器连接到服务器端开始,到客户端与服务端断开为止
    - 可以让我们跨请求保持某些参数,比如在同一个session实例发出的所有请求之间保持cookie
    
            # 创建session实例,可以保持cookie值
            ss = requests.session()
            headers = {"User-Agent":"xxxxxxxxxxx"}
            data = {"name":"云汐风"}
            # 此时,由创建的session管理请求,负责发出请求
            ss.post(url="http://www.baidu.com", headers=headers, data=data)
            
            # 下面我们继续发出请求时,无需再输入一些参数信息,session实例帮我们保持着某些参数,即cookie
            ss.get(url="http;//xxxxx")
            
    - 所以,一般来说,一个网站一个session就够了 
       
- https请求验证ssl证书
    - 参数:
        - verify: 负责表示是否需要验证ss证书,默认是True  
        - 如果不需要验证,则设置成False表示关闭
        
              rsp = requests.get("https://www.baidu.com", verify=False) 


    