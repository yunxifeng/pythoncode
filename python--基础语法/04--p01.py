# 变量类型--String
love="我爱Python"
print(love)
#单双引号交错使用的例子
#<a style="color:red">哈哈哈</a>
#用引号表示上面的字符串
html='<a style="color:red";>哈哈哈</a>'

htmls='''
我爱
Python
'''
print(htmls)


# 字符串(String)---转义字符
#如果想表示出Let's go
#1.可以使用嵌套引号，即外层使用双引号
#2.转义字符
s="Let's go"
print(s)

#\' == '
ss='let\'s go'
print(ss)

#\\ == \
sss="c:\\user"
print(sss)

#回车换行符\r\n
s1="I love \r\n Python"
print(s1)

# 字符串(String)---格式化---%
s="I love %s"
#直接把%s作为字符串的一个内容打印出来了
print(s)
print("I love %s"%"Python")
print(s%"Python")

s="I am %d years old"
#注意下面两句话的区别和结果
print(s)
print(s%18)

s="I am %s,I am %d years old"
print(s)
#注意以下表达的出错原因
#如果字符串中有占位符，则有几个占位符就必须要用几个实际内容代替，或者一个也不要
#print(s%"DeathMadao")
print(s%("DeathMadao",21))

# 字符串(String)---格式化---format
s="I love {}".format("Python")
print(s)
s="I am {1} years old,I love {0} and I am {1} years old.".format("Python",21)
print(s)

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本， 并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))