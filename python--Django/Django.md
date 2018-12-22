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
   - 注: django1.x和django2.0差别巨大
## 服务器端的流程
- 自行查阅
## 创建第一个django程序
- django-admin startproject project_name: 创建django项目
   - manage.py: 命令行(或参数)处理
   - settings.py: 配置文件
   - urls.py: 与路由相关
   - wsgi.py: 通用网关
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
### 正常映射       
- 把某一个符合RE的URL映射到事务处理函数中
   - e.g.
   from showeast import views as sv
   urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^normalmap/', sv.normalmap)
   ]