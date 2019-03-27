from django.contrib import admin
from myAdmin.models import ClassRoom, Teacher, Student
# Register your models here.

# 站头,站标题,主页标题设置
admin.site.site_header = "欢迎来到云汐风Django管理"
admin.site.site_title = "Death--Madao"
admin.site.index_title = "云汐风管理中心欢迎您"

# 定义三个管理类,分别管理ClassRoom,Teacher,Student
class ClassRoomAdmin(admin.ModelAdmin):
    pass
class TeacherAdmin(admin.ModelAdmin):
    # 与Student相比,这里正常,原因???(一对一)
    list_display = ["tea_name", "room", "curTime", "getRoomName"]
    # 添加搜索框
    search_fields = ["tea_name"]

    # 详细信息只显示tea_name,course
    # fields = ["tea_name", "course"]

    # 详细信息分组
    fieldsets = (
        ("基本信息", {"fields":["tea_name",]}),
        ("其他信息", {"fields":["room","course"]}),
    )

# 装饰器方法
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # 设置分页显示个数,同下,ClassRoom也生效
    list_per_page = 2
    # 设置操作选项(动作)位置,这里修改了StudentAdmin,与之相关的ClassRoom也生效
    actions_on_bottom = True
    actions_on_top = False
    # 控制列表显示内容,这里会报错,原因???猜测可能与ClassRoom相关联(一对多)有关系.
    # list_display = ["stu_age"]



# 绑定管理模型,添加管理类
admin.site.register(ClassRoom, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
# 采用装饰器方法添加管理类
# admin.site.register(Student, StudentAdmin)