# 1.算术运算符
#+ ， - ， × ， /
#在Python2.x和Python3.x中，除号（/）结果可能不一致，此处以3.X系列为准
# 2.x只取整
a=(1-2+3)*4/5
print(a)

# % 取余运算
#两数字相除有商有余
# % 只取得余数
a=9%4
print(a)

# // 取商运算，也叫地板除
a=9//4
print(a)

# ** 表示幂运算
a=9**4
print(a)

# 2.比较运算符
# ==，等于号
#1.计算a==80
#2.把结果放入b中
a=3**4
b=a==80
print(b)

# ！=，不等于
print(9!=8)

# < , > , <= ,>=

# 3.赋值运算符
# =，赋值
a=0
c=a=1

# +=,缩写
a=0
a+=7#a=a+7

#所有数学运算符都有缩写形式
#-= ，×= ，/= , //= , %= , **=,都是缩写形式

# 4.逻辑运算符
a=True
b=False
c=True
#以下式子等价于d=1*0+1
d=a and b or c
print(d)

d=a or b and a
print(d)

#逻辑运算中的短路案例

#下面的逻辑表达式，a的值一定是True,则运算到or的时候，整个表达式不会再向下计算
#下面表达式，如果xxxx中包含赋值表达式，则结果很难预期
# a=True or xxxxxxx

#代码示例（伪代码）
b=0
# a=a or (b=9) and 6
#假定上述表达式没有语法错误（先运算（b=9），实际运行到or时后面就被短路了）
#则b的值应该是0而不是9
print(b)
print(a)

# 5.成员运算符
l=[1,2,3,4,5]
a=7

b=a in l
print (b)

a=4
print(a in l)

print(a not in l)

# 身份运算符
a=9
b=9
print(a is b)

a="I love Python."
b="I love Python."
print(a is b)


l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2)

