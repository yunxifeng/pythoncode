# 1.分支
# if语句练习01
# 如果age小于18岁，则打印信息“去叫家长”
age=17
if age<18:
    print("去叫家长吧，孩子")
    print("我们不带你玩")
    print("滚球的")

# if语句练习02
# 如果age小于18岁，则打印信息“去叫家长”
age=19
if age<18:
    print("去叫家长吧，孩子")
    print("我们不带你玩")
    print("滚球的")

print("开始上车喽，老司机们")

# if语句练习03
print("今天学习for循环")
gender = "男"
if gender == "女":
    print("来，叔叔给你糖吃")

print("今天开始讲for循环了")

# 2.双向分支01
# input作用
# 1.在屏幕上输出括号内的字符串
# 2.接受用户输入的内容并返回到程序
# 3.input返回的内容一定是字符串类型
gender = input("请输入性别：")
# 复习字符串的格式化format方法
print("你输入的性别是：{0}".format(gender))
if gender == "男":
    print("来，让我们纪念一下今天吧，代码敲十遍")
else:
    print("发糖喽发糖喽")
    print("你是女生，特殊照顾喽")

print("开始上课喽")

# 2.双向分支02
#考试成绩判断
#90以上：输出优A
#80-90：输出良B
#70-80：输出中C
#60-70：输出差D
#60以下：输出我没你这个学生
score=input("请输入学生成绩：")
#需要把str转换为int
score=int(score)
if score>=90:
    print("A")
if score>=80 and score<90:
    print("B")
if score>=70 and score<80:
    print("C")
if score>=60 and score<70:
    print("D")
if score<60:
    print("我没你这个学生")
#可以与break，continue，return结合使用以达到多路分支的目的

# 3.多路分支
#考试成绩判断
#90以上：输出优A
#80-90：输出良B
#70-80：输出中C
#60-70：输出差D
#60以下：输出我没你这个学生
score=input("请输入学生成绩：")
#需要把str转换为int
score=int(score)
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("我没你这个学生")