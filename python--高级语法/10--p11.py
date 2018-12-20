import json

data = {"name":"hahah", "age":12}
# with语句,打开不用关闭
# "w":写入方式打开,若没有文件会自动生成
# 文件别名为f
with open("t.json", 'w') as f:
    # 把python文件内容以json方式写入json文件f
    json.dump(data, f)

# 以只读方式打开json文件,起别名为m
with open("t.json", 'r') as m:
    # 将json文件以python方式载入
    d = json.load(m)
    print(d)