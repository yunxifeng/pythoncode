'''
requests---post案例
'''
import requests
import json

base_url = "http://fanyi.baidu.com/sug"

value = input("请输入要查询的单词:")
data = {
    "kw":value
}
headers = {
    # 因为使用post,至少应该包括Context-Length字段
    "Content-Length":str(len(data))
}

rsp = requests.post(url=base_url, data=data, headers=headers)

print(rsp.text)
print(rsp.json())

# 暂不知失败原因,老师的代码也不行

