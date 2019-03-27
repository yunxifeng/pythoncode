from django.db import models
import time
# Create your models here.

class ClassRoom(models.Model):
    room_id = models.IntegerField()
    room_location = models.CharField(max_length=20)
    room_name = models.CharField(max_length=20)
    def __str__(self):
        return self.room_name

class Teacher(models.Model):
    tea_name = models.CharField(max_length=5)
    course = models.CharField(max_length=20)
    room = models.OneToOneField(ClassRoom)

    # 关联对象
    def getRoomName(self):
        return self.room.room_name
    getRoomName.short_description = "教室"

    # 方法作为列显示--显示当前时间
    def curTime(self):
        return time.time()
    # 改名
    curTime.short_description = "当前时间"
    # 设置可以按时间排序
    curTime.admin_order_field = "tea_name"

    def __str__(self):
        return self.tea_name

class Student(models.Model):
    stu_name = models.CharField(max_length=20)
    stu_age = models.IntegerField()
    room = models.ForeignKey(ClassRoom)
    def __str__(self):
        return self.stu_name