from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.

# 基于类的views案例
class StudentListView(ListView):
    '''
    需要设置两个主要内容
    1.queryset: 是从哪个表里筛选出来的数据,可以筛选
    2.template_name: 模板名称
    '''
    queryset = Student.objects.all().filter(gender="男")
    # 示例,没建立模板
    template_name = "Student_list.html"
def mySess(request):
    print(type(request.session))
    print(request.session)

    # 取出teacher_name,如果得不到或者没有,则返回默认值NoName
    print(request.session.get("teacher_name", "NoName"))

    # 清空session内的所有值
    request.session.clear()

    print("In mysess")
    return None

def student(request):
    '''
    分页显示学生列表
    '''
    stu = Student.objects.all()
    # 两个参数
    # 1.数据来源,也即从数据库中查询出的结果
    # 2.单页返回数据量
    p = Paginator(stu, 40)
    # 对Paginator进行设置或者使用
    print(p.count) # p的数据总量
    print(p.num_pages) # 页面总数
    print(p.page_range) # 页码列表,从1开始

    # 取得第三页的内容
    # 如果页码不存在,则报异常InvalidPage
    p.page(3)
    return stu

