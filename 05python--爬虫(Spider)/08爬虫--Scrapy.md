# Spider框架
- 常见爬虫框架
    - scrapy
    - pyspider
    - crawley
## Scrapy
- 参考资料:
    - [https://doc.scrapy.org/en/latest/]
    - [http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html]
- 安装: 
    - pip install scrapy
- scrapy概述
    - 包含部件如下:
        - 1.ScrapyEngine: 引擎,神经中枢,大脑核心
        - 2.Scheduler调度器: 引擎发来的request请求,调度器需要处理,然后向引擎报告
        - 3.Downloader下载器: 把引擎发来的request发出请求,得到response
        - 4.Spider爬虫: 负责把下载器得到的网页/结果(response)进行分解,分解成数据(items)+链接(request)(不够严谨)
            - 对应的是spiders文件夹下的py文件
            - spider函数及相关: 
                - __init__: 构造函数
                    - 初始化爬虫名称, status_urls列表
                - start_requests:
                    - 生成Requests对象交给Downloader下载并返回response
                - parse:
                    - 根据返回的response解析出相应的item,item自动进入itempipeline, 如果需要解析出url,url自动交给requests模块的,一直循环下去    
                - start_request(self):
                    - 此方法仅能被调用一次,请求start_urls内容并启动循环过程
                - name:
                    - 设置爬虫名称
                - start_urls:
                    - 设置开始第一批爬取的url
                - allow_domains:
                    - spider允许爬取的域名列表
                - log:
                    - 日志记录
        - 5.ItemPipeline管道: 详细处理Item
            - 爬虫提取出数据存入item后,item中保存的数据需要进行进一步处理,如清洗,去重,存储等
            - pipeline函数相关:
                - process_item(item,spider):
                    - spider提取处理来的item作为参数传入,同时传入的还有,spider
                    - 此方法必须实现
                    - 必须返回一个Item对象,被丢弃的item不会被之后的pipeline处理
                - __init__: 构造函数
                    - 进行一些必要的参数初始化
                - open_spider(spider):
                    - spider对象被开启的时候调用
                - close_spider(spider):
                    - spider对象被关闭的时候调用
        - 6.DownloaderMiddleware下载器中间件: 自定义下载的功能扩展组件
            - 中间件是处于引擎和下载器中间的一层组件
            - 可以有很多个，被按顺序加载执行
            - 作用是对发出的请求和返回的结果进行预处理
            - 在middlewares文件中
            - 需要在settings中设置以便生效
                - 设置settings的相关代码
                USER_AGENTS = [
                            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR
                            3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
                            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0;
                            SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET
                            CLR 1.1.4322)",
                            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR
                            2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko,
                            Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
                            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3)
                            Arora/0.6",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-
                            Ninja/2.1.1",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0
                            Kapiko/3.0",
                            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
                            ]           
   
                PROXIES = [
                        {'ip_port': '111.8.60.9:8123', 'user_passwd': 'user1:pass1'},
                        {'ip_port': '101.71.27.120:80', 'user_passwd': 'user2:pass2'},
                        {'ip_port': '122.96.59.104:80', 'user_passwd': 'user3:pass3'},
                        {'ip_port': '122.224.249.122:8088', 'user_passwd': 'user4:pass4'},
                        ]
            - 一般一个中间件完成一项功能
            - 必须实现以下一个或者多个方法
                - process_request(self, request, spider)
                    - 在request通过的时候被调用
                    - 必须返回None或Response或Request或raise IgnoreRequest其中之一
                    - None: scrapy将继续处理该request
                    - Request： scrapy会停止调用process_request并重新调度返回的reqeust
                    - Response： scrapy不会调用其他的process_request或者process_exception，直接将该response作为结果返回
                                同时会调用process_response函数
                - process_response(self, request, response,  spider)
                    - 跟process_request大同小异
                    - 每次返回结果的时候会自动调用
                    - 可以有多个，按顺序调用
                - 案例代码
                
                        import random
                        import base64
                        
                        # 从settings设置文件中导入值
                        from settings import USER_AGENTS
                        from settings import PROXIES
                        
                        #  随机的 User-Agent
                        class RandomUserAgent(object):
                            def process_request(self, request, spider):
                                useragent = random.choice(USER_AGENTS)
                                request.headers.setdefault("User-Agent", useragent)
                                
                        class RandomProxy(object):
                            def process_request(self, request, spider):
                                proxy = random.choice(PROXIES)
                                if proxy['user_passwd'] is None:
                                    #  没有代理账户验证的代理使用方式
                                    request.meta['proxy'] = "http://" + proxy['ip_port']
                                else:
                                    #  对账户密码进行 base64 编码转换
                                    base64_userpasswd = base64.b64encode(proxy['user_passwd'])
                                    #  对应到代理服务器的信令格式里
                                    request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
                                    request.meta['proxy'] = "http://" + proxy['ip_port']
                
        - 7.SpiderMiddleware爬虫中间件: 对Spider进行功能扩展

