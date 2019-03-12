# Django系统
- 环境
   - Python3.6
   - Django1.8
- 参考资料:
   - [django中文教程](https://yiyibooks.cn/xx/django_182/index.html)
   - <Django架站的16堂课>
- 环境搭建
   - anaconda+pycharm
   - anaconda使用(windows下)
      - conda list: 显示当前环境安装的包
      - conda env list: 显示安装的虚拟环境列表 
      - conda create -n env_name python=3.6: 创建环境
      - conda env remove -n env_name: 删除环境  
      - activate env_name: 激活环境
      - pip install django==1.8: 安装django1.8版本
        - 注: 因网络原因安装失败时,尝试换源
            - pip install -i https://pypi.douban.com/simple django==1.8
   - 注: django1.x和django2.0差别巨大
## 服务器端的流程
- 自行查阅
## 创建第一个django程序
- django-admin startproject project_name: 创建django项目
- 项目文件结构
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
- 外层的 mysite/ 根目录是项目的容器。这个目录的名称对 Django 没有什么作用，你可以根据喜好重命名.
- manage.py 是一个命令行实用脚本，可以通过不同的方式与 Django 项目交互。
- 内部的 mysite/ 目录是项目的 Python 包。导入这里面的内容时要使用目录的名称（如
  mysite.urls）。
- mysite/init.py 是一个空文件，目的是让 Python 把这个目录识别为 Python 包。
- mysite/settings.py 是 Django 项目的设置/配置。
  - 默认情况下，INSTALLED_APPS 包含下述应用
    • django.contrib.admin：管理后台
    • django.contrib.auth：身份验证系统
    • django.contrib.contenttypes：内容类型框架
    • django.contrib.sessions：会话框架
    • django.contrib.messages：消息框架
    • django.contrib.staticfiles：管理静态文件的框架
- mysite/urls.py 是 Django 项目的 URL 声明，即 Django 驱动的网站的“目录”。
- mysite/wsgi.py 是兼容 WSGI 的 Web 服务器的入口点，用于伺服项目.

- 启动django
   - 1.命令行下:python manage.py runserver(在django项目目录下)
   - 2.pycharm下:配置manage.py的参数Parameters为runserver,运行manage.py
   注: 1."GET / HTTP/1.1" 200 1767:  1767:文件长度
       2.db.sqlite3: django自带数据库,可直接用于调试,
         实际使用时在settings更改配置即可切换到实际应用中的数据库
- 测试django
   - 浏览器下:http://127.0.0.1:8000
## 路由系统-urls
- 创建app
   - app: 负责一个具体业务或者一类具体业务的模块
   - python manage.py startapp teacher
- 路由
   - 按照具体的请求url,导入到相应的业务处理模块的一个功能模块
   - django的信息控制中枢
   - 本质上是接受的url和相应的处理模块的一个映射
   - 在接受URL的请求匹配上使用了RE,具体格式见urls.py中所示
- 需要关注两点:
   - 1.接受的URL是什么,即如何使用RE对传入的URL进行匹配
   - 2.接收到的URL应该匹配到哪个处理模块
- url匹配规则:
   - 从上往下逐一进行比对
   - url格式是分级格式,按照级别一级一级往下对比,主要对应url包含子url的情况
   - 子url一旦被调用,则不会返回到主url
      - `/one/two/three/`
   - 正则以r开头,表示不需要转义,注意尖号(^)和美元符号($)
      - `/one/two/three` 配对 r'^one/'
      - `/oo/one/two/three` 不配对 r'^one/'
      - `/one/two/three/` 配对 r'three/$'
      - `/oo/one/two/three/oo/` 不配对 r'three/$' 
      - 正则开头的`/`省略
   - 如果从上到下都没有找到合适的匹配内容,则报错
### 映射
- 1.正常映射       
    - 把某一个符合RE的URL映射到事务处理函数中
    - e.g.
        from showeast import views as sv
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^normalmap/', sv.normalmap)
        ]
