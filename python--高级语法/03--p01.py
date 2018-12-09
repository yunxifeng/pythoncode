#calendar的使用
import calendar
cal = calendar.calendar(2018 , l = 0 , c = 5)
#说明cal是字符串类型
print(type(cal))
print(cal)
#isleap函数:判断某一年是否是闰年
print(calendar.isleap(2018))
#leapdays函数:判断指定年份之间的闰年个数
#当y1>y2时,输出-1
#一般情况下,0代表执行成功,1代表成功的各种情况,负数代表某种错误
print(calendar.leapdays(2000,2008))
#查看函数解释
help(calendar.leapdays)
#month函数
print(calendar.month(2018,12))
#monthrange函数
print(calendar.monthrange(2018,12))
#monthcalendar函数
m = calendar.monthcalendar(2018,12)
print(type(m))
print(m)
#prcal函数
calendar.prcal(2018)
#prmonth函数
calendar.prmonth(2018,12)
#weekday函数
print(calendar.weekday(2018,12,8))

print("*" * 20)
#time模块
import time
#timezone:东八区和UTC差-28800秒
print(time.timezone)
#altzone
print(time.altzone)
#daylight
print(time.daylight)
#time()
print(time.time())
#localtime()
t = time.localtime()
print(type(t))
print(t)
print(t.tm_hour)
#asctime(时间元组)
print(time.asctime(t))
#mktime(时间元组)
print(type(time.mktime(t)))
print(time.mktime(t))
#ctime()
t = time.ctime()
print(type(t))
print(t)
#sleep
for i in range(10):
    print(i)
    time.sleep(0.1)

print("*" * 20)
#clock
t0 = time.clock()
time.sleep(0.5)
t1 = time.clock()
print(t1-t0)
#strftime
#把时间表示成 2018年12月8日15:20
'''
t = time.localtime()
#下面代码因为含有中文会报错
#ft = time.strftime("%Y年%m月%d日 %H:%M" , t)
#下面代码依旧报错...
ft = time.strftime("%Y{y}%m{m}%d{d} %H:%M".format(y="年",m="月",d="日") , t)
print(ft)
'''
print("*" * 20)
#datetime模块
import datetime
#date
dt = datetime.date(2018,12,8)
print(dt)
print(type(dt))
print(dt.year)
print(dt.month)
print(dt.day)

#datetime:datetime模块下的一个模块
from datetime import datetime
dt = datetime(2018,12,8)
print(dt.today())
print(dt.now())
print(dt.fromtimestamp(time.time()))

#timedelta
from datetime import  datetime,timedelta
t1 = datetime.now()
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
#td表示一小时的时间长度
td = timedelta(hours=1)
#当间加上时间间隔td后,把得到的一个小时后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))

print("*" * 20)
#测量程序运行时间间隔实验
def P():
    time.sleep(2)
t1 = time.time()
P()
print(time.time()-t1)

#生成列表两种方法的比较
#如果单纯比较生成一个列表的时间,可能很难实现
import timeit
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''
#利用timeit调用代码,执行100000,查看运行时间
#第一种是通过列表生成式生成列表,stmt后面就是列表生成式的代码,number是执行次数
t1 = timeit.timeit(stmt="[i for i in range(1000)]", number = 100000)
#测量代码c执行100000次运行结果
#第二种是通过上面c的代码,即append生成列表的方式生成列表
t2 = timeit.timeit(stmt=c, number = 100000)
#通过结果可以看出,第一种方式比较快
print(t1)
print(t2)
help(timeit.timeit)

#timeit 也可以执行一个函数,来测量一个函数的执行时间
def doIt():
    num = 3
    for i in range(num):
        print("Repeat for {0}".format(i))
#执行函数,重复10次
t = timeit.timeit(stmt=doIt,number=10)
print(t)

#测试函数运行时间
s = '''
def doIt(num):
    for i in range(num):
        print("Repeat for {0}".format(i))
'''
#执行doIt(num)
#setup负责把环境变量准备好
#实际上相当于给timeit创建了一个小环境
#在这个小环境中代码的执行顺序大致如下
'''
def doIt(num):
    for i in range(num):
        print("Repeat for {0}".format(i))
num=3
doIt(num)

然后执行10次
'''
print(timeit.timeit("doIt(num)",setup=s+"num=3",number=10))