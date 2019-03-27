# post方式
'''
利用parse模块模拟post请求
分析百度翻译
步骤:
1.F12
2.输入单词girl, 发现每敲一个字母,都有一个请求
3.请求地址: http://fanyi.baidu.com/sug
4.NetWork->All->Headers,发现FromData的值是kw: girl
5.检查返回内容格式,发现返回的是json格式的内容-->需要使用json包
'''
from urllib import request, parse
import json
'''
大致流程:
1.利用data构造内容,然后urlopen打开
2.返回一个json格式的结果
3.结果就应该是girl的释义
'''
# 基础url
base_url = "https://fanyi.baidu.com/sug"

# 改造data
value = input("请输入要查询的单词:")
# 存放用来模拟form的数据, dict格式
data = {
    # girl是翻译输入的英文内容,应该是由用户输入,此处使用硬编码
    "kw":value
}

# 需要使用parse模块对data进行编码,
# 返回Str格式,需要转换成bytes格式,才能发出
# data = parse.urlencode(data)
data = parse.urlencode(data).encode("utf-8")

# 需要构造一个请求头,至少包括传入数据的长度
# request要求传入的请求头必须是dict格式
headers = {
    # 因为使用post,至少应该包括Context-Length字段
    "Content-Length":len(data)
}

# 有了url, data, headers, 就可以发出请求了
# 返回HttpResponse
# urlopen不允许放入headers, 也就是说满足不了我们的需求
# 下面换一种方法, 将所有信息放入类实例中
rsp = request.urlopen(base_url, data=data)

json_data = rsp.read().decode("utf-8")
print(type(json_data))
print(json_data)
# 这个案例运行失败,显示errno:1, 操作不被允许,权限不够,暂未解决

# 把json字符串格式转化为字典格式
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data["data"]:
    print(item["k"],"---",item["v"])



# 此案例与上述案例一样,只是做出了改进,使用request.Resquest类来实现,代替urlopen
from urllib import request, parse
import json

base_url = "http://fanyi.baidu.com/sug"

value = input("请输入要查询的单词:")
data = {
    "kw":value
}
data = parse.urlencode(data).encode("utf-8")

headers = {
    "Content-Length":len(data)
}
# 构造一个Request类的实例, 则所有请求信息都可以放在Request这个实例中
req = request.Request(url=base_url, data=data, headers=headers)
# 不影响urlopen函数的使用
rsp = request.urlopen(req)

json_data = rsp.read().decode("utf-8")
print(type(json_data))

json_data = json_data.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data["data"]:
    print(item["k"],"---",item["v"])