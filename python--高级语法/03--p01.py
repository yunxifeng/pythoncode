#calendar的使用
import calendar
cal = calendar.calendar(2018 , l = 0 , c = 5)
#说明cal是字符串类型
print(type(cal))
print(cal)
#isleap函数
print(calendar.isleap(2018))
#leapdays函数
print(calendar.leapdays(2001,2008))
#查看函数解释
help(calendar.leapdays)