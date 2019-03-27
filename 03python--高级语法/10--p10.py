# 导入json包
import json

# 此时student是一个dict格式内容，不是json
student={
    "name": "luidana",
    "age": 18,
    "mobile":"15578875040"
}

print(type(student))
# 把python格式转换为json文件
stu_json = json.dumps(student)
print(type(stu_json))
print("JSON对象:{0}".format(stu_json))
# 把json格式转化为python格式
stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)