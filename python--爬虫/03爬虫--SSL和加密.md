# SSL(Secure Sockets Layer 安全套接层)
- SSL证书就是指遵守SSL安全套阶层协议的服务器数字证书
- 美国网景公司开发
- CA(CA, Certificate Authority 证书颁发机构)
   - 数字证书认证中心,是发放,管理,废除数字证书的收信人的第三方机构
- 遇到不信任的SSL证书,需要单独处理
   - 案例: 03--p01.py
# js加密
- 有的反爬虫策略采用js对需要传输的数据进行加密处理(通常是取md5值)
- 经过加密,传输的就是密文,但是加密函数或者加密过程一定是在浏览器端(Client)完成,
  那么一定会把代码(js代码)暴露给使用者,通过阅读加密算法,从而达到破解的目的 
- 案例: 03--p02.py
- 获取js加密算法代码
  - 以有道翻译为例
     - fanyi.min.js-->复制Response内容-->在线代码格式化-->得到js代码
     - 在js代码中搜索salt, 获得salt的算法: -->获得salt = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
     - 在js代码中搜索sign, 获得sign的算法: -->sign = n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")
        - e是输入的key值
        - i是salt
     - 通过Python代码实现上述算法,然后替换data对应的salt,sign