from urllib import request
import ssl

# 利用非认证上下文环境替换认证的上下文环境
ssl._create_default_https_context = ssl._create_unverified_context
# 此案例失败了,应该是12306已经申请了CA证书???
# 没有替换ssl的上下文环境也成功访问了...

url = "https://www.12306.cn/mormhweb"
rsp = request.urlopen(url)
html = rsp.read().decode()
print(html)