- 2.URL中带参数映射
    - 在事件处理代码中需要URL传入参数,形如 /myurl/param中的param
    - 参数都是字符串形式,如果需要整数等形式需要自行转换
    - e.g.
        /search/page/432 中的432需要经常性变换,所以设置成参数比较合适
### URL在app中处理
- 如果所有应用URL都集中在主路由中,可能导致文件的臃肿
- 可以把urls具体功能逐渐分散到每个app中
    - 从django.conf.urls导入include
    - 注意此时RE的写法
    - include(子路由文件名)
- 使用方法:
    - 确保include被导入
    - 写主路由的开头
    - 写子路由
    - 编写views函数
- e.g.
    - url(r'^teacher/', include(teacherurls)),
- 同样可以使用参数
### URL中的嵌套参数
- 捕获某个参数的一部分
- e.g. 例如URL /index/page-3, 需要捕获数字3作为参数
    - url(r'index/(page-(\d+)/)?$', sv.myindex), #不太好
    - url(r'index/(?:page-(?P<page_number>\d+)/)?$', sv.myindex), #好
    - ?:表示忽略此参数
### 传递额外参数
- 参数不仅仅来自于URL,还可能是我们自己定义的内容(字典格式)
- e.g.
   - 注: 'name'必须与views内一致
   url(r'extrem/$', sv.extremParam, {'name':'yunxifeng'}),
- 附加参数同样适用于include语句
### URL的反向解析
- 防止硬编码
- 本质上是对每一个URL进行命名
- 以后再编码代码中使用的URL的值,原则上都应该使用反向解析

----------------------------------------------------
补充内容:
- from django.conf.urls import include, url
  解析: 两个函数：include，用于导入另一个 URL 配置模块；url，使用正则表达式模式匹配浏览器中的 URL，
        把它映射到 Django 项目中的某个模块上。
- from django.contrib import admin
  解析:  admin 函数传给 include 函数，加载 Django 管理后台的 URL。
- urlpatterns[]
  解析:  url() 实例列表. 要注意的是 urlpatterns 变量，Django 期望 URL 配置模块中有这个变量。它负责定义 URL 与处理
         URL 的代码之间的映射。
         
如果有人请求 /hello[注: 这里正确写法是/hello/] URL（末尾没有斜线）会发生什么。因为我们指定的 URL 模式要求有
末尾的斜线，因此那个 URL 不匹配。然而，默认情况下，如果请求的 URL 不匹配任何 URL 模式，而且末尾
没有斜线，那么 Django 会把它重定向到末尾带斜线的 URL。（这个行为由 Django 的 APPEND_SLASH 设置管理)

关于这个 URL 配置，还有一件事要注意：我们以对象的形式传入 hello 视图函数，而没有调用函数。这是
Python（以及其他动态语言）的一个关键特性：函数是一等对象，可以像其他变量那样传递。

为网站根地址实现视图时，使用的 URL 模式是 ˆ$，即匹配空字符串。
urlpatterns = [url(r'^$', my_homepage_view),]

- django处理请求的流程: 
1. 请求 /hello/。
2. Django 查看 ROOT_URLCONF 设置，找到根 URL 配置。
3. Django 比较 URL 配置中的各个 URL 模式，找到与 /hello/ 匹配的那个。
4. 如果找到匹配的模式，调用对应的视图函数。
5. 视图函数返回一个 HttpResponse 对象。
6. Django 把 HttpResponse 对象转换成正确的 HTTP 响应，得到网页。

把通配数据传给视图函数，以便在一个视图函数中处理任意的偏移
量。为此，我们在 URL 模式中放一对圆括号，把想保存的数据括起来。
url(r'^time/plus/(\d{1,2})/$', hours_ahead), # 使用圆括号从匹配的文本中捕获数据
- 127.0.0.1/time/plus/0-99任意数字
