# for循环--01
# 列表就是一列数字或者其他值，一般用中括号表示
# e.g. ['A','B','C','D']

#打印学生列表姓名
for name in ['A','B','C','D']:
    print(name)

# for循环--02
#打印学生列表姓名
#如果是C，那是我的最爱
#如果是别的人，那就冷酷地拒绝他
for name in ['A','B','C','D']:
    print(name)
    if name=="C":
        print("我最爱的{0}出现了".format(name))
    else:
        print("同学我们不约，不约，同学请自重")

# range练习
# 打印1-10的数字
# 注意，一般在Python中，如果有表示数字范围的两个数，一般包含左边的数字而不包含右边的数字
# randint是特例，左右都包含
# range函数在Python2.x和Python3.x中有严重区别
for i in range(1,11):
    print(i)

# for-else语句
# 打印列表中的同学
# 如果没有在列表中，或者列表结束了，我们需要打印提示语句，表示不会再爱了

#打印学生列表姓名
#如果是C，那是我的最爱
#如果是别的人，那就冷酷地拒绝他
for name in ['A','B','C','D']:
    print(name)
    if name=="C":
        print("我最爱的{0}出现了".format(name))
    else:
        print("同学我们不约，不约，同学请自重")
else:
    print("不会再爱了")

# for循环之break
# 在1-10的数字中，寻找数字7，一旦找到，打印出来，其余则什么也不做
# for循环中的变量表示，一般用i，k，m，n，或者indx，idx，item之类
# 在Python中，如果循环变量名称不重要，可以用下划线（_）代替
for i in range(1,11):
    if i==7:
        print("我找到了")
        break
    else:
        print(i)

# for循环之continue
# continue语句练习（2B青年）
# 在1-10的数字中，寻找偶数，一旦找到，打印出来，其余则什么也不做

for i in range(1,11):
    if i%2==1:
        continue
    else:
        print("{0}是偶数".format(i))

# continue语句练习 版本2（正常青年）
# 在1-10的数字中，寻找偶数，一旦找到，打印出来，其余则什么也不做

for i in range(1,11):
    if i%2==0:
        print("{0}是偶数".format(i))

# continue语句练习 ban版本3（文艺青年）
# 在1-10的数字中，寻找偶数，一旦找到，打印出来，其余则什么也不做
# 如果i是奇数则执行continue，如果i是偶数则不执行continue，直接执行print
for i in range(1, 11):
    if i % 2 == 1:
        continue

    print("{0}是偶数".format(i))

# for循环之pass
# pass例子，一般用于站位
# 没有pass就报语法错误（只有一句for i in range(1,11):）
for i in range(1,11):
    pass
    print("我在这里")



# while循环--01
# 如果说年利率是6.7%，本利是每年翻滚，则多少年后本钱会翻倍
benqian=100000
year=0
while benqian<200000:
    benqian=benqian*(1+0.067)
    year+=1#year=year+1
    print("第{0}年拿了{1}块钱".format(year,benqian))

# while循环--02
# 如果说年利率是6.7%，本利是每年翻滚，则多少年后本钱会翻倍
# 如果拿到的钱翻倍，就用print庆祝一下
benqian=100000
year=0
while benqian<200000:
    benqian=benqian*(1+0.067)
    year+=1#year=year+1
    print("第{0}年拿了{1}块钱".format(year,benqian))
else:
    print("大爷的，终于翻倍了，10多年啊")

