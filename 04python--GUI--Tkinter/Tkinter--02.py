# 事件的简单例子(消息队列)
'''
import tkinter

def baseLabel(event):
        global  baseFrame
        print("哈哈，我被点击了")
        lb = tkinter.Label(baseFrame, text="谢谢点击")
        lb.pack()

# 画出程序的总框架
baseFrame = tkinter.Tk()

lb = tkinter.Label(baseFrame, text="模拟按钮")
# label绑定相应的消息和处理函数
# 自动获取左键点击，并启动相应的处理函数baseLabel
lb.bind("<Button-1>", baseLabel)
lb.pack()

# 启动消息循环
# 到此，表示程序开始运行
baseFrame.mainloop()

# 输入框案例
import tkinter

# 模拟的是登录函数
def reg():
    # 从相应输入框中，得到用户的输入
    name = e1.get()
    pwd = e2.get()

    t1 = len(name)
    t2 = len(pwd)

    if name == "111" and pwd == "222":
        # 需要理解下面代码的含义
        lb3["text"] = "登录成功"
    else:
        lb3['text'] = "用户名或密码错误"
        # 输入框删除掉用户输入的内容
        # 注意delete的两个参数，表示从第几个删除到第几个
        e1.delete(0, t1)
        e2.delete(0, t2)


# 启动舞台
baseFrame = tkinter.Tk()

lb1 = tkinter.Label(baseFrame, text="用户名")
lb1.grid(row=0, column=0, stick=tkinter.W)

e1 = tkinter.Entry(baseFrame)
e1.grid(row=0, column=1, stick=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="密码: ")
lb2.grid(row=1, column=0, stick=tkinter.W)

e2 = tkinter.Entry(baseFrame)
e2.grid(row=1, column=1, stick=tkinter.E)
e2['show'] = '*'

# Button参数command的意思是，当按钮被点击后启动相应的处理函数
btn = tkinter.Button(baseFrame, text="登录", command=reg)
btn.grid(row=2, column=1, stick=tkinter.E)

lb3 = tkinter.Label(baseFrame, text="")
lb3.grid(row=3)

# 启动主Frame
baseFrame.mainloop()

# 普通菜单案例
import tkinter

baseFrame = tkinter.Tk()

menubar = tkinter.Menu(baseFrame)

for item in ['File', 'Edit', 'View', 'About']:
    menubar.add_command(label=item)

baseFrame['menu'] = menubar

baseFrame.mainloop()


# 级联菜单案例
import tkinter

baseFrame = tkinter.Tk()

menubar = tkinter.Menu(baseFrame)

emenu = tkinter.Menu(menubar)
for item in ['Copy', 'Past', 'Cut']:
    emenu.add_command(label=item)

menubar.add_cascade(label='File')
menubar.add_cascade(label='Edit', menu=emenu)
menubar.add_cascade(label='About')

baseFrame['menu'] = menubar

baseFrame.mainloop()

# 弹出式菜单
import tkinter

def makeLabel():
    global baseFrame
    tkinter.Label(baseFrame, text="PHP是最好的编程语言，我用Python").pack()


baseFrame = tkinter.Tk()

menubar = tkinter.Menu(baseFrame)
for x in ['麻辣香菇', '气锅鸡', '东坡肘子']:
    menubar.add_separator()
    menubar.add_command(label=x)

menubar.add_command(label='重庆火锅', command=makeLabel)


# 事件处理函数一定要至少有一个参数，且第一个参数表示的是系统事件
def pop(event):
    # 注意使用 event.x 和 event.x_root的区别
    # menubar.post(event.x_root, event.y_root)
    menubar.post(event.x_root, event.y_root)

# 绑定右键,一旦触发,调用pop函数
baseFrame.bind("<Button-3>", pop)

baseFrame.mainloop()

# 简单画布
import tkinter
baseFrame = tkinter.Tk()
cvs = tkinter.Canvas(baseFrame, width=300, height=200)
cvs.pack()
# 一条线需要两个点指明起始位置
# 参数单位是px
cvs.create_line(1,1, 100,100)
cvs.create_text(101,101, text="I love Python")

baseFrame.mainloop()

# 画五角星
# 画一个五角星
import tkinter
import math as m

baseFrame = tkinter.Tk()

w = tkinter.Canvas(baseFrame, width=300, height=300, background="gray" )
w.pack()


center_x = 150
center_y = 150

r = 150

# 依次存放五个点的位置
points = [
        #左上点
        # pi是一个常量数字，3.1415926
        center_x - int(r * m.sin(2 * m.pi / 5)),
        center_y - int(r * m.cos(2 * m.pi / 5)),

        #右上点
        center_x + int(r * m.sin(2 * m.pi / 5)),
        center_y - int(r * m.cos(2 * m.pi / 5)),

        #左下点
        center_x - int(r * m.sin( m.pi / 5)),
        center_y + int(r * m.cos( m.pi / 5)),

        #顶点
        center_x,
        center_y - r,

        #右下点
        center_x + int(r * m.sin(m.pi / 5)),
        center_y + int(r * m.cos(m.pi / 5)),
    ]

# 创建一个多边形
w.create_polygon(points, outline="green", fill="yellow")
w.create_text(150,150, text="五角星")

baseFrame.mainloop()
'''

# 动画案例
import tkinter

baseFrame = tkinter.Tk()

def btnClick(event):
        global  w
        # x和y移动距离分别是12,5
        w.move(id_ball, 12,5)
        w.move("fall", 0,5)



w = tkinter.Canvas(baseFrame, width=500, height=400)
w.pack()
w.bind("<Button-1>", btnClick)

# 创建组件后返回id
id_ball  = w.create_oval(20,20, 50,50, fill="green")

# 创建组件使用tag属性指定该文本
w.create_text(123,56, fill="red", text="ILovePython", tag="fall")
# 创建的时候如果没有指定tag可以利用addtag_withtag添加
# 同类函数还有 addtag_all, addtag_above, addtag_xxx等等
id_rectangle = w.create_rectangle(56,78,173,110, fill="gray")
w.addtag_withtag("fall", id_rectangle)


baseFrame.mainloop()