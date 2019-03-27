# 测试Tkinter包
#import tkinter
#tkinter._test()

# 简单案例
'''
import tkinter
# 使用tkinter.Tk() 生成主窗口
base = tkinter.Tk()
# 进入消息循环
base.mainloop()

# labal案例
import tkinter
# 1.生成主窗口
base = tkinter.Tk()
# 2.主窗口标题
base.wm_title("Label Test")
# 3.创建一个Label组件,位于base上,内容是Python Label
lb = tkinter.Label(base, text="Python Label")
# 4.给相应组件指定布局,pack是一种布局方式
lb.pack()
# 5.消息循环
base.mainloop()


# 设置Label案例
import tkinter
base = tkinter.Tk()
base.wm_title("Label Test")
# 支持属性很多background, font, underline等
# 第一个参数，制定所属
lb1= tkinter.Label(base, text="Python AI")
lb1.pack()

lb2= tkinter.Label(base, text="绿色背景", background="green")
lb2.pack()

lb3= tkinter.Label(base, text="蓝色背景", background="blue")
lb3.pack()

base.mainloop()


# Button案例
import tkinter
def showLable():
    global baseFrame
    # 在函数中定义了一个label
    # label的父组件是baseFrame
    lb = tkinter.Label(baseFrame, text = "显示Label")
    lb.pack()
baseFrame = tkinter.Tk()
# 生成一个按钮
# command参数, 执行函数
btn = tkinter.Button(baseFrame, text = "Show Label", command=showLable)
btn.pack()

baseFrame.mainloop()


# pack案例
import tkinter

baseFrame = tkinter.Tk()

# 以下所有代码都是创建一个组件，然后布局
btn1 = tkinter.Button(baseFrame, text='A')
btn1.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.Y)

btn2 = tkinter.Button(baseFrame, text='B')
btn2.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

btn2 = tkinter.Button(baseFrame, text='C')
btn2.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.NONE,
          anchor=tkinter.NE)

btn2 = tkinter.Button(baseFrame, text='D')
btn2.pack(side=tkinter.LEFT, expand=tkinter.NO, fill=tkinter.Y)

btn2 = tkinter.Button(baseFrame, text='E')
btn2.pack(side=tkinter.TOP, expand=tkinter.NO, fill=tkinter.BOTH)

btn2 = tkinter.Button(baseFrame, text='F')
btn2.pack(side=tkinter.BOTTOM, expand=tkinter.YES)

btn2 = tkinter.Button(baseFrame, text='G')
btn2.pack(anchor=tkinter.SE)

baseFrame.mainloop()
'''

# grid案例
import tkinter

baseFrame = tkinter.Tk()

#下面被注释掉的一行代码跟下面两行代码等效
#lb1 = tkinter.Label(baseFrame, text="账号: ").grid(row=0, sticky= tkinter.W)
lb1 = tkinter.Label(baseFrame, text="账号: ")
lb1.grid(row=0, sticky= tkinter.W)

en = tkinter.Entry(baseFrame)
en.grid(row=0, column=1, sticky=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="密码: ").grid(row=1, sticky= tkinter.W)

tkinter.Entry(baseFrame).grid(row=1, column=1, sticky=tkinter.E)

btn = tkinter.Button(baseFrame, text="登录").grid(row=2, column=1, sticky=tkinter.W)

baseFrame.mainloop()