- Spider项目大致流程
    - 新建项目: scrapy startproject xxx
    - 明确需要目标/产出: 编写item.py
    - 制作爬虫: 路径:spider/xxspider.py
    - 存储内容: pipelines.py
    
### 去重
- 为了放置爬虫陷入死循环，需要去重
- 即在spider中的parse函数中，返回Request的时候加上dont_filter=False参数

        myspeder(scrapy.Spider):
            def parse(.....):
            
                ......
                
                yield  scrapy.Request(url=url, callback=self.parse, dont_filter=False)                
   
### 如何在scrapy使用selenium
- 可以放入中间件中的process_request函数中
- 在函数中调用selenium，完成爬取后返回Response

        calss MyMiddleWare(object):
            def process_request(.....):
                
                driver = webdriver.Chrome()
                html = driver.page_source
                driver.quit()
                
                return HtmlResponse(url=request.url, encoding='utf-8', body=html, request=request)

## scrapy-shell
- [https://segmentfault.com/a/1190000013199636?utm_source=tag-newest]
- shell 
- 启动
	- Linux： ctr+T,打开终端，然后输入scrapy shell "url:xxxx"
	- windows: scrapy shell "url:xxx"
	- 启动后自动下载指定url的网页
	- 下载完成后，url的内容保存在response的变量中，如果需要，我们需要调用response
- response
	- 爬取到的内容保存在response中
	- response.body是网页主体的代码
	- resposne.headers是返回的http的头信息
	- response.xpath（）允许使用xpath语法选择内容
	- response.css()允许使用css语法选区内容
- selector
	- 选择器，允许用户使用选择器来选择自己想要的内容
	- response.selector.xpath: response.xpath是selector.xpath的快捷方式
	- response.selector.css: response.css是他的快捷方式
	- selector.extract:把节点的内容用unicode形式返回
	- selector.re:允许用户通过正则选区内容
	
## 分布式爬虫
- 单机爬虫的问题：
    - 单机效率
    - IO吞吐量
- 多爬虫问题
    - 数据共享
    - 在空间上不同的多台机器，可以成为分布式
- 需要做：
    - 共享队列
    - 去重
- Redis
    - 内存数据库
    - 同时可以落地保存到硬盘
    - 可以去重
    - 可以把他理解成一个dict，set，list的集合体  
    - 可以对保存的内容进行生命周期控制 
    
- 内容保存数据库
    - MongoDB
    - Mysql等传统关系数据库
  
- 安装scrapy_redis
    - pip install scrapy_reids
    - [github.com/rolando/scrapy-redis]
    - 官方文档: [scrapy-redis.readthedocs.org]
    
## 推荐书籍
- <Python爬虫开发与项目实战>， 范传辉， 机械工业出版社
- <精通 python爬虫框架scrapy>, 李斌 翻译， 人民邮电出版社
- 崔庆才
