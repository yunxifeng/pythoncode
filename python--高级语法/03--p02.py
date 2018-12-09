#os模块
#getcwd()函数
import os
print(os.getcwd())
#chdir()函数
os.chdir('E:\Python code\python--高级语法')
print(os.getcwd())
#listdir()函数
print(os.listdir())
#makedirs()函数
help(os.makedirs)
#如果不给路径,就在当前目录下创建
#print(os.makedirs("yunxifeng"))
#system()函数
#返回0表示执行成功
print(os.system("dir"))
#print(os.system("md yunxifeng"))
#getenv()函数
print(os.getenv("PATH"))

#值部分
print(os.curdir)
print(os.pardir)
print(os.sep)
print(os.linesep)
print(os.name)

#os.path模块
import os.path
#abspath()函数
help(os.path.abspath)
#linux中,"."代表当前目录, ".."代表父目录
print(os.path.abspath("."))
#basepath()函数
print(os.path.basename("c:\windows\system32"))
#join()函数
a = "C:\Windows\System32"
b = "@AudioToastIcon.png"
print(os.path.join(a,b))
#split()函数
a,b = os.path.split("C:\Windows\System32\@AudioToastIcon.png")
print(a,"------",b)
#isdir()函数
print(os.path.isdir("E:\Python code\python--高级语法\pkg01"))
#exists()函数
print(os.path.exists("C:\Windows\System32\@AudioToastIcon.png"))

#shutil模块
import shutil
#copy()
#print(shutil.copy("C:\Windows\System32\@AudioToastIcon.png", "D:\Administrator\yunxifeng.png"))
#copy2()
#print(shutil.copy2("C:\Windows\System32\@AudioToastIcon.png", "D:\Administrator\yunxifeng2.png"))
#copyfile()
#print(shutil.copyfile("D:\Administrator\death.txt", "D:\Administrator\yunxifeng.txt"))
#move()
#print(shutil.move("D:\Administrator\Videos\death.txt", "D:\Administrator"))

#make_archive()
#print(shutil.make_archive("D:\Administrator\make_archive", "zip", "D:\Administrator\photos"))
#unpack_archive()
#print(shutil.unpack_archive("D:\Administrator\make_archive.zip", "D:\Administrator\photos"))

#zipfile模块
import zipfile
#ZipFile():创建了一个zip文件对象实例
a = zipfile.ZipFile("D:\Administrator\make_archive.zip")
print(a)
#ZipFile.getinfo(name):获取zip文档内指定文件的信息
b = a.getinfo("yunxifeng2.png")
print(b)
#ZipFile.namelist()
c = a.namelist()
print(c)
#ZipFile.extractall():解压缩
#print(a.extractall("D:\Administrator"))

#random模块
import random
#random()
print(random.random())
#作业:利用random函数,生成0-100之间的整数
#choice()
l = [str(i)+"haha" for i in range(10)]
print(l)
rst = random.choice(l)
print(rst)
#shuffle()
l = [i for i in range(10)]
print(l)
random.shuffle(l)
print(l)
#randint()
print(random.randint(1,100))


