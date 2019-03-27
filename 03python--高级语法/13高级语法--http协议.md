# http协议
- 参考资料:
  - [https://www.jianshu.com/p/80e25cb1d81a]
- 超文本(HyperText)
  - 包含有超链接(Link)和各种多媒体标记(Markup)文本.这些超文本文件彼此链接,形成网状(Web),
    因此又被称为网页(Web Page).这些超链接使用URL表示.最常见的超文本格式是超文本标记语言
    HTML.  
- URL(Uniform Resource Locator)
  - URL即统一资源定位符,用来唯一的标识万维网中的某一个文档.URL由协议,主机和端口(默认为80),
    文件名三部分构成.
  - e.g. http(协议)://www.sxtyu.com:80(主机+端口(80))/news/index.html(文件名及路径)
         ftp(协议)://rtfm.mit.edu/pub/abc.txt 
- HTTP(HyperText Transfer Protocol)
  - 超文本传输协议,是一种按照URL指示,将超文本文档从一台主机(Web服务器)传输到另一台主机(浏览器)
    的应用层协议,以实现超链接的功能. 
  - 工作原理:
     - 请求/响应模型
     - 连接方式
        - 持久性连接: 即在一个连接中,可以进行多次文档的请求和响应.服务器在发送完响应后,并不立即
              释放连接,浏览器可以使用该连接继续请求其他文档.连接的保持时间可以由双方进行协商.
        - 非持久性连接:即浏览器每请求一个Web文档,就创建一个新的连接,当文档传输完毕后,连接就立刻
              被释放. >HTTP1.0和HTTP0.9采用此连接方式. 对于请求的Web页中包含多个其他文档对象(如
              图像,声音,视频等)的连接情况,由于请求的每个链接对应的文档都要创建新连接,效率低下. 
     - 无状态性: 是指同一个客户端(浏览器)第二次访问同一个Web服务器上的页面时,服务器无法知道这个
           服务器曾经访问过.HTTP的无状态性简化了服务器的设计,使其更容易支持大量并发的HTTP
           请求.
  - HTTP报文结构
     - 请求报文
        - 即从客户端(浏览器)向Web服务器发送的请求报文.报文的所有字段都是ASCII码
        - 三部分组成:
           - 请求行(方法 URL 版本 CRLF), 如 GET www.baidu.com HTTP/1.1
           - 首部行(首部字段名: 值  CRLF)*n
                   (CRLF: 首部行和实体主体之间空一行,作为结束标志)
               - 用来说明浏览器,服务器或者报文主体的一些信息.
               - 如: Host: www.sxtyu.com
                     Connection: close
                     User-Agent: Mozilla/5.0
                     Accept-Language: cn
                     
           - 实体主体(Entity body)
     - 返回(响应)报文
        - 即从Web服务器到客户机(浏览器)的应答,报文的所有字段都是ASCII码
        - 三部分组成:
           - 状态行(版本 状态码 短语 CRLF): 如 HTTP/1.1 200 OK
           - 首部行(首部字段名: 值 CRLF)*n
                   (CRLF: 首部行和实体主体之间空一行,作为结束标志)
               - 用来说明浏览器,服务器或者报文主体的一些信息
               - 如: Data: Web,08 May 2008 22
                     Server: Apache/1.3.2(Unix)
                     Content-Length: DateDaDat4096
                     Content-Type: text/html
                     
           - 实体主体(Entity body)                  
     - 请求报文中的方法
        - 方法(Method)是对所请求对象所进行的操作,也就是一些命令.
        - 常见方法:  
           - GET: 请求读取一个Web页面
           - POST: 附加一个命名资源(如Web页面)
           - DELETE: 删除Web页面
           - CONNECT: 用于代理服务器
           - HEAD: 请求读取一个Web页面的首部
           - PUT: 请求存储一个Web页面
           - TRACE: 用于测试,要求服务器送回收到的请求
           - OPTION: 查询特定选项
     - 响应报文中的状态码
        - 状态码(Status-Code)是响应报文状态行中包含的一个三位数字,指明特定的请求是否被满足.
          如果没有被满足,原因是什么.
        - 分为以下五类:
           状态码       含义        例子
           1xx          通知信息    100=服务器正在处理客户请求
           2xx          成功        200=请求成功(仅表明对方收到请求)
           3xx          重定向      301=页面改变了位置
           4xx          客户错误    403=禁止的页面;404=页面未找到 
           5xx          服务器错误  500=服务器内部错误;503=以后再试
        - 具体各状态码的含义,请参考W3C的HTTP1.1标准规范RFC2616
        - [http;//www.w3.org/Protocols/rfc2616/rfc2616.html]
        - [http://tools.jb51.net/table/http_status_code]
     - 首部字段或消息头
        - [https://blog.csdn.net/ggghub/article/details/50318881]
        - [http://www.cnblogs.com/ys-ys/p/5792572.html]
        - [https://www.jianshu.com/p/47e1ca7b1948]
        - HTTP一共有四种类型的首部字段.
          - 通用首部字段：请求报文和响应报文两方都会使用的首部。
          - 请求首部字段：从客户端向服务器发送请求报文时使用的首部。
          - 响应首部字段：从服务器向客户端返回响应报文时使用的首部。
          - 实体首部字段：针对请求报文和响应报文的实体部分使用的首部。
        - 通用首部字段
                首部字段名	        说明
                Cache	            控制缓存的行为
                Connection	        逐跳首部、连接的管理
                Date	            创建报文的日期时间
                Pragma	            报文指令
                Trailer	            报文末端的首部一览
                Transfer-Encoding	指定报文主体的传输编码方式
                Upgrade	            升级为其他协议
                Via	                代理服务器的相关信息
                Warning	            错误通知
        - 请求首部字段
                首部字段名	        说明
                Accept	            用户代理(客户)可处理的媒体类型,如text/html
                Accept-Charset	    优先的字符集.客户可接受的字符集,如Unicode-1-1
                Accept-Encoding	    优先的内容编码,客户能处理的页面编码方法,如gzip
                Accept-Language	    优先的语言（自然语言）,客户能处理的自然语言,如zh-cn,en
                Authorization	    Web认证信息,客户的信息凭据列表
                Cookie              服务器接收到的Cookie信息.将以前设置的Cookie送回服务器,可用来作为会话信息
                Expect	            期待服务器的特定行为
                From	            用户的电子邮箱地址
                Host	            请求资源所在服务器,服务器的DNS名称,从URL中提取出来,必需
                if-Match	        比较实体标记（ETag）
                if-Modified-Since	比较资源的更新时间
                if-None-Match	    比较实体标记（与if-Match相反）
                if-Range	        资源未更新时发送实体Byte的范围请求
                if-Unmodified-Since	比较资源的更新时间（与if-Modified-Since相反）
                Max-Forwards	    最大传输逐跳数
                Proxy-Authorization	代理服务器要求客户端的认证信息
                Range	            实体的字节范围请求
                Referer	            对请求中URI的原始获取方法
                TE	                传输编码的优先级
                User-Agent	        HTTP客户端程序(浏览器)的信息,如Mozilla5.0
        - 响应首部字段
                首部字段名	        说明
                Accept-Ranges	    是否接受字节范围请求
                Age	                推算资源创建经过时间
                Content-Encoding    内容是如何被编码的,如gzip
                Content-Language    页面所使用的自然语言
                Content-Length      以字节计算的页面长度
                Content-Type        页面的MIME类型
                ETag	            资源的匹配信息
                Last-Modified       页面最后被修改的时间和日期,在页面缓存机制中意义重大
                Location	        令客户端重定向至指定的URI
                Proxy-Authenticate	代理服务器对客户端的认证信息
                Reter-After	        对再次发起请求的时机要求
                Server	            HTTP服务器的安装信息,如Microsoft-IIS/6.0
                Set-Cookie          服务器希望客户保存一个Cookie
                Vary	            代理服务器缓存的管理信息
                WWW-Authenticate	服务器对客户端的认证信息
        - 实体首部字段
                首部字段名	        说明
                Allow	            资源可支持的HTTP方法
                Content-Encoding	实体主体的适用的编码方式
                Content-Language	实体主体的自然语言
                Content-Length	    实体主体的大小（单位：字节）
                Content-Location	替代对应资源的URI
                Content-MD5	        实体主体的报文摘要
                Content-Range	    实体主体的位置范围
                Content-Type	    实体主体的媒体类型
                Expires	            实体主体过期的日期时间
                Last-Modified	    资源的最后修改日期时间
     - 报文结构实例
# http代理
- HTTP代理又称为Web缓存或代理服务器(Proxy Server)是一种网络实体,能代表浏览器发出HTTP请求,并将最近的一些请求
  和响应暂存在本地磁盘中,当请求的Web页面先前暂存过,则直接将暂存的页面发给客户端(浏览器),无需再次访问Internet.
- 习题课--实战
     