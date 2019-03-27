'''
requests之两种请求方式
'''
import requests
# 1.get请求
url = "http://www.baidu.com"
rsp = requests.get(url)
print(rsp.text)
# 2.request请求
rsp = requests.request("get", url)
print(rsp.text)




'''
get请求的返回内容
使用参数headers,params
'''
import requests
# 完整url是下面url加上参数构成
url = "http://www.baidu.com/s?"
# 参数
kw = {
    "wd":"王八蛋"
}
headers = {
    "User-Agent":"Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
}
rsp = requests.get(url, params=kw, headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
# 请求的返回码
print(rsp.status_code)