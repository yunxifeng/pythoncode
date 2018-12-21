# GUI
- [http://www.runoob.com/python/python-gui-tkinter.html]
- 图形用户界面（Graphical User Interface，简称 GUI，又称图形用户接口）
  是指采用图形方式显示的计算机操作用户界面. 
- GUI for Python:
  - Tkinter
     - 绑定的是TK GUI工具集,用Python包装的Tcl代码
     - Tkinter模块(Tk 接口)是Python的标准Tk GUI工具包的接口
  - PyGTK
     - Tkinter的替代品
  - wxPython
     - 跨平台的Python GUI
  - PyQt
     - 跨平台
     - 商业授权问题 
- 参考资料:
  - 辛星GUI, 辛星Python
  - Python GUI Programming cookbook
  - Tkinter reference a GUI for Python
## Tkinter常用组件
- 按钮
      Button                按钮组件
      RadioButton           单选框组件
      CheckButton           选择按钮组件
      Listbox               列表框组件
- 文本输入组件
      Entry                 单行文本框组件
      Text                  多行文本框组件
- 标签组件
      Label                 标签组件，可以显示图片和文字
      Message               标签组件，可以根据内容将文字换行
- 菜单
      Menu                  菜单组件
      MenuButton            菜单按钮组件，可以使用Menu代替
- 滚动条
      scale                 滑块组件
      Scrollbar             滚动条组件
- 其他组件
      Canvas                画布组件
      Frame                 框架组件，将多个组件编组
      Toplevel              创建子窗口容器组件
------------------------------------------------------------------------------------------------------------------------
Button的属性：

anchor 				        设置按钮中文字的对其方式，相对于按钮的中心位置
background(bg) 		        设置按钮的背景颜色
foreground(fg)		        设置按钮的前景色(文字的颜色)
borderwidth(bd)		        设置按钮边框宽度
cursor				        设置鼠标在按钮上的样式
command				        设定按钮点击时触发的函数
bitmap				        设置按钮上显示的位图
font				        设置按钮上文本的字体
width				        设置按钮的宽度(字符个数)
height				        设置按钮的高度(字符个数)
state				        设置按钮的状态
text				        设置按钮上的文字
image				        设置按钮上的图片
------------------------------------------------------------------------------------------------------------------------
控件	            描述
Button	        按钮控件；在程序中显示按钮。
Canvas	        画布控件；显示图形元素如线条或文本
Checkbutton	    多选框控件；用于在程序中提供多项选择框
Entry	        输入控件；用于显示简单的文本内容
Frame	        框架控件；在屏幕上显示一个矩形区域，多用来作为容器
Label	        标签控件；可以显示文本和位图
Listbox	        列表框控件；在Listbox窗口小部件是用来显示一个字符串列表给用户
Menubutton	    菜单按钮控件，由于显示菜单项。
Menu	        菜单控件；显示菜单栏,下拉菜单和弹出菜单
Message	        消息控件；用来显示多行文本，与label比较类似
Radiobutton	    单选按钮控件；显示一个单选的按钮状态
Scale	        范围控件；显示一个数值刻度，为输出限定范围的数字区间
Scrollbar	    滚动条控件，当内容超过可视化区域时使用，如列表框。.
Text	        文本控件；用于显示多行文本
Toplevel	    容器控件；用来提供一个单独的对话框，和Frame比较类似
Spinbox	        输入控件；与Entry类似，但是可以指定输入范围值
PanedWindow	    PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
LabelFrame	    labelframe 是一个简单的容器控件。常用与复杂的窗口布局。
tkMessageBox	用于显示你应用程序的消息框。
------------------------------------------------------------------------------------------------------------------------
标准属性

属性          	描述
Dimension	    控件大小；
Color	        控件颜色；
Font	        控件字体；
Anchor	        锚点；
Relief	        控件样式；
Bitmap	        位图；
Cursor	        光标；
------------------------------------------------------------------------------------------------------------------------
几何方法	        描述
pack()	        包装；
grid()	        网格；
place()	        位置；
------------------------------------------------------------------------------------------------------------------------
## 组件的大致使用步骤
1. 创建总面板(主窗口)
2. 创建面板上的各种组件
   - 指定组件的父组件,即依附关系
   - 利用相应的属性对组件进行设置
   - 给组件安排布局
3. 同步骤2,可创建多个组件
4. 启动总面板的消息循环
## 组件的布局
- [https://www.cnblogs.com/zhangpengshou/p/3626137.html]
- 控制组件的摆放方式
- 三种布局:
   - pack: 按照方位布局
      - 最简单,代码量少,挨个摆放,默认从上到下,系统自动设置
      - 通用的使用方式: 组件对象.pack(设置...)
         - side: 停靠方位,可选值: LEFT,TOP,RIGHT,BUTTON
         - fill: 填充方式,可选值: X,Y,BOTH,NONE
         - expand: 是否扩展,可选值:YES/NO
         - anchor: N,E,S,W,CENTER
         - ipadx: x方向边距
         - ipady: y方向边距
         - padx: x方向外边距
         - pady: y方向外边距
   - palce: 按照坐标布局
      - 明确方位的摆放
      - 相对位置布局,随意改变窗口大小会导致混乱
      - 使用place函数,分为绝对布局和相对布局
      - 相对布局使用relx,rely,relheight,relwidth 
      - 绝对布局使用x,y参数   
   - grid: 网格布局
      - 通用使用方式: 组件对象.grid(设置...)
      - 利用row,column编号,都是从零开始
      - sticky: N,E,S,W表示上下左右,用来决定组件从那个方向开始
      - 支持ipadx,padx等参数,跟pack函数含义一样
      - 支持rowspan,columnspan,表示跨行,跨列数量 
## 消息机制 
- 消息的传递机制
   - 自动发出事件/消息
   - 消息由系统负责发送到队列
   - 由相关组件进行绑定/设置
   - 后端自动选择感兴趣的事件并做出相应反应
- 消息格式：
   - <[modifier-]---type-[-detail]>
   - e.g.
      - <Button-1>: Button表示一个按钮事件，1代表的是鼠标左键，2代表中键
      - <KeyPress-A>: 键盘A键位
      - <Control-shift-KeyPress-A>: 同时按下Control，Shift，A三个键位
      - <F1>: F1键位
   - 键位对应名称
      -[https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html]
## Tkinter的绑定
- bind_all: 全局范围的绑定,默认的是全局快捷键,比如F1是帮助文档
- bind_class: 接受三个参数,第一个是类名,第二个是事件,第三个是操作
  - w.bind class("Entry", "<Control-V>", my_paste)
- bind: 单独对某一个实例绑定
- unbind: 解绑,需要一个参数,即要解绑的事件
### Entry
- 输入框,功能单一 
- entry["show"]="*", 设置遮挡字符 
### Menu
- 菜单
   - 1.普通菜单  
       - 第一个Menu类定义的是parent
       - add_command 添加菜单项,如果菜单是顶层菜单,则从左向右添加,否则就是下拉菜单
          - 参数:
              - label: 指定菜单名称
              - command: 点击后调用相应函数
              - acceletor: 快捷键
              - underline: 指定菜单信息下横线
              - menu: 指定使用哪一个作为顶级菜单
   - 2.级联菜单
       - add_cascade: 级联菜单,作用是引出后面的菜单
          - 参数:
              - menu: 指明把菜单级联到那个菜单上
              - label: 名称
       - 过程:
          - 1.建立menu实例
          - 2.add_command
          - 3.add_cascade 
   - 3.弹出式菜单(上下文菜单)
       - 实现方法:
          - 1.建立菜单并向菜单添加各种功能
          - 2.监听鼠标右键
          - 3.根据位置判断弹出
          - 4.调用Menu的pop方法
       - add_separator: 添加分隔符
### canvas
- 画布: 可以自由地在上面绘制图形
- 在画布上绘制对象,通常用create_xxx, xxx=对象类型, 例如line,rectangle
- 作用: 把一定组件在画布上展示出来
- 画布支持的组件:
   - arc
   - bitmap
   - image(BitmapImage, PhotoImage)
   - line
   - oval
   - polygon
   - rectangle
   - text
   - window
- 每次调用create_xxx都会返回一个创建组件的ID,同时也可以用tag属性指定其标签
- 通过调用canvas.move实现一个一次性动作